import asyncio
import websockets

async def client():
    async with websockets.connect("ws://localhost:8768") as clienter:
        await clienter.send("Привет, сервер!")
        reply = await clienter.recv()
        print(f"Ответ от сервера: {reply}")

asyncio.run(client())