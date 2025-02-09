import os
from core.models import *
import random
from datetime import datetime, timedelta 
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

# from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from django.core.management import call_command

def backup_battery(bin):


    file_path = os.path.join('core', 'battery.json')

    try:
        objects_to_backup = Status.objects.filter(chain=bin) 

        with open(file_path, "w") as out:
            mast_point = serializers.serialize("json", objects_to_backup)
            out.write(mast_point)

        return True
    except Exception as e:
        print(f"Error during backup: {e}")
        return False


def load_battery_data():
    file_path = os.path.join('core', 'battery.json')

    try:
        call_command('loaddata', file_path)
        return True
    except Exception as e:
        print(f"Error during restore: {e}")
        return False


def run():  
    # bin = Chain.objects.get(serial_number="GW.00901")
    
    # if backup_battery(bin):
    #     print("Backup successful!")
    # else:
    #     print("Backup failed!")


    # temp_bin = Chain.objects.get(serial_number="GW.00902")
    # Status.objects.filter(chain=bin).update(chain=temp_bin)

    if load_battery_data():
        print("Restore successful!")
    else:
        print("Restore failed!")
