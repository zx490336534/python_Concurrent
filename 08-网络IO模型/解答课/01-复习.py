# 为什么要学selectors
# 每种操作系统，所支持异步方案是不同的
# windows select python在windows只支持select
    #阻塞，直到东西好了，就继续，并且会告诉你哪些好了
    #我们才能把单线程实现并发（把我们代码的顺序重排一下，避开阻塞的时间）
# linux epoll
    #他的写法和select是不同的，但是基本思想是一样

#学selectors的原因
    #它既可以调用select 也可以调用epoll 它会自动识别操作系统可以使用的方式