from . import appbuilder
from flask import request
from flask_appbuilder.api import BaseApi, expose
from app.views.schema import SCHEMAS
import json
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .. import db
from ..models import Rows


class FormApi(BaseApi):
    resource_name = 'form'
    apispec_parameter_schemas = SCHEMAS
    # data_model = SQLAInterface(Rows)

    @expose('/{id}', methods=['GET'])
    def get(self):
        """Get a form
        ---
        get:
          responses:
            '200':
              description: Get a form
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/Form'
        """
        pass

    @expose('/mysql', methods=['POST'])
    def submit(self):
        """Submit a form
        ---
        post:
          responses:
            200:
              description: Submit form list
              content:
                application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
        """
        form_values = request.json
        user_id = form_values['user_id']
        form_id = form_values['form_id']

        new_rows = Rows(user_id=user_id, form_id=form_id, values=json.dumps(form_values))

        session = db.session
        try:
            session.add(new_rows)
            session.commit()
        finally:
            session.close()
        return self.response(200, message='表单提交成功')

    # @expose('/{id}', methods=['GET'])
    # def submit(self):
    #     return "123"


appbuilder.add_api(FormApi)
