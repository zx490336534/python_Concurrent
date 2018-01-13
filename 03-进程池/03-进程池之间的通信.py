from multiprocessing import Manager,Pool
import os,time,random

def reader(q):
    print('reader启动{},父进程的pid为{}'.format(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        time.sleep(1)
        print('reader从Queue获取到消息{}'.format(q.get()))

def writer(q):
    print('writer启动{},父进程的pid为{}'.format(os.getpid(),os.getppid()))
    for i in 'abcdefg':
        q.put(i)

if __name__ == '__main__':
    p = Pool()
    q = Manager().Queue() #共享队列
    p.apply_async(writer,args=(q,))
    time.sleep(1)
    p.apply_async(reader,args=(q,))
    p.close()
    p.join()
