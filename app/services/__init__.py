import datetime
from datetime import datetime
from typing import List

from app import db
from app import models
from app.models import AbUser
from app.models import CollaborationUser
from app.models import UserAgent, Event, EventType
from app.models.page import Pageable
from app.services.assembler import FormAssembler
from app.utils import to_camel_case


class FormService(object):
    form_assembler = FormAssembler()
    form_repository: models.FormRepository = None
    field_repository: models.FieldRepository = None
    select_field_repository: models.SelectFieldRepository = None
    value_repository: models.ValueFieldRepository = None
    ab_user_repository: models.AbUserFieldRepository = None
    collaboration_user_repository: models.CollaborationUserFieldRepository = None

    def __init__(self, a_db=None):
        if not a_db:
            self.db = db
        else:
            self.db = a_db
        self.form_repository = models.FormRepository(self.db)
        self.field_repository = models.FieldRepository(self.db)
        self.value_repository = models.ValueRepository(self.db)
        self.select_field_repository = models.SelectFieldRepository(self.db)
        # self.value_repository = models.ValueFieldRepository(self.db)
        self.ab_user_repository = models.AbUserFieldRepository(self.db)
        self.collaboration_user_repository = models.CollaborationUserFieldRepository(self.db)

    def add_new_form(self, dto) -> models.Form:
        form = self.form_assembler.to_model(models.Form(), dto)

        session = self.db.session
        session.add(form)
        session.commit()

        return form

    def fetch_forms_not_page(self, user_id):
        return self.form_repository.find_all_all(user_id)

    def remove_form(self, form_id):
        session = db.session
        form = self.field_repository.find_one(form_id)
        form.deleted_at = datetime.now()
        session.commit()

        return field

    def count_field(self):
        session = db.session
        count = self.field_repository.count()
        session.commit()
        return count

    def count_select_field(self):
        count = self.select_field_repository.count()
        self.db.session.commit()
        return count

    def one_minute_commit(self, form_id):
        t = (datetime.datetime.now() - datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
        return self.field_repository.find_by_form_id_and_datetime(form_id, t)

    def fetch_fields(self, form_id, page_request):
        fields = self.field_repository.find_all(form_id, page_request)
        count = self.field_repository.count_all(form_id)
        return Pageable(fields, page_request.create_result(count))

    def change_form(self, form_id, dto):
        form = self.form_repository.find_one(form_id)
        self.form_assembler.to_model(form, dto, True)
        self.db.session.add(form)
        self.db.session.commit()

    def fetch_form(self, form_id, user, user_agent) -> models.Form:
        form = self.form_repository.find_one(form_id)
        form.record_count += 1
        user_id = (user and not user.is_anonymous) and user.id or None
        event = Event(type=EventType.VIEW_FORM, user_id=user_id or None, form_id=form_id)
        event.assemble_from_user_agent(user_agent)
        db.session.add(event)
        db.session.commit()

        return form

    def fetch_forms(self, user_id: int, page_request):
        forms = self.form_repository.find_all(user_id, page_request)
        count = self.form_repository.count_all(user_id)
        return Pageable(forms, page_request.create_result(count))

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

    def submit(self, form: models.Form, user, user_agent: UserAgent):
        """ 提交表单
        """

        if form.validate():
            session = db.session

            v = form.values()
            v.assemble_from_user_agent(user_agent)
            user_id = (user and not user.is_anonymous) and user.id or None
            v.user_id = user_id

            form.increase_value_sequence()
            v.sequence = form.value_sequence
            session.add(v)
            session.commit()

            return v
        return None

    def fetch_values(self, form_id: int, page_request) -> Pageable:
        values = self.value_repository.find(form_id, page_request)
        count = self.value_repository.count(form_id)

        return Pageable(values, page_request.create_result(count))

    def current_date_by_all_minute_commit_count(self, form_id):
        return self.value_repository.current_date_by_all_minute_commit_count(form_id)

    def remove_value(self, value_id):
        session = db.session
        value = self.value_repository.find_one(value_id)
        value.deleted_at = datetime.now()
        session.commit()

        return value

    def fetch_value(self, value_id):
        return self.value_repository.find_one(value_id)

    def add_new_user(self, ab_user):
        user = AbUser(**ab_user)
        session = db.session
        session.add(user)
        session.commit()

        return user

    def add_new_collaboration_user(self, username, form_id):
        user: AbUser = self.ab_user_repository.find_one_by_username_or_email(username)
        collaboration_user = CollaborationUser(user_id=user.id, form_id=form_id)
        session = db.session
        session.add(collaboration_user)
        session.commit()

        return collaboration_user

    def fetch_collaboration_users(self, form_id, page_request):
        users = self.collaboration_user_repository.find_all(form_id, page_request)
        count = self.collaboration_user_repository.form_repository.count_all(form_id)
        return Pageable(users, page_request.create_result(count))

    def remove_collaboration_user(self, collaboration_user_id):
        session = db.session
        collaboration_user = self.collaboration_user_repository.find_one(collaboration_user_id)
        collaboration_user.deleted_at = datetime.now()
        session.commit()

        return collaboration_user
