import socket
import time

def block_wat(pn):
    sock = socket.socket()
    sock.connect(('www.baidu.com',80))
    request = 'GET {} HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(pn))
    sock.send(request.encode())
    response = b''
    chunk = sock.recv(1024)
    while chunk:
        response += chunk
        chunk = sock.recv(1024)
    return response

def main():
    for i in range(10):
        block_wat(i)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('end {}'.format(time.time()-start_time))