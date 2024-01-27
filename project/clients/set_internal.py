import multiprocessing
from typing import Callable
import sys
import time


def wrapper(func: Callable, task_id: str, delay: int):
    func(task_id)
    time.sleep(delay)

def setInterval(func: Callable | None = None, task_id: str | None = None, delay: int | None = None):
    if func is None:
        sys.exit(1)
    if task_id is None:
        sys.exit(1)
    

    p = multiprocessing.Process(target=wrapper, args=(func, task_id, delay))
    p.start()
    p.join()


if __name__ == '__main__':
    def main():
        print("I am working...")

    setInterval(main, 'asd', 1)