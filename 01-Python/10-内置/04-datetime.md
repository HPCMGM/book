# 1. 时间

## 1.1 对象

#### > datetime

手动实例化生成时间对象, 包含年月日时分秒

```python
def def __init__(self, year, month, day, hour ,minute, second, microsecond, tzinfo, *, fold):
return datetime
```

* year: `int`, 年
* month: `int`, 月
* day: `int`, 日
* hour: `int`, 时
* minute: `int`, 分
* second: `int`, 秒
* misrosecond: `int`, 毫秒
* tzinfo: `tuple`, 时区以及夏令时操作
* fold: `0/1`,  用于决定是否清除夏令时引起的时间边界问题.

**示例**

```python
In [4]: datetime(2020, 12, 16, 12, 12, 12)                                                        
Out[4]: datetime.datetime(2020, 12, 16, 12, 12, 12)
```

#### > date

手动实例化生成时间对象, 包含年月日

```python
def __init__(self, year, month, day):
return date
```

* year: `int`, 年
* month: `int`, 月
* day: `int`, 日

#### > time

手动实例化生成时间对象, 包含时分秒

```python
def __new__(cls, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
return time
```

#### > datetime.now

自动获取本地当前的时间, 包含年月日时分秒

```python
In [5]: datetime.now()                                                                            
Out[5]: datetime.datetime(2020, 11, 13, 23, 26, 30, 223185)
```

* hour: `int`, 时
* minute: `int`, 分
* second: `int`, 秒
* misrosecond: `int`, 毫秒
* tzinfo: `tuple`, 时区以及夏令时操作
* fold: `0/1`,  用于决定是否清除夏令时引起的时间边界问题.

## 1.2 字符串

#### > datetime.strptime

将字符串, 按照时间占位符转化为时间对象.

```python
@classmethod
def strptime(cls, date_string, format):
return datetime
```

* date_string: `str`, 需要转换的时间格式的字符串
* format: `str`, 时间占位符

**示例**

```python
In [7]: import datetime                                                                           

In [8]: print(datetime.datetime.strptime('2019-02-17 11:12:59', "%Y-%m-%d %H:%M:%S"))             
2019-02-17 11:12:59
```

#### > datetime.strftime

将时间对象, 按照时间占位符转化为字符串.

```python
def strftime(self, fmt):
return str
```

* fmt: `str`, 时间占位符

**示例**

```python
In [80]: datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S").__str__()
Out[80]: '2019-02-17 11:15:42'

In [81]: datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
Out[81]: '2019-02-17 11:16:24'

In [82]: datetime.datetime(2018, 1, 1, 1, 1, 1).strftime("%Y-%m-%d %H:%M:%S")
Out[82]: '2018-01-01 01:01:01'

In [84]: datetime.date(2018, 1, 1).strftime("%Y-%m-%d %H:%M:%S")
Out[84]: '2018-01-01 00:00:00'

In [85]: datetime.time(1, 1, 1).strftime("%Y-%m-%d %H:%M:%S")
Out[85]: '1900-01-01 01:01:01'
```

## 1.3 时间戳

#### > fromtimestamp

将时间戳, 转化为时间对象

```python
@classmethod
def fromtimestamp(cls, t, tz=None):
return datetime
```

* t: `float`, 时间戳, 默认值`time.time()`
* tz: `tuple`, 时区设置

**示例**

```python
In [11]: datetime.datetime.fromtimestamp(time.time())                                             
Out[11]: datetime.datetime(2020, 11, 13, 23, 40, 44, 598331)
```

#### > timestamp

将时间对象, 转化为时间戳

```python
def timestamp(self):
return float
```

**示例**

```python
In [12]: datetime.datetime.now().timestamp()                                                      
Out[12]: 1605282114.888257
```

## 1.4 占位符

| 序号 | 符号 | 含义                                                         |
| ---- | ---- | ------------------------------------------------------------ |
| 1    | `%a` | Locale的缩写工作日名称。                                     |
| 2    | `%A` | Locale的完整工作日名称。                                     |
| 3    | `%b` | Locale的缩写月份名称。                                       |
| 4    | `%B` | Locale的完整月份名称。                                       |
| 5    | `%c` | Locale的适当日期和时间表示。                                 |
| 6    | `%d` | 十进制数[01,31]。                                            |
| 7    | `%H` | 小时（24小时制）作为十进制数[00,23]。                        |
| 8    | `%I` | 小时（12小时制）作为十进制数[01,12]。                        |
| 9    | `%j` | 一年中的一天作为十进制数[001,366]。                          |
| 10   | `%m` | 月份为十进制数[01,12]。                                      |
| 11   | `%M` | 分数为十进制数[00,59]。                                      |
| 12   | `%p` | Locale相当于AM或PM。                                         |
| 13   | `%S` | 其次是十进制数[00,61]。                                      |
| 14   | `%U` | 一年中的周数（星期日作为一周的第一天）作为十进制数[00,53]。在第一个星期日之前的新年中的所有日子都被认为是在第0周。 |
| 15   | `%w` | 工作日作为十进制数[0（星期日），6]。                         |
| 16   | `%W` | 一年中的周数（星期一作为一周的第一天）作为十进制数[00,53]。在第一个星期一之前的新年中的所有日子被认为是在第0周。 |
| 17   | `%x` | Locale的适当日期表示。                                       |
| 18   | `%X` | Locale的适当时间表示。                                       |
| 19   | `%y` | 没有世纪的年份作为十进制数[00,99]。                          |
| 20   | `%Y` | 年份以世纪为十进制数。                                       |
| 21   | `%z` | 时区偏移指示与格式+ HHMM或-HHMM形式的UTC / GMT的正或负时差，其中H表示十进制小时数字，M表示小数分钟数字[-23：59，+ 23：59]。 |
| 22   | `%Z` | 时区名称（如果不存在时区，则不包含字符）。                   |
| 23   | `%%` | 文字`%`字符。                                                |

# 2. 时间运算

## 2.1 时间替换

#### > replace

将指定, 年/月/日/时/分/秒, 进行替换操作

```python
def replace(self, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, tzinfo=True, *, fold=None):
return datetime
```

* year: `int`, 年
* month: `int`, 月
* day: `int`, 日
* hour: `int`, 时
* minute: `int`, 分
* second: `int`, 秒
* misrosecond: `int`, 毫秒
* tzinfo: `tuple`, 时区以及夏令时操作
* fold: `0/1`,  用于决定是否清除夏令时引起的时间边界问题.

**示例**

```python
In [14]: datetime.datetime.now().replace(year=2000)                                               
Out[14]: datetime.datetime(2000, 11, 13, 23, 45, 3, 608482)
```

## 2.2 时间计算

### 2.2.1 时间差

```python
# 时间对象可以运算
In [174]: a = datetime.datetime.now()
     ...: time.sleep(2)
     ...: b = datetime.datetime.now()
     ...: value = abs(b - a)    # 可以取绝对值, 防止产生负数

In [175]: value.days            # 天数
Out[175]: 0

In [176]: value.seconds         # 秒数
Out[176]: 2

In [177]: value.microseconds    # 毫秒
Out[177]: 746
```

### 2.2.2 下个月的这个时间

```python
n [184]: a = datetime.datetime.now()
     ...: one_day = datetime.timedelta(days=1)
     ...: one_second = datetime.timedelta(seconds=4)
     ...: next_day = a + one_day

In [185]: next_day.__str__()
Out[185]: '2019-02-18 12:13:47.192146'

In [186]: (a + one_second).__str__()
Out[186]: '2019-02-17 12:13:51.192146'

In [187]: (a - one_second).__str__()
Out[187]: '2019-02-17 12:13:43.192146'

In [188]: (a - one_second*2).__str__()
Out[188]: '2019-02-17 12:13:39.192146'

In [189]: (a - one_second/2).__str__()
Out[189]: '2019-02-17 12:13:45.192146'
```

