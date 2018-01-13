# 进程池

# 先把所有的图片地址都找到，放在一个列表里
#串行执行（一个一个执行）
img_list = []
for item in img_list:
    crawal(item) #爬某一个图片

# 并行 同时进行
# 并发 同时发生
# Pool(你有多少个cpu就填多少) 不填默认是cpu个数

import os

print(os.cpu_count())