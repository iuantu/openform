from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
)
from .exceptions import ValidationError
from .constraint import Constraint


class MinConstraint(Constraint):
    id = Column(Integer, ForeignKey('constraint.id'), primary_key=True)
    min = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'min_constraint',
    }

    def validate(self, field, value):
        has_error = False
        if not value:
            has_error = True

        if isinstance(value, int):
            if value < self.min:
                has_error = True

        elif isinstance(value, list):
            if len(value) < self.min:
                has_error = True

        if has_error:
            raise ValueError(field, "min")
