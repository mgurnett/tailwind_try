import machine
import utime
import constants as const
import network   # handles connecting to WiFiimport machine
from board_devices import *
import urequests

def wifi_connect():
    # Create an object, wlan, to create a connection from our code to the Pico W wireless chip.
    # We use this connection to issue commands that will connect and check our Wi-Fi connection.
    wlan = network.WLAN(network.STA_IF)
    # Turn on the Raspberry Pi Pico W’s Wi-Fi.
    wlan.active(True)
    # Connect to your router using the SSID and PASSWORD stored in the secrets.py file.
    wlan.connect(const.ssid, const.password)
        
    if wlan.isconnected():
        return wlan.ifconfig()[0]
    else:
        return None


if __name__ == "__main__":
    print (wifi_connect())
    astronauts = urequests.get("http://api.open-notify.org/astros.json").json()
    print (astronauts)