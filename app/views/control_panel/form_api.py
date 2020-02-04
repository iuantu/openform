import csv
import io
import xlwt
from app.models import form as ff
from io import BytesIO
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
    @expose('/', methods=['POST'])
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
          summary: 更新表单
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
                    $ref: "#/components/schemas/Form"
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
            "reads_today": self.event_repository.count_today(form_id, EventType.VIEW_FORM),
            "submit_count_by_days": submit_count_by_days,
            "read_count_by_days": self.event_repository.count_by_8_days(form_id, EventType.VIEW_FORM),
            "submit_count_by_mintes": self.value_repository.count_by_24_minute(
                user.id, form_id),
            "form": form.asdict(),
        })

    @expose('/<form_id>/value', methods=['GET'])
    def value(self, form_id):
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
    
        @jwt_required
    @expose("/excel", methods=['GET'])
    def from_excel(self):
        book = xlwt.Workbook()
        sheet = book.add_sheet('form')
        title = ['%s' % item for item in ff.Form.__dict__.keys() if not str(item).startswith("_")]
        i = 0
        for h in title:
            sheet.write(0, i, h)
            i = 1

        forms = self.form_service.fetch_forms_not_page(current_user.id)

        for row, form in enumerate(forms):
            for col in range(0, len(title)):
                sheet.write(row  1, col, form[title[col]])

        bio = BytesIO()
        book.save(bio)
        return bio.getvalue()

    @jwt_required
    @expose("/statement", methods=['GET'])
    def statement(self):
         """
            表单报表
        :return:
        """
        field_num = self.form_service.count_field()
        select_field_num = self.form_service.count_select_field()
        return self.response(200, **{"statement": round(select_field_num / field_num, 2)})

    @jwt_required
    @expose("/find_from_commit_and_record/<form_id>", methods=['GET'])
    def find_from_commit_and_record(self, form_id):
        """
            查询数据提交和浏览数据
        :param form_id:
        :return:
        """
        form = self.form_service.fetch_form(form_id)
        commit_count = len(form.fields)
        record_count = form.record_count
        return self.response(200, **{"commit_count": commit_count, "record_count": record_count})

    @expose("/one_minute_commit/<form_id>", methods=['GET'])
    def one_minute_commit(self, form_id):
        """
            一分钟提交的数据量
        :param form_id:
        :return:
        """
        fields = self.form_service.one_minute_commit(form_id)
        return jsonify(fields.asdict())

    @expose('/<form_id>', methods=['DELETE'])
    def delete(self, form_id):
        """Delete a form
        """

        form = self.form_service.remove_form(form_id)
        return jsonify(form.asdict())
appbuilder.add_api(ControlPanelFormApi)
