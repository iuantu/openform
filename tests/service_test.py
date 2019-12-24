from . import OpenFormTestCase
from app.services import FormService
from app.examples import MVP_FORM

class FormServiceTest(OpenFormTestCase):

    def test_create(self):
        service = FormService(self.db)
        service.add_new_form(MVP_FORM)

    def test_update(self):
        pass

form = {
    "id": 1,
    "title": "在 JotForm 上测试 openform MVP",
    "fields": [
        {
            "id": 1,
            "title": "真实姓名",
            "discriminator": "text_field",
            "multiple": False,
            "placeholder": "请输入你的真实姓名",
        },
        {
            "id": 2,
            "title": "如果我们必须要“模仿”一个表单构建器，我们应该模仿谁？",
            "discriminator": "select_field",
            "multiple": False,
            "is_radio": True,
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
            ]
        },
    ]
}