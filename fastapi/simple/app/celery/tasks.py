import time
# from .worker import celery
from app.celery.worker import celery

def __calculate_fibonacci(num: int) -> int:
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

@celery.task(name="calculate_fibonacci")
def fibonacci(number):
    total = __calculate_fibonacci(number)
    return total



@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True