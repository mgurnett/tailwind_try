import utime
import urequests
import constants as const
from board_devices import *
import network   # handles connecting to WiFiimport machine
import machine   # or import from machine depending on your micropython version

#see new_wifi as it has some good ideas

def wifi_connect(debug=False):
    # Create an object, wlan, to create a connection from our code to the Pico W wireless chip.
    # We use this connection to issue commands that will connect and check our Wi-Fi connection.
    wlan = network.WLAN(network.STA_IF)
    # Turn on the Raspberry Pi Pico W’s Wi-Fi.
    wlan.active(True)
    # Connect to your router using the SSID and PASSWORD stored in the secrets.py file.
    wlan.connect(const.ssid, const.password)

    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >=3:
#             print(f'wlan.status {str(wlan.status())}')
            menu_item (0,f'wlan.status {str(wlan.status())}') if debug else None
            break
        max_wait -= 1
#         print('waiting for connection')
        menu_item (1,f'waiting for connect {max_wait}') if debug else None
        utime.sleep_ms(1000)

     # Handle connection error
    if wlan.status() != 3:
        menu_item (3,'network connection failed') if debug else None
#         raise RuntimeError('network connection failed')
        return None
    else:
#         print('connected')
        menu_item (2,'connected') if debug else None
        status = wlan.ifconfig()
#         print( 'ip = ' + status[0] )
        menu_item (3,'ip = ' + status[0]) if debug else None
#         return status[0]
        return status[0]
    
def get_wifi(debug=False):
    ip = None
    connect_attempt = 5
    while connect_attempt > 0 and ip == None:
        ip = wifi_connect()
        if ip == None:
            connect_attempt =- 1
        
    if ip == None:
        return None
    else:
        menu_item (4,f'IP: {ip}') if debug else None
        menu_item (5,f'ca: {connect_attempt}') if debug else None
        return ip
    
if __name__ == "__main__":
    clear_display ()
    new_ip = get_wifi()
    if new_ip:
        menu_item (5,f'Final: {new_ip}')

        
