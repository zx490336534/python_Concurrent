from multiprocessing import Manager,Process

def prc1(l):
    print(type(l))
    l.append('Tuple')

def prc2(l):
    print(type(l))
    print(l)

if __name__ == '__main__':
    mgr = Manager() #产生了一个公共区域
    l = mgr.list() #在公共区域mgr里面生成一个列表,返回一个用来访问这个列表的东西
    # print(type(l))
    p1 = Process(target=prc1,args=(l,))
    p2 = Process(target=prc2,args=(l,))
    p1.start()
    p1.join()   #父进程等待子进程p1结束才继续
    p2.start() #两个子进程都是由父进程启动
    p2.join()
    print(l)
