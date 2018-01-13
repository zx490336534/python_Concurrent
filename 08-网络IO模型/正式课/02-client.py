import socket

sock = socket.socket()
sock.connect(('127.0.0.1',8080))

data = input('>>>')
sock.send(data.encode())
print(sock.recv(1024))