#Manager 实现数据共享，
from multiprocessing import Manager,Process,Lock

def run(d,lock):
    lock.acquire()
    d['count'] -= 1
    lock.release()


if __name__ == '__main__':

    m = Manager()
    lock = Lock()
    dic = m.dict({'count':100})
    process_list = []
    for i in range(100):
        p = Process(target=run,args=(dic,lock))
        process_list.append(p)
        p.start()

    for p in process_list:
        p.join()

    print(dic)

