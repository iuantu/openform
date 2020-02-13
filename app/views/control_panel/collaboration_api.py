from flask_appbuilder.api import BaseApi, expose
from app import appbuilder
from app.services import FormService
from app.services.form_collaboration import FormCollaborationService
from flask import (
    request,
    jsonify
)
from flask_jwt_extended import current_user, jwt_required

class ControlPanelFormRoleApi(BaseApi):
    resource_name = 'cp/form/role'

    def __init__(self):
        super().__init__()

        self.form_service = FormService()

    @expose('')
    def get(self):
        """Get a form
        ---
        get:
          responses:
            200:
              description: 查询表单协作的角色
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Form"
        """
        roles = self.form_service.all_roles()
        return jsonify([role.asdict() for role in roles])

appbuilder.add_api(ControlPanelFormRoleApi)

class CollaborationAssembler:

    def to_dto(self, collaborator):
        return {
            'id': collaborator.id,
            "user": {
                'id': collaborator.user.id,
                'username': collaborator.user.username,
            },
            'role': {
                'name': collaborator.role.name,
                'id': collaborator.role.id,
            },
            'form_id': collaborator.form_id,
            'created_at': collaborator.created_at,
            'updated_at': collaborator.updated_at,
        }

    def to_dto_list(self, collaborators):
        return [
            self.to_dto(collaborator)
            for collaborator in collaborators
        ]

class ControlPanelCollaborationApi(BaseApi):
    resource_name = "cp/form/<form_id>/collaboration"

    def __init__(self):
        super().__init__()

        self.service = FormCollaborationService()
        self.assembler = CollaborationAssembler()

    @jwt_required
    @expose('')
    def get(self, form_id):
        """
        ---
        get:
          responses:
            200:
              description: 查询表单的协作者
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Form"
        """
        collaborators = self.service.collaborators(form_id)
        return jsonify(self.assembler.to_dto_list(collaborators))

    @jwt_required
    @expose('', methods=["POST"])
    def create(self, form_id):
        """
        ---
        post:
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/FormCreation'
          responses:
            200:
              description: 加入协作者
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Form"
        """
        command = request.json.copy()
        command['form_id'] = form_id
        command['current_user'] = current_user
        collaborator = self.service.new_collaborator(command)
        return jsonify(collaborator.asdict()), 201

    @jwt_required
    @expose('<user_id>', methods=["DELETE"])
    def delete(self, form_id, user_id):
        """
        ---
        post:
          responses:
            200:
              description: 移除协作者
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Form"
        """
        collaborator = self.service.remove(form_id, user_id)
        return jsonify(self.assembler.to_dto(collaborator))

    @jwt_required
    @expose('<user_id>', methods=["PUT"])
    def change(self, form_id, user_id):
        """
        ---
        put:
          responses:
            200:
              description: 修改协作者的角色
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Form"
        """
        role_id = request.json['role_id']
        collaborator = self.service.change_collaborator(form_id, user_id, role_id)
        return jsonify(self.assembler.to_dto(collaborator))

appbuilder.add_api(ControlPanelCollaborationApi)