
from typing import Dict, Tuple, Sequence, TypeVar, Generic

E = TypeVar('E')


class Element:
    children : Tuple[E]


class Section(Element):
    title : str


class HtmlInput:
    label : str = None
    value : str = None
    description : str = None
    placeholder : str = None
    type : str = 'text'
    name : str = None

    def __init__(self, **kwargs):
        super().__init__()
        for k, v in kwargs:
            setattr(self, k, v)

    def to_dict(self):
        return {
            'label': self.label,
            'value': self.value,
            'description': self.description,
            'placeholder': self.placeholder,
            'type': self.type
        }


class TitleHtmlInput(HtmlInput):
    name : str = 'title'
    label : str = '标题'
    value : str = '未命名'


class DefaultValueHtmlInput(HtmlInput):
    label : str = '默认值'


class RequiredHtmlInput(HtmlInput):
    type : str = 'checkbox'
    label : str = '必填项'
    description : str = '将所有字段设为 <a href="">必须填</a> 或 非必须填'


class FormFieldTemplate:
    name : str = None
    attributes : Tuple[HtmlInput] = None
    validators : Tuple[HtmlInput] = None

    def to_dict(self):
        return {
            'name': self.name,
            'attributes': [x.to_dict() for x in self.attributes],
            'validators': [x.to_dict() for x in self.attributes],
        }


class FormInputFieldTemplate(FormFieldTemplate):

    @property
    def name(self):
        return 'single_input'

    @property
    def attributes(self):
        return (
            TitleHtmlInput(),
            DefaultValueHtmlInput()
        )

    @property
    def validators(self):
        return (
            RequiredHtmlInput()
        )