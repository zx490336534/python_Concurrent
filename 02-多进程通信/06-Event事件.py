# Event 事件
# event 内部有个标志位 默认是False 可以通过set设置为True
# 通过clear() 设置为False

#wait 阻塞当前进程 event内部的标志位为True
from multiprocessing import Process,Event
import time

def wait_for_event(e):
    print('等待event事件')
    e.wait() #阻塞 直到event标志位为True
    print('1.标志位为：', e.is_set())
    print('++++')

def wait_for_event_timeout(e,t):
    print('等待event事件，有超时事件')
    e.wait(timeout=t) #阻塞t秒，然后继续执行
    print('2.标志位为：',e.is_set())

if __name__ == '__main__':
    e = Event()
    p1 = Process(target=wait_for_event,args=(e,))
    p2 = Process(target=wait_for_event_timeout,args=(e,2))
    p1.start()
    p2.start()
    time.sleep(5)
    e.set()
    print('设置event')
