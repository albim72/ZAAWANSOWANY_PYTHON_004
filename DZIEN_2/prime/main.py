import time
import concurrent.futures
from funkcja_prime import znajdz_sume_liczb_pierwszych

numbers = [(1,40000),(3,50000),(5000,45000),(4,42000),(800,39000)]

def run_heavy_function(params):
    return znajdz_sume_liczb_pierwszych(*params)

def synchroniczna():
    start_time = time.perf_counter()
    for pair in numbers:
        prime_suma = znajdz_sume_liczb_pierwszych(*pair)
        print(prime_suma)
    end_time = time.perf_counter()
    print(f"całkowity czas wyznaczenia sum liczb pierwszych w procesie "
          f"synchronicznym wynosi: {end_time-start_time:.2f} s")

def asynchroniczna():
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        wynik = executor.map(run_heavy_function,numbers)
    print(list(wynik))
    end_time = time.perf_counter()
    print(f"całkowity czas wyznaczenia sum liczb pierwszych w procesie "
          f"asynchronicznym wynosi: {end_time - start_time:.2f} s")

def main():
    synchroniczna()
    asynchroniczna()

if __name__ == '__main__':
    main()
