### aiohttp

```python
async def request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status in [200, 201]:
                data = wait response.text()
                print("[INFO] complete url: {}".format(url))
            else:
                print("[INFO] failed url: {}".format(url))
```

### aiomysql

```python
async def create_pool(loop):
    pool = await aiomysql.create_pool(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER_NAME,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB_NAME,
        loop=loop,
        charset="utf8",
        autocommit=True
    )
    return pool

async def save(pool, data):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql = "insert into table_name(field_name) value(xxx)"
            await cur.execute(insert_sql)
```

**示例**

```python
# coding = utf-8

import asyncio
import re

import aiohttp
import aiomysql
from pyquery import PyQuery

MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER_NAME = "root"
MYSQL_PASSWORD = "dong10"
MYSQL_DB_NAME = "db_new"

start_url = "http://news.baidu.com/tech"
waiting_list = []
seen_urls = set()
reg = ".*baidu.*"
stop = False


async def fetch(url):
    """利用http协议访问url获取response"""
    print("[INFO] get url: {}".format(url))
    for i in range(3):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status in [200, 201]:
                        print("[INFO] complete url: {}".format(url))
                        data = await response.text()
                        return data
                    print("[INFO] failed url: {}".format(url))
        except Exception as e:
            print("[INFO] error msg: {}".format(e))


def extract_urls(html):
    """解析html中的url"""
    urls = []
    if html is None:
        return
    pq = PyQuery(html)
    for link in pq.items("a"):
        url = link.attr("href")
        if "baidu" not in url and url.startswith("http") and url not in seen_urls:
            urls.append(url)
            waiting_list.append(url)
    return urls


# noinspection SqlNoDataSourceInspection,SqlDialectInspection
async def detail_fetch(url, pool):
    html = await fetch(url)
    if html is None:
        return
    seen_urls.add(url)
    # extract_urls(html)
    pq = PyQuery(html)
    title = pq("title").text()
    title = title[:50] if len(title) > 50 else title
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            insert_sql = "insert into tb_new(title) values('{}')".format(title)
            await cur.execute(insert_sql)


async def get_url(pool):
    future_list = []
    while stop is False:
        print("[INFO] request length is {}".format(len(waiting_list)))
        if len(waiting_list) == 0 and len(seen_urls) > 1:
            break
        elif not waiting_list:
            await asyncio.sleep(0.5)
            continue

        url = waiting_list.pop()
        print("[INFO] get ready: {}".format(url))
        if not re.match(r"{}".format(reg), url):
            if url not in seen_urls:
                future_list.append(asyncio.ensure_future(detail_fetch(url, pool)))
        else:
            if url not in seen_urls:
                future_list.append(asyncio.ensure_future(init_urls(url)))
    for future in future_list:
        await future


# noinspection PyShadowingNames
async def create_pool(loop):
    pool = await aiomysql.create_pool(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER_NAME,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB_NAME,
        loop=loop,
        charset="utf8",
        autocommit=True
    )
    return pool


async def init_urls(url):
    html = await fetch(url)
    extract_urls(html)


# noinspection PyShadowingNames
async def main(loop):
    pool = await create_pool(loop)
    html = await fetch(start_url)
    seen_urls.add(start_url)
    extract_urls(html)
    await loop.create_task(get_url(pool))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(main(loop))
    loop.run_until_complete(task)
```

