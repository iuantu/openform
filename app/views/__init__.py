from flask import render_template
from app import appbuilder
from app.views.control_panel import *
from app.views.form_api import *
from app.views.user_api import *
from app.views.form_view import *

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )