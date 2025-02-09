from core.models import *
import random
from datetime import datetime, timedelta 

def make_bins():  # Make all the sensors on a chain. 
    some_bins = [{"bin": "#1", "description": "The east bin", "IP": "10.0.0.4"},
    {"bin": "#2", "description": "The second from the east bin", "IP": "10.0.0.5"},
    {"bin": "#3", "description": "The middle bin", "IP": "10.0.0.6"},
    {"bin": "#4", "description": "The second from the west bin", "IP": "10.0.0.7"},
    {"bin": "#5", "description": "The west bin", "IP": "10.0.0.8"},
    {"bin": "#6", "description": "dryer bin", "IP": "10.0.0.9"},]
    for ms in some_bins:
        chain = Chain (
            name = ms["bin"],
            description = ms["description"],
            ip = ms["IP"]
        )
        print(chain)
        chain.save()  

def make_sensors():
    bins = Chain.objects.all()     
    for b in bins:
        for i in range(5, 35, 5):
            success = False
            while not success:
                random_number = random.randint(100, 400)
                sensor = Sensor (
                    chain = b,
                    depth = i,
                    wire1_id = f"28-12346{random_number}"
                )
                try:
                    sensor.save()
                except:
                    success = False
                else:
                    success = True


def make_fake_readings():  # Make all the sensors on a chain. 
    for time_index in range (0, 1440, 2):
        reading = Reading (
            sensor = Sensor.objects.get(wire1_id="28-12346270"),
            value = (time_index / 25) - 15,
            recorded = datetime.now() + timedelta(minutes=time_index)
        )
        reading.save()
        reading = Reading (
            sensor = Sensor.objects.get(wire1_id="28-12346121"),	
            value = (time_index / 25) - 5,
            recorded = datetime.now() + timedelta(minutes=time_index+2)
        )
        reading.save()
        reading = Reading (
            sensor = Sensor.objects.get(wire1_id="28-12346234"),	
            value = (time_index / 25) + 2,
            recorded = datetime.now() + timedelta(minutes=time_index+4)
        )
        # print(reading)
        reading.save()

def run():
    # Default.temparature = -10
    # make_bins()
    # make_sensors()
    delete = Reading.objects.all().delete()
    make_fake_readings()