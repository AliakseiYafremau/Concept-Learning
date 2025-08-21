from types import TracebackType
import socket
import asyncio


class ConnectionSocket:
    def __init__(self, sock: socket.socket):
        self._sock = sock

    async def __aenter__(self):
        loop = asyncio.get_running_loop()
        self._connection, _ = await loop.sock_accept(self._sock)
        return self._connection

    async def __aexit__(
        self, exc_type: BaseException, exc_val: BaseException, exc_tb: TracebackType
    ):
        self._connection.close()
