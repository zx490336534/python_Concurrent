#Manager 实现数据共享，
from multiprocessing import Manager,Process

def run(d):
    d['count'] -= 1

if __name__ == '__main__':

    m = Manager()
    dic = m.dict({'count':100})
    process_list = []
    for i in range(100):
        p = Process(target=run,args=(dic,))
        process_list.append(p)
        p.start()

    for p in process_list:
        p.join()

    print(dic)

