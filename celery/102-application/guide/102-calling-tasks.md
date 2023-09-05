# Using Celery in your Application

You can call a task using the **delay()** method:

```py
>>> from proj.tasks import add

>>> add.delay(2, 2)
```

This method id actually a star-argument shourtcut to another method called **apply_async()**:

```py
>>> add.apply_async((2, 2))
```

----------

The latter enables you to specify execution options like the time to run (countdown), the queue it should be sent to, and so on:

```py
>>> add.apply_async((2, 2), queue='lopri', countdown=10)
```

In the above example the task will be sent to a queue name "lopri" and tha task will execute, at the earliest, 10 seconds after the message was sent.

----------

Applying the task directly will execute the task in the current process, so that no message is sent:

```py
>> add(2, 2)
4
```

These three methods - **delay()**, **apply_async()**, and applying (__call__), make up the celery calling API, which is also used for signatures.

----------

Every task invocation will be given a unique identifier (an UUID) - this is the task id.

The *delay* and *apply_async* method return an **AsyncResult** instance, which can be used to keep track of the taks execution state. But for this you need to enable a *result backend* so that the state can be stored somewhere. 

----------

Results are disabled by default because there is no result backend that suits every application; to choose one you need to consider the drawbacks of each individual backend. 

For many task keeping the return value isn't even very usefull, so it's a sensible defualt to have. 

Also note that results backends aren't used for monitoring tasks and workers: for that Celery uses dedicated event messages.

If you have a result backend configured you can retrieve the return value of a task:

```py
>>> res = add.delay(2, 2)
>>> res.get(timeout=1)
4
```

You can find the task's id by looking at the **id** attribute:

```py
>> res.id
d6b3aea2-fb9b-4ebc-8da4-848818db9114
```

You can also inspect the exception and traceback if the task raised an exception, in fact *result.get()* will propagate any errors by default:

```py
>>> res = add.delay(2, '2')
>>> res.get(timeout=1)
```

```bash
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "celery/result.py", line 221, in get
    return self.backend.wait_for_pending(
  File "celery/backends/asynchronous.py", line 195, in wait_for_pending
    return result.maybe_throw(callback=callback, propagate=propagate)
  File "celery/result.py", line 333, in maybe_throw
    self.throw(value, self._to_remote_traceback(tb))
  File "celery/result.py", line 326, in throw
    self.on_ready.throw(*args, **kwargs)
  File "vine/promises.py", line 244, in throw
    reraise(type(exc), exc, tb)
  File "vine/five.py", line 195, in reraise
    raise value
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```


If you don't wish for the errors to propafate, you can disable that by passing *propagate*:

```py
>>> res.get(propagate=False)
TypeError("unsupported operand type(s) for +: 'int' and 'str'")
``` 

If this case it'll return the exception instance raised instead -- so to check whether the task succeeded or failed, you'll have to use the corresponding methods on the result instance:

```py
>>> res.failed()
True

>>> res.successful()
False
```

So how does it known if the task has failed or not? It can find out by looking at the tasks *state*:

```py
>>> res.state
'FAILURE'
```

A task can only be in a single state, but it can progress through several states. The stages of a typical task can be:


```
PENDING -> STARTED -> SUCCESS
```

----------

The started state is a special state that's only recorded if the **task_track_started** setting to enabled,, or if the @task(track_started=True) option is set for the task.

The pending state is actually not a recorded state, but rather the default state for any task id that's unknown: 

```py
>>> from proj.celery import app

>>> res = app.AsyncResult('this-id-does-not-exist')
>>> res.state
'PENDING'
```

If the task is retried the stages can become even more complex. to demostrate, for a task that's retried two times the stages woould be:

```
PENDING -> STARTED -> RETRY -> STARTED -> RETRY -> STARTED -> SUCCESS
```