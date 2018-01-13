#Event
'''
isSet() 返回标志位的状态
wait 等待
set 设置标志位为True
clear 设置为False
'''
import threading
import random
import time

class Producer(threading.Thread):
    def __init__(self,integers,event):
        super().__init__()
        self.integers = integers
        self.event = event

    def run(self):
        while True:
            integer = random.randint(0,256)
            self.integers.append(integer)
            print('%d appended to list by %s'%(integer,self.name))
            print('event set by %s'%self.name)
            self.event.set() #设置事件
            self.event.clear() #发送事件
            print('event cleared by %s'%self.name)
            time.sleep(1)

class Consumer(threading.Thread):
    def __init__(self,integers,event):
        super().__init__()
        self.integers = integers
        self.event = event

    def run(self):
        while True:
            self.event.wait()
            try:
                integer = self.integers.pop()
                print('%d popped form list by %s'%(integer,self.name))
            except IndexError:
                time.sleep(1)

if __name__ == '__main__':
    result = []
    event = threading.Event()
    p = Producer(result,event)
    c = Consumer(result,event)
    c1 = Consumer(result,event)
    c2 = Consumer(result,event)

    c.start()
    c1.start()
    c2.start()
    p.start()
