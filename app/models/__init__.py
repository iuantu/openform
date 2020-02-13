import math
import logging
from flask_appbuilder import Model
from dictalchemy import make_class_dictable
from .form import Form, FormCollaborator
from .value import Value
from .user_agent import UserAgent
from .event import Event, EventType
from .fields import Field, TextField, SelectField, PhoneField
from .mixins import SoftDeleteableMixin, TimeStampMixin, MultipleMixin
from .constraints import RequiredConstraint, RangeConstraint, MinConstraint, MaxConstraint
from .page import PageRequest, PageResult
from app.models.repositories import (
    FormRepository,
    FieldRepository,
    ValueRepository,
    EventRepository,
    CollaboratorRepository,
    RoleRepository,
)

make_class_dictable(Model)


logger = logging.getLogger(__file__)