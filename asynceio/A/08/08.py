import asyncio

counter = 0

async def increament():
    global counter
    temp_counter = counter
    temp_counter += 1
    await asyncio.sleep(1) # while this task is sleeping for 1 second , the other task works on that shared resouce
    counter = temp_counter



async def main():
    global counter
    tasks  = [asyncio.create_task(increament()) for _ in range(100)]
    await asyncio.gather(*tasks)
    print(f'counter is {counter}')    

asyncio.run(main())    



#### two tasks are working on a shared resource , so we heads with race condition problem ###



#### !!!!!!!!!! go to 08.2.py file !!!!!!!!!!! ###