from flask_appbuilder import Model
from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    String,
    ForeignKey,
    text,
)
from ..mixins import (TimeStampMixin)

class Constraint(Model, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    field_id = Column(Integer, ForeignKey('field.id'))
    enabled = Column(Boolean, nullable=True, default_server=text("true"))

    discriminator = Column(String(50))
    enabled = Column(Boolean, server_default=text('true'))

    __mapper_args__ = {
        'polymorphic_identity': 'field',
        'polymorphic_on': discriminator
    }
    
    def validate(self, value):
        pass