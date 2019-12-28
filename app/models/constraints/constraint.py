from flask_appbuilder import Model
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from ..mixins import (TimeStampMixin)

class Constraint(Model, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    field_id = Column(Integer, ForeignKey('field.id'))

    discriminator = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'field',
        'polymorphic_on': discriminator
    }
    
    def validate(self, value):
        pass