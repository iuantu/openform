import json

from flask import request, session
from flask_appbuilder.api import BaseApi, expose
from requests import Session

from app import db
from app.models import Form
from . import appbuilder


class ControlPanelFormView(BaseApi):

    resource_name = 'cp/form'

    @expose('/', methods=['POST'])
    def create(self):
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
        request_data = json.loads(request.data)

        form = Form()
        form.title = request_data['title']
        form.creator_id = request.headers.get('userId')
        db.session.add(form)
        db.session.commit()

        return self.response(200, form_id = form.id)

    @expose('/<id>/', methods=['PUT'])
    def update(self, id):
        """update a form
        ---
        put:
          responses:
            200:
              description: update a form
              content:
                application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
        """
        form = Form.query.filter_by(id=id).first()

        request_data = json.loads(request.data)
        form.title = request_data['title']
        db.session.commit()
        return self.response(200, data=request_data)

    @expose('/{id}/publish', methods=['PUT'])
    def publish(self):
        """Publish a form
        ---
        post:
          responses:
            200:
              description: Publish a form
              content:
                application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
        """
        Form.query.filter_by(id=id).update(status=1)
        return self.response(200, form_id = id)

    @expose('/<id>/unpublish', methods=['PUT'])
    def unpublish(self):
        """Unpublish a form
        ---
        delete:
          responses:
            200:
              description: Unpublish a form
              content:
                application/json:
                schema:
                  type: object
                  properties:
                    message:
                      type: string
        """
        Form.query.filter_by(id=id).update(status=0)
        return self.response(200, form_id = id)

    @expose('/<id>', methods=['DELETE'])
    def delete(self, id):
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
        form = Form.query.filter_by(id=id).first()
        db.session.delete(form)

        return self.response(200, form_id = id)

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
        forms = Form.query.all()
        return self.response(200, data = json.dumps(forms))

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
        form = Form.query.filter_by(id=id).first()
        return self.response(200, form=form)


appbuilder.add_api(ControlPanelFormView)