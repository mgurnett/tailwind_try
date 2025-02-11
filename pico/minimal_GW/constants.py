from machine import Pin, ADC
import machine, onewire, ds18x20

# ===============  Wifi 
ssid = 'GranaryWatch'
password = 'Sam5000!!!'
ip_address = 'http://192.168.1.200'
port = '37797'

# ip_address = 'http://10.70.70.100'
# port = '8000'

# ip_address = 'http://192.168.1.205'
# port = '8000'

# ===============URLs
READINGS_URL = f'{ip_address}:{port}/api/add/'
# READINGS_URL = 'http://10.70.70.100:8000/api/add/'
STATUS_URL = f'{ip_address}:{port}/api/status/'

# ===============  Time
TZ = -7

# ===============  Board pins
board_led = machine.Pin('LED', machine.Pin.OUT)
sensor_temp = machine.ADC(4)

# =========== battery declorations
BATT_ADC = machine.ADC(machine.Pin(26)) # Use GP26

# ===============  Constants
# time to sleep for each reading
SLEEP_TIME = 1000 * 60 * 5  # 5 minutes

# Maximum number of data points that can be transmitted at once.
LEN_MAX = 10

# Maximum number of data points that can be stored
MAX_STORAGE = 200

# The minumum amount of space that can be free
MIN_FREE = 80

# The number of transmission cycles that pass for a battery update.
BATT_UPDATE = 10

# Battery voltage cal or fudge number
CAL_NUMBER = 1.0