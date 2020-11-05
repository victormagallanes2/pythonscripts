#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

async def time(websocket, ip_port):
    lista = ['test1', 'test2']
    for x in lista:
        await websocket.send(str(x))
        await asyncio.sleep(1)

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()