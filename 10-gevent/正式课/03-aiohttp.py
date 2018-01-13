import asyncio
import aiohttp #第三方库

async def get_response(url):
    print('请求')
    async with aiohttp.request('GET',url) as r: #请求
        print('开始读取')
        print(await r.text())


url = 'https://www.qiushibaike.com'
loop = asyncio.get_event_loop()
tasks = [get_response(url) for i in range(5)]

loop.run_until_complete(asyncio.wait(tasks))
