from datetime import datetime, time
from time import sleep
from core.models import *
from icecream import ic
from django.db import models
from django.db.models import Avg, Max
import pandas as pd
from core.helpers.archive import archive


def run():
    archive()
        

            

