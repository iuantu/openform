from flask_appbuilder.api import BaseApi, expose
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
        
        return self.response(200, **{})

    @expose('/{id}', methods=['PUT'])
    def update(self):
        """Create a form
        ---
        put:
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
        
        return self.response(200, **{})

    @expose('/{id}', methods=['DELETE'])
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
        
        return self.response(200, **{})

    @expose('/{id}/publish', methods=['POST'])
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
        
        return self.response(200, **{})

    @expose('/{id}/publish', methods=['DELETE'])
    def delete(self):
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
        
        return self.response(200, **{})

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
        
        return self.response(200, **{})

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
        
        return self.response(200, **{})

appbuilder.add_api(ControlPanelFormView)