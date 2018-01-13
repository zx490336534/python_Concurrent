# yield from

def aa():
    yield from range(1,5)
    yield from range(5)

print(list(aa()))

# yield from == for item in iterable:yield item

