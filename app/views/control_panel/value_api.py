from flask_appbuilder.api import BaseApi, expose
from app import appbuilder
from flask import (
    request,
    jsonify
)
from app.services import FormService

class ControlPanelValueApi(BaseApi):
    resource_name = "cp/value"

    def __init__(self):
        super(ControlPanelValueApi, self).__init__()
        self.form_service = FormService()

    @expose('')
    def get(self, form_id):
        """
        ---
        get:
          summary: "查询表格数据"
          description: "查询表格数据"
          responses:
            200:
              description: Get a form
              content:
                application/json:
                  schema:
                    type: array
                    items:
                      $ref: "#/components/schemas/Value"
        """
        data = self.form_service.fetch_values(1, 1, 50)
        return jsonify(data)

    @expose("", methods=["POST"])
    def create(self, values):
        """
        ---
        post:
          summary: "创建表格数据"
          description: "创建表格数据"
          responses:
            200:
              description: Get a form
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Value"
        """
        return jsonify({})

    @expose('/<value_id>')
    def fetch_one(self, value_id):
        """
        ---
        get:
          summary: "查询表格数据"
          description: "查询表格数据"
          parameters:
          - name: value_id
            in: path
            type: integer
            format: int64
            description: "Value 主键ID"
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Value"
        """
        return jsonify({})

    @expose('/<value_id>', methods=["PUT"])
    def update(self, value_id):
        """
        ---
        put:
          summary: "更新表格数据"
          description: "更新表格数据"
          parameters:
          - name: value_id
            in: path
            type: integer
            format: int64
            description: "Value 主键ID"
          requestBody:
            content:
              application/json:
                schema:
                  $ref: "#/components/schemas/Value"
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Value"
        """
        return jsonify({})

    @expose('/<value_id>', methods=["DELETE"])
    def delete(self, value_id):
        """
        ---
        delete:
          summary: "删除表格数据"
          description: "删除表格数据"
          parameters:
          - name: value_id
            in: path
            type: integer
            format: int64
            description: "Value 主键ID"
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Value"
        """
        return jsonify({})

    @expose('/<value_id>')
    def duplicate(self, value_id):
        return jsonify({})

appbuilder.add_api(ControlPanelValueApi)