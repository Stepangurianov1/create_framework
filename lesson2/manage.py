import argparse
import sys
from subprocess import Popen, PIPE


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('command_name', type=str)
    namespace = parser.parse_args()
    return namespace.command_name


if arg_parser() == 'runserver':
    try:
        process = Popen('gunicorn main:app -b 127.0.0.1:8001' , shell=True, stdout=None, stderr=None)
        process.communicate()
    except KeyboardInterrupt:
        sys.exit(0)

