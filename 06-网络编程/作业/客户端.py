import socket

sock = socket.socket()

sock.connect(('127.0.0.1',8080))

while True:
    data = input('请输入要发送的内容：')
    if len(data) == 0:
        break
    sock.send(data.encode())
    content = sock.recv(1024)
    content = content.decode('utf-8')
    print(content)
sock.close()


