from gevent import monkey
# monkey.patch_all() #猴子补丁 使一些阻塞的模块变得不阻塞 遇到IO自动切换
#手动切换 gevent.sleep(0)

import gevent
import socket
import requests #请求库  connect

def get_ip(n):
    print('start')
    requests.get('https://www.baidu.com')
    gevent.sleep(0)
    print('end')


tasks = [gevent.spawn(get_ip,n) for n in range(5)] #启动协程

gevent.joinall(tasks) #阻塞当前流程
