from multiprocessing import Pool



if __name__ == '__main__':
    pool = Pool()
    pool.apply_async()
    pool.close() #关掉提交任务的通道
    # pool.terminate()#关掉
    pool.join() # 这个join之前必须要执行close/terminate