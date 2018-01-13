from multiprocessing import Queue,Process
import time,random

def production(q):
    for i in range(1,11):
        print('生产了%s件商品'%i)
        q.put(i)
        time.sleep(random.random())

def consumption(q):
    while True:
        if not q.empty():
            j = q.get()
            print('消费了%s件商品'%(j))
            time.sleep(1)
        else:
            break

if __name__ == '__main__':
    q = Queue(100)
    p1 = Process(target=production,args=(q,))
    p2 = Process(target=consumption,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('生产完10件商品并销售完了')

