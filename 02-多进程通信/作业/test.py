import multiprocessing
def func():
    pass

p = multiprocessing.Process(target=func) #新的进程
p.start() #先打开一个新的python，从import导入这个文件