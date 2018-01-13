import threading
import time



class Producer(threading.Thread):
    def run(self):
        while True:
            print('{}准备获取锁'.format(self.name))
            if condition.acquire():
                print('{}获取到了锁'.format(self.name))
                if len(task) >= 500:
                    print('----------资源足够等待消费--------------')
                    condition.wait() #当生产者生产的资源足够多的时候，就等待
                else:
                    for i in range(100):
                        task.append(i)
                    print('{} 添加了100个元素到task，task长度为{}'.format(self.name,len(task)))
                    condition.notify() #唤醒等待的线程
                    condition.release() #释放锁

class Consumer(threading.Thread):
    def run(self):
        while True:
            print('{}准备获取锁'.format(self.name))
            if condition.acquire():
                print('{}获取到了锁'.format(self.name))
                if len(task) < 10:
                    print('资源不足，wait等待！')
                    condition.wait()
                else:
                    for i in range(10):
                        task.pop()
                    print('{} 删除了10个元素，task长度为{}'.format(self.name,len(task)))
                    condition.notify()
                    time.sleep(0.5)
                    condition.release()

task = []
condition = threading.Condition()
if __name__ == '__main__':

    for i in range(3):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()