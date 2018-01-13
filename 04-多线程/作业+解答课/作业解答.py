from multiprocessing.dummy import Pool as ThreadPool
import queue
import time
from multiprocessing import cpu_count
from threading import Thread

#高内聚：相关逻辑，放在一起
#低耦合：无关逻辑，尽量分开

# q = queue.Queue()
# q.get()
# q.put()
# q.task_done()
#可以认为，queue就是一个list
# queue.put list.append()
# queue.get list.pop()

# pool = Pool() 先判断，要生成多少线程，会直接生成这么多线程

class MyThreadPool():
    def __init__(self,threads=None):
        self.queue = queue.Queue()#直接生成一个queue
        if not threads:
            threads = cpu_count()
        for i in range(threads):
            Thread(target=self.do_sth,name='i',daemon=True).start() #当主线程结束时，池会销毁

    def apply_async(self,func):
        self.queue.put(func)

    def join(self):
        self.queue.join() #queue.join()是干嘛的？
        #  队列里面的东西被拿完了（错）
        #  在每次put的时候，会给内部数 +1

    def close(self):
        pass

    def do_sth(self):
        #这个会传到target
        #就是所有线程做的事情
        #这个池里面所有的线程做的事，死循环 get函数 调用函数
        while True:
            try:

                task = self.queue.get() #阻塞(等待)
                task()
            finally:
                self.queue.task_done() #把queue里面的那个内部数-1

if __name__ == '__main__':
    pool = MyThreadPool()
    def func1():
        print('1')
    def func2():
        print('2')
    def func3():
        print('3')
    l = [func1,func2,func3]
    for j in l:
        pool.apply_async(j)
    pool.join()

