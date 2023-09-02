import os 

from celery import Celery

DOCKER = os.getenv("DOCKER", 0)
print(DOCKER)

# Set the default Django settings module for the 'celery' program.
if DOCKER:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djcelery.settings.docker')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djcelery.settings.local')


app = Celery("djcelery")

if DOCKER:
    app.config_from_object('django.conf:settings', namespace='CELERY')
else:
    app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')