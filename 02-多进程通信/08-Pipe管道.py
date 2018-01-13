#Pipe 管道
#发送send 接收recv 关闭close
from multiprocessing import Pipe,Process
import time

def procl(pipe):
    while True:
        for i in range(1000):
            print('发送{}'.format(i))
            pipe.send(i)
            time.sleep(1)


def pro(pipe):
    while True:
        print('pro 接收 : ',pipe.recv())
        time.sleep(1)



if __name__ == '__main__':
    pipe = Pipe() #返回元祖 默认是双向的 conn1 conn2 duplex=False---单向
    print(pipe)
    p1 = Process(target=procl,args=(pipe[1],))
    p2 = Process(target=pro,args=(pipe[0],))

    p1.start()
    p2.start()
    p1.join()
    p2.join()