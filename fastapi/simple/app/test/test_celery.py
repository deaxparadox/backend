from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_celery_task_id():
    response = client.get("/celery")
    assert response.status_code == 200