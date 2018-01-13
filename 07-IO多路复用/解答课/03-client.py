#我能不能把爬虫分为三个部分
#如果是单线程，按照原来的思路
#发一个请求，等待服务器返回，再接着发下一个
#连接，0.1s-0.3s
#假如是中国爬美国，那么就意味着，每一个爬取都需要花费0.1s-0.3s等待
#阻塞时间：0.2s-0.6s

#一次性把所有的连接都发过去，一次性建立连接
#一次性发请求
#一次性读响应

import socket
import select
import random

is_readable = []
is_writealbe = []

for i in range(100):
    sock = socket.socket()
    sock.connect(('127.0.0.1',8888))
    is_writealbe.append(sock)



while True:
    readable,writeable,_ = select.select(is_readable,is_writealbe,[])

    for sock in writeable:
        sock.send(str(random.randint(0,99)).encode('utf-8'))
        is_readable.append(sock)
        is_writealbe.remove(sock)
    for sock in readable:
        print(sock.recv(1024))