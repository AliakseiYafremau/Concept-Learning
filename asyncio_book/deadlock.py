from threading import Lock, Thread
from time import sleep

lock_a = Lock()
lock_b = Lock()


def func_a():
    with lock_a:
        sleep(0.5)
        with lock_b:
            print("func a")


def func_b():
    with lock_b:
        with lock_a:
            print("func b")


thread_a = Thread(target=func_a)
thread_b = Thread(target=func_b)
thread_a.start()
thread_b.start()
thread_a.join()
thread_b.join()
