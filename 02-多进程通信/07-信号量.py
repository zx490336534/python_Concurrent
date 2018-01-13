#信号量 维护了一个计数器 每创建一个进程获取计数器 计数器就会减一

from multiprocessing import Process,Semaphore
import time

def func(sem,num):
    sem.acquire()
    print('{} get semaphores '.format(num))
    time.sleep(3)
    sem.release()

if __name__ == '__main__':
    sem = Semaphore(3)
    for i in range(1,11):
        t = Process(target=func,args=(sem,i))
        t.start()
