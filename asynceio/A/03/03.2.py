import asyncio



async def one():
    await asyncio.sleep(8)
    print('hello')

async  def main():
    a = asyncio.create_task(one())

    try:
        await asyncio.wait_for(a , timeout=5)  #instead of manualyy setting cancelling, this function cancels the opration after the given argument in timeout
    except TimeoutError:
        print('deadline reached , please try again ...')
    print(f'was task cancelled ? {a.cancelled()}')           # func.cancelled() -> returnd True of False depends on the opration



asyncio.run(main())