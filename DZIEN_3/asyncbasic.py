import asyncio
import time

async def count():
    print("jeden")
    await asyncio.sleep(1)
    print("dwa")
    return 10

async def main():
    s = count()
    g = count()
    h = count()
    await asyncio.gather(s,g,h)
    print(s)
    return 100

if __name__ == '__main__':
    s = time.perf_counter()
    f = asyncio.run(main())
    print(f)
    e = time.perf_counter() - s
    print(f"{__file__} wykonał się w {e:0.2f} s")

