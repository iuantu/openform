from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
)
from .exceptions import ValidationError
from .constraint import Constraint


class RequiredConstraint(Constraint):
    id = Column(Integer, ForeignKey('constraint.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'required_constraint',
    }

    def validate(self, field, value):
        if not value:
            raise ValidationError(field, "必填字段")
