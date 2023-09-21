from celery import Celery

app = Celery(
    'project',
    backend="redis://localhost", 
    broker='amqp://localhost',
    include=['project.celery.tasks']
)

if __name__ == "__main__":
    app.start()