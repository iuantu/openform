from flask_appbuilder.api import BaseApi, expose
from app import appbuilder
from flask import (
    request,
    jsonify,
    g,
)
from flask_jwt_extended import current_user, jwt_required
from app.services import FormService
from app.models import PageRequest

class ControlPanelFormApi(BaseApi):

    resource_name = 'cp/form'
    form_service = FormService()
  
    @jwt_required
    @expose('', methods=['POST'])
    def create(self):
        """Create a form
        ---
        post:
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Form'
          responses:
            200:
              description: Create a form
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/Form'
        """
        form = request.json.copy()
        form["user_id"] = current_user.id
        form = self.form_service.add_new_form(form)
        
        return jsonify(form.asdict()), 201

    @expose('/{id}', methods=['PUT'])
    def update(self):
        """Create a form
        ---
        put:
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Form'
          responses:
            200:
              description: Create a form
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/Form'
        """
        
        return self.response(200, **{})

    @expose('/{id}/publish', methods=['DELETE'])
    def publish(self):
        """Publish a form
        ---
        delete:
          responses:
            200:
              description: Publish a form
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/Form'
        """
        
        return self.response(200, **{})

    @expose('/{id}/publish', methods=['DELETE'])
    def unpublish(self):
        """Delete a form
        ---
        delete:
          responses:
            200:
              description: Delete a form
              content:
                application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
        """
        
        return self.response(200, **{})

    @jwt_required
    @expose('/', methods=['GET'])
    def get_list(self):
        """Get form list
        ---
        get:
          responses:
            200:
              description: Get form list
              content:
                application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
        """
        forms = self.form_service.fetch_forms(
            current_user.id, PageRequest.create(request.args)
        )
        return jsonify(forms.asdict())

    @expose('/{id}', methods=['GET'])
    def get_detail(self):
        """Get a form
        ---
        get:
          responses:
            200:
              description: Get a form
              content:
                application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
        """
        
        return self.response(200, **{})

appbuilder.add_api(ControlPanelFormApi)
