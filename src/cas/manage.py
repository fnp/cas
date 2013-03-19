#!/usr/bin/env python
from django.core.management import execute_manager

from os import path
import sys

PROJECT_ROOT = path.realpath(path.dirname(__file__))
sys.path = [
    path.abspath(path.join(PROJECT_ROOT, '..')),
] + sys.path

try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    # Append lib and apps directories to PYTHONPATH
    execute_manager(settings)
