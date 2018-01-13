import socket
'''
bind()  绑定地址（127.0.0.1,8000）到套接字
listen() 开始TCP监听
accept() 被动的接收TCP客户端连接（默认阻塞的）
connect() 主动发起TCP连接
recv()  接收数据
send() 发送数据 返回值是字符串的字节数

recvfrom() 接收UDP数据
sendto() 发送UDP数据
close() 关闭套接字
'''

# udp server
sock = socket.socket(type=socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',8000))
while True:
    data,addr = sock.recvfrom(1024)
    print(data,addr)
sock.close()