import asyncio
import aiohttp

async def show_status(session , url , delay):
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        print(f'status for {url} is {result.status}')

async def main():
    async with aiohttp.ClientSession() as session :
        requests = [ #all of these links will be ran into session.get(url)
            show_status(session , 'https://www.wikipedia.org/' , 3),
            show_status(session, 'https://www.wikipedia.org/wiki/Persian_Language', 9),
            show_status(session, 'https://www.wikipedia.org/wiki/Persian_Gulf', 1),
            show_status(session, 'https://www.wikipedia.org/wiki/Persian_cat', 5)
        ]
        for rqs in asyncio.as_completed(requests):
            await rqs #every item in requests will now be putted in await


asyncio.run(main())