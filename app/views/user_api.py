from flask_appbuilder.api import BaseApi, expose
from . import appbuilder
from flask import g, jsonify
from flask_appbuilder.api import safe
from flask_jwt_extended import current_user, jwt_required

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
    @jwt_required
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
        user = self.appbuilder.sm.find_user(username=current_user.username)
        dto = user.asdict()
        del dto['password']
        return jsonify(dto)

appbuilder.add_api(UserApi)