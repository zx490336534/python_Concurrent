#-*- coding:utf-8 -*-

#创建进程的方法
#1.在Unix/Linux操作系统提供了一个fork()函数，它非常特殊，调用一次，返回两次，因为操作系统将当前的进程（父进程）复制了一份（子进程），然后分别在父进程和子进程内返回。windows不支持fork方法。
import os
pid = os.fork()
if pid == 0:
    print('子进程')
else:
    print('父进程')