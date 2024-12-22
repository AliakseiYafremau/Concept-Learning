from decorators.time_counter import time_counter


@time_counter # Выводит время выполнения функции
def f(n):
    sum = 0
    for number in range(n):
        sum += number
    return sum


print(f(1000))