import json
import logging

from channels.generic.websocket import AsyncWebsocketConsumer

from .tasks import process_iot_data

logger = logging.getLogger(__name__)


class IoTConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		logger.info("WebSocket connection attempt")
		await self.accept()
		logger.info("WebSocket connection accepted")
		await self.send(text_data=json.dumps({'message': 'Connected to IoT WebSocket'}))

	async def disconnect(self, close_code):
		logger.info(f"WebSocket disconnected with code: {close_code}")

	async def receive(self, text_data):
		logger.info(f"Received data: {text_data}")
		try:
			data = json.loads(text_data)
			# Trigger Celery task for processing
			process_iot_data.delay(data)

			await self.send(text_data=json.dumps({
				'message': 'Data received and processing initiated',
				'status': 'success'
			}))
		except json.JSONDecodeError:
			await self.send(text_data=json.dumps({
				'message': 'Invalid JSON data',
				'status': 'error'
			}))
		except Exception as e:
			await self.send(text_data=json.dumps({
				'message': f'Error processing data: {str(e)}',
				'status': 'error'
			}))
