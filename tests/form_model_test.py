from app.models import (
    Field,
    Form,
    TextField,
    SelectField,
    Option,
)
from . import OpenFormTestCase

class FormModelTest(OpenFormTestCase):

    def test_create_form(self):
        form = Form()

        self.db.session.add(form)

        field = Field()
        field.name = 'title'

        form.fields.append(field)

        text = TextField()
        text.default = 'test'
        form.fields.append(text)

        self.db.session.add(field)
        self.db.session.add(text)
        self.db.session.commit()

    def test_select_field(self):
        opt1 = Option("男", 1)
        opt2 = Option("女", 0)
        
        field = SelectField(True, [opt1, opt2])
        form = Form([field])
        self.db.session.add(form)
        self.db.session.commit()
        
        self.assertEquals(form.id, 1)
        self.assertEquals(opt1.id, 1)
        self.assertEquals(opt2.id, 2)
        self.assertEquals(field.multiple, True)