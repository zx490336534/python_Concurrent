import socket
import time

all_sock = []
for i in range(10):
    sock = socket.socket()
    sock.connect(('127.0.0.1',8080))
    all_sock.append(sock)

time.sleep(2)

for index,sock in enumerate(all_sock):
    sock.send(b'hello i am client %d' % index)