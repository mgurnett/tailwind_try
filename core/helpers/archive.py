from datetime import datetime, time
from time import sleep
from core.models import *
from icecream import ic
from django.db import models
from django.db.models import Avg, Max
import pandas as pd

def hours_between_dates(time1, time2):
    return int((time2 - time1).total_seconds() / 3600)

def get_hours():
    reading = Reading.objects.all().order_by('recorded').first()
    start_hour = reading.recorded
    tfh = datetime.now() - timedelta(hours=24)
    num_of_hours = hours_between_dates (start_hour, tfh)

    if num_of_hours > 0:
        hour_list = [start_hour + timedelta(hours=x) for x in range(num_of_hours)]
        # ic(num_of_hours,start_hour, tfh, hour_list)
        return hour_list
    else:
        return None

def get_readings_by_hour(date_time):
    hour_start_time = date_time.replace(minute=0, second=0, microsecond=0)
    hour_end_time = hour_start_time + timedelta(hours=1)
    # ic(hour_start_time, hour_end_time)
    readings = Reading.objects.filter(recorded__range=(hour_start_time, hour_end_time))
    if len(readings) == 0:
        # ic("No readings for hour")
        return None
    return readings


def save_history(readings, datetime, save = False):  # we get one hours worth of readings.

    readings_df = pd.DataFrame(list(readings.values('sensor_id').annotate(
            average=Avg('value'),
            high_reading=Max('value')
            )
        )   
    )
    for index, row in readings_df.iterrows():
        # ic (row)

        history = History(
            sensor_id=int(row.sensor_id),
            hour=datetime,
            average=round(row.average,1),
            high=round(row.high_reading,1)
        )
        history.save() if save else None
        # ic (history.__repr__)

def back_up(readings):
    # ic (len (readings))
    df = pd.DataFrame(readings.values())

    print ("Archiving")
    for index, reading in df.iterrows():
        archive = Archive(
            sensor_id=reading["sensor_id"],
            recorded=reading["recorded"],
            value=reading["value"],
            alarm_state=reading["alarm_state"],
        )
        archive.save()
        delete = Reading.objects.get(id = reading["id"]).delete()
        print (f"Archived: {reading['recorded']}  Deleted: {reading['id']}", end="\r")

    print ("")


def archive():
    # delete = History.objects.all().delete()
    # delete = Archive.objects.all().delete()
    print ("Archive started")
    start_len_history = History.objects.all().count()
    target_hour_list = get_hours()
    if target_hour_list is not None:
        print (f"Saving history for {len(target_hour_list)} hours")
        for target_hour in target_hour_list:  #brings back a single hour worth of readings.
            readings_by_the_hour = get_readings_by_hour(target_hour)  #is a <class 'django.db.models.query.QuerySet'>
            # ic (type(readings_by_the_hour), len(readings_by_the_hour))
            if readings_by_the_hour is not None: 
                print (f"Reading for the hour of {target_hour}", end="\r")
                # ic (type(readings_by_the_hour), len(readings_by_the_hour), readings_by_the_hour)
                save_history(readings_by_the_hour, target_hour, save = True)
                back_up(readings_by_the_hour)
        end_len_history = History.objects.all().count()
        print ("")
        print (f"History: {end_len_history - start_len_history}")
    else:
        print ("No dates to archive")
        

            

