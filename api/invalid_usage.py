class InvalidUsage(Exception):
    """Raised when the json validation fails. Meaning that a data point is missing or a data type is incorrect."""

    def __init__(self, message, status_code):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        rv = {}
        rv['message'] = self.message
        return rv