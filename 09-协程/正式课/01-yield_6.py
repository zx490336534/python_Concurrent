def reader():#写
    while True:
        w = yield
        print('>>',w)

def wapper(g):
    yield from g
    # ==
    # g.send(None)
    # while True:
    #     try:
    #         x = yield
    #         g.send(x)
    #     except StopIteration:
    #         pass

w = reader()
wrap = wapper(w)
wrap.send(None)
for i in range(5):
    wrap.send(i)