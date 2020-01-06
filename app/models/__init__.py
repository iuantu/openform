import math
import logging
from flask_appbuilder import Model
from dictalchemy import make_class_dictable
from .form import Form
from .value import Value
from .user_agent import UserAgent
from .event import Event, EventType
from .fields import Field, TextField, SelectField
from .mixins import SoftDeleteableMixin, TimeStampMixin, MultipleMixin
from .constraints import RequiredConstraint, RangeConstraint, MinConstraint, MaxConstraint
from app.models.repositories import FormRepository, FieldRepository, ValueRepository, EventRepository

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

    def create_result(self, count):
        pages = math.ceil(count / self.page_size)
        result = PageResult(self.page, pages, count, self.page_size)
        return result

class PageResult:
    def __init__(self, current_page, page_size, total, per_page_size):
        self.current_page = current_page
        self.page_size = page_size
        self.total = total
        self.per_page_size = per_page_size

    def asdict(self):
        return {
            "current_page": self.current_page,
            "page_size": self.page_size,
            "total": self.total,
            "per_page_size": self.per_page_size,
        }

class Pageable:
    def __init__(self, data, page_result):
        self.data = data
        self.page_result = page_result

    def asdict(self):
        data = None
        if isinstance(self.data, list):
            data = [list_item.asdict() for list_item in self.data]
        else:
            data = self.data.asdict()
        return {
            "data": data,
            "page_result": self.page_result.asdict()
        }

logger = logging.getLogger(__file__)