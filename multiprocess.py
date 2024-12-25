import multiprocessing
import time

def long_task(task_id):
    print(f"Task {task_id} started")
    time.sleep(2)  # Симулируем длительную операцию
    print(f"Task {task_id} finished")

def without_multiprocessing():
    print("Running without multiprocessing")
    start_time = time.time()

    for i in range(5):  # Выполняем 5 задач последовательно
        long_task(i)

    end_time = time.time()
    print(f"Time taken without multiprocessing: {end_time - start_time:.2f} seconds\n")

def with_multiprocessing():
    print("Running with multiprocessing")
    start_time = time.time()

    processes = []
    for i in range(5):  # Выполняем 5 задач параллельно
        process = multiprocessing.Process(target=long_task, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:  # Ждем завершения всех процессов
        process.join()

    end_time = time.time()
    print(f"Time taken with multiprocessing: {end_time - start_time:.2f} seconds\n")

if __name__ == "__main__":
    without_multiprocessing()
    with_multiprocessing()
