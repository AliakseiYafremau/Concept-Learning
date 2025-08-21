from threading import Thread
import socket


class CustomThread(Thread):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection

    def run(self):
        try:
            while True:
                data = self.connection.recv(1024)
                print("Получено:", data)
                self.connection.sendall(data)
        except OSError as e:
            print("Поток прерван", e)

    def close(self):
        if self.is_alive():
            self.connection.sendall(bytes("Остановилась!", encoding="utf-8"))
            self.connection.shutdown(socket.SHUT_RDWR)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 8000))
    server.listen()
    threads = []
    try:
        while True:
            connection, _ = server.accept()
            thread = CustomThread(connection)
            threads.append(thread)
            thread.start()
    except KeyboardInterrupt:
        print("Останавливается")
        [thread.close() for thread in threads]
