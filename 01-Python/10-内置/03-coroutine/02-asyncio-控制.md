### 转化Future

#### > wrap_future

将模块`concurrent.futures.Future`对象, 转化为`asyncio.Future`对象.经过此操作就可以执行协程任务了

```python
def wrap_future(future, *, loop=None):
return Future
```

* future: `Future`, 需要转化的未来对象, 创建于模块`concurrent.futures.Future`
* loop: `loop`, 事件监听对象

### 取消协程

#### > shield

等待协程任务的执行, 禁止协程任务的取消操作.

```python
def shield(arg, *, loop=None):
return Future
```

* arg: `coroutine`, 协程函数
* loop: `loop`, 事件监听对象

**示例**

```python
import asyncio


async def test_shield(i):
    await asyncio.sleep(1)
    print(i)
    return i

async def main():
    print("hello")
    try:
        future = asyncio.shield(test_shield(2))
        print(future)
        future1 = asyncio.ensure_future(test_shield(3))
        future.cancel()
        future1.cancel()
        await future
        await future1
    except asyncio.CancelledError as e:
        print(e)
    await asyncio.sleep(3) # 注意这里要设置异步等待 否则协程因无IO切换而直接走向终止
    print("world")

asyncio.run(main())
```

输出

```python
hello
<Future pending>

2
world
```

### 休眠

```python
def sleep(delay, result):
return 
```



