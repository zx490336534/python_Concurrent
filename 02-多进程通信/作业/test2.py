from multiprocessing import Process

l = []
print(id(l))
#主进程 打印1次
#子进程 打印2次
def func(l):
    l.append(1)
    print(id(l))

if __name__ == '__main__':
    p = Process(target=func,args=(l,))
    p.start()
    print(l)