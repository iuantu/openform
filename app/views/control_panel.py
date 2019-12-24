from flask_appbuilder.api import BaseApi, expose
from . import appbuilder
from flask import (
    request,
    jsonify
)
from datetime import datetime
from app.services import FormService

from sqlalchemy.ext.declarative import DeclarativeMeta

import json
class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

class ControlPanelFormView(BaseApi):

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


class ControlPanelFieldView(BaseApi):
    
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

class ControlPanelValueView(BaseApi):
    resource_name = "cp/value"

    form_service : FormService = FormService()

    @expose('<form_id>')
    def get(self, form_id):
        data = self.form_service.fetch_values(1, 1, 50)
        return jsonify(data)


appbuilder.add_api(ControlPanelFormView)
appbuilder.add_api(ControlPanelFieldView)
appbuilder.add_api(ControlPanelValueView)