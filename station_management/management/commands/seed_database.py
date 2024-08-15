import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from station_management.models import Battery, IoTData, SwappingStation


class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **kwargs):
        # Create SwappingStations
        for i in range(5):
            SwappingStation.objects.create(
                name=f"Station {i + 1}",
                location=f"Location {i + 1}",
                status=random.choice(["Active", "Inactive"]),
                battery_count=random.randint(10, 50),
            )

        # Create Batteries
        stations = SwappingStation.objects.all()
        for i in range(20):
            Battery.objects.create(
                serial_number=f"SN-{i + 1}",
                capacity=random.uniform(50.0, 100.0),
                current_charge=random.uniform(0.0, 100.0),
                status=random.choice(["Available", "In Use", "Under Maintenance"]),
                station=random.choice(stations),
            )

        # Create IoTData
        batteries = Battery.objects.all()
        now = datetime.now()
        for i in range(50):
            IoTData.objects.create(
                battery=random.choice(batteries),
                timestamp=now - timedelta(days=random.randint(0, 10)),
                temperature=random.uniform(20.0, 40.0),
                voltage=random.uniform(3.0, 4.5),
                current=random.uniform(0.0, 10.0),
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database"))
