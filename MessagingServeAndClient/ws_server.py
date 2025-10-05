import asyncio
import websockets

from config import settings

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.websocket = None

    async def handler(self, websocket):
        self.websocket = websocket

        async for message in websocket:
            print(f"📩 От клиента: {message}")


    async def input_loop(self):
        loop = asyncio.get_event_loop()
        while True:
            message = await loop.run_in_executor(None, input, "")
            
            if self.websocket:
                await self.websocket.send(message)

    async def start(self):
        async with websockets.serve(self.handler, self.host, self.port) as server:
            print(f"Сервер запущен на ws://{self.host}:{self.port}")
            asyncio.create_task(self.input_loop())
            await server.serve_forever()


if __name__ == "__main__":
    server = Server(host=settings.WEB_SOCKET_HOST, port=settings.WEB_SOCKET_PORT)
    asyncio.run(server.start())
