import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(f"Получено: {message}")
        await websocket.send(f"Вы сказали: {message}")

async def main():
    async with websockets.serve(echo, "localhost", 8768) as server:
        print("Сервер запущен на ws://localhost:8768")
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
