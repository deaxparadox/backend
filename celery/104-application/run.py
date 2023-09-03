import time 


from project.tasks import add

runners = [
    add.delay(40, 41), 
    add.delay(40, 41), 
    add.delay(40, 41), 
    add.delay(40, 41)
]

status: bool = True
total_runners = len(runners)
count: int = 0

pending = []

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
