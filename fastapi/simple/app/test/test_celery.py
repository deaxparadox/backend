from fastapi.testclient import TestClient
import httpx

from app.main import app

client = TestClient(app)


class CeleryTest(object):
    def __init__(self) -> None:
        self.__status_code: None|int = None

    def get(self, url: str):
        response: httpx.Response = httpx.get(url)
        self.__status_code = response.status_code
        return self
    
    def test(self):
        if self.__status_code:
            assert ...
    


def test_celery_task_id():
    response = httpx.get("http://localhost:8000/celery")
    assert response.status_code == 200
    task_id = response.json().get("task_id")
    assert isinstance(task_id, str)

