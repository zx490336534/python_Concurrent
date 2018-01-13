import socket
import time

sock = socket.socket()
sock.connect(('127.0.0.1',8888))

time.sleep(2)
sock.send(b'hhh')
send_data = input('>>>')
sock.send(send_data.encode())
server_message = sock.recv(1024)
print('server_message:',server_message)
time.sleep(5)
sock.close()