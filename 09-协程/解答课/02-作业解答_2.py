import random
import time
def consumer(p):
    while True:
        item = next(p)
        print('消费了一个数：%s' % item)
        time.sleep(1)

def producer():
    while True:
        item = random.randint(0,99)
        print('生产了一个数：%s' % item)
        yield item
        time.sleep(1)

p = producer() #生产者生成器
c = consumer(p) #消费者函数
