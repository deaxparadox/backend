from celery import Celery

app = Celery(
    'project',
    backend="redis://localhost:6379", 
    broker='redis://localhost:6379',
    include=['project.tasks']
)

if __name__ == "__main__":
    app.start()