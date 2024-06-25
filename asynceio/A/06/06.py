import asyncio


f = asyncio.Future()

print(f.done())
f.set_result('amir')
print(f.done())
print(f.result())