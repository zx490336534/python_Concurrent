#让多个客户端连接服务器 多线程 多进程

#把accept recv变成非阻塞

#setblocking(False)
import socket

sock = socket.socket()
sock.bind(('127.0.0.1',9999))
sock.setblocking(False)
sock.listen(5)

client_list = []

while True:
    try:
        conn,addr = sock.accept() #返回一个和客户端的连接
    except:
        pass
    else:
        print('连接建立成功{}'.format(addr))
        client_list.append((conn,addr))
    for client_socket,client_addr in client_list:
        try:
            data = client_socket.recv(1024)
        except:
            pass
        else:
            if len(data) > 0:
                print('{}:{}'.format(client_addr,data))
            else:
                client_socket.close()
                print('客户端{}已经下线'.format(client_addr))
                client_list.remove((client_socket,client_addr))