# apply 执行任务函数，主进程会被阻塞 直到函数运行结束
# apply_async 他是非阻塞的，而且有返回结果 并且支持回调
# map 和 python内置的map用法基本一致   (方法,序列) 阻塞主进程 直到返回结果
# close() 关闭进程池
# join() 主进程阻塞等待子进程结束

from multiprocessing import Pool

def add_num(num):
    return num*num

if __name__ == '__main__':
    p = Pool()
    result_list = [] #存放apply_async的返回值
    for i in range(10):
        result_list.append(p.apply_async(add_num,args=(i,)))
    p.close()
    p.join()
    print(result_list)
    for reg in result_list:
        print(reg.get())