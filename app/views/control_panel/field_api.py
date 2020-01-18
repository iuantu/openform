from flask_appbuilder.api import BaseApi, expose
from app import appbuilder
from app.models import PageRequest
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

    @expose('/list_by_form_id/<from_id>', methods=['GET'])
    def get_list(self, form_id):
        """
            表单数据查询接口，包括排序
        :param form_id:
        :return:
        """

        fields = self.form_service.fetch_fields(form_id, PageRequest.create(request.args))
        return jsonify(fields.asdict())

    @expose('/add_by_form_id/<from_id>', methods=['POST'])
    def add_by_form_id(self, form_id):
        """
            插入提条数据到表单
        :param form_id:
        :return:
        """
        field = request.json.copy()
        field["form_id"] = form_id
        form = self.form_service.add_new_field(field)
        return jsonify(form.asdict()), 200
appbuilder.add_api(ControlPanelFieldApi)
