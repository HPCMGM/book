# 1. tuple

## 1.1 namedtuple

元组的子类

**特点**

* 可以像普通对象调用一样来处理类似字典功能的容器
* 占用内存少

<hr>

```Python
def namedtuple(typename, field_names, rename=False, defaults=None, module=None)
	return namedtuple
```

* typename: str, 对namedtuple进行命名
* field_names: str/iterable, nametuple可以使用的属性. str需要用`, `分开
* rename: bool, 如果`filed_names`与系统关键字, 或者出现重复, 是否进行重命名处理, False表示直接抛出异常. True表示利用索引进行重命名`_1`, `_2`...
* defaults: iterable, 对`filed_names`设置缺省值. 注意, 此值是从右开始赋予的.
* module: str, 设置`__module__`属性

### 1.1.1 通用方法支持

* getattr: `getattr(t, "x", 1)`

* 切片索引取值: `t[1]`

* 继承

  由于`namedtuple`也是对象, 所以可以利用继承特性对父类进行拓展

* 设置`__doc__`属性

  ```Python
  from collections import *
  
  Test = namedtuple("Test", ["x", "y", "z"], defaults=[1, 2])
  Test.x.__doc__ = "x description"
  help(Test.x)
  ```

  输出

  ```python
  Help on property:
  
      x description
  ```

### 1.1.2 方法

#### \_make()

类方法, 将可迭代对象强转为`namedtuple`中的value

```Python
@classmethod
def _make(cls, iterable):
    return namedtuple
```

* iterable: 可迭代对象

**示例**

   ```python
Test = namedtuple("Test", ["x", "y", "z"], defaults=[1, 2])
t = Test(5)
print(t)
a = [7, 8, 9]
print(t._make(a))
   ```

**输出**

```bash
Test(x=5, y=1, z=2)
Test(x=7, y=8, z=9)
```

#### \_asdict()

* < Python3.8: 将`namedtuple`转化为`OrderedDict`, 即有序字典
* \>=Python3.8: 返回`dict`

```Python
@classmethod
def _asdict(cls, iterable):
    return OrderedDict/Dict
```

**示例**

```Python
from collections import *

Test = namedtuple("Test", ["x", "y", "z"], defaults=[1, 2])
t = Test(5)
print(t)
print(t._asdict())
```

**输出**

```bash
Test(x=5, y=1, z=2)
OrderedDict([('x', 5), ('y', 1), ('z', 2)])
```

#### \_replace()

修改并生成一个新的`namedtuple`

```Python
def _replace(**kwargs):
```

* kwargs: 所要修改的值, 以关键字参数传入

**示例**

```python
Test = namedtuple("Test", ["x", "y", "z"], defaults=[1, 2])
t = Test(5)
print(t)
a = {"x": 5, "y": 7}
print(t._replace(**a))
```

**输出**

```bash
Test(x=5, y=1, z=2)
Test(x=5, y=7, z=2)
```



### 1.1.3 属性

#### \_fields

输出`namedtuple`配置的属性

* 示例

  ```python
  from collections import *
  
  Test = namedtuple("Test", ["x", "y", "z"], defaults=[1, 2])
  t = Test(5)
  print(t._fields)
  ```

* 输出

  ```bash
  ('x', 'y', 'z')
  ```

#### \_field_defaults

输出`namedtuple`的缺省键值对, 以`dict`表示

* 示例

  ```python
  Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
  print(Account._field_defaults)
  ```

* 输出

  ```bash
  {'balance': 0}
  ```

### 1.1.4 常用功能

* 像调用属性一样处理字典

  ```python
  Test = namedtuple("Test", "a,b,c")
  nt = Test(1, 2, 3)
  print(nt.a, nt.b, nt.c)
  ```

  输出

  ```bash
  1 2 3
  ```

  



# 2. list

## 2.1 deque

双端队列,  是通过`queue`队列实现的. 支持线程安全.

```Python
def __init__(self, iterable=None, maxlen=None)
	return queue
```

* iterable: 需要转换为双端队列的可迭代对象

* maxlen: int/None, 限制队列的长度, 超过长度时, 再次添加会从队列的另一端弹出一个. 可以利用这个特性实现`tail`功能

示例一

  ```Python
# 查看后几行: tail -n 10 xx.txt
from collections import *

def tail(filename, n=5):
    with open(filename, "r", encoding="utf-8") as f:
        print("".join(deque(f, n)))

tail(r"E:\project\test\t_ftp\t_ftp.py", 10)
  ```

  示例二

```Python
# 轮询遍历
abc, d, ef  --> a d e b f c

def roundrobin(*iterable):
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n

print(list(roundrobin(["abc", "d", "ef"])))
```



支持的列表方法如下:

* `len()`
* `reversed(d)`
* `copy.copy(d)`
* `copy.deepcopy(d)`
* `x in d`
* `d1 + d2`
* `for x in d`
* 切片
* `d1 * 2`

**注**: 由于此节的方法全部为重复方法, 暂时不举例说明

### 2.1.1 方法

#### append()

从右侧添加元素

```Python
def append(self, x)
return None
```

#### appendleft()

从左侧添加元素

```Python
def appendleft(self, x)
return None
```

#### clear()

清空元素

```Python
def clear(self)
	return None
```

#### copy()

浅copy

```Python
def copy(self):
    return deque
```

#### count()

统计某个元素的个数

```Python
def count(self, x):
    return int
```

#### extend()

从右侧批量添加元素

```Python
def extend(self, iterable):
    return None
```

#### extendleft()

从右侧批量添加元素

```Python
def extendleft(self, iterable):
    return None
```

#### index()

找出某个元素在队列的位置. 

```Python
def index(self, x, start, stop):
    return int/ValueError
```

* x: obj, 需要查找的元素
* start: int, 查找的起始位置
* stop: int, 查找的终止位置

#### pop()

删除最右侧的元素, 并返回

```python
def pop(self):
    return obj/IndexError
```

#### popleft()

删除最左侧的元素, 并返回

```Python
def popleft(self):
    return obj/IndexError
```

#### reverse()

翻转队列

```Python
def reverse(self):
    return None
```

#### rotate()

队列向右移动.  等价于: 循环删除右边的元素, 并添加到左边.   负数反过来. 

```Python
def rotate(self, n=1):
    return None
```

* n: int, 需要移动几个元素. 

示例

```Python
from collections import *

d = deque([1, 2])
d.rotate(3)  # 队列整体移动3次
print(d)
```

输出

```Python
deque([2, 1])
```

### 2.1.2 属性

#### maxlen

获取队列的上限.  如果没有限制, 则为`None`

## 2.2 UserList

`UserList`与`list`对象基本相同, 一般继承并改写`List`时最好是使用`UserList`, 这样`list`还可以用于其他用途, 不会出现冲突.

```Python
def __init__(list):
    return UserList
```

* `self.data`: 用于存储数据的变量

## 2.3 UserString

同`UserString`

```Python
def __init__(sting):
    return UserString
```

* self.data: 用于存储str的变量





# 3. dict

## 3.1 ChainMap

`dict`的子类, 合并多个字典为一个字典. 只是链接映射关系, 所以比`update`要快

```python
def __init__(self, *maps)
	return dict
```

* maps: dict, 多个字典

由于继承`dict`, 拥有全部`dict`功能, 并添加了部分功能

### 3.1.1 新增功能

#### maps

存储的链接列表, 可以被修改.

* 实例

  ```python
  a = {"a": 1, "b": 2}
  b = {1: "c", 2: "d"}
  
  cm = ChainMap(a, b)
  print(cm.maps)
  ```

* 输出

  ```bash
  [{'a': 1, 'b': 2}, {1: 'c', 2: 'd'}]
  ```

#### new_child()

在连接首部插入字典的链接, 并返回

```Python
def new_child(self, m):
    return chainmap
```

* m: mapping, 字典

实例

```Python
a = {"a": 1, "b": 2}
b = {1: "c", 2: "d"}
c = {"t": [1, 2], "f": {3, 4}}

cm = ChainMap(a, b)
print(cm.new_child(c))
```

输出

```bash
ChainMap({'t': [1, 2], 'f': {3, 4}}, {'a': 1, 'b': 2}, {1: 'c', 2: 'd'})
```

#### parents

输出第一个dict

* 实例

  ```python
  a = {"a": 1, "b": 2}
  b = {1: "c", 2: "d"}
  cm = ChainMap(a, b)
  print(cm)
  print(cm.parents)
  ```

* 输出

  ```bash
  ChainMap({'a': 1, 'b': 2}, {1: 'c', 2: 'd'})
  ChainMap({1: 'c', 2: 'd'})
  ```

### 3.1.2 常用功能

* 组合字典

  ```Python
  a = {"a": 1, "b": 2}
  b = {1: "c", 2: "d"}
  for t in ChainMap(a, b).items():
      print(t)
  ```

  输出

  ```Python
  (1, 'c')
  (2, 'd')
  ('a', 1)
  ('b', 2)
  ```

* 系统变量查找顺序

  系统变量查找顺序就是利用类似的方式在寻找的. 模拟代码

  ```python
  from collections import *
  
  import builtins
  pylookup = ChainMap(locals(), globals(), vars(builtins))
  print(pylookup)
  ```

  

## 3.2 Counter

`dict`的子类, 用于数据的统计.

```python
def __init__([iterable or mapping]):
    return Counter
```

**注意**:

* Counter没有实现字典的`fromkey`函数.

### 3.2.1  新增功能

#### update()

增加需要统计的数据

```python
def update(self, __m, **kwargs)
	return None
```

* \_\_m: mapping/iterable, 需要新增统计的数据, 如果为mapping, 则是增加. 不会直接使用mapping中的值
* \*\*kwargs:  类似dict传值.

示例

```Python
from collections import *

c_a = ["a", "b", "c"]
c_b = "abcesoiamo"
c_d = {"a": 3, "c": 2}
c = Counter(c_a)
c.update(c_d)
c.update(c_b, b=5)
print(c)
```

输出

```bash
Counter({'b': 7, 'a': 6, 'c': 4, 'o': 2, 'e': 1, 's': 1, 'i': 1, 'm': 1})
```

#### elements()

按照顺序将`key`(重复的将在一起)依次排列出来

```Python
def elements(self):
    return iterable
```

实例

```Python
from collections import *

c_b = "abcesoiamo"
c = Counter(c_b)
print(list(c.elements()))
```

输出

```Python
['a', 'a', 'b', 'c', 'e', 's', 'o', 'o', 'i', 'm']
```

#### most_common()

从高到低截取最大的`n`个key/value. 相同时会按照加入的顺序排序.

```Python
def most_common(self, n):
    return [(k1, v1)...]
```

实例

```python
from collections import *

c_b = "abracadabra"
c = Counter(c_b)
print(list(c.most_common(3)))
```

输出

```python
[('a', 5), ('b', 2), ('r', 2)]
```

#### subtract()

与`update`相反的操作. 减去元素

```python
@overload
def subtract(self, __mapping:)
```

* \_\_mapping: mapping/iterable, 需要减去的次数. 或者元素

实例

```Python
from collections import *

c_b = "abracadabra"
c = Counter(c_b)
c.subtract("abc")
print(c)
```

输出

```Python
Counter({'a': 4, 'r': 2, 'b': 1, 'd': 1, 'c': 0})
```









## 3.3 OrderedDict

有序字典, `dict`的子类. 由于Python3.7以上版本, `dict`做了变动, 支持了排序功能

| 功能                         | `dict`              | `OrderedDict`                  |
| ---------------------------- | ------------------- | ------------------------------ |
| 排序算法                     | 支持, 但不擅长      | 擅长                           |
| 映射/存储/迭代/空间效率/更新 | 擅长                | 支持, 但不擅长                 |
| 等号校验数据是否相等         | 只比较数据          | 比较数据和顺序                 |
| `popitem()`                  | `FIFO`弹出末尾元素  | 可以指定`FIFO`开始或者末尾弹栈 |
| `move_to_end()`              | 不支持              | 将指定元素移动到末尾           |
| `__reversed__()`             | Python3.8之前不支持 | 支持翻转字典                   |



<hr>

```Python
def __init__([items]):
    return OrderedDict
```

* 传入参数与`dict`相同

示例一:

```Python
# 实现url_cache功能
from collections import OrderedDict

class LruCache(OrderedDict):
    """缓存"""

    def __init__(self, max_size=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_size = max_size

    def __setitem__(self, key, value):
        if len(self) >= self.max_size:
            first = next(iter(self))
            del self[first]
        super().__setitem__(key, value)

    def __getitem__(self, item):
        value = super().__getitem__(item)
        self.move_to_end(item)
        return value

    def __call__(self, size=100):
        self.max_size = size
        def func(fun):
            def wrapper(*args, **kwargs):
                if args in self:
                    res = self[args]
                else:
                    res = fun(*args, **kwargs)
                    self[args] = res
                return res
            return wrapper
        return func

uc = LruCache()

@uc(size=100)
def fib(x):
    print(x)
    if x < 2:
        return 1
    return fib(x - 1) + fib(x - 2)

print(fib(20))
print(fib(30))
print(fib(20))
```



支持`dict`中的全部功能, 并拓展了部分功能

### 3.3.1 新增功能

#### popitem()

依照`FIFO`, 指定左边或者右边弹栈

```Python
def popitem(self, last=True):
    return (key, value)
```

* last: bool.  True表示右边出栈

实例

```Python
from collections import *

od = OrderedDict(x=2, y=3, z=4)
print(od.popitem(False))
print(od.popitem(True))
```

输出

```Python
('x', 2)
('z', 4)
```

#### move_to_end()

将某个键值移动到末尾

```python
def move_to_end(self, key, last)
```

* key: key, 指定需要移动的键

实例

```Python
od = OrderedDict(x=2, y=3, z=4)
od.move_to_end("y", last=True)
print(od)
```

输出

```python
OrderedDict([('x', 2), ('z', 4), ('y', 3)])
```

#### reversed()

利用`__reversed__()`翻转字典, 返回值为`iter`

实例

```Python
from collections import *

od = OrderedDict(x=2, y=3, z=4)
print(list(reversed(od)))
```

输出

```bash
['z', 'y', 'x']
```



## 3.4 defaultdict

继承于`dict`, 增加了字典的缺省值功能

```Python
def __init__([default_factory=None], **kwargs)
	return defaultdict
```

* default_factory: 可调用的函数/对象/None, 第一个参数为缺省值
* **kwargs: 其他参数, 用于构建字典的key/value对

### 3.4.1 新增属性

#### \__missing__()

自动赋予缺省值. 只能用切片, 不能用`.get()`, 否则不能获取到缺省值

```Python
def __missing__(self, key):
    self[key] = default_factory()
```

* key: key, 需要赋予缺省值的可以

示例

```python
class DD(defaultdict):

    def __missing__(self, key):
        value = self.default_factory()
        print("当前key值: ", key)
        self[key] = value
        return value

d = DD(int)
print("切片正常获取到缺省值: ", d[1])
print("get不能获取到缺省值: ", d.get(2))
```

输出

```bash
当前key值:  1
切片正常获取到缺省值:  0
get不能获取到缺省值:  None
```

#### default_factory

存储用来提供缺省值的函数

* 示例

  ```python
  def test1():
      return 2
  
  dd = defaultdict(test1)
  print(dd.default_factory.__name__, dd.default_factory)
  ```

  

* 输出

  ```bash
  test1 <function test1 at 0x000001FEBC66D378>
  ```

### 3.4.2 常用功能

* 统计

  ```python
  dd = defaultdict(int)
  count_str = "ashomoasoiuhoie"
  
  for s in count_str:
      dd[s] += 1
  
  print(dd)
  ```

  输出

  ```bash
  defaultdict(<class 'int'>, {'a': 2, 's': 2, 'h': 2, 'o': 4, 'm': 1, 'i': 2, 'u': 1, 'e': 1})
  ```


## 3.5 UserDict

`UserDict`与`Dict`对象基本相同, 一般继承并改写`Dict`时最好是使用`UserDict`, 这样`dict`还可以用于其他用途, 不会出现冲突.

```Python
def __init__(dict):
    return UserDict
```

* self.data: 用于保存`UserDict`的变量

