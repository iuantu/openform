from flask import request


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
