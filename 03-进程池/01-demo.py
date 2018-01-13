from multiprocessing import Pool,cpu_count #进程池
import os
import time
from random import random

def time_task(name):
    print('Run time {} ({})'.format(name,os.getpid()))
    start = time.time()
    time.sleep(random()*3)
    print('Task %s run %0.f seconds...' %(name,(time.time() - start)))


if __name__ == '__main__':
    print('父进程的pid为{}'.format(os.getpid()))
    print('cpu的个数',cpu_count())
    p = Pool() #参数是进程的数量，默认值是cpu的核数
    for i in range(10):
        p.apply_async(time_task,args=(i,))
    p.close()
    p.join()
    print('全部运行结束')

#并发 和 并行