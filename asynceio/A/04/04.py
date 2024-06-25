import asyncio

async def one(name):
    await asyncio.sleep(2) #do ...
    print(f'hello {name}')

async def main():
    a = asyncio.create_task(one('amir'))
    b = asyncio.create_task(one('kevid'))


    await a # do a
    await b # do b

loop = asyncio.new_event_loop() #a new event loop is created

try:
    loop.run_until_complete(main()) #the new loop is ran
finally:
    loop.close() # then its closed !!! always close the event loops !!!