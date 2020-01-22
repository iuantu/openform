from flask_appbuilder.api import BaseApi, expose
from app import appbuilder
from flask import (
    request,
    jsonify
)

class ControlPanelReporterApi(BaseApi):
    resource_name = "cp/form/<form_id>/reporter"

    @expose('/')
    def get(self, form_id):
        """
        get:
          description: "查询报表"
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: "string"
        """
        data = {}
        return jsonify(data)

appbuilder.add_api(ControlPanelReporterApi)