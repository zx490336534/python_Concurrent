from multiprocessing import Process,Queue
import os
import time
import random

#写数据的函数
def write(q):
    for value in range(10):
        print('put {} to queue...'.format(value))
        q.put(value)
        time.sleep(random.random())

#读数据的函数
def read(q):
    while True:
        if not q.empty():
            value = q.get()
            print('get {} from queue...'.format(value))
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    q = Queue(10)
    p1 = Process(target=write,args=(q,))
    p2 = Process(target=read,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('数据写入读取完成')


