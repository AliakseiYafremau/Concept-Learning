import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests
from util import async_timed
from functools import partial
from threading import Lock


request_amount = 10000
urls = ["http://www.example.com" for _ in range(request_amount)]
counter_lock = Lock()
counter = 0


def get_status(url: str):
    result = requests.get(url).status_code
    global counter
    counter = counter + 1
    return result


async def reporter(request_count: int):
    while counter < request_count:
        print("Завершено:", counter)
        await asyncio.sleep(1)


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as thread_pool:
        tasks = [
            loop.run_in_executor(thread_pool, partial(get_status, url)) for url in urls
        ]
        report = asyncio.create_task(reporter(request_amount))
        results = await asyncio.gather(*tasks)
        await report
        for result in results:
            print(result)
        print("Counter:", counter)


asyncio.run(main())
