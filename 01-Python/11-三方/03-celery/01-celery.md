# 1. 安装

## 1.1 安装

### 1.1.1 celery

最新版本的celery存在与Python默认关键字存在冲突

```python
    from . import async, base
                      ^
SyntaxError: invalid syntax
```

所以需要使用指定版本celery的分支

```python
pip install --upgrade https://github.com/celery/celery/tarball/master
```

### 1.1.2 redis

最新版本redis + celery使用时, 会爆出类型错误

```python
    return x.iteritems()
AttributeError: 'float' object has no attribute 'iteritems'
```

所以也许要指定版本(后期的版本已经修复了此BUG)

```python
pip install redis==2.10.6
```

## 1.2 架构

* deley

  任务添加

* Broker

  任务存储

* worker

  任务执行

# 2 Hello World

## 2.1 celery任务配置

```python
from celery import Celery
    #          任务所在文件名         任务执行结果所在位置                待执行任务所在位置
app = Celery("tasks", backend="redis://localhost:6379/14", broker="redis://localhost:6379/15")
@app.task
def test(x):
    return x + 1
```

## 2.2 开启执行者

```python
celery -A tasks worker --loglevel=info
-A: 指定实例对象位置
--loglevel: 指定日志级别, 可以简写成-l info
```

## 2.3 异步调用

```python
from tasks import app
result = app.delay(7)  # 放入队列中
time.sleep(3)
if result.ready(): # 判断是否执行完毕
    result.get()  # 获取结果
```

# 3. 配置

## 3.1 配置信息

### 3.1.1 储存

```python
broker_url = "redis://127.0.0.1/14"  # 待执行的任务储存
result_backend = "redis://127.0.0.1/15"  # 执行后的结果储存
```



### 3.1.2 root权限运行celery

默认celery是不能以root权限执行的, 否则会报错

```python
Running a worker with superuser privileges when the
worker accepts messages serialized with pickle is a very bad idea!

If you really want to continue then you have to set the C_FORCE_ROOT
environment variable (but please think about this before you do).
```

解决:

* 方法一

  ```python
  from celery import Celery, platforms
  platforms.C_FORCE_ROOT = True  # 开启root执行模式
  ```

* 方法二

  ```python
  # 临时增加linux变量
  export C_FORCE_ROOT = "true"
  # 或者持久化增加到 /etc/profile中
  C_FORCE_ROOT = "true"
  # 或者 使用Python向linux中添加
  os.environ["C_FORCE_ROOT"] = True
  ```

* 方法三

  * 全局禁用

    终极手段, 直接禁用Python断言功能

    ```python
    # 利用Python
    export PYTHONOPTIMIZE=1
    # 或者 利用celery
    celery -O 1 -A celery_tasks worker -l info
    ```

  * 局部禁用

    由于此断言错误是由multiprocessing模块报错导致, 所以直接修改multiprocessing.processing.py中102行, 关闭断言错误即可.



# 4. 参考url

    Django项目配置:
        http://www.cnblogs.com/alex3714/p/6351797.html
    定时:
        https://blog.csdn.net/chenqiuge1984/article/details/80127446
    Python基础配置:
        http://student-lp.iteye.com/blog/2093397
        https://blog.csdn.net/freeking101/article/details/74707619


