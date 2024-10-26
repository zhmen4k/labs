import pytest
import time
from labalotornie import fibonacci, fibonacci_no_cache

def test_fibonacci_values():

    expected_values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i, expected in enumerate(expected_values):
        assert fibonacci(i) == expected
        assert fibonacci_no_cache(i) == expected

def test_fibonacci_performance():
    n = 30

    start_time_cached = time.time()
    fibonacci(n)
    end_time_cached = time.time()
    time_cached = end_time_cached - start_time_cached

    start_time_no_cache = time.time()
    fibonacci_no_cache(n)
    end_time_no_cache = time.time()
    time_no_cache = end_time_no_cache - start_time_no_cache

    print(f"Час виконання з кешуванням: {time_cached} секунд")
    print(f"Час виконання без кешування: {time_no_cache} секунд")

    assert time_cached < time_no_cache
