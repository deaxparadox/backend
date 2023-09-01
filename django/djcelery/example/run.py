import time 

from tasks import fibo, add

runners = [
    fibo.delay(40), 
    fibo.delay(40), 
    fibo.delay(40), 
    fibo.delay(40)
]

status: bool = True
total_runners = len(runners)
count: int = 0
while status:

    for t in runners:
        if not t.ready():
            print(f"RUNNING: {t.id}")
            time.sleep(1)
        else:
            count += 1
            print(f"COMPLETED: {t.id} RESULT: {t.get()}")
    

    if count == total_runners:
        status = False
