from app import db
from app.models import CollaboratorRepository
from flask_appbuilder.security.sqla.models import Role
from app.exceptions import ForbiddenException, DoesNotExistsException
from flask_jwt_extended import current_user

def form_guard(form_id, *roles):

    if not current_user:
        raise ForbiddenException()

    repository = CollaboratorRepository(db)
    session = db.session
    collaborator = repository.find_one(form_id, current_user.id)

    if not collaborator:
        raise DoesNotExistsException()

    is_owner = collaborator.form.user_id == current_user.id
    is_allow = collaborator.role.name in roles
    if not (is_allow or is_owner):
        raise ForbiddenException()