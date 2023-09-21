# Keeping Results


If your wnat ot keep track of the task's states, Celery needs to store or send the states somewhere. There are several built-in result backends to choose from: **SQLAlchemy/Django** ORM, **MongoDB**, **Memcached**, **Redis**, **RPC** (RabbitMQ/AMQP), and – or you can define your own.

For this example we use the rpc result backend, that sends states back as transient messages. The backend is specified via the backend argument to **Celery**, (or via the **result_backend** setting if you choose to use a configuration module). So, you can modify this line in the *simple_tasks.py* file to enable the *rpc://* backend:

```py
app = Celery('tasks', backend='rpc://', broker='pyamqp://')
```

Or if you want to use Redis as the result backend, but still use RabbitMQ as the message broker (a popular conbination):

```py
app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')
```

----------


Now with hte result backend configured, close the current python session and import the tasks module again to put the changes into effect. This time you'll hold on to the **AsyncResult** instance returned when you call a task.

```py
>>> from tasks import add    # close and reopen to get updated 'app'
>>> result = add.delay(4, 4)
```

The **ready()** method returns whether the task has finished processing or not:

```py
>>> result.ready()
False
```

You can wait for the result to complete, but this is rarely used since it turns the asynchronous call into a synchronous one:

```py
>>> result.get(timeout=1)
8
```

In case the task raised an exception, **get()** will re-raise the exception, but you can overrite this by specifying the propagate argument:

```py
>>> result.get(propagate=False)
```

If the task raised an exception, you can also gain access to the original traceback:

```py
>>> result.traceback
```