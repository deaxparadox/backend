# Configuration

Celery, like a consumer appliance, doesn't need much configuration to operate. It has an input and output.  The input must be connected to a broker, and the output can be optionally connected to a result backend. However, if you look closely at the back, there’s a lid revealing loads of sliders, dials, and buttons: this is the configuration.

The default configuration should be good enough for most use cases, but there are many options that can be configured to make Celery work exactly as needed. Reading about the options available is a good idea to familiarize yourself with what can be configured. 

The configuration can be set on the app directly or by using a dedicated configuration module. As an example you can configure the default serializer used for serializing task payloads by changing the **task_serializer** setting:

```py
app.conf.task_serializer = 'json'
```

If you’re configuring many settings at once you can use update:

```py
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)
```

----------

For larger projects, a dedicated configuration module is recommended. Hard coding periodic task intervals and task routing options is discouraged. It is much better to keep these in a centralized location. This is especially true for libraries, as it enables users to control how their tasks behave. A centralized configuration will also allow your SysAdmin to make simple changes in the event of system trouble.

You can tell your Celery instance to use a configuration module by calling the **app.config_from_object()** method:

```py
app.config_from_object('celeryconfig')
```

This module is often called “celeryconfig”, but you can use any module name.

In the above case, a module named celeryconfig.py must be available to load from the current directory or on the Python path. It could look something like this:

**celeryconfig.py**:

```py
broker_url = 'pyamqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True
```

To verify that your configuration file works properly and doesn’t contain any syntax errors, you can try to import it:

```bash
$ python -m celeryconfig
```

----------

To demonstrate the power of configruation files, this is how you'd route a misbehaving task to a decdicated queue:

**celeryconfig.py**:

```py
task_routes = {
    'tasks.add': 'low-priority',
}
```

Or instead of routing if you could rate limit the task instead, so that only 10 tasks of this type can be processed in a minute (10/m):

**celeryconfig.py**:

```py
task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}
```

If you’re using RabbitMQ or Redis as the broker then you can also direct the workers to set a new rate limit for the task at runtime:


```bash
celery -A tasks control rate_limit tasks.add 10/m
worker@example.com: OK
    new rate limit set successfully
```