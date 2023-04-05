#przypadek1

import math
import time

def pomiarczasu(funkcja):
    def wrapper(*args):
        starttime = time.perf_counter()
        a = funkcja(*args)
        endtime = time.perf_counter()
        print(f"czas wykonania funkcji: {endtime-starttime} s")
        return a
    return wrapper


def sleep(funkcja):
    def wrapper(*args):
        time.sleep(3)
        return funkcja(*args)
    return wrapper

@sleep
@pomiarczasu
def big_lista():
    sum([i**2 for i in range(1_000_000)])

big_lista()

@pomiarczasu
def big_eval(a,b):
    return math.exp(a)+a**b

big_eval(4,188)

def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f"wołana funkcja to: {funkcja.__name__}")
        funkcja(*args,**kwargs)
    return wrapper

@debug
def info(i):
    print(f"informacja: {i}.")

info("dziś ostatni dzień rejestracji na zawody!")


def repeater(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper

@repeater(n=15)
@pomiarczasu
def gx(m):
    print(m*math.exp(m-2))

gx(7)






