import random
import time


from rich.live import Live
from rich.table import Table


from celery.tasks.tasks import fibo, add

num = 40

runners = [
    fibo.delay(num), 
    fibo.delay(num), 
    fibo.delay(num), 
    fibo.delay(num)
]
status: bool = True
total_runners = len(runners)
count: int = 0

def generate_table() -> Table:
    global status, total_runners, count

    """Make a new table."""
    table = Table()
    table.add_column("status")
    table.add_column("ready")
    table.add_column("id")
    table.add_column("value")

    # for row in range(random.randint(2, 6)):
    #     value = random.random() * 100
    #     table.add_row(
    #         f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
    #     )


    for t in runners:
        t_ready = t.ready()
        t_id = t.id
        
        if not t_ready:
            # print(f"RUNNING: {t.id}")
            
            table.add_row(
                f"{t.status}",
                f"{t_ready}",
                f"[red]{t_id}" if not t_ready else f"[green]{t_id}",
                f"{t.get()}"
            )
            # time.sleep(1)
        else:
            count += 1
            # print(f"COMPLETED: {t.id} RESULT: {t.get()}")
            table.add_row(
                f"{t.status}",
                f"{t_ready}",
                f"[red]{t_id}" if not t_ready else f"[green]{t_id}",
                f"{t.get()}"
            )
        

    return table


with Live(generate_table(), refresh_per_second=4) as live:
    while status:
        time.sleep(0.4)
        live.update(generate_table())


        if count == total_runners:
            status = False

    
    
