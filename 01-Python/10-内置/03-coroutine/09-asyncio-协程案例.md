# 1. 官方实例

```python
import asyncio


async def compute(x, y):
    print("The params is [{}, {}]".format(x, y))
    await asyncio.sleep(1)
    print("The compute is success")
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print("{} + {} = {}".format(x, y, result))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(print_sum(1, 2))
    loop.run_until_complete(future)
    loop.close()
```

调用IO示例图

![image-20201208085008279](image/05-asyncio-%E5%8D%8F%E7%A8%8B%E6%A1%88%E4%BE%8B/image-20201208085008279.png)

# 2. IO使用

## 2.1 爬取百度

```python
import asyncio
import aiohttp

async def request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            status = response.status
            # 如果获取内容则需要await
            # text = await response.text()
            return status

async def send_url(url):
    print("start url: {}".format(url))
    code = await request(url)
    print("success url: {}".format(code))
    return "function back value"

if __name__ == '__main__':
    t1 = time.time()
    loop = asyncio.get_event_loop()
    tasks = [send_url("http://www.baidu.com") for _ in range(100)]
    future = asyncio.wait(tasks)
    res = loop.run_until_complete(future)
    for task in res[0]:
        print(task.result())
    loop.close()
    t2 = time.time()
    print(t2 - t1)
```

