class ResponseBuilder:
    def __init__(self):
        self.status_code = 200
        self.result = dict()

    def success(self):
        self.status_code = 200
        return self

    def created(self):
        self.status_code = 201
        return self

    def updated(self):
        self.status_code = 204
        return self

    def deleted(self):
        self.status_code = 204
        return self

    def bad_request_400(self):
        self.status_code = 400
        return self

    def not_found_404(self):
        self.status_code = 404
        return self

    def result_object(self, result):
        self.result = result
        return self

    def get_response(self):
        return self.result, self.status_code
