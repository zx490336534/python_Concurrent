from multiprocessing import Pool
import time

def add_num(num):
    time.sleep(2)
    print(num*num)

if __name__ == '__main__':
    p = Pool()
    res = []
    p.map(add_num,range(20))
    print('子进程运行结束')
    p.close()
    p.join()