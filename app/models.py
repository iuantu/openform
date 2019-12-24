from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_sqlalchemy import BaseQuery
from dictalchemy import make_class_dictable
make_class_dictable(Model)

class SoftDeleteable:
    deleted_at = Column(DateTime(), nullable=True)

class SoftDeleteableQuery(BaseQuery):
    def __new__(cls, *args, **kwargs):
        obj = super(QueryWithSoftDelete, cls).__new__(cls)
        with_deleted = kwargs.pop('_with_deleted', False)
        if len(args) > 0:
            super(QueryWithSoftDelete, obj).__init__(*args, **kwargs)
            return obj.filter_by(deleted=False) if not with_deleted else obj
        import pdb; pdb.set_trace()
        return obj

    def __init__(self, *args, **kwargs):
        pass

    def with_deleted(self):
        return self.__class__(db.class_mapper(self._mapper_zero().class_),
                              session=db.session(), _with_deleted=True)

class Form(Model, SoftDeleteable):
    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False)
    fields = relationship('Field')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    query_class = SoftDeleteableQuery

    # def __init__(self, fields=[]):
    #     for field in fields:
    #         self.fields.append(field)

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)

class Field(Model, SoftDeleteable):
    __tablename__ = 'field'

    id = Column(Integer, primary_key=True)
    form_id = Column(Integer, ForeignKey('form.id'))
    name = Column(String(255))
    title = Column(String(500))
    discriminator = Column(String(50))

    layout_row_index = Column(Integer)
    layout_column_index = Column(Integer)
    layout_columns = Column(Integer)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    query_class = SoftDeleteableQuery
    # validators = None

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)

    def format(self, val):
        return val
    
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
    editable = Column(Boolean, default=False)
    ordering = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # def __init__(self, label : str, value: int):
    #     self.label = label
    #     self.value = value
    #     super().__init__()
    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)

class SelectField(Field, MixinMultiple):
    id = Column(Integer, ForeignKey('field.id'), primary_key=True)
    type = Column(String(20))
    options = relationship('Option')
    default = Column(Integer, default=-1)

    # def __init__(self, multiple=False, options=[]):
    #     self.multiple = multiple
    #     for opt in options:
    #         self.options.append(opt)
    #     super().__init__()

    __mapper_args__ = {
        'polymorphic_identity':'select_field',
    }

    def format(self, val):
        if "radio" == type:
            return int(val)
        else:
            return [int(v) for v in val]


class Value(Model):
    id = Column(Integer, primary_key=True)
    form_id = Column(Integer)
    user_id = Column(Integer, ForeignKey("ab_user.id"))
    values = Column(JSON)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)


def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return ''.join(x.title() for x in components)

def get_field_by_discriminator(discriminator : str) -> Field :
    classes = globals()
    return classes[to_camel_case(discriminator)]