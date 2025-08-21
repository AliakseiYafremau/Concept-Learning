import asyncio
from util import delay, async_timed


@async_timed()
async def incorrect():
    [await asyncio.create_task(delay(2)) for _ in range(3)]


@async_timed()
async def a_little_bit_better():
    tasks = [asyncio.create_task(delay(2)) for _ in range(3)]
    [await task for task in tasks]


asyncio.run(incorrect())
asyncio.run(a_little_bit_better())
