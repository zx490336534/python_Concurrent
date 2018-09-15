import threading
import uuid
import time
from multiprocessing.dummy import Pool as ThreadPool

def write_file(n):
    index = str(n).zfill(6)
    filename = r"E:\testfile\a" + index + ".csv"
    writethings = []
    for i in range(8000):
        x = uuid.uuid1()
        x = str(x) + '\n'
        writethings.append(x)
    with open(filename, "a") as f:
        f.writelines(writethings)
    print(n)


if __name__ == '__main__':
    # write_file(1)
    # n = 0
    # for i in range(100):
    #     n += 1
    #     t = threading.Thread(target=write_file, args=(n,))
    #     print(n)
    #     t.start()
    #     t.join()
    starttime = time.time()
    pool = ThreadPool()
    pool.map(write_file, range(100000))
    pool.close()
    pool.join()
    endtime = time.time()
    usetime = endtime - starttime
    print(usetime)

