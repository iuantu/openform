from flask_appbuilder import Model
from sqlalchemy import text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    ForeignKey
)
from .fields import SelectField
from .mixins import TimeStampMixin, SoftDeleteableMixin
from .value import Value


# form_collaborator_table = Table('form_collaborator', Base.metadata,
#     Column('form_id', Integer, ForeignKey('form.id')),
#     Column('user_id', Integer, ForeignKey('user.id')),
#     Column('created_at', DateTime, default=func.now()),
#     Column('updated_at', DateTime, default=func.now(), onupdate=func.now()),
# )

class FormCollaborator(Model, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    form_id = Column(Integer, ForeignKey('form.id'))
    form = relationship('Form', uselist=False, foreign_keys=form_id)
    user_id = Column(Integer, ForeignKey('ab_user.id'))
    user = relationship('User', uselist=False, foreign_keys=user_id)
    role_id = Column(Integer, ForeignKey('ab_role.id'))
    role = relationship('Role', uselist=False, foreign_keys=role_id)

    def __init__(self, form_id=None, user_id=None, role_id=None):
        super().__init__()

        self.form_id = form_id
        self.user_id = user_id
        self.role_id = role_id


class Form(Model, SoftDeleteableMixin, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("ab_user.id"))
    title = Column(String(500), nullable=False)
    description = Column(Text, nullable=True)
    fields = relationship('Field')
    # collaborator = relationship('User', secondary=form_collaborator_table)

    published_at = Column(DateTime, nullable=True, default=None)
    record_count = Column(Integer, server_default=text("0"))

    version = Column(Integer, default=0)
    value_sequence = Column(Integer, default=0)

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)

    def values(self):
        value_dict = {}
        for field in self.fields:
            value_dict[field.id] = field.value

        value = Value(user_id=self.user_id, form_id=self.id, values=value_dict)
        return value

    def populate(self, value):
        for field in self.fields:
            field.value = value.values.get(field.id)

    def validate(self):
        success = True
        for field in self.fields:
            if not field.validate():
                if success:
                    success = False

        return success

    def increase_value_sequence(self):
        if not self.value_sequence:
            self.value_sequence = 0
        self.value_sequence += 1

    @property
    def select_fields(self):
        fields = []
        for field in self.fields:
            if isinstance(field, SelectField):
                fields.append(field)
        return fields

    def sort(self):
        self.fields.sort(key=lambda f: f.layout_row_index)
