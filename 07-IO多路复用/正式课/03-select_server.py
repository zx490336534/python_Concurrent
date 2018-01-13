# select 函数

# 文件描述符
# f = open('xxx','a')
# 读 写

import socket
import select
import queue

sock = socket.socket()
print('socket创建成功')
sock.bind(('127.0.0.1',8888))
sock.listen(5)

inputs = [sock,] #要监听的socket list
'''
select 函数需要三个参数
1.接收了消息的socket
2.需要发信息的socket
3.有错误的socket

返回一个收到了消息的socket
发了消息的socket
'''

outputs = [] #要监听的socket list
message_dic = {}

while True:
    print('等待select监听') #轮询
    readable,writeable,exceptional = select.select(inputs,[],[]) #接收三个参数：一个要监听的读的list，一个写的list 一个error的list
    for s in readable:
        if s is sock: #如果判断成立，表示发生变化的是服务端的sock 也就是来了新的连接
            conn,addr = s.accept()
            print('新的连接建立成功')
            inputs.append(conn)
            message_dic[conn] = queue.Queue()
        else:
            try:
                data = s.recv(1024)
                print('clinet_message',data,)
                message_dic[s].put(data)
                outputs.append(s)
                if data:
                    s.send(data)
            except Exception as e:
                if s in outputs:
                    outputs.remove(s)
                print('连接已经断开')
                inputs.remove(s)
                s.close()

    # for w in writeable: #要返回给客户端的链接列表
    #     client_data = message_dic[w].get()
    #     print('client_data:',client_data)
    #     w.send(client_data)
    #     outputs.remove(w)