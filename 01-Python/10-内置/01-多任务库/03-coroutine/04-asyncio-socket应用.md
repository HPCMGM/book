## 协程专用套接字

#### > open_cocnnection

完成`select`的`register`和`unregister`方法, 遇到IO操作直接返回`future`, 进行`loop`监控, 返回`reader`表示读取操作符, `writer`表示写入操作符. 两个操作符是`File-object`类型, 含有`send`方法.

```python
def open_connection(host=None, port=None, *, loop=None, limit=_DEFAULT_LIMIT, **kwds)
return reader, writer
```

* host: `str`, ip地址
* port: `int`, 端口信息
* loop: `loop`, 事件监听对象
* limit: `int`, 限制两个操作符的buffer大小.
* kwds: `kwargs`, 关键字参数, 向`loop`配置部分关键字参数

**示例**

```python
import asyncio


async def get_url():
    host_ip = ('www.baidu.com', 80)
    reader, writer = await asyncio.open_connection(*host_ip)
    raw_line = []
    writer.write("GET {} HTTP/1.1\r\nHOST:{}\r\nConnection:close\r\n\r\n".format("/", "www.baidu.com").encode())
    async for line in reader:  # 数据按行读取的, 没有分割符
        raw_line.append(line)
    data = b"".join(raw_line)
    return data


async def imap():
    tasks = []
    for _ in range(20):
        tasks.append(loop.create_task(get_url()))
    for task in asyncio.as_completed(tasks):
        # 这样可以实时获取结果
        result = await task  # task是一个coroutine, 需要进行通讯进行StopAsyncIteration异常捕获获取return值
        print(result)


if __name__ == '__main__':
    import time
    start = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(imap())
    loop.run_until_complete(future)
    print("[INFO] running time: {}s".format(time.time() - start))
```

## 1.2 协程锁,协程池

#### Lock

* 限制协程的访问数量, 锁定后只能一个一个去访问(同步)
* 协程是由单线程驱动的, 在执行代码的时候是同步执行的, 无需上锁保证协程安全

支持`with`语法.

```python
def __init__(self):
return lock
```

**使用**

```python
import aiohttp
import asyncio


async def get_url(lk):
    with await lk:
        async with aiohttp.ClientSession() as session:
            print("get!")
            async with session.request("GET", "http://www.baidu.com") as response:
                code = response.status
                print("success!")


lock = asyncio.Lock()
tasks = [get_url(lock) for i in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
```

#### queues.Queue

* 生产者消费者模式, 减少内存开销
* 对数据进行限流操作, 如果不考虑限流的话, 可以用set/list等代替
* 由于进程/线程中的queue的get/put会阻塞, 所以不能用他们的queue

```python
def __init__(self, maxsize=0, *, loop=None):
return queue
```

**示例**

```python
import asyncio

async def put_url():
    for _ in range(100):
        print(_)
        await q.put("a" + str(_))

async def get_url():
    await loop_get()

async def loop_get():
    while True:
        a = await q.get()
        print(a)

q = asyncio.queues.Queue(3)
loop = asyncio.get_event_loop()
tasks = [put_url(), get_url()]
loop.run_until_complete(asyncio.wait(tasks))
```

