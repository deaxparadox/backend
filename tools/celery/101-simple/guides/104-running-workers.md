# Running a Celery worker server

You can now run the worker by executing our program with the worker argument:

```bash
$ celery -A tasks worker --loglevel=INFO
```

For a complete listing of the command-line options available, do:

```bash
$ celery worker --help
```

There are also several other commands avaiable, and help is also available:

```bash
$ celery --help
```