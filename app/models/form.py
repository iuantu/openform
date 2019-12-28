from flask_appbuilder import Model
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from .mixins import TimeStampMixin, SoftDeleteableMixin

class Form(Model, SoftDeleteableMixin):
    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False)
    fields = relationship('Field')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)

    def populate(self, value):
        for field in self.fields:
            field.value = value.values.get(field.id)

    def validate(self, values):
        success = True
        for field in self.fields:
            if not field.validate():
                if success:
                    success = False

        return success
