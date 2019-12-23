from flask import render_template
from flask_appbuilder import expose
from flask_appbuilder.api import BaseApi

from . import appbuilder, db

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::

    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::

    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()


class OpenForm(BaseApi):
    # base_route = '/openform/v1'

    @expose('/forms/', methods=['POST'])
    def create(self):
        """create a form
        ---
        post:
          responses:
            201:
              description: 创建表单
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
        """
        return self.response(201, message="表单创建成功")

    @expose('/forms/info/{form_id}', methods=['GET'])
    def retrieve(self):
        """get form info by form_id
        ---
        get:
          responses:
            200:
              description: 查询指定表单的详情
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: json
        """
        return self.response(200, message="表单详情查询成功")

    @expose('/forms/', methods=['GET'])
    def list(self):
        """get form info list
        ---
        get:
          responses:
            200:
              description: 查询表单列表数据
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: json
        """
        return self.response(200, message="表单列表查询成功")

    @expose('/forms/update_form/{form_id}', methods=['POST'])
    def update(self):
        """update a form by form_id
        ---
        post:
          responses:
            200:
              description: 更新指定表单
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
        """
        return self.response(200, message="表单创建成功")

    @expose('/forms/delete_form/{form_id}', methods=['GET'])
    def delete(self):
        """delete a form by form_id
        ---
        get:
          responses:
            200:
              description: 删除指定的表单
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      message:
                        type: string
        """
        return self.response(200, message="表单删除成功")


appbuilder.add_api(OpenForm)
