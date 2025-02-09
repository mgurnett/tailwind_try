from datetime import datetime, time
from time import sleep
from core.models import *
from icecream import ic
from django.db import models
import pandas as pd

def days_between_dates(date1, date2):
    return (date2 - date1).days

def get_dates():
    reading = Reading.objects.all().order_by('recorded').first()
    start_date = reading.recorded
    tfh = datetime.now() - timedelta(hours=24)
    num_of_days = days_between_dates (start_date, tfh)
    if num_of_days > 0:
        date_list = [start_date + timedelta(days=x) for x in range(num_of_days)]
        ic(num_of_days,start_date, tfh, date_list)
        return date_list
    else:
        return None

def save_history(target_date):
    start_time = datetime.combine(target_date, time.min)
    end_time = datetime.combine(target_date, time.max)
    readings = Reading.objects.filter(recorded__range=(start_time, end_time))
    # ic (len (readings))
    df = pd.DataFrame(readings.values())
    # ic (df)
    grouped_df = df.groupby(['sensor_id', df['recorded'].dt.hour])

    print ("getting history")
    for by_hour in grouped_df:
        sensor_id = by_hour[0][0]
        hour = by_hour[0][1]
        avg_value = round(by_hour[1]['value'].mean(),1)
        high_value = round(by_hour[1]['value'].max(),1)
        # ic(sensor_id, hour, avg_value, high_value)
        working_date = target_date.replace(hour=hour)
        print (f"working_date: {working_date}", end="\r")

        history = History(
            sensor_id=sensor_id,
            hour=working_date,
            average=avg_value,
            high=high_value
        )
        history.save()
    print ("")

def archive(target_date):
    start_time = datetime.combine(target_date, time.min)
    end_time = datetime.combine(target_date, time.max)
    readings = Reading.objects.filter(recorded__range=(start_time, end_time))
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
        print (f"Archived: {reading['recorded']}", end="\r")

        delete = Reading.objects.get(id = reading["id"])
        # ic (repr(delete), repr(archive))
        delete.delete()
    print ("")


def run():
    target_date_list = get_dates()
    print (f'Dates that will be archived: {target_date_list}')

    if target_date_list is not None:
        for target_date in target_date_list:
            start_len_history = History.objects.all().count()
            # save_history(target_date)
            end_len_history = History.objects.all().count()
            print (f"History: {start_len_history} -> {end_len_history} -> {end_len_history - start_len_history}")

            start_len_readings = Reading.objects.all().count()
            start_len_archives = Archive.objects.all().count()
            # archive(target_date)
            end_len_readings = Reading.objects.all().count()
            end_len_archives = Archive.objects.all().count()
            print (f"Readings: {start_len_readings} -> {end_len_readings} -> {end_len_readings - start_len_readings}")
            print (f"Archives: {start_len_archives} -> {end_len_archives} -> {end_len_archives - start_len_archives}")

    else:
        print ("No dates to archive")

