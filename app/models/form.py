from flask_appbuilder import Model
from sqlalchemy import text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from .mixins import TimeStampMixin, SoftDeleteableMixin
from .value import Value

class Form(Model, SoftDeleteableMixin, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("ab_user.id"))
    title = Column(String(500), nullable=False)
    fields = relationship('Field')

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
            self.value_sequence = 1
        self.value_sequence += 1