from flask_appbuilder.api import BaseApi, expose
from . import appbuilder


class UserApi(BaseApi):
    resource_name = 'user'

    @expose('/', methods=['POST'])
    def register(self):
        """Create a form
        ---
        post:
          responses:
            200:
              description: Create a form
              content:
                application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
        """
        pass

    @expose('/', methods=['GET'])
    def get(self):
        """Get user
        ---
        post:
          responses:
            200:
              description: Get user
              content:
                application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
        """
        pass


appbuilder.add_api(UserApi)