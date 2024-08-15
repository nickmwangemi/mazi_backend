from celery import shared_task
from .models import Battery, IoTData, SwappingStation


@shared_task
def process_iot_data(data):
	try:
		battery = Battery.objects.get(serial_number=data['battery_serial'])
		station = SwappingStation.objects.get(id=data['station_id'])

		IoTData.objects.create(
			battery=battery,
			station=station,
			temperature=data['temperature'],
			voltage=data['voltage'],
			current=data['current'],
			charge_level=data['charge_level']
		)

		# Update battery status
		battery.current_charge = data['charge_level']
		battery.last_seen_at = station
		battery.save()

		# Update station status
		station.available_batteries = Battery.objects.filter(last_seen_at=station, current_charge__gte=90).count()
		station.save()

		# Perform any additional processing or analysis
		if data['temperature'] > 50:  # Example threshold
			alert_high_temperature.delay(battery.id, data['temperature'])

	except Battery.DoesNotExist:
		# Log error: battery not found
		pass
	except SwappingStation.DoesNotExist:
		# Log error: station not found
		pass


@shared_task
def alert_high_temperature(battery_id, temperature):
	# Implement alerting logic (e.g., send email, push notification)
	pass