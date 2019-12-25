import logging
from app.markup import Div, Form, Label, Input, Button

class FormViewModel:
    pass

class FieldViewModel:
    def __init__(self):
        pass

class FormViewModelAssembler:


    def to_text_field_markup(self, field):
        return Div(
            Div(*[
                Label(field.title, for_=str(field.id)),
                Input(type="text", 
                    class_=["form-control"], 
                    id=str(field.id), 
                    name=str(field.id), 
                    placeholder=field.placeholder
                )],
                class_=["form-group", "col-md-12"]),
            class_=["form-row"]
        )

    def to_select_field_markup(self, field):

        options = [
            Label(field.title, for_=str(field.id))
        ]
        for opt in field.options:
            logging.info("option value %d" % (opt.value))
            if "checkbox" == field.type:
                id = "%d_%d" % (field.id, opt.value)
                name = "%d[]" % (field.id)
            else:
                id = "%d_%d" % (field.id, opt.value)
                name = "%d" % (field.id,)
            opt = Div(
                Input(
                    class_=["form-check-input"],
                    type=field.type,
                    name=name,
                    id=id,
                    value=str(opt.value)
                ),
                Label(opt.label, class_=["form-check-label"], for_=id),
                class_=["form-check", "form-check-inline"]
            )
            options.append(opt)

        return Div(
            Div(*options,
                class_=["form-group", "col-md-12"]),
            class_=["form-row"]
        ) 

    def to_field_markup(self, field):
        method_name = "to_%s_markup" % field.discriminator
        method = getattr(self, method_name)
        logging.debug("to field markup: %s" % (method_name))
        return method(field)

    def to_view_model(self, model):
        size = len(model.fields)
        fields = []
        
        row = Div(class_=["a"])
        form = Form(row)
        for i in range(size):
            current = model.fields[i]
            previous = i > 0 and model.fields[i-1] or None
            
            logging.debug("title %s" % (current.title))
            field_markup = self.to_field_markup(current)
            logging.debug(field_markup)

            row.append(field_markup)
        form.append(Button("提交", class_=["btn", "btn-primary"]))
        return form
            
            