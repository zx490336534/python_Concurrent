import threading
import queue
import time

class Worker(threading.Thread):
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


def main(tasks):
    work_queue = queue.Queue() #工作队列
    for i in range(3):
        worker = Worker(work_queue,i)
        worker.daemon = True #worker 跟着主线程结束
        worker.start() #是启动一个线程 不是线程池

    for task in tasks:
        work_queue.put(task)

    work_queue.join() #等待队列里面的任务执行完毕

if __name__ == '__main__':
    main('hello python')


'''  
1.创建3个线程
2.把要执行的任务 put到队列
3.再由线程不断的get获取任务 执行
4.当任务执行完毕，程序结束
'''
'''
1.创建一个任务队列
2.创建3个线程
3.把任务put到任务队列
4.run方法 先从队列获取数据 获取到了执行p_print方法
只要get到了 就执行task_done 通知队列完成了一次操作
5.队列join等待 任务执行完毕 也就是等待10次 task_done
'''
#线程在启动之后 就会不断的get
#队列是线程 进程 安全的 不需要自己写lock