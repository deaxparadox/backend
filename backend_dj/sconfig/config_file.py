import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_dj.settings.local')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
