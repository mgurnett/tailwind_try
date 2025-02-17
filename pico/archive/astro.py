
import network
from utime import sleep, ticks_ms, ticks_diff
import urequests
ssid = 'HomeLab'
password = 'Max2024!'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

start = ticks_ms() # start a millisecond counter

astronauts = urequests.get("http://api.open-notify.org/astros.json").json()

delta = ticks_diff(ticks_ms(), start)

number = astronauts['number']
print('There are', number, 'astronauts in space.')
for i in range(number):
    print(i+1, astronauts['people'][i]['name'])

print("HTTP GET Time in milliseconds:", delta)