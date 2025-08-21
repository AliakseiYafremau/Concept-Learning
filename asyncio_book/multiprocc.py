from multiprocessing import Process, Value, Array


shared_progress: Value


def init(progress: Value):
    global shared_progress
    map_progress = progress


async def main():
    global map_progress

    wit


if __name__ == "__main__":
    asyncio.run(main())
