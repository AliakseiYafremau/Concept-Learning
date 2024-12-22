first_variable = 4
second_variable = 5

def decorator(func): # Декоратор с аргументом в виде функции, которую он будет оборачивать
    def wrapper(a, b): # Обертка, которая принимает аргументы функции
        print("-----") # Дополнительный функционал, для которого мы и используем декоратор
        func(a, b) # Вызов самой функции
        print("-----") # Дополнительный функционал, для которого мы и используем декоратор
    return wrapper # Возвращаем обертку/функцию

def simple_function(a, b): # функция, которую мы будем оборачивать
    print("Sum of simply decorated function:", a + b)

@decorator # Используем синтаксический сахар для обертки функции
def sintatic_sugar_function(a, b):
    print("Sum of sintatic sugar decorated function:", a + b)

decorated_function = decorator(func=simple_function) # Указываем функцию, которую хотим обернуть и получаем обертку/функцию с дополнительным функционалом
decorated_function(first_variable, second_variable) # Вызываем обертку/функцию с необходимыми аргументами

sintatic_sugar_function(first_variable, second_variable) # Вызываем обертку/функцию с необходимыми аргументами
