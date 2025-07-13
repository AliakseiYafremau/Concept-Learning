from time import time
from functools import wraps
from typing import Callable, Any


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"// Выполняется {func} с аргументами {args} {kwargs}")
            start = time()
            try:
                return await func(*args, **kwargs)
            finally:
                total = time() - start
                print(f"// {func} завершилась за {total} секунд")

        return wrapped

    return wrapper


def timed(func: Callable):
    async def wrapper(*args, **kwargs) -> Any:
        print(f"// Выполняется {func} с аргументами {args} {kwargs}")
        start = time()
        try:
            return await func(*args, **kwargs)
        finally:
            total = time() - start
            print(f"// {func} завершилась за {total} секунд")

    return wrapper
