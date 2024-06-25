import asyncio
import aiohttp

async def show_status(session,url):
    async with session.get(url) as result: # send request to the url in sessions which comes from main()
        return result.status

async def main():
    async  with aiohttp.ClientSession() as session:
        urls = ['https://www.wikipedia.org/','https://en.wikipedia.org/wiki/[Persian_Gulf']

        rqs = [await show_status(session , url) for url in urls]
        status_codes = await asyncio.gather(*rqs , return_exceptions=True) #run awaitable objects in sequence concurrently | why *args ? : gather dosn't accept list so with *args we send items inside it | return_exceptions : if Ture : it dons't terminate the oprtaion if one of the urls returns rsceptionand it prints the exception
        print(status_codes)

asyncio.run(main())