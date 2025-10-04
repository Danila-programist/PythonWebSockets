import asyncio
import websockets

from config import settings

class Client:
    def __init__(self, url: str):
        self.url = url

    async def echo_connect(self):
        async with websockets.connect(self.url) as ws_client:
            await ws_client.send("Привет, сервер!")
            reply = await ws_client.recv()
            print(f"Ответ от сервера: {reply}")


client = Client(url=settings.WEB_SOCKET_URL) 
asyncio.run(client.echo_connect())