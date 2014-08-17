import socket
import time
import sys

if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
    print('netgeardisc <my IP>')
    sys.exit(1)
else:
    me = sys.argv[1]


p = b'000200000000000000000000000100000c07d2f20000000000000000000000000000000000000000'

sout = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sout.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sout.bind((me, 64513))
try:
    while True:
        sout.sendto(p, ('<broadcast>', 64515))
        time.sleep(0.5)
except KeyboardInterrupt:
    sout.close()
