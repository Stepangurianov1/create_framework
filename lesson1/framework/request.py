class Request:

    def __init__(self, environ):
        self.method = environ['REQUEST_METHOD'].lower()
        self.path = environ['PATH_INFO']
        self.headers = self._get_headers(environ)
        self.query_params = self._get_query_params(environ)

    @staticmethod
    def _get_headers(environ):
        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP'):
                headers[key[5:]] = value
        return headers

    @staticmethod
    def _get_query_params(environ):
        query_params = {}
        qs = environ.get('QUERY_STRING')
        if not qs:
            return {}
        qs = qs.split('&')
        for el in qs:
            key, value = el.split('=')
            if query_params.get('key'):
                query_params[key].append(value)
            else:
                query_params[key] = [value]
        # print(query_params)
        return query_params
