import logging
from flask_appbuilder import Model
from dictalchemy import make_class_dictable
from .form import Form
from .value import Value
from .fields import Field, TextField, SelectField
from .mixins import SoftDeleteableMixin, TimeStampMixin, MultipleMixin
from .constraints import RequiredConstraint, RangeConstraint, MinConstraint, MaxConstraint
from app.models.repositories import FormRepository, FieldRepository

make_class_dictable(Model)

logger = logging.getLogger(__file__)