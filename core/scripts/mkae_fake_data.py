import os
from datetime import datetime
import random
import json
from time import sleep

SENSORS = ['28-12346259', '28-12346208', '28-12346250', '28-12346278', '28-12346213', '28-12346111', '28-12346234', '28-12346121', '28-12346270', 
           '28-12346310', '28-12346373', '28-12346384', '28-12346245', '28-12346375', '28-12346118', '28-12346302', '28-12346144', '28-12346308', 
           '28-12346112', 
           '28-12346217', '28-12346268', '28-12346193', '28-12346266', '28-12346185', '28-12346183', '28-12346146', '28-12346356',
           '28-12346289', '28-12346148', '28-12346187', '28-12346325', '28-12346232', '28-12346257', '28-12346218', '28-12346383']



if __name__ == "__main__":

    for temp in range (-30, 30):
        for sensor in SENSORS:
            time = datetime.now()
            time_stamp = time.isoformat() + "Z"
            os.system(f"""curl -X POST -H "Content-Type: application/json" -d '[{{"recorded": "{time_stamp}", "value": {temp}, "sensor": "{sensor}"}}]' http://127.0.0.1:8000/api/add/""")
        print (f'{time_stamp = } {temp = } {sensor = }')
        sleep(5) 
    



# os.system(f'curl -X POST -H "Content-Type: application/json" -d "[{{"recorded": "{time_stamp}", "value": {temp}, "sensor": "{sensor}"}}]" http://127.0.0.1:8000/api/add/')
# curl -X POST -H 'Content-Type: application/json' -d '[{"recorded": "2024-12-30T16:12:41.799476Z", "value": 26.5, "sensor": "28-12346270"}]' http://127.0.0.1:8000/api/add/


            # payload = {"data": [{"recorded": time_stamp, "value": temp, "sensor": sensor}]}
            # json_payload = json.dumps(payload)
            # os.system(f'curl -X POST -H "Content-Type: application/json" -d "{json_payload}" http://127.0.0.1:8000/api/add/')