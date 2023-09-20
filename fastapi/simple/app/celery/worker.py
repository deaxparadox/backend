import os 
import time 
from celery import Celery

celery = Celery(
    __name__,
    broker="redis://localhost:6379",
    backend="redis://localhost:6379",
    include=[
        "app.celery.tasks"
    ]
)

# celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
# celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

# celery.conf.broker_url = "redis://"
# celery.conf.result_backend = "redis://"


