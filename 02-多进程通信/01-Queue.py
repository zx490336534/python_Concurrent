#进程间的通信 共享

#两个进程有关系吗

#队列Queue 先进先出

from multiprocessing import Queue

q = Queue(3) #初始化一个Queue对象，(3)最多接收3条信息.(-1)无限接收视内存而定

# q.put() #添加数据 q.put_nowait()
# q.get() #获取 q.get_nowait() block默认为True 如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常；
# q.qsize() #获取队列长度
# q.empty() #判断队列是否为空 空为True 非空为False
# q.full() #判断队列是否满了 满为True 不满为False

q.put(1)
q.put(2)
q.put(3)
# q.put_nowait(1) #队列满了立即会报错
# q.put(1,timeout=2) #timeout时间之后报错
print(q.get())

print('-'*3)
print('队列长度：',q.qsize())
print('-'*3)
print(q.full())
print('-'*3)
print(q.empty())
