from celery import Celery
from base import fibonacci

app = Celery(
    'tasks',
    backend="redis://localhost/", 
    broker='redis://localhost/'
)

@app.task
def add(x, y):
    return x + y

@app.task 
def fibo(num: int | float, /) -> int:
    return fibonacci(num)