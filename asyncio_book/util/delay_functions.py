import asyncio


async def delay(delay_seconds: int) -> int:
    print(f"Start sleep {delay_seconds}")
    await asyncio.sleep(delay_seconds)
    print(f"Finish sleep {delay_seconds}")
    return delay_seconds
