import csv
import io
import logging
from flask_appbuilder.api import BaseApi, expose
from app import appbuilder, db
from app.views.decorators import form_guard
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
    FormRepository,
)

class ControlPanelFormApi(BaseApi):

    resource_name = 'cp/form'
    form_service = FormService()

    def __init__(self):
        super().__init__()

        self.event_repository = EventRepository(db)
        self.value_repository = ValueRepository(db)
        self.form_repository = FormRepository(db)
        self.logger = logging.getLogger('ControlPanelFormApi')

    @jwt_required
    @expose('', methods=['POST'])
    def create(self):
        """Create a form
        ---
        post:
          summary: 创建表单
          description: 创建表单
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/FormCreation'
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
        
        return jsonify(form.asdict(follow={
            'fields': {
                "follow": {
                    "options": {},
                    "constraints": {},
                }
            }
        })), 201

    @jwt_required
    @expose('/<int:form_id>', methods=['PUT'])
    def update(self, form_id: int):
        """Create a form
        ---
        put:
          summary: 更新表单
          requestBody:
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/FormEdition'
          responses:
            200:
            description: Create a form
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/Form'
        """

        form_guard(int(form_id), ['Manager'])

        form_dto = request.json.copy()
        form_dto['id'] = int(form_id)
        form = self.form_service.change_form(form_id, form_dto)
        return jsonify(form.asdict(follow={
            'fields': {
                "follow": {
                    "options": {},
                    "constraints": {},
                }
            }
        }))

    @expose('/{id}/publish', methods=['POST'])
    def publish(self):
        """Publish a form
        ---
        post:
          summary: 发布表单
          responses:
            200:
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
          summary: 取消表单发布
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
          summary: 查询表单列表
          responses:
            200:
              content:
                application/json:
                  schema:
                    type: array
                    items:
                      $ref: "#/components/schemas/Form"
        """
        forms = self.form_service.fetch_forms(
            current_user.id, PageRequest.create(request.args)
        )
        return jsonify(forms.asdict())

    @jwt_required
    @expose('/<int:form_id>', methods=['GET'])
    def get_detail(self, form_id: int):
        """Get a form
        ---
        get:
          responses:
            200:
              description: Get a form
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Form"
        """
        form_guard(form_id, ['Viewer', 'Editor', 'Manager'])
        form = self.form_service.fetch_form(form_id, current_user)
        return jsonify(form.asdict(follow={
            'fields': {
                "follow": {
                    "options": {},
                    "constraints": {},
                }
            }
        }))

    @jwt_required
    @expose("/<int:form_id>/summary", methods=["GET"])
    def summary(self, form_id: int):
        form_guard(form_id, ['Viewer', 'Editor', 'Manager'])

        user = current_user
        submit_count_by_days = self.value_repository.count_by_8_days(user.id, form_id)
        form = self.form_repository.find_one(form_id)

        return jsonify({
            "submit_count": self.value_repository.count_all(user.id, form_id),
            "submit_count_today": self.value_repository.count_today(
                user.id, form_id),
            "reads_today": self.event_repository.count_today(form_id, EventType.VIEW_FORM),
            "submit_count_by_days": submit_count_by_days,
            "read_count_by_days": self.event_repository.count_by_8_days(form_id, EventType.VIEW_FORM),
            "submit_count_by_mintes": self.value_repository.count_by_24_minute(
                user.id, form_id),
            "form": form.asdict(),
        })

    @jwt_required
    @expose('/<int:form_id>/value', methods=['GET'])
    def value(self, form_id: int):
        form_guard(form_id, ['Viewer', 'Editor', 'Manager'])

        page_request = PageRequest.create(request.args)
        page_request.order("created_at", "desc")

        value = self.form_service.fetch_values(
            form_id, page_request
        )
        return jsonify(value.asdict())

    @jwt_required
    @expose("/<form_id>/export", methods=["GET"])
    def export(self, form_id):
        """
        ---
        get:
          description: "导出CSV文件"
          responses:
            200:
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/Form"
        """
        # TODO: 根据 Request Content Type 来导出返回的内容，例如JSON
        form_id = int(form_id)
        count = self.value_repository.count(form_id)
        form = self.form_repository.find_one(form_id)
        db.session.commit()
        fields_map = {}
        for field in form.fields:
            fields_map[int(field.id)] = field

        def to_export(row):
            ex = {}

            for field_id, value in row['values'].items():
                field = fields_map[int(field_id)]
                ex[field.title] = field.to_text_value(value)
            ex['id'] = row['sequence']
            ex['created_at'] = row['created_at']
            ex['updated_at'] = row['updated_at']

            return ex
        
        def generate():
            paginator = PageRequest.create(request.args)
            args = [int(form_id), paginator]
            i = 0
            position = 0
            while i < paginator.page_size:
                print(i)
                args[1].page = i + 1
                values = self.value_repository.find(*args)
                if i == 0:
                    iostream = io.StringIO()
                    first = to_export(values[0].asdict())
                    keys = first.keys()
                    csv_writer = csv.DictWriter(iostream, fieldnames=keys)
                    csv_writer.writeheader()

                for value in values:
                    csv_writer.writerow(to_export(value.asdict()))
                
                iostream.seek(position)
                for line in iostream.readline():
                    yield line
                position = iostream.tell()
                i += 1

        response = Response(stream_with_context(generate()))
        response.headers["Content-Type"] = "text/csv"

        return response
appbuilder.add_api(ControlPanelFormApi)
