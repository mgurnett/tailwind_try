from machine import Pin, ADC
import machine

# ===============  Wifi 
ssid = 'HomeLab'
password = 'Max2024!'
URL = 'http://192.168.1.205:8000/api/add/'

# ===============  Time
TZ = -5

# ===============  Board pins
board_led = machine.Pin('LED', machine.Pin.OUT)
sensor_temp = machine.ADC(4)

buttonK4= Pin(5, Pin.IN, Pin.PULL_UP)
buttonK3= Pin(4, Pin.IN, Pin.PULL_UP)
buttonK2= Pin(3, Pin.IN, Pin.PULL_UP)
buttonK1= Pin(2, Pin.IN, Pin.PULL_UP)

led1 = Pin(21, Pin.OUT)
led2 = Pin(20, Pin.OUT)
led3 = Pin(19, Pin.OUT)
led4 = Pin(18, Pin.OUT)

VBUS_POWER          = 24        # GP24 (USB or battery power indicator)
USBpower = Pin(VBUS_POWER, Pin.IN)

    if USBpower() != 1:  # check to see if on battery or USB power

# main.py file
#import constant as const

#print('Value of PI:', cons.PI)
#print('Value of Gravitational force:', cons.GRAVITY)

#curl -X POST -H 'Content-Type: application/json' -d '{"recorded": "2024-12-18T21:21:41.799476Z", "value": 9.5, "sensor": 61}' http://127.0.0.1:8000/api/add/
