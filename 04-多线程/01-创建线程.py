#多线程
#GIL python解释器 一个python进程 一次只能运行一个线程
#如果是多个线程 是交替运行的 GIL本质就是互斥锁
#计算密集型 和 IO密集型
#python不适合计算密集型 适合IO密集型

#如何创建线程
# Threading
import threading #多线程模块
import time

def func(name):
    print('I am {}'.format(name))
    time.sleep(2)

t1 = threading.Thread(target=func,args=('爬虫1号',),name='zx')
t1.start()
print(t1.getName()) #获取线程的名字
t1.setName('666') #设置线程的名字
print(t1.getName())