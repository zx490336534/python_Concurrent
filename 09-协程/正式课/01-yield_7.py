#thow
class SpanException(Exception):
    pass

def write():
    while True:
        try:
            w = yield
        except SpanException:
            print('*****')
        else:
            print('>>',w)

def write_wrapper(g):
    yield from g
    # g.send(None)
    # while True:
    #     try:
    #         try:
    #             x = yield
    #         except Exception as e:
    #             g.throw(e)
    #         else:
    #             g.send(x)
    #     except StopIteration:
    #         pass

w = write()
wrap = write_wrapper(w)
wrap.send(None)
for i in range(5):
    if i == 3:
        wrap.throw(SpanException)
    else:
        wrap.send(i)