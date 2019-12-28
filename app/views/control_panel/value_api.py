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

    @expose('<form_id>')
    def get(self, form_id):
        data = self.form_service.fetch_values(1, 1, 50)
        return jsonify(data)

appbuilder.add_api(ControlPanelValueApi)