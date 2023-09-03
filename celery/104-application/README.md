# Using Celer in your Application

## Our Project 

----------
Project layout:

```bash
project/
|-- celery.py
|-- maths.py
`-- tasks.py
```

**project/celery.py** : here celery is configured with `redis`

- to install redis in docker: **docker run --rm -p 6379:6379 redis:7**

```py
from celery import Celery

app = Celery(
    'project',
    backend="redis://localhost/", 
    broker='redis://localhost/'
)

if __name__ == "__main__":
    app.start()
```

- to use rabbitmq: **docker run -d -p 5672:5672 rabbitmq**

```py
from celery import Celery

app = Celery('project',
    broker='amqp://',
    backend='rpc://',
    include=['proj.tasks']
)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
```



In this module you created our Celery instance (sometimes referred to as the app). To use Celery within your project you simply import this instance.

- The broker argument specifies the URL of the broker to use.
- The backend argument specifies the result backend to use.


----------

project/tasks.py

```py
from .celery import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
```

