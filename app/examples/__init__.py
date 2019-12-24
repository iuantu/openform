import json
from app.models import Form, TextField

# f = Form()

# name = TextField(title="真实姓名", )

MVP_FORM = json.loads("""{
    "title": "在 JotForm 上测试 openform MVP",
    "fields": [
        {
            "title": "真实姓名",
            "discriminator": "text_field",
            "multiple": false,
            "placeholder": "请输入你的真实姓名"
        },
        {
            "title": "如果我们必须要“模仿”一个表单构建器，我们应该模仿谁？",
            "discriminator": "select_field",
            "multiple": false,
            "type": "radio",
            "options": [
                {
                    "label": "金数据"
                },
                {
                    "label": "帆软"
                },
                {
                    "label": "轻流"
                },
                {
                    "label": "问卷星"
                },
                {
                    "label": "JotForm"
                },
                {
                    "label": "Typeform"
                },
                {
                    "label": "Google Forms"
                },
                {
                    "label": "Other",
                    "editable": true
                }
            ]
        },
        {
            "title": "对于提交按钮组件，除了其本身之外，openform MVP#1 的开发还应该包含如下哪些配置项？",
            "discriminator": "select_field",
            "multiple": true,
            "type": "checkbox",
            "options": [
                {
                    "label": "按钮在页面中的左中右对齐",
                    "default": true
                },
                {
                    "label": "按钮文字的自定义"
                },
                {
                    "label": "可开启保存按钮以便稍后继续"
                },
                {
                    "label": "可开启打印按钮以便调用打印机"
                },
                {
                    "label": "可选的预设按钮样式"
                },
                {
                    "label": "可上传图片作为按钮"
                },
                {
                    "label": "Other",
                    "editable": true
                }
            ]
        }
    ]
}""")