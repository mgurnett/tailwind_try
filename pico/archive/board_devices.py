import machine
import utime
import constants as const
from oled_setup import *

# BOX = purple
# FONT_COLOUR = red
# HIGHLIGHT_BOX = red
# HIGHLIGHT_FONT_COLOUR = purple
BOX = white
FONT_COLOUR = black
HIGHLIGHT_BOX = black
HIGHLIGHT_FONT_COLOUR = white
 
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

def menu_item (pos, text, highlight = False):
    box = BOX
    font_color = FONT_COLOUR
    top_pos = pos*40+10
    bottom_pos = 30
    if highlight:
        font_color = HIGHLIGHT_FONT_COLOUR
        box = HIGHLIGHT_BOX
        
    display.fill_rectangle(15, top_pos, 215, bottom_pos, color=box)
    display.set_color(font_color, box)
    display.set_pos(30,top_pos+3)
    display.set_font(tt24)
    display.print(text)

def clear_display():
    display.erase()
    
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
    
