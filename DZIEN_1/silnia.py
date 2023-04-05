#n!=1*2*...*n n -> C
import sys
sys.set_int_max_str_digits(0x1000000)
sys.setrecursionlimit(0x100000)

def silnia(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych")
    wynik = 1
    for i in range(1,n+1):
       wynik *= i
    return wynik


def silnia_rek(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych")
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj wartość agrmumentu n funkcji silnia: "))
    print(f"dla n= {n} silnia wynosi {silnia(n)}")
    print(f"dla n= {n} silnia rekurencyjna wynosi {silnia_rek(n)}")
except ValueError as ve:
    print(ve)
