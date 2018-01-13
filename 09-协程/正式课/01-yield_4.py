def f_write():
    tally = 0
    while True:
        nex = yield 5
        if nex is None:
            return tally #StopIteration
        tally += nex

def add_tallist(tall):
    while True:
        tal = yield from f_write()
        tall.append(tal)

tall = []
acc = add_tallist(tall)
next(acc)
for i in range(4):
    print(acc.send(i))

acc.send(None)
print(tall)