

# 1. Coroutine

自从Python3.4以后, Python引入了`asyncio`, 为了将语义更加明确, Python3.5正式引入协程语法`async`与`await`, 作为关键字.

注意事项:

* `async`函数不能出现`yield`/`yield from`
* `async`函数不支持耗时操作
* `async`函数其他关键字: `async for`, `async with`
* `async`函数相关的三方库: `aiohttp`, `aiomysql` ... 等

协程创建三要素:

* 创建异步任务. `create_task/ensure_future/Coroutine(asyc def)`. 异步任务构建
* 将**所有耗时任务**使用`await`进行监听操作. 监听异步事件.

* 使用`asyncio.run`开启事件监听. 函数的入口点

**示例**

```python
import asyncio


async def requests(url, t):
    await asyncio.sleep(t)
    print("wait: {}s".format(t), url)
    return url


async def main():
    print("hello")
    task1 = asyncio.create_task(requests("http://www.baidu.com22", 2))
    task2 = asyncio.create_task(requests("http://www.baidu.com11", 1))
    await task1
    await task2
    print("world")


asyncio.run(main())
```

输出

```python
hello
wait: 1s http://www.baidu.com11
wait: 2s http://www.baidu.com22
world
```

## 1.1 await

关键字`await`主要用于异步等待此函数的执行, 并在适当的时候回调回来继续执行. 可接受类型:

1. 协程
   * `async def`创建的协程
   * `asyncio.coroutine`装饰转化为的协程
2. task
   * `asyncio.create_task`创建的`task`对象
3. future
   * `asyncio.ensure_future`创建的对象

**示例**

```python
async def async_func(url):
    """协程"""
    return url

@asyncio.coroutine
def trans_async_func_for_asyncio(url):
    """使用asyncio转化的协程"""
    return url

async def test_task_obj(url):
    """测试task对象"""
    await asyncio.sleep(2)
    return url

async def test_future_obj(url):
    """测试futur对象"""
    await asyncio.sleep(2)
    return url

async def main():
    print("hello")
    print(await async_func("http://www.baidu.com1"))
    print(await trans_async_func_for_asyncio("http://www.baidu.com2"))
    task = asyncio.create_task(test_task_obj("http://www.baidu.com3"))  # 注意这个中转变量不能省略
    future = asyncio.ensure_future(test_future_obj("http://www.baidu.com4"))
    print(await task)
    print(await future)
    print("world")
asyncio.run(main())
```

### 1.1.1 协程对象

#### 关键字创建

```python
async def requests(url, t):
    print("wait: {}s".format(t), url)
    return url
```

#### > coroutine

使用`coroutine`装饰创建

```python
@asyncio.coroutine
def trans_async_func_for_asyncio(url):
    """使用asyncio转化的协程"""
    return url
```

### 1.1.2 task

#### > create_task

将协程任务加入监听序列中, 当任务被执行完成后回调挂起位置继续向下执行, 而不是阻塞等待任务执行完成. 

```python
def create_task(coro, *, name=None):
return Task
```

* coro: `coroutine`, 协程对象.
* name: `str`, 用来指定`task`的名称

**示例**

```python
import asyncio


async def requests(url, t):
    await asyncio.sleep(t)
    print("wait: {}s".format(t), url)
    return url


async def main():
    task1 = asyncio.create_task(requests("http://www.baidu.com22", 2))
    task2 = asyncio.create_task(requests("http://www.baidu.com11", 1))
    await task1
    await task2

asyncio.run(main())
```

输出

```python
wait: 1s http://www.baidu.com11
wait: 2s http://www.baidu.com22
```

### 1.1.3 future

#### > ensure_future

相对于`create_task`来说, 此函数更为底层. 功能同样是连接底层回调式代码, 将协程任务加入监听序列中.

```python
def ensure_future(obj, *, loop=None):
return Future
```

* obj: `Future/Task/coroutine`, 需要异步执行的任务对象. 可以为含`_asyncio_future_blocking`属性的对象或者`Future/Task/coroutine`
* loop: `loop`, 事件监听对象.

**示例**

```python
import asyncio


async def requests(url, t):
    await asyncio.sleep(t)
    print("wait: {}s".format(t), url)
    return url


async def main():
    future1 = asyncio.ensure_future(requests("http://www.baidu.com22", 2))
    future2 = asyncio.ensure_future(requests("http://www.baidu.com11", 1))
    await asyncio.wait([future1, future2])

asyncio.run(main())
```

输出

```python
wait: 1s http://www.baidu.com11
wait: 2s http://www.baidu.com22
```

## 1.2 loop

低层级函数可被用于获取、设置或创建事件循环

### 1.2.1 监听事件

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

### 1.2.2 开启事件监听

#### > run

此函数用于管理 asyncio 事件循环, 总是会创建一个新的事件循环并在结束时关闭之。它应当被用作 `asyncio` 程序的主入口点，理想情况下应当只被调用一次。

```python
def run(coro, *, debug=False):
return None
```

* coro: `coroutine`, 协程, 一般为协程的入口函数.
* debug: `bool`, 是否开启调试模式.

#### > run_until_complete



# 2. 返回值

## 2.1 < Task

类似`future`对象, 用来控制协程的一些操作方式的对象. 非线程安全.  一个事件运行时 
事件循环使用协同日程调度: 一个事件循环每次运行一个 Task 对象。而一个 Task 对象会等待一个 Future 对象完成，该事件循环会运行其他 Task、回调或执行 IO 操作。

**此对象由系统自动构建无需手动操作**.

### 2.1.1 取消任务

#### > cancel

取消协程任务. 成功取消返回`True`否则`False`

```python
def cancel(self):
return bool
```

#### > cancelled

判断, 协程任务是否被取消

```python
def cancelled(self):
return None
```

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
        task = asyncio.create_task(test_shield(2))
        task.cancel()
        await task
    except asyncio.CancelledError as e:
        print(e)
    print(task.cancelled())
    await asyncio.sleep(3) # 注意这里要设置异步等待 否则协程因无IO切换而直接走向终止
    print("world")

asyncio.run(main())
```

输出

```python
hello

True
world
```

### 2.1.2 获取结果

#### > result

获取任务的执行结果. 如果非正常执行完成, 则会抛出异常

```python
def result(self):
return result
```

#### > done

判断, 协程任务是否已经执行完成

#### > exception

获取任务执行中内部存在的异常, 如果`cancel`后, 调用此函数会抛出异常

```python
def exception(self):
return None/objectError
```

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
        task = asyncio.create_task(test(3))
        await task
        print(task.exception())
        print(task.done())
        print(task.result())
    except asyncio.CancelledError as e:
        print(e)
    await asyncio.sleep(3)
    print("world")

asyncio.run(main())
```

输出

```python
hello
3
None
True
3
world
```

### 2.1.3 回调函数

#### > add_done_callback

当`task`执行完成后, 将`task`执行完成后, 会将`task`对象重新交给此函数继续执行, 可以添加多个函数.

```python
def add_done_callback(fn):
return None
```

* fn: `function`: 需要添加的回调函数

#### > remove_done_callback

移除`task`被添加的回调函数. 并返回被移除的回调函数数量, 通常这个值为1, 除非你使用`add_done_callback`增加了多个回调函数

```python
def remove_done_callback(fn):
return int
```

* fn: `funtion`: 需要移除的回调函数, 可以执行多次, 但是如果该函数不存在, 或者已经移除, 返回值的数量也会增加, 但是没有任何实际意义.

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
        task = asyncio.create_task(test(3))
        fn = lambda x: print(3333333, x)
        task.add_done_callback(lambda x: print(1111111, x.result()))
        task.add_done_callback(lambda x: print(2222222, x))
        task.add_done_callback(fn)
        task.add_done_callback(fn)
        task.add_done_callback(fn)
        print("remove function count: ", task.remove_done_callback(fn))
        await task
    except asyncio.CancelledError as e:
        print(e)
    await asyncio.sleep(3)
    print("world")

asyncio.run(main())
```

输出

```python
hello
remove function count:  3
3
1111111 3
2222222 <Task finished coro=<test() done, defined at E:/project/test/t_builtins/test1.py:9> result=3>
world
```

### 2.1.4 栈对象

#### > get_stack

获取栈对象列表

```python
def get_stack(limit=None):
return list
```

* limit: `int`, 栈对象中的行数限制.

#### > print_stack

打印栈对象异常时的信息.

```python
def print_stack(limit=None, file=None):
return None
```

* limit: `int`, 栈对象中的行数限制
* file: `file-object`, 需要将信息输出在哪种流对象中. 类似`traceback`

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
        task = asyncio.create_task(test(3))
        print(task.get_stack())
        task.print_stack()
        await task
    except asyncio.CancelledError as e:
        print(e)
    await asyncio.sleep(3)
    print("world")

asyncio.run(main())
```

输出

```python
hello
[<frame at 0x0000013523CC41F0, file 'E:/project/test/t_builtins/test1.py', line 9, code test>]
Stack for <Task pending coro=<test() running at E:/project/test/t_builtins/test1.py:9>> (most recent call last):
	File "E:/project/test/t_builtins/test1.py", line 9, in test
		async def test(i):
3
world
```

### 2.1.5 任务信息

#### > get_coro

获取由`task`包装后的协程对象. 

```python
def get_coro(self):
return coroutine
```

#### > get_name

获取`task`的名称. `asyncio Task `实现会在实例化期间生成一个默认名称。

```python
def get_name(self):
return str
```

#### > set_name

设置`task`名称

```python
def set_name(value):
return None
```

* value: `any`, 可以为任意对象，它随后会被转换为字符串。

## 2.2 < Future

`Future`代表一个底层的可等待对象, 线程不安全. `Future`类似模块`concurrent.futures.Furure`, 主要区别为`asyncio.Future`可以直接用于协程操作, 而后者需要使用转换才能进行操作

**此对象, 拥有`Task`对象的属性和方法, 这里就不再赘述.**



