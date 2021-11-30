import asyncio
import time

"""def say_after(delay, text):
    time.sleep(delay)
    print(text)


say_after(5, "привет")"""


async def say_after(delay, text):
    await asyncio.sleep(delay)
    print(text)


async def main():
    task1 = asyncio.create_task(say_after(3, "привет"))
    task2 = asyncio.create_task(say_after(3, "Хай"))
    print("Time start:", time.strftime("%X"))
    await task1
    await task2
    print("Time end", time.strftime("%X"))

asyncio.run(main())