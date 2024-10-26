from typing import Callable

def cached(func: Callable[[int], int]) -> Callable[[int], int]:
    cache = {}

    def wrapper(n: int) -> int:
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper

def fibonacci_no_cache(n: int) -> int:
    if n <= 1:
        return 1
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)

@cached
def fibonacci(n: int) -> int:
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
