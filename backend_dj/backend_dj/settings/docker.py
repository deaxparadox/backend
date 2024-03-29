from .base import *


DEBUG = os.environ.get("DEBUG")

ALLOWED_HOSTS_STRING = os.environ.get("DJANGO_ALLOWED_HOSTS")
if ALLOWED_HOSTS_STRING is None:
    print("\n\tDocker settings didn't found allowed hosts\n")
    exit(1)
ALLOWED_HOSTS = ALLOWED_HOSTS_STRING.split(" ")
        