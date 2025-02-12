import machine
import constants as const
            
def board_temp():
    conversion_factor = 3.3 / (65535)
    reading = const.sensor_temp.read_u16() * conversion_factor 
    temperature = round(27 - (reading - 0.706)/0.001721, 1)
    return temperature  #float