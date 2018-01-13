#创建进程的方法
#2.multiprocessing
from multiprocessing import Process
import time
def hello(name):
    print('I am {}'.format(name))
    time.sleep(2)
    print('Hello python')

if __name__ == '__main__':
    #创建一个进程实例
    p = Process(target=hello,args=('子进程',))
    #启动一个进程
    p.start()
    time.sleep(1)
    print('父进程结束了')

#进程里面 父进程会等待子进程运行
