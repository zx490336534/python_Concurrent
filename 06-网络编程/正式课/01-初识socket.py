# osi 5层 物理层 数据链路层 网络层 传输层 应用层

# TCP/IP协议（族）

# IP地址 能定位互联网上面的一台电脑
# 端口2^16=65536 定位一台计算机上的某个进程 443-https 22-ssh

# TCP协议 是面向连接 在收发数据之前必须建立可靠连接

# 三次握手 建立连接
# 四次挥手 断开连接

# UDP协议 是非连接的


#socket
import socket

# s =socket.socket(family=,type=) #默认创建TCP协议
# family - AF INET(网络进程之间的通信) AF UNIX(同一台机器之间的通信)
# type - SOCK_STREAM TCP协议 SOCK_DGRAM UDP协议

#TCP socket
import socket
s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
print(s)

# UDP网络程序
# 1.创建套接字
# 2.发送信息
# 3.关闭套接字

import socket
sock = socket.socket(type=socket.SOCK_DGRAM)
send_addr = ('127.0.0.1',8080)
send_data = input('请输入要发送的数据：')
sock.sendto(send_data.encode(),send_addr)
sock.close()