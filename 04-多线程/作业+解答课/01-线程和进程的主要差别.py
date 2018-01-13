#线程和进程的主要差别
# 1.进程是很久以前的计算机模型，他是当时最小的执行单元
# 2.线程是后来设计的计算机模型，他是现在最小的执行单元
# 3.执行单元就是可以分配CPU的单元
# 4.线程是在一个进程里面的
# 5.多个线程由于在一个进程里面，因此，他们可以互相看到对方的全局变量

# 主线程 和子线程
# 1.主线程可以用来类比父进程
# 2.子线程可以用来类比子进程

from threading import Thread

t = Thread()
print(t.getName()) #python已经发展了很多年，驼峰命名
print(t.name)

def func(x):
    print(x)

l = [1,2,3,4]
print(list(range(10)))
list(map(func,l)) #python3里面，map会得到一个生成器 和range类似
print('--------------')
m = map(func,l)
next(m)
next(m)
next(m)
next(m)
