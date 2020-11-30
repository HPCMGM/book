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

### 加入多个协程任务

#### > gather

将多个可等待对象(协程对象, `Task`, `Future`)加入到事件监听序列中, 此函数可重复执行. 如果`gather`被取消, 则会将所有本次提交的任务全部取消.

```python
def gather(*aws, loop=None, return_exceptions=False):
return 
```

* aws: `coroutine/Task/Future`, 需要加入监听序列的操作对象
* loop: `loop`,  事件监听对象
* return_exception: `bool`, `False`表示如果执行时当前提交序列出现一个异常, 将当前提交的全部序列清空, 并返回引发的异常信息(不是抛出异常), `True`表示等待当前序列执行完成, 并返回结果和异常结果. 

**示例**

```python
import asyncio

async def test_task_obj(url):
    """测试task对象"""
    await asyncio.sleep(2)
    if url.endswith("1"):
        raise TypeError("1234566")
    return url

async def main():
    print("hello")
    gather1 = asyncio.gather(test_task_obj("http://www.baidu.com1"), test_task_obj("http://www.baidu.com2"), return_exceptions=True)
    gather2 = asyncio.gather(test_task_obj("http://www.baidu.com1"), test_task_obj("http://www.baidu.com2"), return_exceptions=False)
    gather3 = asyncio.gather(gather1, gather2, return_exceptions=True)
    res = await gather3
    print("world")
    print("gather1 result: {}".format(str(res[0])))
    print("gather2 result: {}".format(repr(res[-1])))

asyncio.run(main())
```

输出

```python
hello
world
gather1 result: [TypeError('1234566'), 'http://www.baidu.com2']
gather2 result: TypeError('1234566')
```



### 等待协程的执行完成

#### > wait

批量执行协程对象, 并等待协程的执行完成. `done`/`pending`均为`list`类型.分别表示执行完成的结果集和执行失败的结果集

```python
def wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)
return (done, pending)
```

* aws: `list`, 需要加入监听序列的操作对象列表(`task`/`future`), `coroutine`方式将被废弃
* loop: `loop`,  事件监听对象
* timeout: `int/float`, 需要等待的最长时间
* return_when: `int`, 等待何时返回结果. 常数有如下
  * FIRST_COMPLETED: 当任意一个协程执行完成或者取消时.
  * FIRST_EXCEPTION: 当任意一个协程引发异常, 如果没有异常, 相当于`ALL_COMPLETED`
  * ALL_COMPLETED: 当全部执行完成, 或者取消时

#### > wait_for

等待可等待对象的执行完成, 与`wait` 不同之处在于:

* 如果协程在规定时间内没有执行完成, 则会引发`asyncio.TimoutError`异常, 如果被取消了也会发生异常.
* 只能接受一个协程对象

```python
def wait_for(aw, timeout, *, loop=None):
return result
```

* aw: `task`/`future`, 需要加入监听序列的操作对象
* loop: `loop`,  事件监听对象
* timeout: `int/float`, 需要等待的最长时间

**示例**

```python
import asyncio

async def test_wait(i):
    await asyncio.sleep(i)
    return i

async def main():
    print("hello")
    task = asyncio.create_task(test_wait(2))
    task1 = asyncio.create_task(test_wait(1))
    wait_obj1 = asyncio.wait([task, task1], timeout=3)
    done_task1, pending_future1 = await wait_obj1
    if task in done_task1:
        print(task.result())
    print("******************************")
    task = asyncio.create_task(test_wait(2))  # 如果超时, 则会引发异常
    res = await asyncio.wait_for(task, timeout=3)
    print(res)
    print("world")

asyncio.run(main())
```

输出

```python
hello
2
******************************
2
world
```

### 获取协程结果

#### > as_completed

实时返回协程结果, 需要用`await`接受结果. 如果在所有`future`完成前任务中出现了超时, 则会引发`asyncio.TimeoutError`异常

````python
def as_completed(fs, *, loop=None, timeout=None):
return result_list
````

**示例**

```python
import asyncio

async def test_as_completed(i):
    await asyncio.sleep(1)
    return i

async def main():
    for task in asyncio.as_completed([asyncio.create_task(test_as_completed(i)) for i in range(3)]):
        res = await task
        print(res)

if __name__ == '__main__':
    asyncio.run(main())
```

输出

```python
0
1
2
```

### 线程间调用

#### > run_coroutine_threadsafe

指定向特定的事件监听`loop`中提交一个协程, 此操作为线程安全的.

```python
def run_coroutine_threadsafe(coro, loop):
return future
```

* coro: `coroutine`, 协程函数
* loop: `loop`, 时间监听对象

**示例**

```python
import asyncio
import threading

async def create_task(loop):
    future = asyncio.run_coroutine_threadsafe(production(1), loop)
    try:
        result = future.result(3)
    except asyncio.TimeoutError:
        print('The coroutine took too long, cancelling the task...')
        future.cancel()
    except Exception as exc:
        print(f'The coroutine raised an exception: {exc!r}')
    else:
        print(f'The coroutine returned: {result!r}')
    await asyncio.sleep(1)

async def production(i):
    print("{}第{}个coroutine任务".format(threading.current_thread(), i))
    await asyncio.sleep(1)
    return i

son_loop = asyncio.new_event_loop()
# 让线程3秒后终止
run_loop_thread = threading.Thread(target=son_loop.run_until_complete, args=(asyncio.wait([asyncio.sleep(2)]), ))
run_loop_thread.start()

asyncio.run(create_task(son_loop)) # 向其他事件循环loop中, 插入协程
asyncio.run(production(2)) # 当前事件中执行该函数
```

输出

```python
<Thread(Thread-1, started 31340)>第1个coroutine任务
The coroutine returned: 1
<_MainThread(MainThread, started 24144)>第2个coroutine任务
```



### 获取当前任务信息

#### > current_task

获取当前运行协程的`task`对象. 如果没有`task`任务, 则会返回`None`.

```python
def current_task(loop=None):
return task/None
```

* loop: `loop`, 事件监听对象.

**示例**

```python

```

输出

```python

```

#### > all_task

获取当前事件监听对象中的全部任务

```python
def all_task(loop=None):
return list
```

* loop: `loop`, 事件监听对象.

**示例**

```python

```

输出

```python

```

#### > isfuture

判断, `obj`是否为`Future`, `Task`或者携带`_asyncio_future_blocking`属性的对象.

```python
def isfuture(obj):
return bool
```

* obj: `coroutine`, 协程对象.

