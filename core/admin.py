from django.contrib import admin
from .models import *

# admin.site.register (Reading)
admin.site.register (Default)

@admin.register (Chain)
class ChainAdmin (admin.ModelAdmin):
    list_display = ["serial_number", "name", "description", "ip", "latest_update"]

@admin.register (Sensor)
class SensorAdmin (admin.ModelAdmin):
    list_display = ["chain", "depth", "wire1_id", "alarm"]

@admin.register (Reading)
class ReadingAdmin (admin.ModelAdmin):
    list_display = ["recorded", "value", "sensor", "alarm_state"]

@admin.register (History)
class HistoryAdmin (admin.ModelAdmin):
    list_display = ["hour", "sensor", "average", "high"]

@admin.register (Archive)
class ArchiveAdmin (admin.ModelAdmin):
    list_display = ["recorded", "value", "sensor", "alarm_state"]

@admin.register (Status)
class StatusAdmin (admin.ModelAdmin):
    list_display = ["recorded", "battery", "chain", "internal_temp"]
