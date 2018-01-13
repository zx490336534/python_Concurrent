#死锁 死锁的出现有两把锁
import threading
import time

class Thread1(threading.Thread):
    def run(self):
        if A.acquire():
            print(self.name+'----A----')
            time.sleep(1)
            if B.acquire():
                print(self.name+'----B----')
                B.release()
            A.release()

class Thread2(threading.Thread):
    def run(self):
        if B.acquire():
            print(self.name+'----B----')
            time.sleep(1)
            if A.acquire():
                print(self.name+'----A----')
                A.release()
            B.release()
#1.两个都执行
# A = threading.Lock()
# B = threading.Lock()

#2.只执行一个
# A = B = threading.Lock()

#3.正常运行
A = B = threading.RLock()

if __name__ == '__main__':
    t1 = Thread1()
    t2 = Thread2()
    t1.start()
    t2.start()
