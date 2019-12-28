from flask_appbuilder.api import BaseApi, expose
from app import appbuilder
from flask import (
    request,
    jsonify
)
from app.services import FormService

class ControlPanelFieldApi(BaseApi):
    
    resource_name = 'cp/field'

    form_service : FormService = FormService()

    @expose('', methods=['POST'])
    def create(self):
        """Create a field
        ---
        post:
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Field'
          responses:
            200:
              description: Create a field
              content:
                application/json:
                schema:
                    $ref: '#/components/schemas/Field'
        """

        field = self.form_service.add_new_field(request.json)
        return jsonify(field.asdict()), 201

    @expose('<field_id>', methods=['PUT'])
    def update(self, field_id):
        changed = self.form_service.change_field(field_id, request.json)
        return jsonify(changed.asdict())

    @expose('<field_id>', methods=['DELETE'])
    def delete(self, field_id):
        field = self.form_service.remove_field(field_id)
        return jsonify(field.asdict())

    @expose('<field_id>')
    def get(self, field_id):
        """Get a form
        ---
        get:
          
          responses:
            200:
              description: Get a form
              content:
                application/json:
                schema:
                    $ref: '#/components/schemas/Field'
        """

        field = self.form_service.fetch_field(field_id)
        return jsonify(field.asdict())

appbuilder.add_api(ControlPanelFieldApi)