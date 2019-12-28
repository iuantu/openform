from flask_appbuilder import Model
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    JSON,
)
from .mixins import TimeStampMixin

class Value(Model, TimeStampMixin):
    id = Column(Integer, primary_key=True)
    form_id = Column(Integer)
    user_id = Column(Integer, ForeignKey("ab_user.id"))
    values = Column(JSON)

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)