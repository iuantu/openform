from flask import render_template
from app import appbuilder
from app.views.control_panel import *
from app.views.form import *
from app.views.user import *
from app.views.core import *

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )