from app import appbuilder
from flask_appbuilder.api import BaseApi, expose
from app.views.schema import SCHEMAS
from app.views.utils import to_user_agent
from app.services import FormService
from flask import jsonify, request
from flask_jwt_extended import current_user


class FormApiAssembler:

    def assemble(self, form):
        r = request.json['fields']
        for field in form.fields:
            fieldValue = r.get(str(field.id))
            field.value = field.format(fieldValue)


class FormApi(BaseApi):
    resource_name = 'form'
    apispec_parameter_schemas = SCHEMAS
    assembler = FormApiAssembler()

    form_service = FormService()

    @expose('<form_id>', methods=['GET'])
    def get(self, form_id):
        """Get a form 
        ---
        get:
          parameters:
          - name: form_id
            description: "表单ID"
            required: true
            type: integer
            format: int64
          responses:
            '200':
              description: Get a form
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/Form'
        """
        user_agent = to_user_agent(request)
        form = self.form_service.fetch_form(form_id, current_user)

        return jsonify(form.asdict(follow={
            'fields': {
                "follow": {
                    "options": {},
                    "constraints": {},
                }
            }
        }))

    @expose('/<form_id>/value', methods=['POST'])
    def submit(self, form_id):
        """Submit a form 
        ---
        post:
          description: "提交表单数据"
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Value"
        """
        status = 200

        user_agent = to_user_agent(request)
        form = self.form_service.fetch_form(form_id, None)
        self.assembler.assemble(form)

        if form.validate():
            response = self.form_service.submit(form, None, user_agent)\
                .asdict(follow={})
        else:
            status = 400
            response = {
                "fields": [
                    dict(id=field.id, errors=[str(error) for error in field.errors])
                    for field in form.fields
                ]
            }

        return jsonify(response), status

    @expose('/<form_id>/value/<int:value_id>', methods=['PUT'])
    def form_value_edit(self, form_id, value_id):
        status = 200

        user_agent = to_user_agent(request)
        form = self.form_service.fetch_form(form_id, None)
        self.assembler.assemble(form)

        if form.validate():
            response = self.form_service.submit(form, None, user_agent, value_id)\
                .asdict(follow={})
        else:
            status = 400
            response = {
                "fields": [
                    dict(id=field.id, errors=[str(error) for error in field.errors])
                    for field in form.fields
                ]
            }

        return jsonify(response), status

    @expose('/<form_id>/<int:value_id>', methods=['GET'])
    def form_value_edit(self, form_id, value_id):
        return jsonify(self.form_service.fetch_value(value_id))

appbuilder.add_api(FormApi)
