#把一个文件夹里面的文件全部copy到一个新的文件夹
# 1.获取文件夹所有文件名
import os,time
from multiprocessing import Pool,Manager
def copy_file(filename,old_name,new_name,q):
    with open(old_name+'/'+filename,encoding='utf-8',errors='ignore') as file:
        content = file.read()
        q.put(1)

    with open(new_name+'/'+filename,'w',encoding='utf-8') as f_w:
        f_w.write(content)
def main():
    old_name = input('请输入要复制的文件夹的名字：')
    new_name = input('请输入要copy的文件夹的名字:')
    if not os.path.exists(new_name): #判断exists里面的path存不存在 返回布尔值
        os.mkdir(new_name) #mkdir创建文件夹

    filenames = os.listdir(old_name) #获取当前文件夹中的文件名
    pool = Pool()
    q = Manager().Queue()
    total = len(filenames)
    print('总文件数是：%s' % total)
    for name in filenames:
        pool.apply_async(copy_file,args=(name,old_name,new_name,q))
    # pool.map(copy_file,filenames)
    # pool.close()
    # pool.join()
    num = q.qsize()
    while num < total:
        num1 = q.qsize()
        num = q.qsize()
        if num != num1:
            print('\r当前复制进度%.2f%%,num是%d'%(float((num/total)*100),num))
        if num == total:
            print('复制完成')

if __name__ == '__main__':
    main()




