from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Battery, IoTData, SwappingStation
from .serializers import BatterySerializer, IoTDataSerializer, SwappingStationSerializer


class SwappingStationViewSet(viewsets.ModelViewSet):
    queryset = SwappingStation.objects.all()
    serializer_class = SwappingStationSerializer

    @action(detail=True, methods=["GET"])
    def available_batteries(self, request, pk=None):
        station = self.get_object()
        batteries = station.battery_set.filter(status="available")
        serializer = BatterySerializer(batteries, many=True)
        return Response(serializer.data)


class BatteryViewSet(viewsets.ModelViewSet):
    queryset = Battery.objects.all()
    serializer_class = BatterySerializer

    @action(detail=True, methods=["POST"])
    def swap(self, request, pk=None):
        battery = self.get_object()
        station_id = request.data.get("station_id")

        station = get_object_or_404(SwappingStation, id=station_id)

        # check if battery is already assigned to another station
        if battery.station and battery.station.id != station:
            return Response(
                {"error": "Battery is already assigned to another station."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # check if station has capacity for new battery
        if not station.has_capacity():
            return Response(
                {"error": "Swapping station has no available slots."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # perform battery swap
        previous_station = battery.station
        battery.station = station
        battery.save()

        # update station statuses, if required
        if previous_station:
            previous_station.update_status()
        station.update_status()

        return Response(
            {"status": "Battery swapped successfully"}, status=status.HTTP_200_OK
        )


class IoTDataViewSet(viewsets.ModelViewSet):
    queryset = IoTData.objects.all()
    serializer_class = IoTDataSerializer
