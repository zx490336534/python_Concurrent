import threading
import time
import uuid


class My_thread(threading.Thread):
    def __init__(self,n):
        super().__init__()
        self.n = n

    def run(self):
        index = str(self.n).zfill(6)
        filename = r"E:\testfile\a" + index + ".csv"
        writethings = []
        for i in range(8000):
            x = uuid.uuid1()
            x = str(x) + '\n'
            writethings.append(x)
        with open(filename, "a") as f:
            f.writelines(writethings)
        print(self.n)

if __name__ == '__main__':
    starttime = time.time()
    for i in range(100000):
        t1 = My_thread(i)
        t1.start()
    t1.join()
    endtime = time.time()
    usetime = endtime - starttime
    print(usetime)
