from flask_appbuilder.api import BaseApi, expose
from app import appbuilder
from flask import (
    request,
    jsonify
)

class ControlPanelCollaborationApi(BaseApi):
    resource_name = "cp/form/<form_id>/collaboration"

    @expose('')
    def get(self, form_id):
        data = {}
        return jsonify(data)

    @expose('', methods=["POST"])
    def create(self):
        pass

    @expose('', methods=["DELETE"])
    def delete(self):
        pass

    @expose('role', methods=["POST"])
    def change_role(self):
        pass

appbuilder.add_api(ControlPanelCollaborationApi)