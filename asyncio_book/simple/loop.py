from util import delay
import asyncio


def call():
    print("Вызов функции")


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call)  # call() вызовется на следующей итерации цикла событий
    await delay(1)  # Запускается delay() и когда она приостановится, запустится call()


asyncio.run(main())
