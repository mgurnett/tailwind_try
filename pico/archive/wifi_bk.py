import machine
import utime
import constants as const
import network   # handles connecting to WiFiimport machine
from board_devices import *

def connect_to_wifi():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(const.ssid, const.password)
    
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        blink_led ("waiting", 1)
        double_blink ()
    ip_address = wlan.ifconfig()[0]
    return ip_address

def wifi_connect():
    try:
        ip = connect_to_wifi()
        #print(f'Connected on {ip}')
    except KeyboardInterrupt:
        ip = 0
    return ip

def wifi_connect2():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(const.ssid, const.password)
    
    max_wait = 10
    while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        return = wlan.ifconfig()

if __name__ == "__main__":
    ip = wifi_connect2()
    print (ip)


    while wlan.isconnected() == False:
        print('Waiting for connection...')
        blink_led ("waiting", 1)
        double_blink ()
    ip_address = wlan.ifconfig()[0]
    return ip_address