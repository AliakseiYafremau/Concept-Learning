import asyncio
from util import async_timed, delay


@async_timed()
async def cpu_bound() -> list[int]:
    return [i for i in range(100000000)]


@async_timed()
async def main():
    task1 = asyncio.create_task(cpu_bound())
    task2 = asyncio.create_task(cpu_bound())
    task3 = asyncio.create_task(delay(5))
    await task1
    await task2
    await task3


if __name__ == "__main__":
    asyncio.run(main())
