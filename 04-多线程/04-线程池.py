#一个线程池包含的部分
#1.线程池管理器  用于启动 管理 线程
#2.工作线程
#3.请求接口
#4.任务队列
#5.结果队列
from multiprocessing.dummy import Pool as ThreadPool #线程池模块
import time

def get(url):
    print('get:{}'.format(url))
    time.sleep(2)

#方法1
# start = time.time()
# for i in range(10):
#     get(i)
# print('运行时间为：{}'.format(time.time()-start))

#方法2
start = time.time()
pool = ThreadPool(10) #默认线程 cpu核数
# print(dir(pool))
pool.map(get,range(10)) #map是阻塞的
print('运行时间为：{}'.format(time.time()-start))
pool.close()
pool.join()
print('运行时间为：{}'.format(time.time()-start))