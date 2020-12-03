# 2. greenlet

此模块是协程的最初版本, 使用`swith`手动切换执行函数, 特点:

* 多线程中创建出来的每个协程是孤立的, 不能互通, 只能于用本线程创建的协程
* 不能在循环中使用, 官方特意声明的
* 需要手动切换, 每个`switch`只执行自己创建协程时输入的函数

**示例**

```python
import threading
import time
import greenlet

def demo1():
    print("[INFO] get {}".format("www.baidu.com"))
    time.sleep(1)
    print("[INFO] complete {}".format("www.baidu.com"))
    print("demo", threading.current_thread().name)

def demo2():
    print("[INFO] get1 {}".format("www.baidu.com"))
    time.sleep(1)
    print("[INFO] complete1 {}".format("www.baidu.com"))
    print("demo", threading.current_thread().name)

a = []
for i in range(3):
    g = greenlet.greenlet(demo1)
    a.append(g)
    g = greenlet.greenlet(demo2)
    a.append(g)
[g.switch() for g in a]
```

