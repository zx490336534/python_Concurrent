import threading

num = 0

def add_num(n):
    global num
    num += n
    num -= n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            add_num(n)
        finally:
            lock.release()

if __name__ == '__main__':
    lock = threading.Lock()#定义一把锁
    for i in range(1000):
        t1 = threading.Thread(target=run_thread,args=(5,))
        t2 = threading.Thread(target=run_thread,args=(8,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(num)

# 当多个线程修改一个共享数据的时候，我们需要对数据访问进行同步（加锁）
# 加锁部分的代码应该越少越好，因为加锁相当于单线程运行
# lock 互斥锁
