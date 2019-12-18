from . import appbuilder
from flask_appbuilder.api import BaseApi, expose
from app.views.schema import SCHEMAS

class FormApi(BaseApi):
    resource_name = 'form'
    apispec_parameter_schemas = SCHEMAS

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

    @expose('/{id}', methods=['POST'])
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
        pass

appbuilder.add_api(FormApi)