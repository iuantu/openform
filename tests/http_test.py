import os
import json
import requests

session = requests.Session()
URL = os.getenv('BASE_URL', "https://staging.oform.cn/api/v1")

USER = "%s/user/" % URL
USER_LOGIN_URL = "%s/security/login" % URL
FORM_LIST = "%s/cp/form" % URL
FORM_CREATE_URL = "%s/cp/form" % URL
FORM_ID = 0
FORM = None
def test_user_register():
    response = session.post(USER, json={
        'username': 'test',
        'email': 'test@example.com',
        'password': '111111',
    })

def test_user_login():
    response = session.post(USER_LOGIN_URL, json={
        "password": "111111",
        "provider": "db",
        "refresh": True,
        "username": "test"
    })
    
    tokens = response.json()
    session.headers.update({'Authorization': "Bearer %s" % tokens['access_token']})

def test_create_form():
    global FORM
    payload = {
        "title": "一些小问题",
        "description": "一些小问题",
        "fields": [
            {
                "title": "你喜欢的编程语言",
                "description": "你喜欢的编程语言",
                "discriminator": "select_field",
                "multiple": True,
                "type": "checkbox",
                "options": [
                    {
                        "label": "PHP",
                        "default": True
                    }
                ],
                "constraints": [
                    {
                        "discriminator": "required_constraint"
                    }
                ]
            },
            {
                "title": "",
                "description": "这是一段描述",
                "discriminator": "description_field",
            }
        ]
    }
    response = session.post(FORM_CREATE_URL, json=payload)
    FORM = response.json()
    assert len(FORM['fields'][0]['options']) > 0

def test_form_list():
    global FORM_ID
    response = session.get(FORM_LIST)
    forms = response.json()
    FORM_ID = forms['data'][0]['id']
    
    assert FORM_ID > 0

def test_form():
    response = session.get("%s/cp/form/%d" % (URL, FORM_ID))
    form = response.json()

    assert "一些小问题" == form["description"]
    assert "你喜欢的编程语言" == form['fields'][0]['description']

    assert "这是一段描述" == form['fields'][1]['description']

def test_change_form():
    field = FORM['fields'][0]
    field_id = field['id']
    option = field['options'][0]
    option_id = option['id']
    constraint = field['constraints'][0]
    response = session.put("%s/cp/form/%d" % (URL, FORM_ID), json={
        "title": "一些小问题",
        "fields": [
            {
                "id": field_id,
                "title": "你喜欢的编程语言？",
                "discriminator": "select_field",
                "multiple": True,
                "type": "checkbox",
                "options": [
                    {
                        "id": option_id,
                        "label": "PHP"
                    },
                    {
                        "label": "Java"
                    }
                ],
                "constraints": [
                    {
                        "discriminator": "required_constraint"
                    }
                ]
            }
        ]
    })

    assert len(response.json()['fields'][0]['options']) == 2