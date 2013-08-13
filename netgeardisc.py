import socket
import time

p = b'000200000000000000000000000100000c07d2f20000000000000000000000000000000000000000'
me = '192.168.9.201'

sout = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sout.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sout.bind((me, 64513))
try:
    while True:
        sout.sendto(p, ('<broadcast>', 64515))
        time.sleep(0.5)
except KeyboardInterrupt:
    sout.close()
