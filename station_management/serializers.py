from rest_framework import serializers
from .models import SwappingStation, Battery, IoTData

class SwappingStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwappingStation
        fields = '__all__'

class BatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Battery
        fields = '__all__'

class IoTDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IoTData
        fields = '__all__'