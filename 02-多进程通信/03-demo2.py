from multiprocessing import Process,Queue

def read():
    print(q.empty()) #字进程的q 是空队列
    print(q.get(timeout=1))

q = Queue()
if __name__ == '__main__':

    reader = Process(target=read)
    q.put(100)
    q.put(101)
    reader.start()
    print(q.get())
    reader.join()
    print(q.get())