from time import perf_counter_ns

def time_counter(func): # Выводит время выполнения функции
    def wrapper(*args, **kwargs): # обертка
        start_time = perf_counter_ns() # начало отсчета времени
        result = func(*args, **kwargs) # вызов функции
        final_time = perf_counter_ns() # конец отсчета времени
        print("Procces time:", final_time - start_time, "nanoseconds")
        return result # возвращение результата
    return wrapper # возвращение обертки