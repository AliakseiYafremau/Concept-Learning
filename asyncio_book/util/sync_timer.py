import time
from functools import wraps


def time_count():
    def wrapper(func):
        wraps(func)

        def wrapped(*args, **kwargs):
            print(f"// Выполняется {func} с аргументами {args} {kwargs}")
            start = time.time()
            try:
                return func(*args, **kwargs)
            finally:
                total = time.time() - start
                print(f"// {func} завершилась за {total} секунд")

        return wrapped

    return wrapper
