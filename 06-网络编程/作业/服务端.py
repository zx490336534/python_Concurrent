import socket


s = socket.socket()
server_addr = ('127.0.0.1',8080)
s.bind(server_addr)
s.listen(5)

while True:
    conn,client_addr = s.accept()
    while True:
        data = conn.recv(1024)
        if data == b'break':
            break
        data = data.decode('utf-8')
        print('{}发送的消息为：{}'.format(client_addr,data))
        send_data = input('请输入要发送的内容：')
        conn.send(send_data.encode())
        break

conn.close()
s.close()


