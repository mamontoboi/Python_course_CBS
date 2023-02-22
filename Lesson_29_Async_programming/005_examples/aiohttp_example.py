import aiohttp
import asyncio


async def get_page(session, url):
    """The function used for extraction the text from url"""
    async with session.get(url) as req:
        print(await req.text())


async def get_all(session, urls):
    """The coroutine, created to make a get_page for list of urls"""
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_page(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)  # results is a future. It awaits for all tasks to complete
    return results


async def main(urls):
    async with aiohttp.ClientSession() as session:
        data = await get_all(session, urls)
        return data

if __name__ == '__main__':
    urls = [
        'https://www.newspapers.com/',
        'https://en.wikipedia.org/wiki/Main_Page',
        'https://en.wikipedia.org/wiki/Paramount_leader'
    ]

    asyncio.run(main(urls))
