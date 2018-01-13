import threading
import time

class My_thread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print('我是{}'.format(self.name))

if __name__ == '__main__':
    t1 = My_thread('zx')
    t1.start()