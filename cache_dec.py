from functools import wraps


def cache(func):
    results = []
    @wraps(func)
    def wrapper(*args, **kwargs):
        
    return wrapper



def sum_range(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


for _ in range(4):
    print(sum_range(100000000))
