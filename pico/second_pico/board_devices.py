import machine
import utime

# addresses on the board
board_led = machine.Pin('LED', machine.Pin.OUT)
sensor_temp = machine.ADC(4)
button = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_UP)
board_led_red = machine.Pin(21, machine.Pin.OUT)
board_led_yellow = machine.Pin(18, machine.Pin.OUT)
 
def led_blink (on_time, off_time):
    board_led.value(1)
    utime.sleep(on_time)
    board_led.value(0)
    utime.sleep(off_time)
    
def blink_led (style, number):
    if style == "waiting":
        for x in range (number + 1):
            led_blink (1,0.4)
    if style == "warning":
        for x in range (number + 1):
            led_blink (0.3,0.3)
    if style == "running":
        for x in range (number + 1):
            led_blink (0.2,0.8)
            
def board_temp():
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = round(27 - (reading - 0.706)/0.001721, 1)
    return temperature  #float
    
if __name__ == "__main__":
    blink_led ('running', 5)
    print (str(board_temp()))
    while True:
        board_led_red.value(0)
        board_led_yellow.value(0)
        if button.value() == 0:
            board_led_red.value(0)
            board_led_yellow.value(1)
        else:
            board_led_red.value(1)
            board_led_yellow.value(0)
    
