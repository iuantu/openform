from flask_appbuilder.api import BaseApi, expose
from app import appbuilder
from flask import (
    request,
    jsonify
)
from app.services import FormService

class ControlPanelFormApi(BaseApi):

    resource_name = 'cp/form'

    form_service = FormService()

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
        form = self.form_service.add_new_form(request.json)
        
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
        
        return self.response(200, **{})

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
