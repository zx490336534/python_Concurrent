import gevent
from gevent import monkey
monkey.patch_all()
import requests
import time

def get_respose(url):
    html = requests.get(url)
    print(html.status_code)


if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/8hr/page/{}/'
    start = time.time()
    for i in range(1,10):
        get_respose(url.format(i))
    print('单线程：',time.time()-start)

    start = time.time()
    tasks = [gevent.spawn(get_respose,url.format(i)) for i in range(1,10)]
    gevent.joinall(tasks)
    print('协程：',time.time() - start)