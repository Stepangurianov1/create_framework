import cgi
import sys

from framework.request import Request
from framework.response import Response
from framework.view import View
import argparse
from pprint import pprint


class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = Request(environ)
        length = environ.get('wsgi.input')
        print(length)
        view = self._get_view(request)
        response = self._get_response(request, view)
        # print(request.query_params)
        # self.arg_parser()
        start_response(response.status, list(response.headers.items()))
        # print(int(response.status[:3]))
        # print(request.method)
        self.write_bode(environ)
        # pprint(environ)
        return [response.body.encode() if int(response.status[:3]) <= 226 else b'ERROR']

    def _get_view(self, request: Request):
        print(self.urls)
        for url in self.urls:
            print(url.path)
            print(1, request.path)
            if url.path == request.path:
                return url.view
            # else:
            #     return None

    @staticmethod
    def get_bode(environ):
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        post_value = post.getvalue('index', 'none')
        return post_value

    def write_bode(self, environ):
        personal_data = self.get_bode(environ)
        if personal_data is not None:
            with open('personal_data.txt', 'w') as f:
                f.write(f'Birthday: {personal_data[0]}\nFirstname: {personal_data[1]}\nEmail: {personal_data[2]}')

    @staticmethod
    def _get_response(request: Request, view: View):
        print(request.method)
        # print(hasattr(view, request.method))
        print(view)
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        else:
            return Response(status='404 ERROR')
