import asyncio
from asyncio import Semaphore


async def some_operation(semaphore: Semaphore):
    print("Ожидание захвата")
    async with semaphore:
        print("Захват")
        await asyncio.sleep(1)
    print("Освобождение")


async def main():
    semaphore = Semaphore(5)
    await asyncio.gather(*[some_operation(semaphore) for _ in range(10)])


asyncio.run(main())
