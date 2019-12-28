from sqlalchemy import (
    Column,
    Boolean,
    DateTime,
)
from sqlalchemy.sql import func

class SoftDeleteableMixin:
    deleted_at = Column(DateTime(), nullable=True)

class MultipleMixin:
    multiple = Column(Boolean, default=False)

class TimeStampMixin:
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())