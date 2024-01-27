import requests
import asyncio
import json
import multiprocessing
import enum
import time

class Status(enum.Enum):
    SUCCESS = 0
    PENDING = 1

class Client:
    _url_submit = "http://localhost:9000/maths/submit/"
    _url_result = "http://localhost:9000/api/result/{}/"
    _task_id: str | None = None

    def __init__(self, *args):
        self._a = args[0]
        self._b = args[1]

    def submit(self):
        res = requests.post("http://localhost:9000/maths/submit/", data={"a": self._a, "b": self._b})
        if res.status_code == 202:
            self._task_id = json.loads(res.text).get("task_id")
    
    def _result(self):
        if self._task_id:
            res = requests.get(self._url_result.format(self._task_id))
            
            d = json.loads(res.text)
            if d.get("status") == Status.PENDING.name:
                time.sleep(1)
                self._result()
            else:
                print(d)
    

    def result(self):
        self._result()

    def run(self):
        self.submit()
        self.result()

    def run_multiple(self, pro: int = 1):
        ps = [
            multiprocessing.Process(
                target=self.run
            ) for _ in range(pro)
        ]
        for p in ps:
            p.start()
        for p in ps:
            p.join()


class AyncClient:
    _url_submit = "http://localhost:9000/maths/submit/"
    _url_result = "http://localhost:9000/maths/result/{}/"
    _task_id: str | None = None

    def __init__(self, *args):
        self._a = args[0]
        self._b = args[1]

    async def submit(self):
        res = requests.post("http://localhost:9000/maths/submit/", data={"a": self._a, "b": self._b})
        if res.status_code == 202:
            self._task_id = json.loads(res.text).get("task_id")
    
    def _result(self):
        if self._task_id:
            res = requests.get(self._url_result.format(self._task_id))
            
            d = json.loads(res.text)
            if d.get("status") == Status.PENDING.name:
                self._result()
            else:
                print(d)
    

    async def result(self):
        self._result()
        # self._task_id = json.loads(res.text).get("task_id")
        # print(res.text)

    
        

# async def main():
#     c = Client(10, 2)
#     await c.submit()
#     await c.result()

# def main():
#     asyncio.run(main())
