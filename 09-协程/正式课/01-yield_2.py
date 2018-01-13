#yield 不会返回值 send发送
def func(max):
    n,a,b = 0,0,1
    while n < max:
        r = yield
        print(r)
        a,b = b,a+b
        n += 1

a = func(5)
a.send(None)
for i in range(5):
    try:
        a.send(i)
    except StopIteration:
        pass

