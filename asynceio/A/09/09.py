import asyncio
import functools

async def trigger_event(event):
    event.set()

async def do_work_on_event(event):
    print('waiting for event ...')
    await event.wait()
    print('performing works ...')
    await asyncio.sleep(2)
    print('finished work ...')
    event.clear()

async def main():
    event = asyncio.Event()
    asyncio.get_running_loop().call_later(5 , functools.partial(trigger_event , event))
    await  asyncio.gather(do_work_on_event(event) , do_work_on_event(event))

asyncio.run(main())