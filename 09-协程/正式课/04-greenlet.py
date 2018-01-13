#IO 很慢 gevent 遇到IO就切换到其他的greelet
#多进程 + 协程
from greenlet import greenlet

def test1():
    print('11')
    gr2.switch()
    print('22')

def test2():
    print('33')
    gr1.switch()
    print('44')


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch() #切换到gr1运行
gr2.switch()
