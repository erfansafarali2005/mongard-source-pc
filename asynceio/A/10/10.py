import asyncio


async def do_work(condition):
    async with condition: ### !!! use context manager in order to prevent writing aquire and clear and etc ... (also can prevent multiple releasing)
        print('locked ...')
        await condition.wait()
            # codes below will runs after start signal comming
        print('event happened...')
        await asyncio.sleep(2)
        print('work finished ...')

async def fire_event(condition):
    await asyncio.sleep(5)
    async with condition:
        print('notifying all tasks ...')
        condition.notify_all()  #sends signal to all tasks
        print('notifying finished ...')


async def main():
    condition = asyncio.Condition()
    asyncio.create_task(fire_event(condition))
    await asyncio.gather(do_work(condition) , do_work(condition))