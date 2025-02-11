import machine
import time

# Configure the ADC pin
adc = machine.ADC(machine.Pin(26)) # Use GP26
board_led = machine.Pin('LED', machine.Pin.OUT)

while True:
    board_led.value(1)
    # Read the ADC value (0-65535)
    adc_value = adc.read_u16()

    # Convert to voltage (0-3.3V)
    cal_number = .855

    # Convert to voltage (0-3.3V)
    battery_voltage = adc_value * (4.0 / 65535) * 2 * cal_number

    board_led.value(0)
    print("Battery Voltage:", battery_voltage, "V")
    time.sleep(1) # Read every 1 second
