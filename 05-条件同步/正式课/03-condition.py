#Condition 对lock对象
'''
acquire()
release()
wait()  #首先会释放当前获取到的锁 进入等待状态
notify() #唤醒一个等待的线程 它不会释放锁 所以它后面会写release()
notifyAll() #唤醒所有等待的线程
'''

import threading
import time

def condition_func():
    ret = 1
    while True:
        if ret > 5:
            con.acquire()
            con.notify() #唤醒进入等待的线程
            print('继续')
            con.release() #释放锁
            time.sleep(2)
            print('222')
        else:
            ret += 1

def run():
    while True:
        con.acquire()
        con.wait() #释放锁 进入等待
        print('run the thread 2')


if __name__ == '__main__':
    con = threading.Condition()
    t = threading.Thread(target=condition_func)
    t1 = threading.Thread(target=run)
    t1.start()
    t.start()