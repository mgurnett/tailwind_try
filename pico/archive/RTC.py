import machine
import time
import utime
import struct
import constants as const
import socket

NTP_DELTA = 2208988800
host = "pool.ntp.org"

def set_time(TZ):
    print ("setting the time")
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(host, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    finally:
        s.close()
    val = struct.unpack("!I", msg[40:44])[0]
    t = val - NTP_DELTA - (TZ * 3600)
    tm = time.gmtime(t)
#     machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))

if __name__ == "__main__":
    set_time(-5)
    print(time.localtime())
    
    timestamp = utime.time() - 2208988800 + (5 * 3600)
    print (type(timestamp))
    print (timestamp)
    tm = time.gmtime(timestamp)
    print (tm)