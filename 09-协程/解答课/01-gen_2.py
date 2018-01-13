def gen():
    yield  #有什么作用，会暂停当前这个生成器
           #会返回它后面的值
           #接收外面send进来的值

def gen():
    yield 1
    yield 2
    yield 3


g = gen()
print(next(g))
print(next(g))
print(next(g))
