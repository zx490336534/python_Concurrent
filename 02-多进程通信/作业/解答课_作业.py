from multiprocessing import Process,Queue
import random
import time
#1.先写模子
'''
class XXX(Process):
    def __init__(self):
        super().__init__()

    def run(self):
        pass
'''
class Producer(Process):
    def __init__(self,queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(10):
            # if self.queue.full():
            #     continue
            item = random.randint(0,255)
            self.queue.put(item)
            print('生产者生产了{item}'.format(item=item))
            time.sleep(1)



class Consumer(Process):
    def __init__(self,queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for i in range(10):
            time.sleep(1)
            # if self.queue.empty():
            #     # break 如果消费者先消费，那么消费者之间退出（因为empty）
            #     continue
            item = self.queue.get()
            print('消费者消费了{item}'.format(item=item))

if __name__ == '__main__':
    queue = Queue(3)
    producer = Producer(queue)
    consumer = Consumer(queue)
    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
