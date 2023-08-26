import requests
import json 
from typing import Any
from random import choice
import regular_client

data = {
  "title": "",
  "code": f"print({choice(range(100, 1000))})",
  "linenos": False,
  "language": "python",
  "style": "friendly"
}

def post():
    res = requests.post(
        data=data,
        url=regular_client.URL.path
    )

    print(res.status_code, res.text)
    print(res)
    


if __name__ == "__main__":
    post()