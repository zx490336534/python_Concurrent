from multiprocessing import Process
import os
import time

def aa():
    print('111')
def run(name,age,**kwargs):
    a = Process(target=aa)
    a.start()
    for i in range(10):
        print('子进程运行中，name = {},age = {}, pid = {} ...'.format(name,age,os.getpid()))
        print(kwargs)
        time.sleep(2)

if __name__ == '__main__':
    print('父进程{}'.format(os.getpid()))
    p = Process(target=run,args=('test','23'),name='11',kwargs={'m':2})
    # p.daemon = True #守护进程,1.守护进程中不能创建子进程：a.start()会报错 2.当主进程结束了，守护进程也会结束
    p.start()
    print(p.name)
    print(p.is_alive())
    time.sleep(3)

    p.terminate() #不管任务是否完成 立刻结束
    p.join() # 没用
    print('子进程结束')