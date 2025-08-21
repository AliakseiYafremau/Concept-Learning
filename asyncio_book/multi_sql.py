import asyncio
import asyncpg
from util import async_timed
from concurrent.futures import ProcessPoolExecutor


async def select_statement(pool: asyncpg.Pool, stmt: str):
    async with pool.acquire() as connection:
        return await connection.execute(stmt)


def execute_stmt(amount: int):
    async def run():
        query = "SELECT * FROM brand"
        async with asyncpg.create_pool(
            host="127.0.0.1",
            port=5432,
            user="postgres",
            database="products",
            password="1234",
            min_size=2,
            max_size=2,
        ) as pool:
            return await asyncio.gather(
                *[select_statement(pool, query) for _ in range(amount)]
            )

    return [result for result in asyncio.run(run())]


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as process_pool:
        tasks = [
            loop.run_in_executor(process_pool, execute_stmt, 1000000)
            for _ in range(100)
        ]
        results = await asyncio.gather(*tasks)
        print(len(results))


asyncio.run(main())
