from core.models import *
import random
from datetime import datetime, timedelta 

# from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd


def set_alarms():
    readings = Reading.objects.all()
    for reading in readings:
        if reading.alarm_state != "Cleared" and reading.value > reading.sensor.alarm:
            reading.alarm_state = 1
            reading.save()


def run():  
    
    delete = History.objects.all().delete()
