import requests
import json
import random
import typing

class Add(object):
    def __init__(self):
        self.__url: str = "http://localhost:8000/da/add/"
        self.__id: str|None = None
        self.__request: requests.Response|None = None

    def request(self, **kwargs):
        self.__request = requests.post(
            data=kwargs,
            url=self.__url,
        )
        return self
    
    def process(self):
        print(self.__request.text)
        self.__id = json.loads(self.__request.text)["id"]
        return self

    def result(self):
        print(requests.get(f"http://localhost:8000/da/add/?id={self.__id}").text)
        return


def main():
    a = Add()

    iterate_range = 1
    x = [random.randint(100, 1000) for i in range(iterate_range)]
    y = [random.randint(100, 1000) for j in range(iterate_range)]

    for i, j in zip(x, y):
        a.request(x=i, y=j).process().result()

if __name__ == "__main__":
    main()