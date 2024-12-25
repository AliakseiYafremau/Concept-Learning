import threading
import time

def long_task(task_id):
    print(f"Task {task_id} started")
    time.sleep(2)  # Симулируем длительную операцию
    print(f"Task {task_id} finished")

def without_threading():
    print("Running without threading")
    start_time = time.time()

    for i in range(5):  # Выполняем 5 задач последовательно
        long_task(i)

    end_time = time.time()
    print(f"Time taken without threading: {end_time - start_time:.2f} seconds\n")

def with_threading():
    print("Running with threading")
    start_time = time.time()

    threads = []
    for i in range(5):  # Выполняем 5 задач параллельно
        thread = threading.Thread(target=long_task, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:  # Ждем завершения всех потоков
        thread.join()

    end_time = time.time()
    print(f"Time taken with threading: {end_time - start_time:.2f} seconds\n")

if __name__ == "__main__":
    without_threading()
    with_threading()
