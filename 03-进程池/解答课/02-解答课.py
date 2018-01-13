from multiprocessing import Pool,Process

if __name__ == '__main__':
    pool = Pool(2)

    pool.apply_async()
    #apply_async的等价理解
    p1 = Process()
    p2 = Process()
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    pool.apply()
    #apply的等价理解
    p1.start()
    p1.join()
    p2.start()
    p2.join()


#map 一次性只能传一个参数
#列表推导混合apply_async
