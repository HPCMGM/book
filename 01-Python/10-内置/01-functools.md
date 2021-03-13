# 1. 操作函数

#### > partial

对函数的参数进行扩充操作.(偏函数)

```python
def partial(func, /, *args, **keywords):
return func
```

* fun: `function`, 需要拓展变量的函数
* args: `args`, 需要拓展的位置参数
* keywords: `kwargs`, 需要拓展的关键字参数

**原理类似**

```python
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
```

**示例**

```python
from functools import partial
def fun(a, b, c):
    print("此函数必须接收三个参数: ", a, b, c)

def tex(func, a):
    """函数托管执行, 比如线程运行的函数托管imap, 只允许传入一个参数"""
    return func(a)

f = partial(fun, 1, 2)
tex(f, 3)
```

输出

```python
此函数必须接收三个参数:  1 2 3
```

#### > reduce

对函数的返回值进行累积处理. 

```python
def reduce(function, iterable, initializer=None):
return function_value
```

* function: `function`, 需要执行的函数
* iterable: `iterable`, 函数的参数列表
* initializer: `value`, 初始累积数据

**示例(累加)**

```python
import time
from functools import wraps, reduce
def clock(func):
    @wraps(func)
    def clocked(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        use_time = time.time() - start_time
        name = func.__name__
        param = reduce(lambda x, y: x + ", " + str(y[0]) + "=" + str(y[1]) if x else str(y[0]) + "=" + str(y[1]), kwargs.items(),
                       reduce(lambda x, y: x + "," + str(y) if x else str(y), args, ""))
        print("[{:.5f}s] {}({}) ==> {}".format(use_time, name, param, result))
        return result
    return clocked

@clock
def pt(a=1):
    time.sleep(2)
    print("test massage", a)

pt(a=3)
```

输出

```python
test massage 3
[2.00075s] pt(a=3) ==> None
```

#### > singledispatch

根据函数的参数, 分发不同的函数执行任务. 单调泛函数

```python
@singledispatch
def fun(*args):
	pass

@fun.register
def do_1(ver, *args):
    pass
```

**示例**

```python
from functools import singledispatch

@singledispatch
def fun(arg, verbose=False):
    """其他类型"""
    if verbose:
        print("fun执行: ", end=" ")
    print(arg)

@fun.register(int)
def _(arg, verbose=False):
    """整形"""
    if verbose:
        print("int执行: ", end=" ")
    print(arg)

@fun.register(list)
def _(arg, verbose=False):
    """列表类型"""
    if verbose:
        print("list执行: ", end=" ")
    for i, elem in enumerate(arg):
        print(i, elem)

@fun.register(complex)
def _(arg, verbose=False):
    """复数类型"""
    if verbose:
        print("complex执行: ", end=" ")
    print(arg.real, arg.imag)

def nothing(arg, verbose=False):
    """空类型"""
    print("nothing执行: ", end=" ")
    print(arg)

fun.register(type(None), nothing)

@fun.register(float)
@fun.register(Decimal)
def _(arg, verbose=False):
    """小数类型"""
    if verbose:
        print("float执行:", end=" ")
    print(arg / 2)


print("支持分发的全部类型: ", fun.registry.keys())
print(_ is fun)  # 说明

fun("12342", verbose=True)
fun(123, verbose=True)
fun([123, 234, 345], verbose=True)
fun(complex(1), verbose=True)
fun(None, verbose=True)
fun(0.123, verbose=True)
```

输出

```python
支持分发的全部类型:  dict_keys([<class 'int'>, <class 'list'>, <class 'complex'>, <class 'object'>, <class 'NoneType'>, <class 'decimal.Decimal'>, <class 'float'>])
False
fun执行:  12342
int执行:  123
list执行:  0 123
1 234
2 345
complex执行:  1.0 0.0
nothing执行:  None
float执行: 0.0615
```

#### > lru_cache

函数缓存.

```python
def lru_cache(maxsize = 128，typed = False):
return function_value
```

* maxsize: `int`, 函数缓存的最大字节
* typed: `bool`, 是否区分类型(如: 3.0和3)

**示例**

```python
# 缓存函数运行结果, 提高函数运行效率
from functools import lru_cache, reduce, wraps
import time


def clock(func):
    @wraps(func)
    def clocked(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        use_time = time.time() - start_time
        name = func.__name__
        param = reduce(lambda x, y: x + ", " + str(y[0]) + "=" + str(y[1]) if x else str(y[0]) + "=" + str(y[1]), kwargs.items(),
                       reduce(lambda x, y: x + "," + str(y) if x else str(y), args, ""))
        print("[{:.5f}s] {}({}) ==> {}".format(use_time, name, param, result))
        return result
    return clocked

@lru_cache(maxsize=32)
@clock
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(100))
```

输出

```python
...
[0.00103s] fib(98) ==> 135301852344706746049
[0.00103s] fib(99) ==> 218922995834555169026
[0.00103s] fib(100) ==> 354224848179261915075
354224848179261915075
```

#### > cmp_to_key

创建排序规则的函数, 目的是将Python2中的比较语法转换到Python3中.针对函数: `sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest(), itertools.groupby()...`等`key`比较函数. 返回值负数说明x < y, 整数表示x>y, 0表示相等

```python
def cmp_to_key(func):
return object
```

* func: `funtion`, 需要使用的比较规则

**示例**

```python
from functools import cmp_to_key
t_list = [1, 5, 4]

def sorting(x, y):
    print(x, y)
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0

print(sorted(t_list, key=cmp_to_key(sorting)))
```

输出

```python
5 1
4 5
4 5
4 1
[1, 4, 5]
```

#### > wraps

将被装饰的属性替换为装饰函数的属性值. 主要针对属性: `'__module__', '__name__', '__qualname__', '__doc__', '__annotations__'`.

```python
def wrapps(func):
return function_value
```

* func: `func`, 被装饰的函数

**示例**

```python
from functools import wraps

def my_decorator1(f):
    """自定义装饰器"""
    def wrapper(*args, **kwargs):
        """装饰器1内部函数"""
        print('调用装饰函数1')
        return f(*args, **kwargs)
    return wrapper

def my_decorator2(f):
    """自定义装饰器"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        """装饰器2内部函数"""
        print('调用装饰函数2')
        return f(*args, **kwargs)
    return wrapper

@my_decorator1
def demo1():
    """Demo1函数"""
    print('Doing something1')

@my_decorator2
def demo2():
    """Demo2函数"""
    print('Doing something2')

print(demo1.__name__)
print(demo2.__name__)
print(demo1.__doc__)
print(demo2.__doc__)
demo1()
demo2()
```

输出

```python
wrapper
demo2
装饰器1内部函数
Demo2函数
调用装饰函数1
Doing something1
调用装饰函数2
Doing something2
```

# 2. 操作类

#### > total_ordering

比较运算符补全方法. 只要实现`__eq__`和其他比较魔法方法中的任意一个. 即可推算出全部的比较运算.

```python
def total_ordering(cls):
return cls
```

* cls: `class`, 需要补全的类

**示例**

```python
from functools import total_ordering


# noinspection PyUnresolvedReferences
@total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))


s1 = Student()
s1.lastname = "a"
s1.firstname = "b"
s2 = Student()
s2.lastname = "c"
s2.firstname = "d"
print(s1 < s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1 < s2)
print(s1 == s2)
```

输出

```python
True
False
True
True
False
```



# 3 异常

## 3.1 版本问题

* 错误信息

  此异常是模块内部错误, 需要修改部分源码

  ```python
    File "C:\Python27\lib\functools.py", line 56, in <lambda>
      '__lt__': [('__gt__', lambda self, other: other < self),
    ...
    File "C:\Python27\lib\functools.py", line 56, in <lambda>
      '__lt__': [('__gt__', lambda self, other: other < self),
  RuntimeError: maximum recursion depth exceeded in cmp
  ```

* 解决方案

  修改源码, 将如下信息进行修改

  ```python
  convert = {
          '__lt__': [('__gt__', lambda self, other: other < self),
                     ('__le__', lambda self, other: not other < self),
                     ('__ge__', lambda self, other: not self < other)],
          '__le__': [('__ge__', lambda self, other: other <= self),
                     ('__lt__', lambda self, other: not other <= self),
                     ('__gt__', lambda self, other: not self <= other)],
          '__gt__': [('__lt__', lambda self, other: other > self),
                     ('__ge__', lambda self, other: not other > self),
                     ('__le__', lambda self, other: not self > other)],
          '__ge__': [('__le__', lambda self, other: other >= self),
                     ('__gt__', lambda self, other: not other >= self),
                     ('__lt__', lambda self, other: not self >= other)]
      }
  
  ```

  修改为

  ```python
      convert = {
          '__lt__': [('__gt__', lambda self, other: not (self < other or self == other)),
                     ('__le__', lambda self, other: self < other or self == other),
                     ('__ge__', lambda self, other: not self < other)],
          '__le__': [('__ge__', lambda self, other: not self <= other or self == other),
                     ('__lt__', lambda self, other: self <= other and not self == other),
                     ('__gt__', lambda self, other: not self <= other)],
          '__gt__': [('__lt__', lambda self, other: not (self > other or self == other)),
                     ('__ge__', lambda self, other: self > other or self == other),
                     ('__le__', lambda self, other: not self > other)],
          '__ge__': [('__le__', lambda self, other: (not self >= other) or self == other),
                     ('__gt__', lambda self, other: self >= other and not self == other),
                     ('__lt__', lambda self, other: not self >= other)]
      }
  
  ```

  