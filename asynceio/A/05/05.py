import asyncio
import aiohttp

async def show_status(session,url):
    async with session.get(url) as result: # send request to the url in sessions which comes from main()
        return result.status

async def main():
    async  with aiohttp.ClientSession() as session:
        url = 'https://www.wikipedia.org/'
        status = await show_status(session , url)
        print(f'staits is {status}')

asyncio.run(main())