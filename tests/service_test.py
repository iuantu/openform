from . import OpenFormTestCase
from app.services import FormService
from app.examples import MVP_FORM
from app import models

class FormServiceTest(OpenFormTestCase):

    def test_create(self):
        service = FormService(self.db)
        form = service.add_new_form(MVP_FORM)
        for f in form.fields:
            print(f.id)

        v = service.submit(1, {
            "name": None,
            2: 1,
            3: "18621068396"
        })
        
        i = 1
        for opt in form.fields[1].options:
            self.assertEquals(i, opt.value)
            i += 1

        service.change_form(form.id, CHANGED_FORM)
        changed = service.fetch_form(form.id)

        self.assertEquals("在 JotForm 上测试 openform MVP Changed", changed.title)
        for field in changed.fields:
            if field.id == 3:
                self.assertTrue(False)

            if field.id == 2:
                for option in field.options:
                    if option.id == 7:
                        self.assertTrue(False)

        mobile = changed.fields[-1]
        self.assertEquals("手机号码", mobile.title)
        print(changed.fields)
        from app import db
        for i in db.session.query(models.Field).all():
            print(i.to_json())

        v = service.submit(1, {
            "name": "魏琮举",
            2: 1,
            3: "18621068396"
        })
        v = service.submit(1, {
            "name": None,
            2: 1,
            3: "18621068396"
        })
        print(changed.fields[0].title)
        print(changed.fields[0].errors)

    def test_update(self):
        pass

CHANGED_FORM = {
    "id": 1,
    "title": "在 JotForm 上测试 openform MVP Changed",
    "fields": [
        {
            "id": 1,
            "form_id": 1,
            "name": "name",
            "title": "真实姓名",
            "discriminator": "text_field",
            "multiple": False,
            "placeholder": "请输入你的真实姓名",
            "constraints": [
                {
                    "discriminator": "required_constraint"
                }
            ]
        },
        {
            "id": 2,
            "form_id": 1,
            "title": "如果我们必须要“模仿”一个表单构建器，我们应该模仿谁？",
            "discriminator": "select_field",
            "multiple": False,
            "options": [
                {
                    "id": 1,
                    "label": "金数据"
                },
                {
                    "id": 2,
                    "label": "帆软"
                },
                {
                    "id": 3,
                    "label": "轻流"
                },
                {
                    "id": 4,
                    "label": "问卷星"
                },
                {
                    "id": 5,
                    "label": "JotForm"
                },
                {
                    "id": 6,
                    "label": "Typeform"
                },
                {
                    "id": 8,
                    "label": "Other",
                    "editable": True
                }
            ],
        },
        {
            "title": "手机号码",
            "discriminator": "text_field",
            "multiple": False,
            "placeholder": "请输入你的手机号码",
        },
    ]
}