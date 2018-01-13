# Condition 消费者生产者模型 队列

import threading
import time
import random

class Producer(threading.Thread):
    def __init__(self,integer,condition):
        super().__init__()
        self.integer = integer
        self.condition = condition

    def run(self):
        while True:
            integer = random.randint(0,256) #获取一个随机数
            self.condition.acquire()
            self.integer.append(integer)
            print('{}生产了一个{}'.format(self.name,integer))
            self.condition.notify()#唤醒等待的线程
            self.condition.release()#释放


class Consumer(threading.Thread):
    def __init__(self,integer,condition):
        super().__init__()
        self.integer = integer
        self.condition = condition

    def run(self):
        while True:
            self.condition.acquire()
            if self.integer:
                integer = self.integer.pop()
                print('{}删除了{}'.format(self.name,integer))
            else:
                print('{}准备消费，但是没有资源，进入等待'.format(self.name))
                self.condition.wait()

            self.condition.release()

if __name__ == '__main__':
    con = threading.Condition()
    li = []
    p = Producer(li,con)
    c = Consumer(li,con)
    c1 = Consumer(li,con)
    c2 = Consumer(li,con)
    p.start()
    c.start()
    c1.start()
    c2.start()