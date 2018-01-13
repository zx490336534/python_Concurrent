#发送消息给02-socket对象常用方法.py
import socket
sock = socket.socket(type=socket.SOCK_DGRAM)
send_addr = ('127.0.0.1',8000)
while True:
    send_data = input('请输入要发送的数据：')
    sock.sendto(send_data.encode(),send_addr)
sock.close()