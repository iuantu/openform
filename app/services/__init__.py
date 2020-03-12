import json
import logging
from flask import jsonify
from app import models
from app import db
from datetime import datetime
from app.services.assembler import FormAssembler
from app.utils import to_camel_case
from app.models import UserAgent, Event, EventType, Choice
from app.models.page import Pageable
from typing import List
from flask_appbuilder.security.sqla.models import Role

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
        self.value_repository = models.ValueRepository(self.db)
        self.role_repository = models.RoleRepository(self.db)
        self.logger = logging.getLogger('FormService')

    def add_new_form(self, command) -> models.Form:
        form = self.form_assembler.to_model(models.Form(), command)

        session = self.db.session
        session.add(form)
        session.flush()

        collaborator = models.FormCollaborator(
            form.id,
            form.user_id,
            self.role_repository.find_by("Manager").id,
        )
        session.add(collaborator)
        session.commit()

        return form

    def change_form(self, form_id, dto) -> models.Form:
        form = self.form_repository.find_one(form_id)
        self.form_assembler.to_model(form, dto, True)
        self.db.session.add(form)
        self.db.session.commit()
        return form

    def fetch_form(self, form_id, user) -> models.Form:
        form = self.form_repository.find_one(form_id)
        form.record_count += 1
        user_id = (user and not user.is_anonymous) and user.id or None
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

            # 查找所有的选项字段并保存选择的结果
            
            def find_option_id(field, value):
                for option in field.options:
                    if value == option.value:
                        return option.id

                return -1

            for field in form.select_fields:
                for value in field.value:
                    choice = Choice(
                        form_id=form.id,
                        field_id=field.id,
                        option_id=find_option_id(field, value['value']),
                        value=value['value']
                    )
                    session.add(choice)

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

    def all_roles(self):
        session = self.db.session
        return session.query(Role)\
            .filter(Role.name.in_(['Editor', 'Manager', 'Viewer']))\
            .all()