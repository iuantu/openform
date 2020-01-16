from flask_appbuilder.api import BaseApi, expose
from . import appbuilder
from flask import g, jsonify, request
from flask_appbuilder.api import safe
from flask_jwt_extended import current_user, jwt_required
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
)
from app import db

class UserApi(BaseApi):
    resource_name = 'user'

    @expose('/', methods=['POST'])
    def register(self):
        """注册用户
        ---
        post:
          description: "注册用户"
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      jwt:
                        $ref: "#/components/schemas/JWT"
                      user:
                        $ref: "#/components/schemas/User"
        """
        registration = request.json
        username = registration["username"]
        email = registration["email"]
        password = registration["password"]

        user = self.appbuilder.sm.add_user(
            username, '', '', email, self.appbuilder.sm.find_role("Public"), password
        )

        if not user:
            return {
                "message": "注册失败，请检查用户名或密码。"
            }

        access_token = create_access_token(
            identity=user.id, fresh=True
        )
        refresh_token = create_refresh_token(
            identity=user.id
        )

        return jsonify({
            "user": user.asdict(),
            "jwt": {
                "access_token": access_token,
                "refresh_token": refresh_token
            }
        })

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
                    $ref: "#/components/schemas/User"
        """
        user = self.appbuilder.sm.find_user(username=current_user.username)
        dto = user.asdict()
        del dto['password']
        return jsonify(dto)

appbuilder.add_api(UserApi)