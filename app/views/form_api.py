from app import appbuilder
from flask_appbuilder.api import BaseApi, expose
from app.views.schema import SCHEMAS
from app.views.utils import to_user_agent
from app.services import FormService
from flask import jsonify, request
from flask_jwt_extended import current_user

class FormApi(BaseApi):
    resource_name = 'form'
    apispec_parameter_schemas = SCHEMAS

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

    @expose('/{id}/value', methods=['POST'])
    def submit(self):
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
        pass

appbuilder.add_api(FormApi)