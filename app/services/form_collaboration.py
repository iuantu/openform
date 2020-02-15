from app import models
from app import db
from app.exceptions import DuplicatedException, DoesNotExistsException, ForbiddenException
from datetime import datetime
from app.services.assembler import FormAssembler
from app.utils import to_camel_case
from app.models import UserAgent, Event, EventType
from app.models.page import Pageable
from app.models.repositories import CollaboratorRepository, UserRepository, FormRepository
from typing import List
from flask_appbuilder.security.sqla.models import Role
from app.models.form import FormCollaborator

class FormCollaborationService(object):

    def __init__(self):
        self.db = db
        self.repository = CollaboratorRepository(db)
        self.user_repository = UserRepository(db)
        self.form_repository = FormRepository(db)

    def new_collaborator(self, command):
        username = command['username']
        user = self.user_repository.find_by(username)

        form = self.form_repository.find_one(command['form_id'])

        collaborator = self.repository.find_one(
            command['form_id'],
            user.id
        )

        is_owner = form.user_id == command['current_user'].id
        is_manager = user.role.name != "Manager"
        if is_owner or is_manager:
            raise ForbiddenException()

        if collaborator:
            raise DuplicatedException()

        collaborator = FormCollaborator(**command)
        session = self.db.session
        session.add(collaborator)
        session.commit()

        return collaborator

    def change_collaborator(self, form_id, user_id, role_id):
        session = self.db.session
        collaborator = self.repository.find_one(form_id, user_id)
        if collaborator:
            collaborator.role_id = role_id
            session.add(collaborator)
            session.commit()
        else:
            pass
            
        return self.repository.find_one(form_id, user_id)

    def remove(self, form_id, user_id):
        session = self.db.session

        collaborator = self.repository.find_one(form_id, user_id)

        if not collaborator:
            raise DoesNotExistsException()

        user = collaborator.user
        role = collaborator.role
        # not lazy

        session.delete(collaborator)
        session.commit()

        return collaborator

    def collaborators(self, form_id):
        session = self.db.session
        collaborators = session\
            .query(FormCollaborator)\
            .filter(FormCollaborator.form_id==form_id)\
            .all()

        return collaborators