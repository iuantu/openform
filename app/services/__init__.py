from app import models
from app import db
from datetime import datetime
from app.services.assembler import FormAssembler
from app.utils import to_camel_case
from app.models.value import UserAgent

class FormService(object):
    form_assembler = FormAssembler()
    form_repository: models.FormRepository = None
    field_repository: models.FieldRepository = None

    def __init__(self, a_db=None):
        if not a_db:
            self.db = db
        else:
            self.db = a_db
        self.form_repository = models.FormRepository(self.db)
        self.field_repository = models.FieldRepository(self.db)

    def add_new_form(self, dto) -> models.Form:
        form = self.form_assembler.to_model(models.Form(), dto)

        session = self.db.session
        session.add(form)
        session.commit()

        return form

    def change_form(self, form_id, dto):
        form = self.form_repository.find_one(form_id)
        self.form_assembler.to_model(form, dto, True)
        self.db.session.add(form)
        self.db.session.commit()

    def fetch_form(self, form_id):
        return self.form_repository.find_one(form_id)

    def fetch_forms(self, user_id: int, page_request):
        forms = self.form_repository.find_all(user_id, page_request)
        return forms

    def add_new_field(self, field):
        
        class_name = to_camel_case(field['discriminator'])
        class_ = getattr(models, class_name)

        field = class_(**field)
        session = db.session
        session.add(field)
        session.commit()

        return field

    def fetch_field(self, field_id):
        return self.field_repository.find_one(field_id)

    def change_field(self, field_id, field):
        session = db.session
        f = self.field_repository.find_one(field_id)
        for k, v in field.items():
            setattr(f, k, v)
        session.commit()

        return f

    def remove_field(self, field_id):
        session = db.session
        field = self.field_repository.find_one(field_id)
        field.deleted_at = datetime.now()
        session.commit()

        return field

    def submit(self, form: models.Form, user_agent: UserAgent):
        """ 提交表单
        """
       
        if form.validate():
            session = db.session
            
            v = form.values()
            v.ip = user_agent.ip
            v.ua_browser = user_agent.browser
            v.ua_browser_version = user_agent.browser_version
            v.ua_os = user_agent.os
            v.ua_os_version = user_agent.os_version
            v.ua_device = user_agent.device
            v.ua_device_brand = user_agent.device_brand
            v.ua_device_model = user_agent.device_model

            form.increase_value_sequence()
            v.sequence = form.value_sequence
            session.add(v)
            session.commit()

            return v
        return None

    def fetch_values(self, form_id: int, page: int = 0, page_size: int = 50):
        values = db\
            .session\
            .query(models.Value)\
            .order_by(models.Value.id.desc())\
            .filter(models.Value.form_id==form_id)\
            .limit(page_size)\
            .offset((page - 1) * page_size)\
            .all()

        return {
            "data": [v.asdict() for v in values],
            "count": 0
        }