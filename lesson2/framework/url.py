from dataclasses import dataclass
from framework.view import View


# @dataclass
class Url:
    def __init__(self, path, view):
        self.path = path
        self.view = view

    # path: str
    # view: View
