# Things that need to be done.
1. DONE!!!! Get history displaying as a graph
2. have an archive button in history - DONE - sort of
3. have a enable/disable of bins.
4. DONE!!!! Fix the permissions for the picture.
5. Make a focus graph
6. have the model for readings show a delta
7. Done!!!! add internal temp for the box.
    Done!!!!display it on the screen
    have an alarm set up.
8. done!!!!!measure battery for pico
    DONE!!!! I need to write another API to tell the system the chain's voltage.
9. Have an initialise chain button. This will delete all data, archive and history for that chain.
10. Set up a full alarm system. It need to include, sensor temps, LOS from chain, internal temp, battery low,
11. DONE!!!!!add serial number to the chain. GW.###### 00900s are prototypes and 01000 are production
12. I need a CRM as a second app. Customer info, Maximizer and serial information


```
import machine
import time

# Configure the ADC pin
adc = machine.ADC(machine.Pin(26)) # Use GP26


while True:

# Read the ADC value (0-65535)
adc_value = adc.read_u16()

# Convert to voltage (0-3.3V)
voltage = adc_value * (3.3 / 65535)

# Calculate the actual battery voltage (multiply by 2)
battery_voltage = voltage * 2

print("Battery Voltage:", battery_voltage, "V")
time.sleep(1000) # Read every 1 second
```
  

[finite state machine](https://github.com/viewflow/django-fsm)

```
class Stage(Enum):

NEW = 1
DONE = 2
HIDDEN = 3

class MyFlow(object):
state = State(Stage, default=Stage.NEW)
```
