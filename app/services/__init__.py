from app import models
from app import db
from datetime import datetime
from app.services.assembler import FormAssembler

def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return ''.join(x.title() for x in components)

class FormService(object):
    form_assembler = FormAssembler()

    def __init__(self, a_db=None):
        if not a_db:
            self.db = db
        else:
            self.db = a_db

    def add_new_form(self, dto):
        form = self.form_assembler.to_model(dto)

        session = self.db.session
        session.add(form)
        session.commit()

        return form

    def fetch_form(self, form_id):
        #.filter(models.Form.deleted_at != None)\
        form = db.session.query(models.Form).filter(models.Form.id==form_id)\
            .first()
        return form

    def add_new_field(self, field):
        
        class_name = to_camel_case(field['discriminator'])
        class_ = getattr(models, class_name)

        field = class_(**field)
        session = db.session
        session.add(field)
        session.commit()

        return field

    def fetch_field(self, field_id):

        return db.session.query(models.Field).filter(models.Field.id==field_id).first()

    def change_field(self, field_id, field):
        session = db.session
        f = session.query(models.Field).filter(models.Field.id==field_id).first()
        for k, v in field.items():
            setattr(f, k, v)
        session.commit()

        return f

    def remove_field(self, field_id):
        session = db.session
        field = session.query(models.Field).filter(models.Field.id==field_id).first()
        field.deleted_at = datetime.now()
        session.commit()

        return field

    def submit(self, form_id : int, values : dict):
        """ 提交表单
        """
        form = db.session.query(models.Form).filter(models.Form.id==form_id)\
            .first()
        session = db.session
        v = self.form_assembler.to_value(form, values)
        session.add(v)
        session.commit()

    def fetch_values(self, form_id : int, page : int = 0, page_size : int = 50):
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