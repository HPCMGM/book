# 1. 协程队列

由于协程为单线程推动的, 所以协程队列之间可以不需要进行特殊处理即可通讯, 

* 所以可以直接用`list`代替. 
* 也可以使用`gevent.Queue`

## 1.1 `gevent`

协程队列, 原理使用双端队列`collections.deque`实现.

```python
def __init__(self, maxsize=None, items=(), _warn_depth=2):
return Queue
```

* maxsize: `int`, 队列容纳上限
* items: `tuple`, 队列初始化数据
* _warn_depth: `int`, 如果`maxsize=0`, 是否发出警告, 2以上表示不警告, 以下表示警告

**示例**

```python
import time
import gevent
from gevent.monkey import patch_all
from gevent.queue import Queue
from gevent.pool import Pool
patch_all()


def demo1(q):
    i = 0
    while True:
        q.put(i)
        if i == 20:
            break
        i += 1


def demo2(q):
    while True:
        print(q.get())
        time.sleep(1)
        if q.empty() is True:
            break
    print("over")


if __name__ == "__main__":
    q = Queue(2)
    # g1 = gevent.spawn(demo1, q)
    # g2 = gevent.spawn(demo2, q)
    # g3 = gevent.spawn(demo2, q)
    # g1.start()
    # g2.start()
    # g3.start()
    # g1.join()
    # g2.join()

    """池"""
    pool = Pool(10)
    pool.apply_async(demo1, args=(q,))
    pool.apply_async(demo2, args=(q,))
    pool.apply_async(demo2, args=(q,))
    pool.join()
```

## 1.2 使用list

由于协程是通过单线程实现的, 容器对象(`list`, `dict`, `set`)时全局通用的, 所以可以使用这些容器代替队列进行操作

**示例(list)**

```python
import time
import gevent
from gevent.monkey import patch_all
from gevent.pool import Pool
patch_all()

class Queue(object):
    def __init__(self, size):
        self.data = list()
        self.size = size

    def put(self, data):
        while True:
            if len(self.data) < self.size:
                self.data.append(data)
                break
            time.sleep(0.01)

    def get(self):
        return self.data.pop(0)

    def empty(self):
        return len(self.data) == 0

def demo1(q):
    i = 0
    while True:
        q.put(i)
        if i == 20:
            break
        i += 1


def demo2(q):
    while True:
        print(q.get())
        time.sleep(1)
        if q.empty() is True:
            break
    print("over")


if __name__ == "__main__":
    q = Queue(2)
    g1 = gevent.spawn(demo1, q)
    g2 = gevent.spawn(demo2, q)
    g3 = gevent.spawn(demo2, q)
    g1.start()
    g2.start()
    g3.start()
    g1.join()
    g2.join()

    """池"""
    # pool = Pool(10)
    # pool.apply_async(demo1, args=(q,))
    # pool.apply_async(demo2, args=(q,))
    # pool.apply_async(demo2, args=(q,))
    # pool.join()
```

# 2. 返回对象

前期可参照进程或者线程的`Queue`进行操作, 后期会更新

## 2.1 Queue

### 2.1.1 存取数据

### 2.1.2 状态监测

方法

 

```
from gevent.pool import Pool
from gevent import monkey
monkey.patch_all()
pool = Pool(3)

1. 普通版
tasks = []
for i in range(10):
    task = pool.apply_async(demo, args=(1, 2))
    task.start()
    tasks.append(task)
[task.join() for task in tasks]
for task in tasks:
    print(task.value)

2. 实时获取(形参只能传递一个):
    <1> imap_unorderd:
        params = [(1, i) for i in range(10)]
        tasks = pool.imap_unordered(partial(demo, randint(4, 10)/10), params)
        for task in tasks:
            print(task)
    <2> imap:
        params = [(randint(4, 10) / 10, i) for i in range(10)]
        tasks = pool.imap(partial(demo, 1), params)
        for task in tasks:
            print(task)

3. 获取执行结果:
    <1> 不限制参数:
        params = [(randint(4, 10) / 10, i) for i in range(10)]
        tasks = pool.map(partial(demo, 1), params)
        print(tasks)
    <2> 只能传递一个:
        params = [(randint(4, 10) / 10, i) for i in range(10)]
        tasks = pool.map_async(partial(demo, 1), params)
        print(tasks.get())
```

使用

 

```
import time
from random import randint
from functools import partial
from gevent import pool, monkey

monkey.patch_all()


def demo(a, b):
    print("[INFO] get {}".format("www.baidu.com"))
    time.sleep(a)
    print("[INFO] complete {}".format("www.baidu.com"))
    return a, b


if __name__ == '__main__':
    pool = pool.Pool(3)
    # tasks = []
    # for i in range(10):
    # # func, args=None, kwds=None, callback=None
    # task = pool.apply_async(demo, args=(1, 2))
    # task.start()
    # tasks.append(task)
    # [task.join() for task in tasks]
    # for task in tasks:
    # print(task.value)

    # params = [(1, i) for i in range(10)]
    # tasks = pool.imap_unordered(partial(demo, randint(4, 10)/10), params)
    # for task in tasks:
    # print(task)

    # params = [(randint(4, 10) / 10, i) for i in range(10)]
    # tasks = pool.imap(partial(demo, 1), params)
    # for task in tasks:
    # print(task)

    params = [(randint(4, 10) / 10, i) for i in range(10)]
    tasks = pool.map_async(partial(demo, 1), params)
    for task in tasks.get():
        print(task)

    # params = [(randint(4, 10) / 10, i) for i in range(10)]
    # tasks = pool.map(partial(demo, 1), params)
    # print(tasks)
    print("run over")
```

