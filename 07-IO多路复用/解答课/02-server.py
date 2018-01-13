import socket
import select
import time

# select.select() #调用系统的select函数
#需要监控，是否可以读的列表
#需要监控，是否可以写的列表
#需要监控，是否有错的列表

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #可以解决端口占用的问题
server.bind(('127.0.0.1',8000))
server.listen(5)




is_readable = [server,]
while True:
    readable,_,_, = select.select(is_readable,[],[]) #阻塞到第一个东西准备好
    # print(readable[0] is server)
    for sock in readable:
        if sock is server:
            conn,addr = sock.accept() #此时，accept() 不会阻塞 此时服务端已经出现了两种socket
            #server accept以后，就变回了不可读状态
            is_readable.append(conn)
        else: #客户端发消息来了
            sock.recv(1024)




# conn,addr = sock.accept() #如果没有人请求，那么就会阻塞。如果已经有人请求了，那就不阻塞
input('>>>')
print(time.time())
conn,addr = sock.accept()
print(time.time())