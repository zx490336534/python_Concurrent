import multiprocessing
import time

class MyProcess(multiprocessing.Process):
    def __init__(self,name):
        super().__init__()
        self.name = name

    #重构父类的run方法
    def run(self):
        print('I am {}'.format(self.name))
        time.sleep(2)
        print('Welcome to python')

if __name__ == '__main__':
    p = MyProcess('zhongxin')
    p.start()
    print('父进程结束啦')

#在windows使用start方法，必须在if判断(if __name__ == '__main__':)下面