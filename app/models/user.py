from flask_appbuilder import Model
from sqlalchemy import text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Boolean
)
from .mixins import TimeStampMixin, SoftDeleteableMixin

class AbUser(Model):
    __tablename__ = 'ab_user'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False, unique=True)
    password = Column(String(256))
    active = Column(Boolean)
    email = Column(String(64), nullable=False, unique=True)
    last_login = Column(DateTime, default=func.now())
    login_count = Column(Integer)
    fail_login_count = Column(Integer)
    created_on = Column(DateTime, default=func.now())
    changed_on = Column(DateTime, default=func.now(), onupdate=func.now())
    created_by_fk = Column(Integer, ForeignKey("ab_user.id"))
    changed_by_fk = Column(Integer, ForeignKey("ab_user.id"))

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)


class CollaborationUser(Model, TimeStampMixin, SoftDeleteableMixin):
    __tablename__ = 'collaboration_user'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("ab_user.id"))
    form_id = Column(Integer, ForeignKey('form.id'))
    author = relationship('AbUser', backref='CollaborationUsers')