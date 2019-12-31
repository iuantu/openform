from flask_appbuilder import BaseView, expose
from app import appbuilder
from flask import request
from app.models.value import UserAgent
from app.services import FormService
from app.views.models import FormViewModelAssembler
from user_agents import parse

class FormView(BaseView):
    form_service = FormService()
    route_base = '/form'
    assembler = FormViewModelAssembler()

    @expose('/<form_id>', methods=["GET", "POST"])
    def form(self, form_id):
        form = self.form_service.fetch_form(form_id)
        form_view = self.assembler.to_view_model(form, request.form)

        if "POST" == request.method:
            ua = parse(request.user_agent)
            user_agent = UserAgent(
                request.remote_addr,
                ua.browser.family,
                ua.browser.version_string,
                ua.os.family,
                ua.os.version_string,
                ua.device.family,
                ua.device.brand,
                ua.device.model
            )

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