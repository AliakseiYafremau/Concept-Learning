import selectors
import socket


def get_server_socket(address: str, port: int, blocking: bool = False) -> socket.socket:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((address, port))
    server_socket.listen()
    server_socket.setblocking(blocking)
    return server_socket


def main():
    connections: list[socket.socket] = []
    server_socket = get_server_socket("127.0.0.1", 8000)
    while True:
        try:
            connection, _ = server_socket.accept()
            connection.setblocking(False)
            connections.append(connection)
            response = f"Connection established. Your connection: {connection.getpeername()}. All connections: \n"
            for con in connections:
                response += f"- {con.getpeername()}\n"
            response += "Enter your message:\n"
            connection.send(response.encode())
        except BlockingIOError:
            pass

        for connection in connections:
            try:
                data = connection.recv(1024)
                if not data:
                    connections.remove(connection)
                else:
                    response = f"Here is your data: {data}"
                    connection.send(response.encode())
            except BlockingIOError:
                pass


if __name__ == "__main__":
    main()
