from django.contrib import admin
from .models import SwappingStation, Battery, IoTData

admin.site.register(SwappingStation)
admin.site.register(Battery)
admin.site.register(IoTData)