from flask_appbuilder import Model
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    JSON,
)

from .mixins import TimeStampMixin
from .user_agent import UserAgentMixin, SoftDeleteableMixin

class Value(Model, TimeStampMixin, UserAgentMixin, SoftDeleteableMixin):
    id = Column(Integer, primary_key=True)

    sequence = Column(Integer)
    form_id = Column(Integer)
    user_id = Column(Integer, ForeignKey("ab_user.id"))
    values = Column(JSON)

    ip = Column(String(15), nullable=True)
    ua_browser = Column(String(100), nullable=True)
    ua_browser_version = Column(String(10), nullable=True)
    ua_os = Column(String(100), nullable=True)
    ua_os_version = Column(String(10), nullable=True)
    ua_device = Column(String(50), nullable=True)
    ua_device_brand = Column(String(50), nullable=True)
    ua_device_model = Column(String(50), nullable=True)

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)
