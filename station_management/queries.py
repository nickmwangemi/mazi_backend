from django.db.models import Avg, Count

from .models import Battery, SwappingStation


def get_station_statistics():
    return SwappingStation.objects.annotate(
        battery_count=Count("battery"), avg_charge=Avg("battery__charge_level")
    ).values("id", "name", "battery_count", "avg_charge")


def get_low_battery_stations(threshold=20):
    return (
        SwappingStation.objects.filter(battery__charge_level__lt=threshold)
        .distinct()
        .values("id", "name")
    )


def get_battery_history(battery_id):
    return (
        Battery.objects.get(id=battery_id)
        .swaphistory_set.select_related("station")
        .order_by("-swap_time")
    )
