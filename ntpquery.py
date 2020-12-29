# NTP Query script using Python3
import socket
import struct
import sys
import time
def RequestTimefromNTP(addr="0.de.pool.ntp.org"):
    REF_TIME_1970 = 2208988800
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    data = b'\x1b' + 47 * b'\0'
    client.sendto(data,(addr,123))
    data,address = client.recvfrom(1024)
    if data:
        t = struct.unpack('!12I',data)[10]
        t -= REF_TIME_1970
    return time.ctime(t),t
# invoke the script
if __name__ == '__main__':
    print(RequestTimefromNTP())