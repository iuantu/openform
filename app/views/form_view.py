from flask_appbuilder import BaseView, expose
from app import appbuilder, db
from flask import request, g, redirect, url_for
from app.models import UserAgent
from app.services import FormService
from app.views.models import FormViewModelAssembler
from app.views.utils import to_user_agent
from app.models import Event, EventType

class ParameterContainer:
    def __init__(self):
        pass

    def get(self, name):
        query_string = request.args.get(name, None)
        if query_string:
            return query_string
        
        form = request.form.get(name, None)
        if form:
            return form
        
        return None

    def getlist(self, name):
        query_string = request.args.getlist(name, None)
        if query_string:
            return query_string
        
        form = request.form.getlist(name, None)
        if form:
            return form
        
        return []

class FormView(BaseView):
    form_service = FormService()
    route_base = '/form'
    assembler = FormViewModelAssembler()

    @expose('/<form_id>', methods=["GET", "POST"])
    def form(self, form_id):
        user_agent = to_user_agent(request)
        form = self.form_service.fetch_form(form_id, g.user)
        form_view = self.assembler.to_view_model(form, ParameterContainer())

        if "POST" == request.method:
            if self.form_service.submit(form, g.user, user_agent):
                return redirect(
                    url_for("FormView.success_redirect", form_id=form_id)
                )
        else:
            event = Event(type=EventType.VIEW_FORM, user_id=None, form_id=form_id)
            event.assemble_from_user_agent(user_agent)
            db.session.add(event)
            db.session.commit()

        return self.render_template(
            "openform/form.html",
            form_view = form_view,
            form = form
        )

    @expose('/<form_id>/success_redirect', methods=['GET'])
    def success_redirect(self, form_id):

        return redirect(
            url_for("FormView.form_success", form_id=form_id)
        )

    @expose('/<form_id>/success', methods=['GET'])
    def form_success(self, form_id):

        return self.render_template(
            'openform/form_success.html'
        )

appbuilder.add_view_no_menu(FormView)