from flask_appbuilder.api import BaseApi, expose
from app import appbuilder
from flask import (
    request,
    jsonify
)
from app.services import FormService

class ControlPanelValueApi(BaseApi):
    resource_name = "cp/value"
    form_service : FormService = FormService()

    @expose('')
    def get(self, form_id):
        """
        get:
          description: "查询表格数据"
          responses:
            200:
              description: Get a form
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Form"
        """
        data = self.form_service.fetch_values(1, 1, 50)
        return jsonify(data)

    @expose('<value_id>')
    def fetch_one(self, value_id):
        pass

    @expose('<value_id>')
    def update(self, value_id):
        pass

    @expose('<value_id>', methods=["DELETE"])
    def delete(self, value_id):
        pass

    @expose('<value_id>')
    def duplicate(self, value_id):
        pass

appbuilder.add_api(ControlPanelValueApi)