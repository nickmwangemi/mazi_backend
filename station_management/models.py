from django.db import models


class SwappingStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    battery_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Battery(models.Model):
    serial_number = models.CharField(max_length=50, unique=True)
    capacity = models.FloatField()
    current_charge = models.FloatField()
    status = models.CharField(max_length=50)
    station = models.ForeignKey(SwappingStation, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.serial_number


class IoTData(models.Model):
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    voltage = models.FloatField()
    current = models.FloatField()

    def __str__(self):
        return f"IoT Data for {self.battery} at {self.timestamp}"
