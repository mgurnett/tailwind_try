from machine import Pin, ADC
import machine, onewire, ds18x20

# ===============  Wifi 
ssid = 'GranaryWatch'
password = 'Sam5000!!!'
# URL = 'http://192.168.1.205:8000/api/add/'
URL = 'http://192.168.1.200:37797/api/add/'
STATUS_URL = 'http://192.168.1.200:37797/api/status/'

# ===============  Time
TZ = -7

# ===============  Board pins
board_led = machine.Pin('LED', machine.Pin.OUT)
sensor_temp = machine.ADC(4)


 
ip = None
SLEEP_TIME = 1000 * 90  # 90 seconds
LEN_MAX = 10
MAX_STORAGE = 200
MIN_FREE = 80
BATT_UPDATE = 10

buttonK4= Pin(5, Pin.IN, Pin.PULL_UP)
buttonK3= Pin(4, Pin.IN, Pin.PULL_UP)
buttonK2= Pin(3, Pin.IN, Pin.PULL_UP)
buttonK1= Pin(2, Pin.IN, Pin.PULL_UP)

led1 = Pin(21, Pin.OUT)
led2 = Pin(20, Pin.OUT)
led3 = Pin(19, Pin.OUT)
led4 = Pin(18, Pin.OUT)