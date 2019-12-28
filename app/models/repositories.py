from app.models import (Form, Field,)
class FormRepository:
    def __init__(self, db):
        self.db = db

    def find_one(self, form_id):
        return self.db\
            .session\
            .query(Form)\
            .filter(Form.id==form_id)\
            .first()

class FieldRepository:
    def __init__(self, db):
        self.db = db

    def find_one(self, field_id: int):
        return db\
            .session\
            .query(Field)\
            .filter(Field.id==field_id)\
            .first()