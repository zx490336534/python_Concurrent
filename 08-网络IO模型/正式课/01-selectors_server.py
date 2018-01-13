import selectors
import socket

sel = selectors.DefaultSelector() #根据不同的平台 选择对应的select epoll

def accept(sock):
    conn,addr = sock.accept() #建立连接
    # print('accept',conn)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)

def read(conn):
    data = conn.recv(1024)
    if data:
        print('client_message:',data)
        conn.send(data)
    else:
        print('close',conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('127.0.0.1',8080))
sock.listen(5)

sel.register(sock,selectors.EVENT_READ,accept) #注册事件

while True:
    print('select 监听中')
    events = sel.select() #有可能调用的是select，也有可能是epoll
    for event_key,event_mask in events:
        # print(event_key)
        func = event_key.data #获取到回调函数
        # print(event_key.fileobj,'===============')#event_key.fileobj = sock
        func(event_key.fileobj) #调用回调函数


