from time import sleep

from celery import shared_task


@shared_task
def fibonacci(x: int):
    sleep(10)
    return x