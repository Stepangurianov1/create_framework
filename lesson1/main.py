from framework.template import render
from framework.wsgi import Framework
from framework.url import Url
from framework.view import View
from framework.response import Response


class MyFirstView(View):
    def get(self, request):

        return Response(body=render('templates/template_for_get.html'))

    def post(self, request):
        return Response(status='201 CREATED', body=render('templates/template_for_post.html'), headers={'Babayka': '123'})


urls = [
    Url('/', MyFirstView)
]

app = Framework(urls)
