from cachetools import cached,LRUCache,TTLCache
import time

@cached(cache=TTLCache(maxsize=33,ttl=15))
def specfunc(n):
    s = time.perf_counter()
    time.sleep(n)
    print(f"\nCzas wykonania: {time.perf_counter()-s} s")
    return f"funkcja wykonana: {n}"

print(specfunc(3))
print(specfunc(3))
time.sleep(20)
print(specfunc(3))
