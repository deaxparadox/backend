# Choosing a Broker

Celery requries a solution to send and receive messages; usually this comes in the form of a separate service called a message broker.

There are several choices avaiable, including:

### RabbitMQ

RabbitMQ is feature-complete, stable, durable and easy to install. It’s an excellent choice for a production environment. Detailed information about using RabbitMQ with Celery:

If you’re using Ubuntu or Debian install RabbitMQ by executing this command:

```bash
$ sudo apt-get install rabbitmq-server
```

Or, if you want to run it on Docker execute:

```bash
$ docker run -d -p 5672:5672 rabbitmq
```

For using RabbitMQ broker use **amqp://localhost**


### Redis

Redis is also feature-complete, but is more susceptible to data loss in the event of abrupt termination or power failures. Detailed information about using Redis:

If you want to run it on Docker execute this:

```bash
$ docker run -d -p 6379:6379 redis
```

For using Radis broker use **redis://localhost**
