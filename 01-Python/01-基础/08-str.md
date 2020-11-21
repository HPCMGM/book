# 1. 字符串

## 1.1 特点

编程语言的文本特性, 可以拼接, 用于数据展示,在Python中字符串为不可变类型, 一经创建不可修改

## 1.2 定义

Python中单引号、双引号和三引号没有严格的区分, 但是要成对存在, 不能交叉存在

```bash
"你好", '世界'
"""
啊啊啊啊啊啊啊啊啊啊
aaaaaaaa
"""
```

# 2. 常见操作

## 2.1 查询

### 2.1.1 切片

切片操作主要用处有两种: 

**单个取值**

```Python
string[index]
return str
```

* index: 索引

**范围取值**

```Python
string[start:end:sep]
return str
```

* start: `int`,起始索引. 可选参数
* end: `int`,终止索引. 可选参数
* sep: `int`,步长. 可选参数

特殊说明:

```bash
string[:] # 表示将string进行浅copy
```

示例

```bash
In [1]: str1 = "askjflsjfadfp"

In [2]: str1[0]
Out[2]: 'a'

In [3]: str1[1:]
Out[3]: 'skjflsjfadfp'

In [4]: str1[:-1]
Out[4]: 'askjflsjfadf'

In [5]: str1[::2]
In [5]: 'akfsfdp'

In [6]: str1[2::-2]
In [6]: 'ka'

In [7]: str1[2::2]
In [7]: 'kfsfdp'
```

### 2.1.2  索引查找

#### > index

从左边查询sub字符串所在的位置, 如果sub不存在则报错

```Python
def index(self, sub, start, end):
return int
```

* sub:  `str`, 需要查找的字符串
* start: `int`, 查找的起始位置
* end: `int`,查找的终止位置

示例

```bash
In [5]: a_str = "absad"

In [6]: a_str.index("a")
Out[6]: 0
```

#### > rindex

同`index`, 不同之处在于, 从右边开始查找

#### > find

同`index`, 不同之处在于, 如果没有查找到返回空, 而不会抛出异常.

#### > rfind

同`rindex`, 不同之处在于, 如果没有查找到返回空, 而不会抛出异常.

### 2.1.3 统计

#### > count

统计某个元素出现的个数

```Python
def count(x, start, end):
return int
```

* x: `str`, 需要统计的字符串
* start: `int`, 统计起始位置
* end: `int`,统计结束位置

示例

```bash
>>> a_str = "abcd, abcd, abcd"
>>> a_str.count("a", 2, -1)
2
```

## 2.2 修改

**注意**: 这里的增加不是在原有的基础上进行增加, 而是返回一个组合好的新字符串.

### 2.2.1 字符串拼接

#### > 符号拼接

使用`+`进行字符串拼接

```bash
>>> a = "hello"
>>> b = "word"
>>> a + " " + b
'hello word'
```

#### > join

将可迭代对象以某种方式进行拼接在一起

```python
def join(self, iterable):
return str
```

* iterable: `iterable`, 可迭代对象, 内部元素必须是`str`类型, 否则会抛出异常`TypeError`.

示例

```python
>>> ",".join(["1", "2", "3"])
'1,2,3'
```

### 2.2.2 切分

#### > split

从左查找, 以`sep`为分隔符, 不保留分隔符进行分割.

```Python
def split(self, maxsplit=None):
return list
```

* `maxsplit`:  `int`, 最大分割数量, 默认为全部.

示例

```python
In [9]: a_str = "abcdaefdaff"

In [10]: a_str.split("a")
Out[10]: ['', 'bcd', 'efd', 'ff']
```



#### > rsplit

同`split`, 不同之处在于, 从右开始分割

#### > partition

同`split`, 不同之处在于, 保留分隔符号且只分割一个, 返回一个**三元组**(前一部分, 切割符号, 后一部分)

#### > rpartition

同`partition`, 不同之处在于, 从右开始分割

#### > splitlines

以字符串标识符`\r\n`, `\n`开始分割

```python
def splitlines(keepends=False):
return list
```

* `keepends`: `bool`, 是否保留分割符号.

示例

```python
>>> a_str = "a\rb\tc\nd"
>>> a_str.splitlines()
['a', 'b\tc', 'd']
```



### 2.2.3 替换

#### > replace

将指定`str`替换成另一个`str`

```python
def replace(old, new, count=None):
return str
```

* `old`: `str`, 待替换的原字符串
* `new`: `str`, 替换字符串
* `count`: `int`, 替换次数

示例

```python
In [12]: a_str = "aabbccadf"

In [14]: a_str.replace("a", "b", 2)
Out[14]: 'bbbbccadf'
```

#### > expandtabs

将转义字符`\t`替换成空格, 默认8个

```python
def expandtabs(tabsize=8):
return str
```

* `tabsize`: `int`, 需要替换的大小

示例

```bash
In [20]: a_str = "a\tb"

In [21]: a_str.expandtabs()
Out[21]: 'a       b'
```



#### > 映射

映射是需要两部分组成的

* 映射表

  映射表构建有一下两种方式

  * `dict`
  * `maketrans`构建, 最终返回的还是`dict`

* 映射函数`translate`

**maketrans**

创建一个映射表, 构建方式有三种

* `dict`
* 字符一一映射
* 空间映射, 类似选中删除

```python
def maketrans(self, x, y=None, z=None):
return dict
```

* `x`: `dict`/`str`, `dict`表示一一映射, `str`表示, 将`x`中的每个字符对应的映射到`y`中的字符, 所以`x/y`的长度要一一对应
* `y`: `str`, 如果`y`存在, `x`必须为`str`.  表示需要替换的字符, 长度必须等于`x`的长度
* `z`: `str`, 如果`z`存在, `x`必须为`str`. 表示需要删除的字符

**translate**

启用映射关系

```python
def translate(self, table):
return str
```

* table: `dict`, 映射关系表

示例

```python
>>> a = "abcedf"
>>> b = str.maketrans("a", "1", "ef")
>>> b
{97: 49, 101: None, 102: None}
>>> a.translate(b)
'1bcd'
>>> c = str.maketrans({"a": "33", "e": None, "f": None})
>>> a.translate(c)
'33bcd'
>>> str.maketrans("a", "33", "ef")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: the first two maketrans arguments must have equal length
```

### 2.2.4 填充

#### > zfill

检查当前字符串长度, 如果不够指定长度, 则从左边进行`0`填充

```python
def zfill(self, with):
return str
```

* with: `int`, 填充宽度

示例

```python
>>> a_str = "ab123"
>>> a_str.zfill(10)
'00000ab123'
```

#### > center

检查当前字符串长度, 如果不够指定长度, 则进行居中填充

```python
def center(self, width, fillchar):
return str
```

* width: `int`, 填充宽度
* `fillchar`: `str`, 填充的符号

示例

```python
In [15]: a_str = "a"

In [17]: a_str.center(10, "b")
Out[17]: 'bbbbabbbbb'
```

#### > ljust

同`center`, 不同之处在于, 左边填充

#### > rjust

同`ljust`, 不同之处在于, 右边填充

#### > strip

清理两边的填充符号

```python
def strip(self, chars=None):
return str
```

* chars: `str`, 需要清理的符号. 默认`None`, 表示清理(空格, "\r", "\t", "\n"等字符串标志符)

示例

```python
In [18]: a_str = "bbbbabbbbb"

In [19]: a_str.strip("b")
Out[19]: 'a'
```

#### > lstrip

同`strip`, 不同之处在于, 只左边清理

#### > rstrip

同`strip`, 不同之处在于, 只右边清理

### 2.2.5 大小写转换

#### > upper

将所有字母转换为大写

```python
def upper(self):
return str
```

示例

```python
In [1]: "ab cd".upper()                                                                                     
Out[1]: 'AB CD' 
```

#### > capitalize

将每句话中的首字母大写

#### > title

将每个单词大写

#### > lower

将所有字母转换为小写

#### > casefold

将其他语种(非汉语或英语)转换小写

#### > swapcase

将每个字母大小写互转

## 2.3 判断

### 2.3.1 数字判断

#### > isdigit

判断, 是否存在且字符中全部为数字(Unicode数字, byte数字, 全角数字, 罗马数字)

```python
def isdigit(self):
return bool
```

示例

```python
In [2]: "12".isdigit()                                                                                       
Out[2]: True
```

#### > isdecimal

判断, 是否存在且字符中全为十进制数字(unicode数字, 全角数字)

#### > isnumeric

判断, 是否存在且字符中全为十进制数字(Unicode数字, bytes数字, 全角数字, 罗马数字)

### 2.3.2 字母判断

#### > isalpha

判断, 是否存在且字符中全为字母

#### > isupper

判断, 是否存在且字符中全为大写字母

#### > islower

判断, 是否存在且字符中全为小写字母

#### > isalnum

判断, 是否存在且字符中全为字母, 数字, 或者两者皆有.

#### > isspace

判断, 是否全部为空格

### 2.3.3 边界判断

#### > startswith

判断, 是否以某个字符开头

```python
def startswith(prefix, start, end):
return bool
```

* prefix: `str`, 判断以什么开头
* start: `int`, 判断起始索引值
* end: `int`, 判断终止索引值

示例

```python
In [4]: "12345".startswith("2", 1)                                                                           
Out[4]: True
```

#### > endswith

判断, 是否以某个字符结尾





