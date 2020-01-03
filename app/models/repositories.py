from app.models import (Form, Field,)
from sqlalchemy import func

class BaseRepository:
    def __init__(self, db):
        self.db = db

    def order_by(self, query, page_request, model):

        for k, v in page_request.order_by.items():
            query = query.order_by(getattr(getattr(model, k), v)())

        return query.limit(page_request.page_size)\
            .offset((page_request.page - 1) * page_request.page_size)

class FormRepository(BaseRepository):

    def find_one(self, form_id):
        return self.db\
            .session\
            .query(Form)\
            .filter(Form.id==form_id)\
            .first()

    def find_all(self, user_id: int, page_request):
        
        if not "id" in page_request.order_by:
            page_request.order_by["id"] = "desc"

        return self.order_by(
            self.db\
            .session\
            .query(Form)\
            .filter(Form.user_id==user_id),

            page_request,
            Form
        )\
            .all()

    def count_all(self, user_id: int):
        count = self.db\
            .session\
            .query(func.count(Form.id).label("count"))\
            .filter(Form.user_id==user_id)\
            .first()
        return count[0]

class FieldRepository:
    def __init__(self, db):
        self.db = db

    def find_one(self, field_id: int):
        return db\
            .session\
            .query(Field)\
            .filter(Field.id==field_id)\
            .first()