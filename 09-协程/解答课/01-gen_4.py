def gen():
    print((yield '你好'))

g = gen()
print(next(g))
g.send(4)