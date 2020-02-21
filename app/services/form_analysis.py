from app import db
from app.models import Form, Choice
from sqlalchemy import func

class FormAnalysisService:
    def fetch(self, id):
        result = db.session.query(
            Choice.field_id,
            Choice.option_id,
            func.count(Choice.option_id).label('count')
        )\
        .filter(Choice.form_id==id)\
        .group_by(Choice.field_id, Choice.option_id)\
        .all()

        return result