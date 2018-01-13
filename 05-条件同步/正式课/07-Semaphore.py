#Semaphore 信号量
import threading
import time

def func():
    sm.acquire()
    print(threading.current_thread().getName())
    time.sleep(2)
    sm.release()

if __name__ == '__main__':

    sm = threading.Semaphore()
    for i in range(10):
        t = threading.Thread(target=func)
        t.start()