# 1. Coroutine

协程. Python3.4中新加入了协程, 并引入了`async def`和`await`异步关键字.

```python
import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())

```

