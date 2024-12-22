import asyncio

from decorators.time_counter import time_counter


async def slow_function():
    await asyncio.sleep(1) # имитация долгой операции
    print("Long function")
    return 0

async def fast_function():
    print("Fast function")
    return 0

@time_counter # вернет время, за которое создастся корутина
async def main():
    result = await asyncio.gather(
        slow_function(),
        fast_function()
    )


if __name__ == '__main__':
    asyncio.run(main())