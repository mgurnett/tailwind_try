import machine, onewire, ds18x20
from machine import Pin
import utime
import urequests
import gc
import os 
import constants as const
from board_devices import *
from wifi import *
from RTC import *
 
# ========= initializations
ip = None
temp_list = []
USB_POWER = False
DEBUG = True

# =============== Serial number
SERIAL_NUMBER = "GW.00901"

# =========== DS18B20 declorations
ds_pin = Pin(27)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
    
def get_time ():
    return time.localtime()[3] * 3600 + time.localtime()[4] * 60 + time.localtime()[5]

def debug_save (text, time=False):
    with open('debug_file.txt', 'a') as the_file:
        if time:
            log_time = time_string()
            the_file.write (f'Log time {log_time}: {text}\n')
            print (f'{log_time}: {text}\n')
        else:
            the_file.write (f'{text}\n')
            print (f'{text}\n')

def get_batt_voltage ():
            # Read the ADC value (0-65535)
            adc_value = const.BATT_ADC.read_u16()
            # Convert to voltage (0-3.3V)
            battery_voltage = adc_value * (3.3 / 65535) * 2 * const.CAL_NUMBER
            if DEBUG: debug_save(f"Battery Voltage: {battery_voltage}V")
            return battery_voltage
    
def init_run ():
    double_blink()
    gc.enable()
    s = os.statvfs('/')
    vbus = Pin('WL_GPIO2', Pin.IN)
    if DEBUG:
        debug_save (f"Free storage: {s[0]*s[3]/1024} KB")
        debug_save (f"Memory: {gc.mem_alloc()} of {gc.mem_free()} bytes used.")
        debug_save (f"CPU Freq: {machine.freq()/1000000}Mhz")
        debug_save (f'init - USB: {vbus()}')
    return vbus()

if __name__ == "__main__":
    USB_POWER = init_run ()
    batt_count = 9
    
    roms = ds_sensor.scan()
    if DEBUG: debug_save  (roms)
    if USB_POWER:
        if DEBUG:
            debug_save ('USB power')
        else:
            debug_save ('Battery power')
            
    const.board_led.value(1)
    
    #  get ip and time
    while ip == None:
        ip = get_wifi()
        if ip:
            set_time(const.TZ)
            if DEBUG: debug_save (f'ip: {ip}', time=True)
        else:
            ip = None
            if DEBUG: debug_save (f'ip: NOT SET')
            
    while True:
        batt_count += 1
        fail_tx_num = 0
        sleep_time_start = get_time ()
        
        gc.collect()  #free up memory
        memory = round(gc.mem_free()/1024, 1)
        if DEBUG: debug_save (f"Memory: {memory}KB", time=True)

        # read all sensors and a small pause
        ds_sensor.convert_temp()
        utime.sleep_ms(750)
        
        for rom in roms:
            tempC = ds_sensor.read_temp(rom)
            temperature = round(tempC,1)
            if DEBUG: debug_save (str(f"Temp: {temperature}C"), time=True)
            time_str = time_string()  # from RTC.py

            # build one record in the log
            log = {"recorded": time_str, "value": temperature, "sensor": rom.hex()}
            if DEBUG: debug_save (log, time=True)

            #if there are too many logs stored, then dump the oldest one based on free memory.
            if (gc.mem_free()/1024) < const.MIN_FREE:
                del temp_list [0] # this was to throw out the oldest data.
                
            #add log to list
            temp_list.append(log)
            if DEBUG: debug_save (f'logs: {len(temp_list)}', time=True)
            
        gc.collect()  #free up memory
        memory = round(gc.mem_free()/1024, 1)
        if DEBUG: debug_save (f"Memory: {memory}KB", time=True)
            
        while len(temp_list) > 0 and fail_tx_num < 5: 
            if DEBUG: debug_save (f'logs: {len(temp_list)}', time=True) 
            if DEBUG: debug_save (f'Sending json', time=True)
            gc.collect()
            memory = round(gc.mem_free()/1024, 1)
            if DEBUG: debug_save (f"Memory: {memory}KB", time=True)
            
            send_list = temp_list [0:const.LEN_MAX]
            try:
                print (const.READINGS_URL, send_list)
                response = urequests.post(const.READINGS_URL, json=send_list)
                if DEBUG: debug_save (f"response code {response.status_code}", time=True) 
                response.close()
            except:
                fail_tx_num +=1             
                if DEBUG: debug_save (f'logs: {len(temp_list)}', time=True)
                if DEBUG: debug_save (f"upload attempt {fail_tx_num}", time=True)
            else:             
                if DEBUG: debug_save (f"response code {response.status_code}", time=True)
                del temp_list [0:const.LEN_MAX]
                if DEBUG: debug_save (f'logs: {len(temp_list)}', time=True)
                fail_tx_num = 0
                
        if DEBUG: debug_save (f'batt_count: {batt_count}', time=True)
        if batt_count >= const.BATT_UPDATE and not USB_POWER:
            batt_count = 0
            batt_voltage = get_batt_voltage ()
            
            internal_temp = board_temp()
            batt_log = {"recorded": time_str, "battery": batt_voltage, "chain": ip, "internal_temp": internal_temp, "serial_number": SERIAL_NUMBER}
            if DEBUG: debug_save (batt_log)
            try:
                print (const.STATUS_URL, batt_log)
                response = urequests.post(const.STATUS_URL, json=batt_log)
                if DEBUG: debug_save (f"response code {response.status_code}", time=True) 
                response.close()
            except:            
                if DEBUG: debug_save (f'Battery: {batt_voltage}V', time=True)
            else:                             
                if DEBUG: debug_save (f"response code {response.status_code}", time=True) 
        
        gc.collect()
        memory = round(gc.mem_free()/1024, 1)
        if DEBUG: debug_save (f"Memory: {memory}KB", time=True)
        
        sleep_time_end = get_time ()
        difference = sleep_time_end - sleep_time_start - 2
        const.board_led.value(0)
        utime.sleep_ms(const.SLEEP_TIME - difference)
        const.board_led.value(1)