class HttpStatusException(Exception):
    def __init__(self, http_status_code, message):
        super().__init__()
        self.http_status_code = http_status_code
        self.message = message

class ForbiddenException(HttpStatusException):
    def __init__(self):
        super().__init__(403, "Forbidden")

class DoesNotExistsException(HttpStatusException):
    def __init__(self):
        super().__init__(404, "Does not exists")

class DuplicatedException(HttpStatusException):
    def __init__(self):
        super().__init__(409, "Duplicated")