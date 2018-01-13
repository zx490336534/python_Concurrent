import socket
import time

sock =socket.socket()
sock.connect(('localhost',8080))
sock.send(b'xxx')
# input()
sock.close()