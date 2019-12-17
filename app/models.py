from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Form(Model):
    id = Column(Integer, primary_key=True)
    fields = relationship('Field')

    def __init__(self, fields=[]):
        for field in fields:
            self.fields.append(field)
    # attributes = None

class Field(Model):
    __tablename__ = 'field'

    id = Column(Integer, primary_key=True)
    form_id = Column(Integer, ForeignKey('form.id'))
    name : str = Column(String(255))
    discriminator = Column(String(50))
    # validators = None
    
    __mapper_args__ = {
        'polymorphic_identity': 'field',
        'polymorphic_on': discriminator
    }

class MixinMultiple:
    multiple = Column(Boolean, default=False)

class TextField(Field, MixinMultiple):
    __tablename__ = 'text_field'

    id = Column(Integer, ForeignKey('field.id'), primary_key=True)
    placeholder = Column(String(1000), nullable=True)
    default = Column(String(1000), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity':'text_field',
    }

class Option(Model):
    id = Column(Integer, primary_key=True)
    field_id = Column(Integer, ForeignKey('select_field.id'))
    label = Column(String(100), nullable=False)
    value = Column(Integer, nullable=False)

    def __init__(self, label : str, value: int):
        self.label = label
        self.value = value
        super().__init__()


class SelectField(Field, MixinMultiple):
    id = Column(Integer, ForeignKey('field.id'), primary_key=True)
    options = relationship('Option')
    default = Column(Integer, default=-1)

    def __init__(self, multiple=False, options=[]):
        self.multiple = multiple
        for opt in options:
            self.options.append(opt)
        super().__init__()

    __mapper_args__ = {
        'polymorphic_identity':'select_field',
    }