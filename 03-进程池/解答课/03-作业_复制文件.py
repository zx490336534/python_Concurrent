#Manager开辟一个公共的空间  #统一用这个
#进程池里面不能用普通的queue
from os import listdir,mkdir
from os.path import isfile,abspath,join,exists
from multiprocessing import Pool

i = 0

def count(orig_files):
    global i
    i = i + 1
    s = len(orig_files)
    print('\r复制进度%2.2f%%' %(i/s*100))

def copy_dir(pool,orig_path,dest_path):
    if not exists(dest_path):
        mkdir(dest_path)
    filename_list = find_filenames(orig_path)
    orig_files = [join(orig_path,filename) for filename in filename_list]
    dest_files = [join(dest_path,filename) for filename in filename_list]

    for args in zip(orig_files,dest_files):
        pool.apply_async(copy_file, args=args,callback=count(orig_files))
        #提交任务,当进程池完成了这个任务会自动去调用这个函数
    pool.close()
    pool.join()


def find_filenames(dir_path):
    return [filename_item for filename_item in listdir(dir_path) if isfile(join(dir_path,filename_item))]

def copy_file(orig_path,dest_path,chunksize=10240): #10KB
    with open(orig_path,'rb') as orig_file, open(dest_path,'wb') as dest_file:
        while True:
            content = orig_file.read(chunksize)
            if not content:
                break
            dest_file.write(content)
            dest_file.flush() #每一次写入，要记得flush

#自顶向下，再自底向上

if __name__ == '__main__':
    pool = Pool()
    orig_path = abspath(input('原始路径：'))
    dest_path = abspath(input('目标路径：'))
    # print(orig_path,dest_path)
    copy_dir(pool,orig_path,dest_path)
