import asyncio
import aiohttp

async def show_status(session , url):
    async with session.get(url) as result:
        return f'status for {url} is {result.status}'

async def main():
    async with aiohttp.ClientSession() as session :
        requests = [asyncio.create_task(show_status(session , 'https://www.w=kipedia.org/')), #wrong adress to terminate the rest of the code
                    asyncio.create_task(show_status(session , 'https://www.python.org/'))
                    ]
        done , pending = await asyncio.wait(requests , return_when=asyncio.FIRST_EXCEPTION) # done and pending will collect the done and pending tasks
        print(f'Done-> {done}')#                                   asynicio.FIRST_COMPLETED ->after the first task that it runs , it terminates the whole app and put all other tasks to the pending | !!! always you can see only one task in done !!!
        print(f'pending -> {pending}')

        for d in done:
            if d.exception() is None:
                print(d.result()) # prints the completed tasks if there is not any exceptions
            else:
                print('Error ...') # if there is any exception , it prints the error , (next code) :
        for p in pending: # every tasks which dont get excuted now ill be cancelled
            p.cancel()
        print(f'after cancel {pending}')


asyncio.run(main())