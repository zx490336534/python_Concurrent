#LOCK
#多进程 会不会共享全局变量？----不会共享 共享的是文件系统
#加锁部分的代码越少越好

import multiprocessing

def worker_write(lock,file):
    lock.acquire()#如果获取锁的时候没有，会阻塞
    try:
        fs = open(file,'a+')
        n = 1000000
        while n > 0:
            fs.write('a\n')
            n -= 1
        fs.close()
    finally:
        lock.release()

def workers_write(lock,file):
    lock.acquire()
    try:
        fs = open(file,'a+')
        n = 1000000
        while n > 0:
            fs.write('b\n')
            n -= 1
        fs.close()
    finally:
        lock.release()

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    f = 'file.txt'
    p1 = multiprocessing.Process(target=worker_write,args=(lock,f))
    p2 = multiprocessing.Process(target=workers_write,args=(lock,f))
    p1.start()
    p2.start()
    print('父进程end')
    p1.join()
    p2.join()
    print('子进程end')

#队列 queue