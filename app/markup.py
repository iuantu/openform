
from typing import Dict, Sequence, TypeVar, Generic, List
import logging
from io import StringIO

E = TypeVar('E')

class Element:
    # children : List[E] = []
    class_ = []

    output = StringIO()

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.children = []
        if args:
            for arg in args:
                self.children.append(arg)
        
        print("element init %s" % (self,))
        print(self.children)
        print('')
        for k, v in kwargs.items():
            setattr(self, k, v)

    def append(self, *args):
        for arg in args:
            self.children.append(arg)

    @property
    def tag_name(self):
        return self.__class__.__name__.lower()

    def render_attribute(self, name, value, output):
        value = value and value or ""
        logging.debug("render attribute %s=%s" % (name, value))
        output.write(" ")
        output.write(name)
        output.write("=\"")
        output.write(str(value))
        output.write("\"")

    def render_attributes(self, output):
        if self.class_:
            output.write(" class=\"")
            output.write(" ".join(self.class_))
            output.write("\"")

    def as_html(self, output=None):
        logging.debug("%s as html" % (self.tag_name))
        output = not output and StringIO() or output
        output.write("<")
        output.write(self.tag_name)

        self.render_attributes(output)

        output.write(">")

        for child in self.children:
            if isinstance(child, Element):
                child.as_html(output)
            else:
                logging.debug(child)
                if child:
                    output.write(child)

        output.write("</")
        output.write(self.tag_name)
        output.write(">")

        return output.getvalue()

    def _as_html(self, output):
        pass

    def render(self):
        pass

class Div(Element):
    class_ = []

class Label(Element):
    for_ = None

    def render_attributes(self, output : StringIO):
        super().render_attributes(output)

        if self.for_:
            output.write(" for=\"")
            output.write(self.for_)
            output.write("\"")

class Section(Element):
    title : str

class Form(Element):
    action : str = ''

class Input(Element):
    def render_attributes(self, output : StringIO):

        super().render_attributes(output)

        for attr in ["id", "value", 'name', "type"]:
            if hasattr(self, attr):
                self.render_attribute(attr, getattr(self, attr), output)

class Button(Element):
    type : str = 'submit'

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
    attributes = None
    validators = None

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