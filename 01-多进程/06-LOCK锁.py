#LOCK 最简单的锁
#进程之间的数据是不共享的 共享同一个文件系统
#如果多个进程同时对一个文件修改 就会造成数据错乱

i = 0 #1.读取i的值
i = i + 1 #2.对i的值进行加1的操作   3.再把值赋值给i

#对一个数据多次加减一个变量
from multiprocessing import Process
import multiprocessing
blanece = 0

def change_it(n):
    global blanece
    blanece = blanece + n
    print(blanece)
    blanece = blanece - n



lock = multiprocessing.Lock() #创建一把锁

def run_process(n):
    lock.acquire()
    for i in range(1000000):
        change_it(n)
        # # lock.acquire()#获取锁
        # try:
        #     change_it(n)
        # finally:
        #     pass
        #     # lock.release()#释放锁
    lock.release()


if __name__ == '__main__':
    for i in range(100):
        p1 = Process(target=run_process,args=(5,))
        p2 = Process(target=run_process,args=(8,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print(blanece)
