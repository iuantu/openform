from flask_appbuilder import Model
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    JSON,
)
from .mixins import TimeStampMixin
from .user_agent import UserAgentMixin

class EventType:
    VIEW_FORM = 0

class Event(Model, TimeStampMixin, UserAgentMixin):
    id = Column(Integer, primary_key=True)

    type = Column(Integer)
    form_id = Column(Integer, nullable=True)
    user_id = Column(Integer, ForeignKey("ab_user.id"), nullable=True)

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)