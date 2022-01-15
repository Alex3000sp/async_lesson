import asyncio
import time
from urllib import request
import aiohttp

async def make_request(url, sem):
    # return request.urlopen('https://google.com')
    async with sem:
        async with aiohttp.ClientSession() as sess:
            async with sess.request('GET', 'https://google.com') as req:
                return await req.text()

async def main():
    # await asyncio.gather(
    #     make_request(),
    #     make_request(),
    #     make_request(),
    #     make_request(),
    #     make_request()
    # )
    urls = 15*['']
    sem = asyncio.Semaphore(1)
    await asyncio.gather(
        *[make_request(url, sem) for url in urls]
    )

start = time.time()
asyncio.run(main())
print(time.time() - start)