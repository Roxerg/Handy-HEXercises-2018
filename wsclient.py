
import json

import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8000') as websocket:
        await websocket.send("weh")




asyncio.get_event_loop().run_until_complete(hello())

asyncio.get_event_loop().run_forever()