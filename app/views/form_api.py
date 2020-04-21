from app import appbuilder
from flask_appbuilder.api import BaseApi, expose
from app.views.parameter_container import ParameterContainer
from app.views.schema import SCHEMAS
from app.views.utils import to_user_agent
from app.services import FormService
from flask import jsonify, request
from flask_jwt_extended import current_user
from app.views.models import FormViewModelAssembler


class FormApi(BaseApi):
    resource_name = 'form'
    apispec_parameter_schemas = SCHEMAS
    assembler = FormViewModelAssembler()

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

    @expose('/<form_id>', methods=['POST'])
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
        user_agent = to_user_agent(request)
        form = self.form_service.fetch_form(form_id, None)
        try:
            form_view = self.assembler.to_view_model(form, ParameterContainer())
        except Exception as e:
            response = {
                "message": e
            }

            status = 400

            return jsonify(response), status

        status = 200
        if form.validate():
            try:
                response = self.form_service.submit(form, None, user_agent)
            except:
                response = {
                    "message": "exception"
                }

                status = 400
        else:
            status = 400
            response = {
                "fields": [
                    dict(id=field.id, errors=[str(error) for error in field.errors])
                    for field in form.fields
                ]
            }

        return jsonify(response), status


appbuilder.add_api(FormApi)
