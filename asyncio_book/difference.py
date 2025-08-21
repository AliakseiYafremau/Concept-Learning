import requests
import asyncio
from util import async_timed, time_count
from concurrent.futures import ThreadPoolExecutor
from functools import partial


def get_status(url):
    return requests.get(url).status_code


urls = ["http://www.example.com" for _ in range(1000)]


@async_timed()
async def async_main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as thread_pool:
        tasks = [
            loop.run_in_executor(thread_pool, partial(get_status, url)) for url in urls
        ]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)


@time_count()
def sync_main():
    results = [get_status(url) for url in urls]
    for result in results:
        print(result)


asyncio.run(async_main())
sync_main()
