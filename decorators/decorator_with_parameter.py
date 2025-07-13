def decorator(separator):
    def wrapper(func):
        def inner(*args, **kwargs):
            print(separator * 10)
            return func(*args, **kwargs)
        return inner
    return wrapper


@decorator("2")
def hello(output):
    return output


print(hello("hi"))
