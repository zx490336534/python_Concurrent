#进程 和 线程 都是操作系统的概念

#进程是对正在运行的程序的抽象

#创建进程

#并发 -- 伪并行 单个cpu+多道技术
#并行

#阻塞，例如time.sleep()
import time
time.sleep(1)

#非阻塞

#GIL锁 在一个python进程里面一次只能运行一个线程

#多线程
# 1.适合io操作
# 2.不适合计算型。计算型使用多线程会更慢：切换进程消耗时间