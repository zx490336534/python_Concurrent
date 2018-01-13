import gevent
import time
from gevent.queue import Queue
import random


queue = Queue(3)

def producer(name):
    while True:
        item = random.randint(0,99)
        print('生产者:',name,item)
        queue.put(item) #队列满，阻塞->切换

def consumer(name):
    while True:
        print(name,'尝试拿')
        item = queue.get() #队列空，阻塞->切换
        print('消费者',name,item)

coro1 = gevent.spawn(producer,'p')
coro2 = gevent.spawn(consumer,'c1')
coro3 = gevent.spawn(consumer,'c2')
coro4 = gevent.spawn(consumer,'c3')

gevent.joinall([coro1,coro2,coro3,coro4])