'''
loop 事件循环
task 对协程的封装
'''

#定义一个协程
print('--------loop---------')
import asyncio

async def some(x): #协程
    print('par:',x)

loop = asyncio.get_event_loop()
loop.run_until_complete(some(2))


print('--------Task---------')
#Task
import asyncio

async def work(x):
    print('par:',x)
    return 'Done'

loop = asyncio.get_event_loop()
task = loop.create_task(work(2))
print(task)
loop.run_until_complete(task)
print(task)


#绑定回调函数
print('--------绑定回调函数---------')
import asyncio
async def work(x):
    print('par:',x)
    return 'Done {}'.format(x)

def callback(futrue):
    print('Callback:',futrue)

loop = asyncio.get_event_loop() #创建事件循环
task = asyncio.ensure_future(work(2)) #创建task对象
task.add_done_callback(callback) #注册回调函数
loop.run_until_complete(task) #启动事件循环


print('--------并发---------')
import asyncio

async def work(x):
    print('xxx:',x)
    await asyncio.sleep(2)
    return 'Done'

tasks = [
    asyncio.ensure_future(work(2)),
    asyncio.ensure_future(work(4)),
    asyncio.ensure_future(work(6))
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print(task)

print('--------嵌套---------')
import asyncio

async def work(x):
    print('xxx:',x)
    await asyncio.sleep(2)
    return 'Done'

async def main():
    tasks = [
        asyncio.ensure_future(work(2)),
        asyncio.ensure_future(work(4)),
        asyncio.ensure_future(work(6))
    ]
    done = await asyncio.wait(tasks)
    print(done)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

