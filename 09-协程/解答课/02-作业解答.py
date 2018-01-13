#生产者和消费者
#生产者只管生成，消费者只管消费

#错误的思考方式，我生成的东西怎么让消费者受到 生产者是怎么生成给我的呢

#正确的思考，我是生产者我只管生成，把东西生成到对的地方就行。我是消费者，我只管从对的地方消费

import random
import time
def consumer():
    while True:
        # yield 拿到send进来的东西
        # send 拿到yeild出来的东西
        item = yield
        print('消费了一个数：%s' % item)
        time.sleep(1)

def producer(c):
    c.send(None)
    while True:
        item = random.randint(0,99)
        print('生产了一个数：%s' % item)
        c.send(item)
        time.sleep(1)


c = consumer() #消费者生成器
p = producer(c) #生产者函数
