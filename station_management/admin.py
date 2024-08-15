from django.contrib import admin

from .models import Battery, IoTData, SwappingStation

admin.site.register(SwappingStation)
admin.site.register(Battery)
admin.site.register(IoTData)
