from flask_appbuilder.api import BaseApi, expose
from app import appbuilder
from flask import (
    request,
    jsonify
)
from app.models import PageRequest
from app.services import FormService

class ControlPanelUserApi(BaseApi):

    resource_name = 'cp/user'
    form_service = FormService()

    @expose('/', methods=['POST'])
    def register(self):
        """

        :return:
        """
        user = request.json.copy()
        form = self.form_service.add_new_user(user)
        return jsonify(form.asdict())

    @expose('/collaborators/add', methods=['GET'])
    def add_collaborators(self, username):
        username = request.json['username']
        form_id = request.json['form_id']
        collaboration_user = self.form_service.add_new_collaboration_user(username, form_id)
        return jsonify(collaboration_user.asdict())

    @expose('/collaborators/list/<form_id>', methods=['GET'])
    def get_collaborators_list(self, form_id):
        collaboration_users = self.form_service.fetch_collaboration_users(
            form_id, PageRequest.create(request.args)
        )
        return jsonify(collaboration_users.asdict())

    @expose('/collaborators/<c_id>', methods=['DELETE'])
    def delete(self, c_id):
        collaboration_user = self.form_service.remove_collaboration_user(c_id)
        return jsonify(collaboration_user.asdict())