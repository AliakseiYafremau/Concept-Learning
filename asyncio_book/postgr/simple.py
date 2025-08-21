import asyncio
import asyncpg
from util import async_timed


async def select_statement(pool: asyncpg.Pool, stmt: str):
    async with pool.acquire() as connection:
        return await connection.execute(stmt)


@async_timed()
async def main():
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
        await asyncio.gather(*[select_statement(pool, query) for _ in range(100)])


asyncio.run(main())
