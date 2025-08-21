import logging
import socket
import asyncio


def get_server_socket(address: str, port: int) -> socket.socket:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((address, port))
    server_socket.setblocking(False)
    return server_socket


async def echo(conn: socket.socket, loop: asyncio.AbstractEventLoop):
    try:
        while data := await loop.sock_recv(conn, 1024):
            if data == b"caboom\n":
                raise Exception
            response = f"Here is your message: {data}\n"
            await loop.sock_sendall(conn, response.encode())
    except Exception as ex:
        logging.exception(ex)
    finally:
        conn.close()


async def listen_socket(server_socket: socket.socket, loop: asyncio.AbstractEventLoop):
    while True:
        connection, _ = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        asyncio.create_task(echo(connection, loop))


async def main():
    server = get_server_socket("127.0.0.1", 8000)
    server.listen()

    await listen_socket(
        server_socket=server,
        loop=asyncio.get_running_loop(),
    )


asyncio.run(main())
