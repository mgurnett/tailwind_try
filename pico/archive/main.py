import utime
import urequests
import constants as const
from board_devices import *
import network   # handles connecting to WiFiimport machine
#from wifi import *

def wifi_connect():
    # Create an object, wlan, to create a connection from our code to the Pico W wireless chip.
    # We use this connection to issue commands that will connect and check our Wi-Fi connection.
    wlan = network.WLAN(network.STA_IF)
    # Turn on the Raspberry Pi Pico W’s Wi-Fi.
    wlan.active(True)
    # Connect to your router using the SSID and PASSWORD stored in the secrets.py file.
    wlan.connect(const.ssid, const.password)

    max_wait = 100
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >=3:
            print(f'wlan.status {str(wlan.status())}')
            menu_item (0,f'wlan.status {str(wlan.status())}')
            break
        max_wait -= 1
        print('waiting for connection')
        menu_item (1,f'waiting for connect {max_wait}')
        utime.sleep_ms(1000)

     # Handle connection error
    if wlan.status() != 3:
        menu_item (3,'network connection failed')
#         raise RuntimeError('network connection failed')
        return wlan.status()
    else:
        print('connected')
        menu_item (2,'connected')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )
        menu_item (3,'ip = ' + status[0])
        return status[0]
    
if __name__ == "__main__":
    while True:
        ip = wifi_connect()
        menu_item (4,f'Final: {ip}')
        