from threading import Thread, RLock


lock = RLock()


def fib(v: int) -> int:
    with lock:
        if v == 0:
            return 0
        elif v == 1:
            return 1
        else:
            return fib(v - 1) + v


thread = Thread(target=fib, args=(10,))
thread.start()
thread.join()
