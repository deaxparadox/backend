def fibonacci(num: int | float) -> int:
    if num == 1:
        return 0
    elif num == 2:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)
