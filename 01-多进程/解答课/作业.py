#类继承创建进程
from multiprocessing import Process
import multiprocessing
import time
class New_Process(multiprocessing.Process):#类的继承
    def __init__(self):
        super().__init__()
    def run(self):
        n = 50
        while n > 0:
            print('the time is {}'.format(time.time()))
            time.sleep(2)
            n -= 1


if __name__ == '__main__':
    for i in range(5):
        p = New_Process()
        p.start()

#并发 进程数大于cpu数
#并行 cpu个数 大于等于进程数