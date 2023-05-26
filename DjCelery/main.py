import requests
import json
import time

GET = "http://localhost:8000/?limit=1"
STATUS = "http://localhost:8000/status/{}/"
RESULT = "http://localhost:8000/result/{}/"


def response_id(url: str) -> str | None:
    res = requests.get(url)
    if res.status_code == 200:
        worker_id = json.loads(res.text)["id"]
        return worker_id
    return None

def status(id: str) -> bool:
    res = requests.get(STATUS.format(id))
    if res.status_code == 200:
        status = json.loads(res.text)["status"]
        
        match status:
            case "SUCCESS":
                return True
            case _:
                return False
    return False

def result(id: str) -> str | None:
    res = requests.get(RESULT.format(id))
    if res.status_code == 200:
        result_json = json.loads(res.text)
        return result_json["result"]
    return None

if __name__ == "__main__":
    worker_id = response_id(GET)
    # print(worker_id)
    stat: bool = False
    for i in range(10):
        stat = status(worker_id)
        print(stat)
        if stat:
            break
        time.sleep(1)

    print(result(worker_id))    