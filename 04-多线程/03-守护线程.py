import threading
import time

def run(name):
    print('我是{}'.format(name))
    time.sleep(2)
    print('{}结束了'.format(name))

if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=('爬虫1号',))
    t2 = threading.Thread(target=run,args=('爬虫2号',))
    t1.setDaemon(True)
    t1.start()
    t2.start()
    t2.join()
    print('end ')

#在主线程A里面 创建了子线程B，在主线程A里面调用了B.setDaemon,子线程B会随着主线程A结束