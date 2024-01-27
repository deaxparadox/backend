from time import sleep
from celery import shared_task

@shared_task
def task_sum(a, b):
    sleep(1)
    return int(a) + int(b)