# 1. gevent

## 1.1 协程创建

由于`greenlet`缺点比较多, 所以后期有人迭代开发了`gevent`, 特点:

* 优化智能切换
* 但是只能识别自己的延时操作`gevent.time()`, 无法识别`time.sleep`

**示例**

```python
import gevent

def demo1(a, b):
    print("[INFO] get {}".format("www.baidu.com"))
    gevent.sleep(1)
    print("[INFO] complete {}".format("www.baidu.com"))
    return a, b

g_list = []
for i in range(10):
    g = gevent.spawn(demo1, 1, 2)
    g.start()
    g_list.append(g)
gevent.iwait(None)
```

### 1.1.2 协程补丁

#### > patch_all

对于网络IO可以开启非阻塞模式, 使用`monkey.patch_all()`(对`socket`设置`setblocking=False`操作) 
注意:

- 所有使用`socket`的包需要在`patch_all()`之前导入
- `gevent`支持其他延迟操作, 除了`input`

**示例**

```python
import time
import gevent
from gevent import monkey

monkey.patch_all()


def test_gevent(a, *, b):
    print(1111)
    time.sleep(1)
    print(2222)


g_list = []
for i in range(10):
    g = gevent.spawn(test_gevent, 1, b=1)
    g.start()
    g_list.append(g)
[g.join() for g in g_list]
```

### 1.1.3 协程等待

#### > join

单个协程等待.

**示例**

```python
import gevent
from gevent import monkey
monkey.patch_all()

g_list = []
for i in range(10):
    g = gevent.spawn(fun1, *args, **kwargs)
    g.start()
    g_list.append(g)
[g.join() for g in g_list]
```

#### > joinall

等待多个协程列表.

**示例**

```python
import time
import gevent
from gevent import monkey

monkey.patch_all()


def demo1(a, b):
    print("[INFO] get {}".format("www.baidu.com"))
    time.sleep(1)
    print("[INFO] complete {}".format("www.baidu.com"))
    return a, b


gevent_list = []
for i in range(10):
    g = gevent.spawn(demo1, 1, 2)
    g.start()
    gevent_list.append(g)
# [g.join() for g in gevent_list]
gevent.iwait(None)
# gevent.wait()
# gevent.joinall(gevent_list)
```

#### > wait

#### > iwait

**示例**

```python
import gevent

def demo1(a, b):
    print("[INFO] get {}".format("www.baidu.com"))
    gevent.sleep(1)
    print("[INFO] complete {}".format("www.baidu.com"))
    return a, b

for i in range(10):
    g = gevent.spawn(demo1, 1, 2)
    g.start()
gevent.iwait(None)

# a =[]
# for i in range(10):
#     g = gevent.spawn(demo1, 1, 2)
#     a.append(g)
# for i in gevent.iwait(a):
#     print(i.get())
```

