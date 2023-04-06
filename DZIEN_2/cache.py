from cachetools import cached
import time

def fibonacci(n):
    return n if n<2 else fibonacci(n-1)+fibonacci(n-2)

s = time.perf_counter()
print(fibonacci(21))
print(f"czas realizacji /bez cache/: {time.perf_counter() - s} s")


@cached(cache={})
def fibonacci_cache(n):
    return n if n<2 else fibonacci_cache(n-1)+fibonacci_cache(n-2)

s = time.perf_counter()
print(fibonacci_cache(21))
print(f"czas realizacji /z cache/: {time.perf_counter() - s} s")
