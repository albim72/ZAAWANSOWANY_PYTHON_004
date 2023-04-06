from cachetools import cached,LRUCache
import time

@cached(cache=LRUCache(maxsize=3))
def specfunc(n):
    s = time.perf_counter()
    time.sleep(n)
    print(f"\nCzas wykonania: {time.perf_counter()-s} s")
    return f"funkcja wykonana: {n}"

print(specfunc(3))
print(specfunc(3))
print(specfunc(2))
print(specfunc(1))
print(specfunc(4))
print(specfunc(1))
print(specfunc(3))
