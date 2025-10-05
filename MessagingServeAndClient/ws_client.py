import asyncio
import websockets

from config import settings

class Client:
    def __init__(self, url: str):
        self.url = url

    async def connect(self):
        async with websockets.connect(self.url) as ws_client:
            
            async def receive():
                async for message in ws_client:
                    print(f"\n💬 От сервера: {message}")

            async def send():
                loop = asyncio.get_event_loop()
                while True:
                    text = await loop.run_in_executor(None, input, "")
                    await ws_client.send(text)
            
            await asyncio.gather(send(), receive())


client = Client(url=settings.WEB_SOCKET_URL) 
asyncio.run(client.connect())