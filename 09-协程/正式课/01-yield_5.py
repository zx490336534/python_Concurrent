def reader():#写
    for i in range(4):
        yield '>>',i

def wapper(g):
    # for v in g:
    #     yield v
    yield from g

warp = wapper(reader())

for i in warp:
    print(i)