import machine
import utime
from RTC import *

# ===============  Board pins
board_led = machine.Pin("LED", machine.Pin.OUT)
sensor_temp = machine.ADC(4)

# =========== battery declorations
BATT_ADC = machine.ADC(machine.Pin(26))  # Use GP26


def led_blink(on_time, off_time):
    board_led.value(1)
    utime.sleep(on_time)
    board_led.value(0)
    utime.sleep(off_time)


def double_blink():
    led_blink(0.25, 0.25)
    led_blink(0.25, 0.25)


def board_temp():
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706) / 0.001721, 1)
    return temperature  # float


def get_time():
    return time.localtime()[3] * 3600 + time.localtime()[4] * 60 + time.localtime()[5]


def debug_save(text, time=False):
    with open("debug_file.txt", "a") as the_file:
        if time:
            log_time = time_string()
            the_file.write(f"Log time {log_time}: {text}\n")
            print(f"{log_time}: {text}\n")
        else:
            the_file.write(f"{text}\n")
            print(f"{text}\n")


def get_batt_voltage(cal_number=1.0):
    # Read the ADC value (0-65535)
    adc_value = BATT_ADC.read_u16()
    # Convert to voltage (0-3.3V)
    battery_voltage = adc_value * (3.3 / 65535) * 2 * cal_number
    return battery_voltage
