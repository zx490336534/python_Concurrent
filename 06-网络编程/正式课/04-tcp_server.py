#TCP服务端
#1.导入模块
import socket

#2.创建TCPsocket对象
sock =socket.socket()

#3.绑定ip地址和端口
sock.bind(('127.0.0.1',8080))

#4.开始监听
sock.listen(5)

while True:
    #5.阻塞，等待连接建立 返回一个通道和地址
    conn,addr = sock.accept()
    print('有客户端建立连接地址是{}'.format(addr))
    #6.接收数据
    while True:
        data = conn.recv(1024)
        if data == b'break':
            break
        data = data.decode('utf-8')
        print(data)
        send_data = input('请输入要发送的内容：')
        conn.send(send_data.encode())
        break


conn.close()#关闭管道
sock.close()#关闭套接字