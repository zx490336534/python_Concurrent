# 5层模型 传输模型 只需要关注两层（传输层，应用层）
#HTTP 建立在TCP/IP
import socket
socket.socket() #默认参数就是TCP/IP SOCK.STREAM 可靠链接
#HTTP协议就是一串字符串，有特定的格式 bytes字符串，如果添加上了具体的格式要求，满足了HTTP协议 就变成了应用层的HTTP
#我必须要知道的：
'''
1.socket怎么连接的
    服务端：绑定地址（IP和端口），并且监听（要有个while True）
    客户端：主动链接（请求链接）
2.怎么发
    send（字节 b字符串）
3.怎么收
    recv（字节 b字符串）
'''
