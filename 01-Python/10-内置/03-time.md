# 1. 时间

## 1.1 时间转换

### 1.1.1 时间对象

#### > gmtime

将时间戳转化为时间对象, 格林威治时间.

```python
def gmtime(seconds=time.time()):
return struct_time
```

* seconds: `float`, 时间戳

**示例**

```python
import time
from datetime import datetime

print(datetime.now())
print(time.gmtime(time.time()))
```

输出

```python
2020-11-11 22:19:53.142862
time.struct_time(tm_year=2020, tm_mon=11, tm_mday=11, tm_hour=14, tm_min=19, tm_sec=53, tm_wday=2, tm_yday=316, tm_isdst=0)
```

#### > localtime

将时间戳转化为时间对象, 本地时间.

```python
def localtime(seconds=time.time()):
return struct_time
```

* seconds: `float`, 时间戳

**示例**

```python
print(datetime.now())
print(time.localtime(time.time()))
```

输出

```python
2020-11-11 22:19:53.142862
time.struct_time(tm_year=2020, tm_mon=11, tm_mday=11, tm_hour=22, tm_min=19, tm_sec=53, tm_wday=2, tm_yday=316, tm_isdst=0)
```

#### > strptime

将字符串按照指定格式, 转化为时间对象

```python
def strptime(string, format):
return struct_time
```

* string: `str`, 需要转换成时间对象的字符串
* format: `str`, 需要将`string`以哪种占位符格式转换成时间对象,占位符格式参见`datetime`模块

**示例**

```python
import time

date_str = "2020-11-11 22:19:53"
print(time.strptime(date_str, "%Y-%m-%d %H:%M:%S"))
```

输出

```python
time.struct_time(tm_year=2020, tm_mon=11, tm_mday=11, tm_hour=22, tm_min=19, tm_sec=53, tm_wday=2, tm_yday=316, tm_isdst=-1)
```

### 1.1.2 时间戳

#### > time

获取当前时间的时间戳. 此操作会因操作系统时间改变而改变.  精确度: 秒

```python
def time():
return float
```

#### > time_ns

获取当前时间的时间戳. 此操作会因操作系统时间改变而改变.  精确度: 纳秒

```python
def time_ns():
return int
```

#### > mktime

此函数为`localtime`的反函数, 将时间对象转化为时间戳.

```python
def mktime(p_tuple=None): 
return float
```

* p_tuple: `struct_time/9元组`, 时间对象, 或者类似时间对象的9元组. 默认取值`time.localtime()`

**示例**

```python
import time
str_time = "2019-12-20 23:59:59"
time_obj = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
print(time.mktime(time_obj))

time_tuple = (2019, 12, 20, 23, 59, 59, 6, 300, 0)
            # 年, 月, 日, 时, 分, 秒, 星期几, 一年中的第几天, 夏令时
print(time.mktime(time_tuple))
```

输出

```python
1576857599.0
1576857599.0
```

### 1.1.3 格式化输出

#### > asctime

将时间对象转化为字符串, 格式为: `Wed Nov 11 22:34:45 2020`. 区域信息将会被忽略

```python
def asctime(p_tuple=None): 
return str
```

* p_tuple: `struct_time/9元组`, 时间对象, 或者类似时间对象的9元组.默认取值`time.localtime()`

#### > strftime

将时间对象按照某种格式转化为字符串. 格式参见`datetime`模块

```python
def strftime(format, p_tuple=None):
return str
```

* format: `str`, 时间的输出格式, 参见`datetime`模块
* p_tuple: `struct_time/9元组`, 时间对象, 或者类似时间对象的9元组. 默认取值`time.localtime()`

## 1.2 时区

#### - daylight

本地时区, 如果开启夏令时, 则为`0`, 否则`1

#### - altzone

本地时区, 开启夏令时的时区偏移量. (-8 * 60 * 60(东八区) - (夏令时一小时)1 * 60 * 60) , -9小时, 即`-14400`

#### - timezone

本地时区, 未开启夏令时的时区偏移量. (-8 * 60 * 60(东八区) ), -8小时, 即`-10800`

#### - tzname

返回二元组(本地时区非夏令时名称, 夏令时名称) 

# 2. 计数器

## 2.1 时间计数器

#### > monotonic

计数器, 连续调用取差值. 不受系统时间影响, 精确单位: 秒

```python
def monotonic():
return float
```

#### > monotonic_ns

计数器, 连续调用取差值. 不受系统时间影响, 精确单位: 纳秒

```python
def monotonic_ns():
return int
```

#### > perf_counter

计数器, 调用后开始计时, 连续调用取差值. 精确单位: 秒

```python
def perf_counter():
return float
```

#### > perf_counter_ns

计数器, 调用后开始计时, 连续调用取差值. 精确单位: 纳秒

```python
def perf_counter_ns():
return int
```

## 2.2 资源计数器

#### > process_time

获取当前进程占用CPU的时间, 精确单位: 秒

#### > process_time_ns

获取当前进程占用CPU的时间, 精确单位: 纳秒

**示例**

```python
import time
from multiprocessing import Process

def recursive_feb(index):
    if index <= 2:
        return 1
    else:
        return recursive_feb(index - 1) + recursive_feb(index - 2)

def process_use_cpu_time(i):
    start_use = time.process_time()
    start_use_ns = time.process_time_ns()
    recursive_feb(i)
    print(i, time.process_time() - start_use)
    print(i, time.process_time_ns() - start_use_ns)

if __name__ == '__main__':
    p1 = Process(target=process_use_cpu_time, args=(35,))
    p2 = Process(target=process_use_cpu_time, args=(34,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
```

#### > thread_time

获取当前线程占用CPU的时间, 精确单位: 秒

#### > thread_time_ns

获取当前线程占用CPU的时间, 精确单位: 纳秒

# 5. 时间等待

#### > sleep

暂停执行指定时间的调用线程.

```python
def sleep(secs):
return None
```

* secs: `int`, 线程睡眠时长, 单位: 秒

