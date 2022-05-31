class Response:

    def __init__(self, body=None, status='200 OK', headers=None):
        self.status = status
        self.headers = self._set_headers(headers)
        self.body = body

    @staticmethod
    def _set_headers(user_headers):
        headers = {
            'content': 'text'
        }
        if user_headers:
            headers.update(user_headers)
        return headers
