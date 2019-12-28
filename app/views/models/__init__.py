import logging
from app.markup import Div, Form, Label, Input, Button, Li

class FormViewModelAssembler:
    def to_text_field_markup(self, field):
        input_classes = ["form-control"]
        if field.has_errors:
            input_classes.append("is-invalid")
        children = [
            Label(field.title, for_=str(field.id)),
            Input(type="text", 
                class_=input_classes, 
                id=str(field.id), 
                name=str(field.id), 
                value=field.value,
                placeholder=field.placeholder
            )
        ]

        if field.has_errors:
            children.append(
                Div(*[Li(str(e)) for e in field.errors], class_=["invalid-feedback"])
            )
        return Div(
            Div(*children,
                class_=["form-group", "col-md-12"]),
            class_=["form-row"]
        )

    def to_select_field_markup(self, field):
        input_classes = ["of-form-title"]
        if field.has_errors:
            input_classes.append("is-invalid")
        options = [
            Label(field.title, for_=str(field.id), class_=input_classes)
        ]
        
        for opt in field.options:
            if "checkbox" == field.type:
                id = "%d_%d" % (field.id, opt.value)
                name = "%d[]" % (field.id)
            else:
                id = "%d_%d" % (field.id, opt.value)
                name = "%d" % (field.id,)

            input_classes = ["form-check-input"]
            if field.has_errors:
                input_classes.append("is-invalid")
            kwargs = {
            }
            field_value = None
            try:
                if isinstance(field.value, (list,)):
                    if opt.value in field.value:
                        kwargs['checked'] = "checked"
                else:
                    if int(field.value) == opt.value:
                        kwargs['checked'] = "checked"
            except Exception as e:
                pass

            opt = Div(
                Input(
                    class_=input_classes,
                    type=field.type,
                    name=name,
                    id=id,
                    value=str(opt.value),
                    **kwargs,
                ),
                Label(opt.label, class_=["form-check-label"], for_=id),
                class_=["form-check", "form-check-inline"]
            )
            options.append(opt)

        if field.has_errors:
            options.append(
                Div(*[Li(str(e)) for e in field.errors], class_=["invalid-feedback"])
            )
        return Div(
            Div(*options,
                class_=["form-group", "col-md-12"]),
            class_=["form-row"]
        )

    def to_field_markup(self, field):
        method_name = "to_%s_markup" % field.discriminator
        method = getattr(self, method_name)
        # logging.debug("to field markup: %s" % (method_name))
        return method(field)

    def to_view_model(self, model):
        size = len(model.fields)
        fields = []
        
        row = Div(class_=["a"])
        form = Form(row)
        for i in range(size):
            current = model.fields[i]
            previous = i > 0 and model.fields[i-1] or None
            
            # logging.debug("title %s" % (current.title))
            field_markup = self.to_field_markup(current)
            # logging.debug(field_markup)

            row.append(field_markup)
        form.append(Button("提交", class_=["btn", "btn-primary"]))
        return form
            
            