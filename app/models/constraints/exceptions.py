class ValidationError(Exception):
    def __init__(self, field, description):
        self.field = field
        super(ValidationError, self).__init__(description)
