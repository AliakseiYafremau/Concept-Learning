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
    server_socket = get_server_socket("127.0.0.1", 8000)
    selector = selectors.DefaultSelector()
    selector.register(server_socket, selectors.EVENT_READ)
    while True:
        events: list[tuple[selectors.SelectorKey, int]] = selector.select()

        for event, _ in events:
            event_socket = event.fileobj

            if event_socket == server_socket:
                connection, _ = server_socket.accept()
                connection.setblocking(False)
                response = f"Connection established. Your connection: {connection.getpeername()}. All connections: \n"
                # for con in connections:
                #    response += f"- {con.getpeername()}\n"
                response += "Enter your message:\n"
                selector.register(connection, selectors.EVENT_READ)
            else:
                data = event_socket.recv(1024)
                response = f"Here is your data: {data}"
                event_socket.send(response.encode())


if __name__ == "__main__":
    main()
