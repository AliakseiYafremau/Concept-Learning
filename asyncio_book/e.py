import asyncio
from util import async_timed
from asyncio import Future


async def set_value(future: Future) -> None:
    await asyncio.sleep(3)
    future.set_result(25)


def make_request() -> Future:
    # Создаем обьект, которому будет присвоено значение в будущем
    future_object = Future()
    # Создаем задачу, которая после присвоет значение будущему обьекту
    asyncio.create_task(set_value(future_object))
    # Возвращаем обьект (он все еще "пустой")
    return future_object


@async_timed()
async def main():
    future_obj = make_request()
    print("Готовность обьекта:", future_obj.done())
    value = await future_obj  # Ожидаем значение обьекта
    print("Готовность обьекта:", future_obj.done())
    print("Значение:", value)


asyncio.run(main())
