import threading
import queue
import time

class My_ThreadPool(threading.Thread):
    def __init__(self,work_queue,name):
        super().__init__()
        self.work_queue = work_queue
        self.name = name

    def p_print(self,work):
        print('当前线程{},正在执行{}'.format(self.name, work))
        time.sleep(2)

    def run(self):
        while True:
            try:
                work = self.work_queue.get() #从队列获取任务
                self.p_print(work)
            finally:
                self.work_queue.task_done() #通知队列 get的这次任务执行完了


if __name__ == '__main__':
    work_queue = queue.Queue() #工作队列
    for i in range(3):
        worker = My_ThreadPool(work_queue,i)
        worker.daemon = True #worker 跟着主线程结束
        worker.start() #是启动一个线程 不是线程池

    for task in '124124':
        work_queue.put(task)

    work_queue.join() #等待队列里面的任务执行完毕