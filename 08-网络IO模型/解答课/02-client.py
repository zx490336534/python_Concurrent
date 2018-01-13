import socket
import selectors
import random
sel = selectors.DefaultSelector() #整个监控机制

def read(sock): #函数调用的前提是，这个可读事件已经发生了
    recv_data = sock.recv(1024)
    if not recv_data:
        sel.unregister(sock)
        sock.close()
        return
    print(recv_data)


def write(sock):
    sock.send(str(random.randint(0,99)).encode())
    # 一个sock只能一次注册一个事件
    sel.unregister(sock) #取消对可写的监听
    sel.register(sock,selectors.EVENT_READ,read)

for i in range(100):
    client = socket.socket()
    # accept 生成一个你的配对的那个sock，你才能给它发
    sel.register(client, selectors.EVENT_WRITE, write)
    client.connect(('127.0.0.1', 8080))
    # 可以写了么？不一定 如果对方accept了，那就能写，如果没有就不能



while True: #我一直监控，一直检查 哪些事件发生了，发生了我就调用对应的回调

    for event,_ in sel.select(): #sel.select() 就是和select()作用是一样的 看什么东西发生了
        # sel.select() 会把你注册所有事件中所有已经发送的给你返回，并且返回的是一个特殊的对象
        #它不仅把socket房子里面，而且把回调函数也放在里面
        sock = event.fileobj #获得这个sock
        callback = event.data #获得回调函数
        callback(sock) #调用
