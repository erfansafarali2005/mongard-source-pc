import asyncio


counter = 0


async def increament(lock):
    global counter
    async with lock : # dont put () after lock , its not callable
        temp_counter = counter
        temp_counter += 1
        await asyncio.sleep(1) 
        counter = temp_counter
    



async def main():
    lock = asyncio.Lock()
    global counter
    tasks  = [asyncio.create_task(increament(lock)) for _ in range(10)]
    await asyncio.gather(*tasks)
    print(f'counter is {counter}')    

asyncio.run(main())    
