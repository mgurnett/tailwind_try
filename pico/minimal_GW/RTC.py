import machine
import time
import utime
import struct
import constants as const
import socket
import urequests
from board_devices import *
from wifi import *
from machine import Pin

def time_string ():
    return f'{time.localtime()[0]}-{time.localtime()[1]}-{time.localtime()[2]} {time.localtime()[3]}:{time.localtime()[4]:02}:{time.localtime()[5]:02}'

def set_time(hrs_offset=-5, debug = False):
    NTP_DELTA = 2208988800
    host = "pool.ntp.org"

    led = Pin("LED", Pin.OUT)

    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    except:
        return
    finally:
        s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    t = val - NTP_DELTA + hrs_offset * 3600 
    tm = time.gmtime(t)
    machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))
    

if __name__ == "__main__":
    ip = None
    ip = get_wifi()
    if ip:
        print (f'ip: {ip}')
    else:
        ip = None
        print (f'ip: NOT SET')
        
    set_time(-5)
    print (time.localtime())
