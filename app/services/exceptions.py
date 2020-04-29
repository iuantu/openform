class Field:
    def __init__(self, name, code, description):
        self.name = name
        self.code = code
        self.description = description

    def to_dict(self):
        return {
            'name': self.name,
            'code': self.code,
            'description': self.description,
        }


class InvalidFormException(Exception):
    def __init__(self, errors):
        self.errors = errors

    def to_dict(self):
        return {
            'errors': [error.to_dict() for error in self.errors]
        }

    @staticmethod
    def with_from(form):

        field_errors = []
        exception = InvalidFormException(field_errors)
        for field in form.fields:
            for error in field.errors:
                field_errors.append(Field(
                    field.id,
                    field.discriminator,
                    str(error),
                ))

        return exception

