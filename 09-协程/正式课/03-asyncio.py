#python 3.5 把@asyncio.coroutine 换成了 async    yield from 换成了await
import asyncio

async def test(i):
    print('test',i)
    await asyncio.sleep(1)
    print('test2',i)

loop = asyncio.get_event_loop()

tasts = [test(i) for i in range(5)]
loop.run_until_complete(asyncio.wait(tasts))
loop.close()