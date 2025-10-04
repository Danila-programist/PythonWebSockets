import asyncio
import websockets

from config import settings

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    async def handler(self, websocket):
        async for message in websocket:
            print(f"Получено: {message}")
            await websocket.send(f"Вы сказали: {message}")

    async def main(self):
        async with websockets.serve(self.handler, self.host, self.port) as server:
            print(f"Сервер запущен на ws://{self.host}:{self.port}")
            await server.serve_forever()


if __name__ == "__main__":
    server = Server(host=settings.WEB_SOCKET_HOST, port=settings.WEB_SOCKET_PORT)
    asyncio.run(server.main())
