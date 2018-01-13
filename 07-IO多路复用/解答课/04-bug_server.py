import socket
import time

HOST = 'localhost'
PORT = 8080

server = socket.socket()
server.bind((HOST,PORT))
server.listen(5)
conn,addr = server.accept()

#客户端和服务端通信，一定要一收一发，或一发一收

while True:
    print('循环')
    # print(conn.recv(1024))  #我第一次recv的时候，如果客户端没有发送-阻塞
    #但是，并不是对方发多少个，你就只能收多少次
    #因为，只要你没有send，那么他就认为，一直可以收（或者认为，一直没有收干净）
    msg = conn.recv(1024)
    if not msg:
        break
    time.sleep(1)
