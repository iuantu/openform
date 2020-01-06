from flask_appbuilder import BaseView, expose
from app import appbuilder
from flask import request, g
from app.models import UserAgent
from app.services import FormService
from app.views.models import FormViewModelAssembler
from app.views.utils import to_user_agent

class FormView(BaseView):
    form_service = FormService()
    route_base = '/form'
    assembler = FormViewModelAssembler()

    @expose('/<form_id>', methods=["GET", "POST"])
    def form(self, form_id):
        user_agent = to_user_agent(request)
        form = self.form_service.fetch_form(form_id, g.user, user_agent)
        form_view = self.assembler.to_view_model(form, request.form)

        if "POST" == request.method:
            
            user_agent = to_user_agent(request)

            if self.form_service.submit(form, user_agent):
                return self.render_template(
                    'openform/form_success.html'
                )

        return self.render_template(
            "openform/form.html",
            form_view = form_view,
            form = form
        )

appbuilder.add_view_no_menu(FormView)