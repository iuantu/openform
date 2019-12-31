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

class PageRequest:
    def __init__(self, page, page_size=50, order_by={}):
        self.page = page
        self.page_size = page_size
        self.order_by = order_by

    @staticmethod
    def create(request):
        order_by = {}
        for k, v in request.items():
            if k.endswith("_order_by"):
                field = k.split("_")[0]
                direction = v
                order_by[field] = v

        return PageRequest(
            int(request.get("page", 1)),
            int(request.get("page_size", 50)),
            order_by
        )

logger = logging.getLogger(__file__)