import socket
import time

def block_wat(pn):
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(('www.baidu.com',80))
    except BlockingIOError:
        pass

    request = 'GET {} HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(pn))
    while True:
        try:
            sock.send(request.encode())
            break
        except OSError:
            pass
    response = b''
    while True:
        try:
            chunk = sock.recv(1024)
            while chunk:
                response += chunk
                chunk = sock.recv(1024)
            break
        except OSError:
            pass
    return response

def main():
    for i in range(10):
        block_wat(i)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('end {}'.format(time.time()-start_time))