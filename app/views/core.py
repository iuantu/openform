from flask_appbuilder import BaseView, expose
from app import appbuilder
from flask import request
from app.services import FormService
from app.views.models import FormViewModelAssembler

class FormView(BaseView):
    form_service = FormService()
    route_base = '/form'

    @expose('/<form_id>')
    def form(self, form_id):

        form = self.form_service.fetch_form(form_id)
        assembler = FormViewModelAssembler()
        return self.render_template(
            "openform/form.html",
            form = assembler.to_view_model(form)
        )

    @expose('/<form_id>', methods=['POST'])
    def submit(self, form_id):
        self.form_service.submit(form_id, request.form)

        return self.render_template(
            'openform/form_success.html'
        )

appbuilder.add_view_no_menu(FormView)