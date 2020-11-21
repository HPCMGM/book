# 1. 协程池

## 1.1 gevent

三方模块`gevent.pool.Pool`, 创建一个协程池

```python
def __init__(self, size=None, greenlet_class=None):
```

* size: `int`, 开启进程的数量
* greenlet_class: `object`, 协程创建类, 默认读取`Greenlet`

**示例**

```python
import time
from gevent.pool import Pool
from gevent.monkey import patch_all
patch_all()

def test_gevent(a, *, b):
    print(1111)
    time.sleep(1)
    print(2222)
    return a

g_list = []
p = Pool(3)
for i in range(10):
    g = p.apply_async(test_gevent, args=(i,), kwds={"b": 1})
    g.start()
    g_list.append(g)
[g.join() for g in g_list]
for task in g_list:
    print(task.value)
```

