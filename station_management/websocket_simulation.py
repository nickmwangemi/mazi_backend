import asyncio
import json
import random

import websockets


async def send_iot_data():
    uri = "ws://localhost:8001/ws/iot/"
    async with websockets.connect(uri) as websocket:
        # Simulate connection message
        response = await websocket.recv()
        print(f"< {response}")

        # Simulate sending IoT data
        for _ in range(100):  # Send 100 messages
            data = {
                "battery_serial": f"BAT-{random.randint(1000, 9999)}",
                "station_id": random.randint(1, 10),
                "temperature": round(random.uniform(20, 60), 2),
                "voltage": round(random.uniform(3.6, 4.2), 2),
                "current": round(random.uniform(0, 10), 2),
                "charge_level": random.randint(0, 100),
            }
            await websocket.send(json.dumps(data))
            print(f"> Sent: {data}")

            response = await websocket.recv()
            print(f"< {response}")

            await asyncio.sleep(1)  # Wait for 1 second between messages


asyncio.get_event_loop().run_until_complete(send_iot_data())
