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
    include=['project.tasks']
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


**The include argument is a list of modules to import when the worker starts. You need to add our tasks module here so that the worker is able to find our tasks.**

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

----------

### Starting the worker

The **celery** program can be used to start the worker (you need to run the worker in the directory above project):

```bash
$ celery -A proj worker -l INFO
```

When the worker starts you should see a banner and some messages:

```bash
--------------- celery@halcyon.local v4.0 (latentcall)
--- ***** -----
-- ******* ---- [Configuration]
- *** --- * --- . broker:      amqp://guest@localhost:5672//
- ** ---------- . app:         __main__:0x1012d8590
- ** ---------- . concurrency: 8 (processes)
- ** ---------- . events:      OFF (enable -E to monitor this worker)
- ** ----------
- *** --- * --- [Queues]
-- ******* ---- . celery:      exchange:celery(direct) binding:celery
--- ***** -----

[2012-06-08 16:23:51,078: WARNING/MainProcess] celery@halcyon.local has started.
```

- The **broker** is the URL you specified in the broker argument in our celery module. You can also specify a different broker on the command-line by using the -b option.
- **Concurrency** is the number of prefork worker process used to process your tasks concurrently. When all of these are busy doing work, new tasks will have to wait for one of the tasks to finish before it can be processed.

The default concurrency number is the number of CPU’s on that machine (including cores). You can specify a custom number using the celery worker -c option. There’s no recommended value, as the optimal number depends on a number of factors, but if your tasks are mostly I/O-bound then you can try to increase it. Experimentation has shown that adding more than twice the number of CPU’s is rarely effective, and likely to degrade performance instead.   

Including the default prefork pool, Celery also supports using Eventlet, Gevent, and running in a single thread 


– *Events* is an option that causes Celery to send monitoring messages (events) for actions occurring in the worker. These can be used by monitor programs like **celery events**, and **Flower** – the real-time Celery monitor

– Queues is the list of queues that the worker will consume tasks from. The worker can be told to consume from several queues at once, and this is used to route messages to specific workers as a means for Quality of Service, separation of concerns, and prioritization.

You can get a complete list of command-line arguments by passing in the --help flag:

```bash
$ celery worker --help
```

### Stopping the workers

To stop the worker simply hit Control-c. 

### In the Background

In production you’ll want to run the worker in the background.

The daemonization scripts uses the **celery multi** command to start one or more workers in the background:

```bash
$ elery multi start w1 -A proj -l INFO
celery multi v4.0.0 (latentcall)
> Starting nodes...
    > w1.halcyon.local: OK
```

You can restart it too:

```bash
$ celery  multi restart w1 -A proj -l INFO
celery multi v4.0.0 (latentcall)
> Stopping nodes...
    > w1.halcyon.local: TERM -> 64024
> Waiting for 1 node.....
    > w1.halcyon.local: OK
> Restarting node w1.halcyon.local: OK
celery multi v4.0.0 (latentcall)
> Stopping nodes...
    > w1.halcyon.local: TERM -> 64052
```

or stop it:


```bash
$ celery multi stop w1 -A proj -l INFO
```

The **stop** command is asynchronous so it won’t wait for the worker to shutdown. 

You’ll probably want to use the **stopwait** command instead, which ensures that all currently executing tasks are completed before exiting:

```bash
$ celery multi stopwait w1 -A proj -l INFO
```

----------
## Note:

celery multi doesn’t store information about workers so you need to use the same command-line arguments when restarting. Only the same pidfile and logfile arguments must be used when stopping.
----------


By default it’ll create pid and log files in the current directory. To protect against multiple workers launching on top of each other you’re encouraged to put these in a dedicated directory:

```bash
$ mkdir -p /var/run/celery
$ mkdir -p /var/log/celery
celery multi start w1 -A proj -l INFO --pidfile=/var/run/celery/%n.pid \
                                        --logfile=/var/log/celery/%n%I.log
```

With the multi command you can start multiple workers, and there's a powerfull command-line syntax to specify arguments for different workers too, for example:

```bash
$ celery multi start 10 -A proj -l INFO -Q:1-3 images,video -Q:4,5 data \
    -Q default -L:4,5 debug
```


#### About the `--app` argument

The **--app** argument specifies the Celery app instance to use, in the form of **module.path:attribute**

But it also supports a shortcut form. If only a package name is specified, it’ll try to search for the app instance, in the following order:


With **--app=proj**:

- an attribute named **proj.app**, or
- an attribute named **proj.celery**, or
- any attribute in the module **proj** where the value is a Celery application, or

If none of these are found it’ll try a submodule named proj.celery:

- an attribute named **proj.celery.app**, or
- an attribute named **proj.celery.celery**, or
- Any attribute in the module **proj.celery** where the value is a **Celery** application.

This scheme mimics the practices used in the documentation – that is, **proj:app** for a single contained module, and **proj.celery:app** for larger projects.

