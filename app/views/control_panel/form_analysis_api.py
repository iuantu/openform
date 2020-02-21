from flask import jsonify
from flask_appbuilder.api import BaseApi, expose
from app import appbuilder
from app.services.form_analysis import FormAnalysisService


class FormAnalysisApi(BaseApi):

    resource_name = 'cp/form/analysis'
    service = FormAnalysisService()

    @expose('/<int:form_id>')
    def index(self, form_id: int):
        result = []
        for item in self.service.fetch(form_id):
            result.append({
                'field_id': int(item.field_id),
                'option_id': int(item.option_id),
                'count': int(item.count)
            })
        print(result)
        return jsonify(result)

appbuilder.add_api(FormAnalysisApi)
