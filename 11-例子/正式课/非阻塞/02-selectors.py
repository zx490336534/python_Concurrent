import socket
import selectors,time

selector = selectors.DefaultSelector()

Flag = False
pn_list = [i for i in range(10)]

class Fetcher(object):
    def __init__(self,pn):
        self.pn = pn
        self.response = b''

    def fetch(self):
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect(('www.baidu.com', 80))
        except BlockingIOError:
            pass
        selector.register(sock, selectors.EVENT_WRITE, self.connect)

    def connect(self,sock):
        selector.unregister(sock)
        request = 'GET {} HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(self.pn))
        sock.send(request.encode())
        selector.register(sock, selectors.EVENT_READ, self.read)

    def read(self,sock):
        global Flag
        chunk = sock.recv(1024)
        if chunk:
            self.response += chunk
        else:
            selector.unregister(sock)
            pn_list.pop()
            if not pn_list:
                Flag = True

def Event_loop():
    while not Flag:
        events = selector.select()
        for event_key,_ in events:
            callback = event_key.data
            callback(event_key.fileobj)

if __name__ == '__main__':
    start_time = time.time()
    for i in range(10):
        fet = Fetcher(i)
        fet.fetch()
    Event_loop()
    print('end {}'.format(time.time() - start_time))