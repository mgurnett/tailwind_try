from machine import Pin, ADC
import machine, onewire, ds18x20

# ===============  Wifi 
ssid = 'HomeLab'
password = 'Max2024!'
# URL = 'http://192.168.1.205:8000/api/add/'
URL = 'http://192.168.1.200:37797/api/add/'

# ===============  Time
TZ = -7

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

#if USBpower() != 1:  # check to see if on battery or USB power



# main.py file
#import constant as const

#print('Value of PI:', cons.PI)
#print('Value of Gravitational force:', cons.GRAVITY)

#curl -X POST -H 'Content-Type: application/json' -d '{"recorded": "2024-12-18T21:21:41.799476Z", "value": 9.5, "sensor": 61}' http://127.0.0.1:8000/api/add/


SENSORS = ['28-12346186', '28-12346257', '28-12346343', '28-12346294', '28-12346244', '28-12346130',
             '28-12346400', '28-12346323', '28-12346215', '28-12346339', '28-12346309', '28-12346306',
             '28-12346210', '28-12346353', '28-12346242', '28-12346313', '28-12346127', '28-12346263',
             '28-12346348', '28-12346361', '28-12346191', '28-12346192', '28-12346288', '28-12346151',
             '28-12346251', '28-12346331', '28-12346364', '28-12346377', '28-12346229', '28-12346395',
             '28-12346160', '28-12346267', '28-12346227', '28-12346252', '28-12346136', '28-12346312']