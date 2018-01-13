'''
python 协程
1，yield/send
2.(python3.4)@asyncio.coroutine /yield from(python3.3)
3.async/await
'''
#1.gevent 第三方的协程库
#2.asyncio(3.4版本)

import asyncio
@asyncio.coroutine #把一个生成器标记为协程，然后可以把协程丢到事件循环
def hello():#生成器
    print('Welcome to async')
    yield from asyncio.sleep(2)
    print('bye bye')

loop = asyncio.get_event_loop() #事件循环
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks)) #启动协程
loop.close()#结束