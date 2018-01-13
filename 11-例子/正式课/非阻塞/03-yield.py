import socket
import selectors, time

selector = selectors.DefaultSelector()

Flag = False
pn_list = [i for i in range(10)]


class Future(object):
    def __init__(self):
        self.result = None
        self._callback = None

    def add_done_callback(self, fn):
        self._callback = fn

    def set_result(self, result):
        self.result = result
        if self._callback:
            self._callback(self)


class Fetcher(object):
    def __init__(self, pn):
        self.pn = pn
        self.response = b''

    def fetch(self):
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect(('www.baidu.com', 80))
        except BlockingIOError:
            pass

        f = Future()

        def writeable():
            f.set_result(None)

        selector.register(sock, selectors.EVENT_WRITE, writeable)
        yield f
        selector.unregister(sock)
        request = 'GET {} HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(self.pn))
        sock.send(request.encode())
        global Flag

        while True:
            f = Future()

            def readable():
                data = sock.recv(1024)
                f.set_result(data)

            selector.register(sock, selectors.EVENT_READ, readable)
            chunk = yield f
            selector.unregister(sock)
            if chunk:
                self.response += chunk
            else:
                pn_list.pop()
                if not pn_list:
                    Flag = True


class Task(object):
    def __init__(self, coro):
        self.coro = coro  # 生成器 fetch
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            next_futrue = self.coro.send(future.result)
        except StopIteration:
            pass

        next_futrue.add_done_callback(self.step)


def Event_loop():
    while not Flag:
        events = selector.select()
        for event_key, _ in events:
            callback = event_key.data
            callback()


if __name__ == '__main__':
    start_time = time.time()
    for i in range(10):
        fet = Fetcher(i)
        Task(fet.fetch())
    Event_loop()
    print('end {}'.format(time.time() - start_time))
