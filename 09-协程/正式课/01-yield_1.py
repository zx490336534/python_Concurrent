'''
1.迭代
2.可迭代对象
3.迭代器
'''

def func(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n += 1

a = func(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

