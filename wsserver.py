#!/usr/bin/env python
import asyncio
import websockets


import frontend_to_backend

# Receives WS messages and passes them to a function
async def consumer_handler(websocket, path):
    async for message in websocket:
          res = frontend_to_backend.receive_request(message) 
          websocket.send(res) #sends result back to client

start_server = websockets.serve(consumer_handler, 'localhost', 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()