import hashlib
from functools import partial
import asyncio
from util import async_timed
from concurrent.futures.thread import ThreadPoolExecutor
import time


def hash(password: bytes) -> str:
    return str(
        hashlib.scrypt(
            password,
            salt=b"example",
            n=2048,
            p=1,
            r=8,
        )
    )


passwords = [b"example" for _ in range(10000)]


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    tasks = []
    with ThreadPoolExecutor() as thread_pool:
        for password in passwords:
            tasks.append(loop.run_in_executor(thread_pool, partial(hash, password)))
        await asyncio.gather(*tasks)


asyncio.run(main())
