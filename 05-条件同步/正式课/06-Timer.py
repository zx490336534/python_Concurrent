import threading

def hello():
    print('111')

def Welcome():
    print('222')

t1 = threading.Timer(1,hello)
t2 = threading.Timer(3,Welcome) #指定时间执行
t1.start()
t2.start()