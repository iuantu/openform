def url():
    return "http://localhost:5000/mysql/form"

def method():
    return "POST"

def headers():
    return {
        "Content-Type": ["application/json"]
    }

def data():
    return {
        "form_id": 1,
        "user_id": 1,
        "values": {
            "name": "CJ",
            "email": "cj@iuantu.com",
            "title": "Python 工程师",
            "company": "元图（上海）网络科技有限公司",
            "bio": "简介： 不知道该说什么。"
        }
    }