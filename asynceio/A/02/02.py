import asyncio
import datetime

async def one(name):    #async : decleares a function as an asynce objext
    await asyncio.sleep(2) #await : means wait for smt
    print(f'hello  {name}')


async def main():
    a = asyncio.create_task(one('amir')) #asynceio.create_task : it creats a task
    b = asyncio.create_task(one('kevin'))

    await a  ### !! after declearing our functions like one() -> we await them in another fuction and runs this function !! ###
    await b # await a  ,  b -> wait for  a and b to pass response
#   do a , do b -> await
print(datetime.datetime.now())
asyncio.run(main()) # we runs the function which has all of the needed functions not the one()
print(datetime.datetime.now())

### the task appears to be done in 4 seconds but its done in 2 seconds