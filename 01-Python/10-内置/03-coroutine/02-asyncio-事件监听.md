# 1. 监听对象

低层级函数可被用于获取、设置或创建事件循环

### 1.1.1 监听事件

#### > new_event_loop

创建一个新的事件监听对象.

```python
def new_event_loop():
return Loop
```

#### > get_event_loop

获取当前使用的事件循环对象. 如果不存在, 则会创建一个新的对象.

```python
def get_event_loop():
return Loop
```

#### > set_event_loop

将`loop`设置为当前线程的事件监听对象.

```python
def set_event_loop(loop):
return None
```

#### > get_running_loop

获取当前线程中使用的事件监听对象, 如果没有将会引发异常.

```python
def get_running_loop():
return Loop
```

### 1.1.2 开启事件监听

#### > run_until_complete

监听当前事件循环表中事件, 阻塞直至全部完成.

```python
def run_until_complete(self, future):
return (list(success_task), list(fail_task))
```

* future: `coroutine`, 可监听对象

**示例**

```python
import asyncio


async def test(i):
    await asyncio.sleep(1)
    print(i)
    return i

async def main():
    print("hello")
    try:
        task1 = asyncio.create_task(test(2))
        future2 = asyncio.ensure_future(test(3))
        await future2
        await task1
    except asyncio.CancelledError as e:
        print(e)
    await asyncio.sleep(3)
    print("world")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

#########################
loop.run_forever()                          # 不停止, 一直监听
res = loop.run_until_complete(future/task)
# 事件完成后, 函数内部将Stop=True, 再次调用loop.run_forever(), 程序正常向下执行

# 其结果为元组(成功的, 失败的)
success, failed = res
for task in success:
    # 可以通过迭代获取事件对象
    print(task.result())
```

#### > run

此函数用于管理 `asyncio` 事件循环, 总是会创建一个新的事件循环并在结束时关闭。它应当被用作 `asyncio` 程序的主入口点，理想情况下应当只被调用一次。

```python
def run(coro, *, debug=False):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coro)
return None
```

* coro: `coroutine`, 协程, 一般为协程的入口函数.
* debug: `bool`, 是否开启调试模式.



