import asyncio



async def one():
    await asyncio.sleep(8)
    print('hello')

async  def main():
    a = asyncio.create_task(one())

    try:
        await asyncio.wait_for(asyncio.shield(a) , timeout=5)  #shield prevents task to be cancelled , it only gives the TimeputError  and pauses the task
    except TimeoutError:
        print("task is taking longer than ususall , but we are working on it ")    # now user choose to cancel the opration or let it go !
        await a   #if we dont await it again , it will be paused for ever



asyncio.run(main())