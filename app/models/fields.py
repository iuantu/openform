import logging
from flask_appbuilder import Model
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import event
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    JSON,
)
from .constraints import ValidationError
from .mixins import SoftDeleteableMixin, TimeStampMixin, MultipleMixin
from .constraints import RequiredConstraint

logger = logging.getLogger(__file__)

class Field(Model, SoftDeleteableMixin):
    __tablename__ = 'field'

    id = Column(Integer, primary_key=True)
    form_id = Column(Integer, ForeignKey('form.id'))
    name = Column(String(255))
    title = Column(String(500))
    discriminator = Column(String(50))
    constraints = relationship('Constraint')

    layout_row_index = Column(Integer)
    layout_column_index = Column(Integer)
    layout_columns = Column(Integer)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    __mapper_args__ = {
        'polymorphic_identity': 'field',
        'polymorphic_on': discriminator
    }

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.errors = []
        self._value = None

    @property
    def value(self):
        if not hasattr(self, '_value'):
            return None
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def has_errors(self):
        if hasattr(self, 'errors') and self.errors:
            return True
        return False

    def get_key(self):
        if self.name:
            return self.name
        return str(self.id)

    def format(self, val):
        return val

    def validate(self):
        self.errors = []
        logger.debug("validate %s" % self.title)
        for constraint in self.constraints:
            try:
                constraint.validate(self.value)
            except ValidationError as e:
                self.errors.append(e)

        if len(self.errors) > 0:
            logger.debug("%s has %d errors", self.title, len(self.errors))
        return 0 == len(self.errors)

    def to_text_value(self, val):
        return str(val)

class TextField(Field, MultipleMixin):
    __tablename__ = 'text_field'

    id = Column(Integer, ForeignKey('field.id'), primary_key=True)
    placeholder = Column(String(1000), nullable=True)
    default = Column(String(1000), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity':'text_field',
    }

    def to_text_value(self, val):
        return val

class Option(Model):
    id = Column(Integer, primary_key=True)
    field_id = Column(Integer, ForeignKey('select_field.id'))
    label = Column(String(100), nullable=False)
    value = Column(Integer, nullable=False)
    editable = Column(Boolean, default=False)
    ordering = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)

class SelectField(Field, MultipleMixin):
    id = Column(Integer, ForeignKey('field.id'), primary_key=True)
    type = Column(String(20))
    option_sequence = Column(Integer, default=0)
    options = relationship('Option')
    default = Column(Integer, default=-1)

    __mapper_args__ = {
        'polymorphic_identity':'select_field',
    }

    def format(self, values):
        formatted_values = []
        for value in values:
            formatted_values.append(
                {
                "value": int(value["value"]),
                "text": value["text"]
                }
            )
        return formatted_values

    def to_text_value(self, val):
        options_map = {}
        for opt in self.options:
            options_map[opt.value] = opt

        value = []
        for v in val:
            opt = options_map[v['value']]
            print(opt.editable)
            if opt.editable:
                print('edit')
                print(v)
                value.append(v['text'])
            else:
                value.append(opt.label)

        if "radio" == self.type:
            return value[0]

        return "，".join(value)

@event.listens_for(SelectField.options, 'append', propagate=True)
def selected_append_listener(target, value, initiator):
    if not target.option_sequence:
        target.option_sequence = 0
    target.option_sequence += 1
    value.value = target.option_sequence
    value.ordering = target.option_sequence