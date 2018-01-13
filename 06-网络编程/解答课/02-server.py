#先写服务端
import socket
from multiprocessing.dummy import Pool

sock = socket.socket() #套接字
sock.bind(('127.0.0.1',8080)) #这个服务器已经把这个机子上的这个端口占用了
# sock.bind(('',8080)) #对外开放

sock.listen(5) #监听

pool = Pool() #线程池

def func(conn,addr):
    msg = conn.recv(1024) #字节为单位
    print(b'recive message from client: %s' % msg) #处理了
    conn.close()


while True:
    # 一个accept只能接收一个，并且阻塞
    conn,addr = sock.accept() #真正的等待连接（会阻塞）
    print('established connection from %s'% str(addr)) #连接了
    # msg = conn.recv() #conn也是一个sock，直接和客户端连接的，recv会阻塞直到对方发了东西
    pool.apply_async(func,args=(conn,addr))