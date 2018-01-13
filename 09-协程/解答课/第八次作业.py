def Producer(c):
    c.send(None)
    n = 0
    while n < 10:
        n += 1
        print('生产了%s...'%n)
        r = c.send(n)
        print('消费完了，待生产')
    c.close()
def Consumer():
    while True:
        c = yield
        if not c:
            return
        print('消费了%s...'%c)
c = Consumer()
Producer(c)
