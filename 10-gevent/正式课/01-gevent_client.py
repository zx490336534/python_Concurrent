import socket
import gevent
from gevent import monkey
monkey.patch_all()

client_list = []

for i in range(10):
    s = socket.socket()
    s.connect(('127.0.0.1',8888))
    s.send(b'Welcome')
    client_list.append(s)

def read(conn):
    data = conn.recv(1024)
    if not data:
        print('没有数据')
        conn.close()
    print('sever_message:',data)

if __name__ == '__main__':
    tasks = [gevent.spawn(read,conn) for conn in client_list]
    gevent.joinall(tasks)