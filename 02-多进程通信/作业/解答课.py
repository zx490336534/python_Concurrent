#Process 类
# 创建进程
#   1.直接实例化Process target参数
#   2.子类Process 重写run方法

# 怎么启动一个新的进程
# start()  先把这个进程启动，然后再去调用这个run
# run() 不能启动进程，普通的方法调用


# 一定要把start() 的调用写在__name__ == __main__
#    有两个文件a.py和b.py
#    a 里面导入了 b
#    python a.py  a.py就是__main__
#    python b.py  b.py就是__main__
#    import b = 将b里面的代码执行了一遍
#    直接运行什么文件，那么那个文件就是__main__
#在windows上，我们start()一个进程的时候
# 1.windows系统会重新打开一个新的python
# 2.接着，python会自己import 父进程的这个文件
'''
    import multiprocessing
    def func():
        pass

    p = multiprocessing.Process(target=func) #新的进程
    p.start() #先打开一个新的python，从import导入这个文件
'''
# 3.如果不放在__main__下面，会无限的创建进程(python不会让它怎么做，所以报错)


#不同的进程，他们之间所有的变量，都是不共用的
#如果的一个进程，我想要让一个函数里的修改，在另一个函数里能看见---使用全局变量
#但是在多进程里面，他们互相看不见

#如果要让进程间可以通信，就需要Queue Manager
#队列先进先出 = 排队
# 队列有两头。一头如(put),一头出(get)
# put方法：往队列里加一个人
# get方法：把现在队列里，最老的一个人，拿出来

#如果我把队列想象成一条隧道，连接山的两边
#Manager新开辟了一个空间，是可以通过Manager产生的对象所访问的
#mgr = multiprocessing.Manager() 生成了一个Manager
#d = mgr.dict() 在mgr这个空间里面，生成了一个字典
#d 是一个用来访问mgr里面字典的一个对象，所以要把这个d传给每一个子进程

#put 当队列满了的时候，阻塞（等待）到队列不为满
#get 当队列为空的时候，阻塞（等待）到队列不为空

#生产者消费者的设计思路：
#不是去设计一个生产者生产以后，消费者怎么消费
#应该是先单独设计两方，然后只考虑
#   消费者只关心队列空还是不空
#   生产者只关心队列满还是不满