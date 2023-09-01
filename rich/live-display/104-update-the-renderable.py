import random
import time

from rich.live import Live
from rich.table import Table



count: int = 0

def generate_table() -> Table:
    global count

    
    """Make a new table."""
    table = Table()
    table.add_column("ID")
    table.add_column("Value")
    table.add_column("Status")

    for row in range(random.randint(2, 6)):
        value = random.random() * 100
        table.add_row(
            f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
        )
        count += 1
        
    return table



with Live(generate_table(), refresh_per_second=4) as live:
    while count < 100:
        time.sleep(0.4)
        live.update(generate_table())

        if count > 10:
            break