# gevent是协程库
# 核心对象就是协程，围绕着协程听了些可以用的函数

#Web开发框架
#核心对象是URL分发 围绕这个核心功能 提供了一堆的东西

#gevent开发出来是为了解决
'''
socket小程序，那么协程阻塞
就是在解决网络IO，它底层封装了IO多路复用，再外面再实现协程
'''
#gevent 他不需要你改变太多的代码
#可以让现在的很多代码都可以继续用
import gevent
import time

def func1():
    # time.sleep(10) #计算型阻塞
    gevent.sleep(10) #IO阻塞
    print('xx')

def func2():
    print('yy')

coro1 = gevent.spawn(func1)
coro2 = gevent.spawn(func2)

gevent.joinall([coro1,coro2])
#主动切换：我们可以实现比较优秀的切换算法
#类比成多线程