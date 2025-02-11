import utime
import urequests
import constants as const
from board_devices import *
from wifi import *
from RTC import *

ip = None
ip_set = False
time_set = False
temp_list = []
index = 0

if __name__ == "__main__":
    
    while True:            
        clear_display ()
        const.led1.value(1) if not ip_set else const.led1.value(0)
        const.led2.value(1) if not time_set else const.led2.value(0)
        temperature = board_temp()

        menu_item (0,str(f"Temp: {temperature}C"))
        
        if not ip:
            ip = wifi_connect()
        print ("ip: ", ip)
        if ip != 0:
            ip_set = True
            menu_item (1, ip)
        else:
            ip_set = False
        const.led1.value(1) if not ip_set else const.led1.value(0)
        
        print ("time_set: ", time_set, " ---- ip_set: ", ip_set)

        if not time_set and ip_set:
            set_time(const.TZ)
            time_set = True
            
        if time_set:
            time_str = f'{time.localtime()[0]}-{time.localtime()[1]}-{time.localtime()[2]} {time.localtime()[3]}:{time.localtime()[4]:02}:{time.localtime()[5]:02}'
            menu_item (2, time_str)
            print (time_str)
        
#         log = {"recorded": time_str, "value": temperature, "sensor": 46}
        log = {"recorded": time_str, "value": temperature, "sensor": "28-12346193"}
        temp_list.append(log)
        log = {"recorded": time_str, "value": temperature+.2, "sensor": "28-12346268"}
        temp_list.append(log)
        if ip and index > 1:
            try:
                # response = urequests.post(URL, json=log)
                response = urequests.post(const.URL, json=temp_list)
                print (temp_list)
            except:
                menu_item (4, f"response error code {response.status_code}")
            else:
                menu_item (4, f"response code {response.status_code}")
                index = 0
                temp_list = []
        index +=1
        menu_item (3, f"{index}")
        
        #utime.sleep_ms(120000)
        utime.sleep_ms(3000)
