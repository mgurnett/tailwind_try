from core.models import *

def latest_readings():
    sensors = Sensor.objects.all()
    for sensor in sensors:
        if sensor.latest_reading is not None:
