import asyncio
from asyncio import CancelledError


async def one():
    await asyncio.sleep(8)
    print('hello')

async  def main():
    a = asyncio.create_task(one())
    secs = 0

    while not a.done():
        print('Task is not finished ...')
        await asyncio.sleep(1)
        secs += 1
        if secs ==5:
            a.cancel()

    try:
        await a
    except CancelledError:
        print('task is cancelled ...')



asyncio.run(main())

