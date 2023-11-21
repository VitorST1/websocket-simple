import asyncio
import websockets

connected = []


async def handler(websocket):
    print("Client connected", websocket.id)
    connected.append(websocket)
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            for client in connected:
                if client.id != websocket.id:
                    await client.send(f'{websocket.id}: {message}')
    finally:
        connected.remove(websocket)

start_server = websockets.serve(handler, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
