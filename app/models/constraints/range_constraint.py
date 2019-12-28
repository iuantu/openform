from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
)
from .exceptions import ValidationError
from .constraint import Constraint

class RangeConstraint(Constraint):
    id = Column(Integer, ForeignKey('constraint.id'), primary_key=True)
    min = Column(Integer)
    max = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity':'range_constraint',
    }

    def validate(self, value):
        message = "必须在 %d 和 %d 之间" % (self.min, self.max)
        has_error = False
        if not value:
            has_error = True

        if isinstance(value, int):
            if value < self.min:
                has_error = True
            if value > self.max:
                has_error = True

        elif isinstance(value, list):
            if len(value) < self.min:
                has_error = True
            if len(value) > self.max:
                has_error = True
        
        if has_error:
            raise ValidationError(message)
        return True