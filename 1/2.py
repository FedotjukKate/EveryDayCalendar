import asyncio


async def fib(n):
    if n > 1:
        k1 = asyncio.create_task(fib(n - 1))
        k2 = asyncio.create_task(fib(n - 2))
        await asyncio.gather(k1, k2)
        return k1.result() + k2.result()
    else:
        return 1

print(asyncio.run(fib(5)))