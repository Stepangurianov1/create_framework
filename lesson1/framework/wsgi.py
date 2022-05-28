import sys

from framework.request import Request
from framework.response import Response
from framework.view import View
import argparse


class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = Request(environ)
        view = self._get_view(request)
        response = self._get_response(request, view)
        # print(request.query_params)
        # self.arg_parser()
        start_response(response.status, list(response.headers.items()))
        # print(int(response.status[:3]))
        # print(request.method)
        return [response.body.encode() if int(response.status[:3]) <= 226 else b'ERROR']

    def _get_view(self, request: Request):
        # print(self.urls)
        for url in self.urls:
            print(url.path)
            print(request.path)
            if url.path == request.path:
                return url.view
            else:
                return None

    @staticmethod
    def _get_response(request: Request, view: View):
        # print(request.method)
        # print(hasattr(view, request.method))
        # print(view)
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        else:
            return Response(status='404 ERROR')
