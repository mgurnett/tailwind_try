import machine
import utime
import constants as const

def led_blink (on_time, off_time):
    const.board_led.value(1)
    utime.sleep(on_time)
    const.board_led.value(0)
    utime.sleep(off_time)
    
def double_blink():
    led_blink (.25,.25)
    led_blink (.25,.25)
            
def board_temp():
    conversion_factor = 3.3 / (65535)
    reading = const.sensor_temp.read_u16() * conversion_factor 
    temperature = round(27 - (reading - 0.706)/0.001721, 1)
    return temperature  #float