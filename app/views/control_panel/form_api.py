import csv
import io
from flask_appbuilder.api import BaseApi, expose
from app import appbuilder, db
from flask import (
    request,
    jsonify,
    g,
    stream_with_context,
    Response
)
from flask_jwt_extended import current_user, jwt_required
from app.services import FormService
from app.models import (
    EventType,
    PageRequest,
    EventRepository,
    ValueRepository,
    FormRepository
)

class ControlPanelFormApi(BaseApi):

    resource_name = 'cp/form'
    form_service = FormService()

    def __init__(self):
        super().__init__()

        self.event_repository = EventRepository(db)
        self.value_repository = ValueRepository(db)
        self.form_repository = FormRepository(db)
  
    @jwt_required
    @expose('', methods=['POST'])
    def create(self):
        """Create a form
        ---
        post:
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Form'
          responses:
            200:
              description: Create a form
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/Form'
        """
        form = request.json.copy()
        form["user_id"] = current_user.id
        form = self.form_service.add_new_form(form)
        
        return jsonify(form.asdict()), 201

    @expose('/{id}', methods=['PUT'])
    def update(self):
        """Create a form
        ---
        put:
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Form'
          responses:
            200:
              description: Create a form
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/Form'
        """
        
        return self.response(200, **{})

    @expose('/{id}/publish', methods=['DELETE'])
    def publish(self):
        """Publish a form
        ---
        delete:
          responses:
            200:
              description: Publish a form
              content:
                application/json:
                  schema:
                    $ref: '#/components/schemas/Form'
        """
        
        return self.response(200, **{})

    @expose('/{id}/publish', methods=['DELETE'])
    def unpublish(self):
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

    @jwt_required
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
        forms = self.form_service.fetch_forms(
            current_user.id, PageRequest.create(request.args)
        )
        return jsonify(forms.asdict())

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

    @jwt_required
    @expose("/<form_id>/summary", methods=["GET"])
    def summary(self, form_id):
        user = current_user
        submit_count_by_days = self.value_repository.count_by_8_days(user.id, form_id)
        form = self.form_repository.find_one(form_id)

        return jsonify({
            "submit_count": self.value_repository.count_all(user.id, form_id),
            "submit_count_today": self.value_repository.count_today(
                user.id, form_id),
            "reads_today": self.event_repository.count(form_id, EventType.VIEW_FORM),
            "submit_count_by_days": submit_count_by_days,
            "read_count_by_days": self.event_repository.count_by_8_days(form_id, EventType.VIEW_FORM),
            "submit_count_by_mintes": self.value_repository.count_by_24_minute(
                user.id, form_id),
            "form": form.asdict(),
        })

    @jwt_required
    @expose("/<form_id>/export", methods=["GET"])
    def export(self, form_id):
        # TODO: 根据 Request Content Type 来导出返回的内容，例如JSON
        form_id = int(form_id)
        count = self.value_repository.count(form_id)
        
        def generate():
            args = [int(form_id), PageRequest.create(request.args)]
            i = 0
            position = 0
            while i < count:
                args[1].page = i + 1
                values = self.value_repository.find(*args)
                if i == 0:
                    iostream = io.StringIO()
                    first = values[0]
                    keys = first.asdict().keys()
                    csv_writer = csv.DictWriter(iostream, fieldnames=keys)
                    csv_writer.writeheader()

                for value in values:
                    csv_writer.writerow(value.asdict())
                
                iostream.seek(position)
                for line in iostream.readline():
                    print(line)
                    yield line
                position = iostream.tell()
                i += 1

        response = Response(stream_with_context(generate()))
        response.headers["Content-Type"] = "text/csv"

        return response
appbuilder.add_api(ControlPanelFormApi)
