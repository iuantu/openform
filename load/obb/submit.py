import core


class HttpRequestBehaviour(core.AbstractHttpRequestBehaviour):

    user_id = 1

    def __init__(self, index):
        self.index = index

    def url(self):
        return "http://localhost:5000/mysql/form"

    def method(self):
        return "POST"

    def headers(self):
        return {
            "Content-Type": ["application/json"]
        }

    def data(self):
        if self.index % 10 == 0:
            HttpRequestBehaviour.user_id += 1

        user_id = HttpRequestBehaviour.user_id
        return {
            "form_id": 1,
            "user_id": user_id,
            "values": {
                "name": "CJ",
                "email": "cj@iuantu.com",
                "title": "Python 工程师",
                "company": "元图（上海）网络科技有限公司",
                "bio": "简介： 不知道该说什么。"
            }
        }