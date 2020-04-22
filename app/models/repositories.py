import logging
from . import (Form, Field, Value, Event, PageRequest, FormCollaborator)
from sqlalchemy import func, Date, cast, or_
from datetime import date, timedelta
from typing import List
from flask_appbuilder.security.sqla.models import User, Role


class BaseRepository:
    def __init__(self, db):
        self.db = db

    def order_by(self, query, page_request, model):
        if page_request.order_by:
            for k, v in page_request.order_by.items():
                query = query.order_by(getattr(getattr(model, k), v)())

        return query.limit(page_request.page_size) \
            .offset((page_request.page - 1) * page_request.page_size)


class UserRepository(BaseRepository):
    def find_by(self, username):
        session = self.db.session
        user = session \
            .query(User) \
            .filter(or_(
            User.username == username,
            User.email == username
        )) \
            .first()

        return user


class RoleRepository(BaseRepository):

    def find_by(self, name: str) -> Role:
        session = self.db.session
        role = session \
            .query(Role) \
            .filter(Role.name == name) \
            .first()

        return role


class CollaboratorRepository(BaseRepository):
    def find_one(self, form_id, user_id):
        session = self.db.session
        collaborator = session \
            .query(FormCollaborator) \
            .filter(FormCollaborator.form_id == form_id,
                    FormCollaborator.user_id == user_id) \
            .first()

        return collaborator


class FormRepository(BaseRepository):

    def find_one(self, form_id):
        return self.db \
            .session \
            .query(Form) \
            .filter(Form.id == form_id) \
            .first()

    def find_all(self, user_id: int, page_request):
        if not "id" in page_request.order_by:
            page_request.order_by["id"] = "desc"

        return self.order_by(
            self.db \
                .session \
                .query(Form) \
                .join(FormCollaborator, FormCollaborator.form_id == Form.id) \
                .filter(FormCollaborator.user_id == user_id),

            page_request,
            Form
        ) \
            .all()

    def count_all(self, user_id: int):
        count = self.db \
            .session \
            .query(func.count(Form.id).label("count")) \
            .filter(Form.user_id == user_id) \
            .first()
        return count[0]


class FieldRepository:
    def __init__(self, db):
        self.db = db

    def find_one(self, field_id: int):
        return db \
            .session \
            .query(Field) \
            .filter(Field.id == field_id) \
            .first()


class EventRepository(BaseRepository):
    def count_by_8_days(self, form_id, type) -> int:
        c = self.db.session \
            .query(
            func.count(Event.created_at).label("count"),
            func.year(Event.created_at).label("year"),
            func.month(Event.created_at).label("month"),
            func.day(Event.created_at).label("day"),
        ) \
            .filter(
            Event.form_id == form_id,
            Event.created_at >= timedelta(days=8)
        ) \
            .order_by(func.max(Event.created_at).desc()) \
            .group_by(
            func.year(Event.created_at),
            func.month(Event.created_at),
            func.day(Event.created_at)
        ) \
            .all()

        logging.debug("count_by_8_days")

        return [c._asdict() for c in c]

    def count_today(self, form_id, type) -> int:
        return self.db.session \
            .query(Event) \
            .filter(
            Event.form_id == form_id,
            Event.type == type,
            Event.created_at >= date.today().strftime("%Y-%m-%d")
        ) \
            .count()

    def count(self, form_id, type) -> int:
        return self.db.session \
            .query(Event) \
            .filter(
            Event.form_id == form_id,
            Event.type == type
        ) \
            .count()


class ValueRepository(BaseRepository):

    def find_one(self, id):
        return self.db.session.query(Value).filter(Value.id==id).first()

    def find(self, form_id, page_request: PageRequest):
        return self.order_by(
            self.db \
                .session \
                .query(Value) \
                .filter(Value.form_id == form_id),

            page_request,
            Value
        ) \
            .all()

    def count(self, form_id):
        return self.db \
            .session \
            .query(Value) \
            .filter(Value.form_id == form_id) \
            .count()

    def count_by_24_minute(self, user_id, form_id) -> int:
        c = self.db.session \
            .query(
            func.count(Value.id).label("count"),
            func.minute(Value.created_at).label("minute"),
        ) \
            .filter(
            Value.form_id == form_id,
            Value.created_at >= timedelta(minutes=24)
        ) \
            .order_by(func.max(Value.id).desc()) \
            .group_by(
            func.minute(Value.created_at),
        ) \
            .all()

        return [c._asdict() for c in c]

    def count_by_8_days(self, user_id, form_id):
        c = self.db.session \
            .query(
            func.count(Value.id).label("count"),
            func.year(Value.created_at).label("year"),
            func.month(Value.created_at).label("month"),
            func.day(Value.created_at).label("day"),
        ) \
            .filter(
            Value.user_id == user_id,
            Value.form_id == form_id,
            Value.created_at >= timedelta(days=8)
        ) \
            .order_by(func.max(Value.created_at).desc()) \
            .group_by(
            func.year(Value.created_at),
            func.month(Value.created_at),
            func.day(Value.created_at)
        ) \
            .all()

        return [c._asdict() for c in c]

    def count_all(self, user_id, form_id) -> int:
        return self.db.session \
            .query(Value) \
            .filter(
            Value.user_id == user_id,
            Value.form_id == form_id
        ) \
            .count()

    def count_today(self, user_id, form_id) -> int:
        return self.db.session \
            .query(Value) \
            .filter(Value.created_at >= date.today().strftime("%Y-%m-%d"),
                    Value.user_id == user_id,
                    Value.form_id == form_id,
                    ) \
            .count()
