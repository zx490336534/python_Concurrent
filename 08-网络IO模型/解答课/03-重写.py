import socket
import selectors
import random

#需要监控事件，要什么，要selectors
sel = selectors.DefaultSelector() #自动选择适合你系统的底层方法

def read(sock):
    data = sock.recv(1024)
    if not data:
        sel.unregister(sock)
        sock.close()
        return
    print(data)

def write(sock):
    sock.send(b'xxx')
    sel.unregister(sock)
    sel.register(sock,selectors.EVENT_READ,read)

for i in range(100):
    client = socket.socket()
    sel.register(client,selectors.EVENT_WRITE,write)
    client.connect(('127.0.0.1',8080))

while True:
    all_event = sel.select()
    for event,_ in all_event:
        sock = event.fileobj
        callback = event.data
        callback(sock)