import asyncio
import json, logging, websockets
import bcrypt, jwt, tempfile, os
import random
from websockets.server import serve, WebSocketServerProtocol
from websockets.exceptions import ConnectionClosed
import json

logging.basicConfig()
logger = logging.getLogger("server") 

async def handler(websocket, path):
    while True:
        data = random.uniform(0.1, 5.0)
            
        await websocket.send(json.dumps(data))
        await asyncio.sleep(0.1)

async def main():
    async with serve(handler, "", 6789):
        await asyncio.Future()  

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
