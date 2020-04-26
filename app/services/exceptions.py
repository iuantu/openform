class InvalidField:
    def __init__(self, field, code, description):
        self.field = field
        self.code = code
        self.description = description


class InvalidFields(Exception):
    def __init__(self, errors):
        self.errors = errors
