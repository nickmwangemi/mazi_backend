from rest_framework import viewsets
from .models import SwappingStation, Battery, IoTData
from .serializers import SwappingStationSerializer, BatterySerializer, IoTDataSerializer

class SwappingStationViewSet(viewsets.ModelViewSet):
    queryset = SwappingStation.objects.all()
    serializer_class = SwappingStationSerializer

class BatteryViewSet(viewsets.ModelViewSet):
    queryset = Battery.objects.all()
    serializer_class = BatterySerializer

class IoTDataViewSet(viewsets.ModelViewSet):
    queryset = IoTData.objects.all()
    serializer_class = IoTDataSerializer