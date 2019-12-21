import datetime

# from flask_appbuilder import Model
# from app.db import Model
from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Form(Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    status = Column(Integer, nullable=False, default=1)
    creator_id = Column(Integer, ForeignKey('user.id'))
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class User(Model):
    id = Column(Integer, primary_key=True)
    user_name = Column(String(32), nullable=False)
    password = Column(String(128), nullable=False)
    email = Column(String(64), nullable=False)
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class FormFieldRelation(Model):
    id = Column(Integer, primary_key=True)
    form_id = Column(Integer, ForeignKey('form.id'))
    field_type = Column(String(32), nullable=False)
    field_id = Column(Integer, nullable=False)


# class Field(Model):
#     __tablename__ = 'field'
#
#     id = Column(Integer, primary_key=True)
#     form_id = Column(Integer, ForeignKey('form.id'))
#     name : str = Column(String(255))
#     discriminator = Column(String(50))
#     # validators = None
#
#     __mapper_args__ = {
#         'polymorphic_identity': 'field',
#         'polymorphic_on': discriminator
#     }


class MixinMultiple:
    multiple = Column(Boolean, default=False)


class TextField(Model):
    __tablename__ = 'text_field'

    id = Column(Integer, primary_key=True)
    placeholder = Column(String(1000), nullable=True)
    default = Column(String(1000), nullable=True)


class Option(Model):
    id = Column(Integer, primary_key=True)
    field_id = Column(Integer, ForeignKey('select_field.id'))
    label = Column(String(100), nullable=False)
    value = Column(Integer, nullable=False)

    def __init__(self, label : str, value: int):
        self.label = label
        self.value = value
        super().__init__()


class SelectField(Model):
    id = Column(Integer, primary_key=True)
    # options = relationship('Option')
    # default = Column(Integer, default=-1)
    text = Column(String(100), nullable=False)
    value = Column(Integer, nullable=False)

    # def __init__(self, multiple=False, options=[]):
    #     self.multiple = multiple
    #     for opt in options:
    #         self.options.append(opt)
    #     super().__init__()

    # __mapper_args__ = {
    #     'polymorphic_identity':'select_field',
    # }