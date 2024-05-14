import os
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", 'django-insecure-_whye!!lzfzt2^#)ndydi12%#na3vmdtz&ne_%@qe0o)(ld65p')

# SECURITY WARNING: don't run with debug turned on in production!
__debug = os.environ.get('DEBUG', 1)
DEBUG = int(__debug)

__allowed_host = os.environ.get("DJANGO_ALLOWED_HOSTS", None)
if not __allowed_host:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = __allowed_host.split(" ")

