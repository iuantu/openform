import logging
from app import models
from app.markup import (
    Div,
    Form,
    Label,
    Input,
    Button,
    Li,
    TextArea
)

class FormView:
    def __init__(self, form: models.Form, request):
        self.form = form
        self.request = request

        self._assemble_fields()

    def _assemble_fields(self):
        field_views = []
        for field in self.form.fields:
            field_view = self._create_field_view(field, self.request)
            field_views.append(field_view)

            field.value = field_view.value

        self.fields = field_views

    def _create_field_view(self, field: models.Field, request):
        mapping = {
            models.TextField: TextFieldView,
            models.SelectField: SelectFieldView,
            models.PhoneField: PhoneFieldView,
        }
        field_view_class = mapping[field.__class__]

        return field_view_class(field, request)

    def as_element(self):
        fields = []
        
        row = Div(class_=["a"])
        form = Form(row)
        size = len(self.fields)

        for i in range(size):
            current = self.fields[i]
            previous = i > 0 and self.fields[i-1] or None

            row.append(current.as_element())
        form.append(Button("提交", class_=["btn", "btn-primary"]))

        return form

class OptionView:

    def __init__(self, field, field_view, option, request):
        self.field = field
        self.field_view = field_view
        self.option = option
        self.request = request

    @property
    def id(self):
        return "%d_%d" % (self.field.id, self.option.value)

    @property
    def name(self):
        if "checkbox" == self.field.type:
            name = "%d[]" % (self.field.id)
        else:
            name = "%d" % (self.field.id,)
        return name

    @property
    def checked(self):
        get_value = "checkbox" == self.field.type and self.request.getlist or self.request.get
        checked_values = get_value(self.name)

        if not checked_values:
            return False

        for checked_value in checked_values:
            if int(checked_value) == self.option.value:
                return True
        return False

    @property
    def class_(self):
        input_classes = ["form-check-input"]
        if self.field.has_errors:
            input_classes.append("is-invalid")
        return input_classes

    @property
    def value(self):
        return {
            "value": self.option.value,
            "text": self.text,
        }

    @property
    def text(self):
        return self.request.get("text_%d" % self.option.id)

    def as_element(self) -> Div:

        kwargs = {}
        if self.checked:
            kwargs["checked"] = "checked"

        opt_element = [
            Input(
                class_=self.class_,
                type=self.field.type,
                name=self.name,
                id=self.id,
                value=str(self.option.value),
                **kwargs,
            ),
            Label(self.option.label, class_=["form-check-label"], for_=self.id),
        ]

        if self.option.editable:
            id_or_name = "text_%d" % self.option.id
            opt_element.append(
                Input(class_=['form-control'], id=id_or_name, name=id_or_name, value=self.text)
            )

        opt = Div(
            *opt_element,
            class_=["form-check", "form-check-inline"]
        )

        return opt

class FieldView:
    def __init__(self, field, request):
        self.field = field
        self.request = request

class TextFieldView(FieldView):

    @property
    def value(self):
        return self.field.format(self.request.get("%d" % self.field.id))

    @property
    def class_(self):
        input_classes = ["form-control"]
        if self.field.has_errors:
            input_classes.append("is-invalid")
        return input_classes

    @property
    def id(self):
        return str(self.field.id)

    def as_element(self):
        if self.field.multiple:
            input = TextArea(
                self.value,
                class_=self.class_, 
                id=self.id, 
                name=self.id, 
                placeholder=self.field.placeholder
            )
        else:
            input = Input(type="text", 
                class_=self.class_, 
                id=self.id,
                name=self.id, 
                value=self.value,
                placeholder=self.field.placeholder
            )
        
        children = [
            Label(self.field.title, for_=self.id),
            input
        ]

        if self.field.has_errors:
            children.append(
                Div(*[Li(str(e)) for e in self.field.errors], class_=["invalid-feedback"])
            )
        return Div(
            Div(*children,
                class_=["form-group", "col-md-12"]),
            class_=["form-row"]
        )

class PhoneFieldView(TextFieldView):
    pass

class SelectFieldView(FieldView):

    def __init__(self, field, request):
        super().__init__(field, request)

        self._assemble_options()

    def _assemble_options(self):
        self.options = []
        for opt in self.field.options:
            option_view = OptionView(self.field, self, opt, self.request)
            self.options.append(option_view)

    @property
    def value(self):
        return self.field.format([opt.value for opt in self.options if opt.checked])

    def as_element(self):
        input_classes = ["of-form-title"]
        if self.field.has_errors:
            input_classes.append("is-invalid")

        options = [
            Label(self.field.title, for_=str(self.field.id), class_=input_classes)
        ]
        
        for opt in self.options:
            options.append(opt.as_element())

        if self.field.has_errors:
            options.append(
                Div(*[Li(str(e)) for e in self.field.errors], class_=["invalid-feedback"])
            )
        return Div(
            Div(*options,
                class_=["form-group", "col-md-12"]),
            class_=["form-row"]
        )


class FormViewModelAssembler:

    def to_view_model(self, model, request):
        form_view = FormView(model, request)
        return form_view
            
            