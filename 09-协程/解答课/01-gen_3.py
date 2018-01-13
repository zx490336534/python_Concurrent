def gen():
    print((yield ))
    print('第一个已经收了')
    print((yield ))
    print('第二个已经收了')
    print((yield ))
    print('第三个已经收了')



g = gen()
# g.send(None) == next(g)
g.send(None)
g.send(1)
g.send(2)
g.send(3)