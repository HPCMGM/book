# 1. itertools

## 1.1 迭代组合

#### > accumulate

和`functools.reduce`类似, 区别在于将每次迭代时的过程获取到.

```python
def accumulate(iterable, func=operator.add):
return iterable
```

* iterable: `iterable`, 需要迭代处理的参数
* func: `function`, 需要对参数处理的函数, 需要接受两个参数, 第一个参数为上次此函数的结果, 第二个参数为`iterable`迭代出来的元素

**类似**

```python
def accumulate(iterable, func=operator.add):
    """类似reduce, 不过会把每个步骤都输出"""
    ite = iter(iterable)
    try:
        total = next(ite)
    except StopIteration:
        return
    yield total
    for i in ite:
        total = func(total, i)
        yield total
```

**示例**

```python
from itertools import accumulate
from functools import reduce
range_list = range(5)
for i in accumulate(range_list, lambda x, y: x + y):
    print(i)

print(reduce(lambda x, y: x + y, range_list))
```

输出

```python
0
1
3
6
10
10
```

#### > chain

组合迭代, 类似

`[1, 2], [2, 3]` --> `[1, 2, 3, 4]`

```python
def __init__(self, *iterables):
return iterable

@classmethod
def from_iterable(cls, iterable):
return iterable
```

* iterable: `iterable`, 可变参数, 接受的每个参数都必须可迭代

**示例**

```python
for i in chain([1, 2], [2, 3]):
    print(i)
from i in chain.from_iterable("abc"):
	print(i)
```

输出

```python
1
2
2
3
a
b
c
```

#### > groupby

分组迭代, 类似数据库操作的`group by`.

```python
def groupby(iterable, key=None):
return iterable
```

* iterable: `iterable`, 需要进行处理的可迭代对象
* key: `function`, 需要进行排序的键指定

**示例**

```python
import itertools
a_list = ["ab", "ac", "be", "bc", "ca"]
print({k: list(v) for k, v in itertools.groupby(a_list, key=lambda x: x[0])})
```

输出

```python
{'a': ['ab', 'ac'], 'b': ['be', 'bc'], 'c': ['ca']}
```

#### > islice

类似切片

```python
def islice(iterable, start, stop, step):
    # islice('ABCDEFG', 2) --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G
return iterable
```

* iterable: `iterable`, 需要操作的可迭代对象
* start: `int`, 起始索引值
* stop: `int`, 终止索引值
* step: `int`, 步长

#### > starmap

类似`map`,区别在于, 元素中每个元素在传入`func`时, 会自动拆包操作

```python
def starmap(func, iterable):
return iterable
```

* func: `function`, 需要进行处理的函数
* iterable: `iterable`, 函数的参数, 此参数在传入函数时会进行拆包处理

**类似代码**

```python
def starmap(function, iterable):
	for args in iterable:
        yield function(*args)
```

#### > zip_longest

类似`zip`函数, 不同在于如果某一个可迭代对象长度较小, 则使用特定的字符进行填充处理, 不在遗弃

```python
def zip_longest(*args, fillvalue=None):
return iterable
```

* args: `args`, 需要迭代组合的可迭代对象
* fillvalue: `object`, 特定的字符进行填充

**示例**

```python
print(list(itertools.zip_longest([1, 2, 3], [1, 2, 3, 4], fillvalue="~")))
```

输出

```python
[(1, 1), (2, 2), (3, 3), ('~', 4)]
```



## 1.2 排列组合

### 1.2.1 不重复组合

#### > combinations

将`p`中的全部元素, 按照`r`个进行自由组合, 不得重复

类似:

```python
def combinations(p, r):
    """
    combinations('ABCD', 2) --> AB AC AD BC BD CD
    combinations(range(4), 3) --> 012 013 023 123
    """
return iterable
```

* p: `iterable`, 需要组合的可迭代对象
* r: `int`, 需要组合的数量

**原理类似**

```python
def combinations(iterable, c):
    ite = list(iterable)
    n = len(ite)
    d = n - c
    if n <= c:
        yield tuple(ite)
        return
    # index用于索引取值的列表
    index = list(range(c))
    # 用来控制index
    control = list(reversed(index))
    # 迭代出第一项
    yield tuple(ite[i] for i in index)
    while True:
        # 此循环用于寻找偏移的对称点
        for i in control:
            # 控制索引不越界, 如果越界则说明当前index已达上线, 则需要将i减少一位, 直至没有越界, 否则说明遍历完成
            if index[i] < i + d:
                # 索引前后偏移一位
                index[i] += 1
                break
        else:
            return
        for j in range(i + 1, c):
            # 把前一项的索引+1赋值给当前
            index[j] = index[j - 1] + 1
        yield tuple(ite[i] for i in index)
```

**示例**

```python
print(list(combinations("ABCD", 2)))
```

输出

```python
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
```

#### > product

笛卡尔积

```python
def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
return iterable
```

* args: `iterable`, 不定长参数每项中必须都可迭代, 用于非重复性排列组合
* repeat: `int`, 表示将`*args`中的都拓展为`repeat`倍, 然后在进行排列组合

**类似代码**

```python
def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
```

**示例**

```python
print(list(product("AB", "ab", repeat=1)))
print(list(product("AB", "ab", repeat=2)))
```

输出

```python
[('A', 'a'), ('A', 'b'), ('B', 'a'), ('B', 'b')]
[('A', 'a', 'A', 'a'), ('A', 'a', 'A', 'b'), ('A', 'a', 'B', 'a'), ('A', 'a', 'B', 'b'), ('A', 'b', 'A', 'a'), ('A', 'b', 'A', 'b'), ('A', 'b', 'B', 'a'), ('A', 'b', 'B', 'b'), ('B', 'a', 'A', 'a'), ('B', 'a', 'A', 'b'), ('B', 'a', 'B', 'a'), ('B', 'a', 'B', 'b'), ('B', 'b', 'A', 'a'), ('B', 'b', 'A', 'b'), ('B', 'b', 'B', 'a'), ('B', 'b', 'B', 'b')]
```

### 1.2.2 可重复组合

#### > combinations_with_replacement

可重复性排列组合

```python
def combinations_with_replacement(p, r):
    """
    排列组合:
         combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    """
```

* p: `iterable`, 需要组合的可迭代对象
* r: `int`, 需要组合的数量

**类似代码**

```python
def combinations_with_replacement(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
```

**示例**

```python
print(list(itertools.combinations.combinations_with_replacement("ABC", 2)))
```

输出

```python
[AA AB AC BB BC CC]
```

#### > permutations

带顺序的随机排列组合

```python
def permutations(p, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
return iterable
```

* p: `iterable`, 需要组合的可迭代对象
* r: `int`, 需要组合的数量

**类似代码**

```python
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
```

### 1.3 不定长迭代

#### > repeat

不定长迭代

```python
def repeat(object, times=None):
    # repeat(10, 3) --> 10 10 10
return iterable
```

* object: `object`, 任意Python数据类型
* times: `int/None`, 表示需要迭代的次数, 如果为`None`表示无限迭代

**类似源码**

```python
def repeat(object, times=None):
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object
```

**示例**

```python
print(list(repeat(object="abc", times=2)))
```

输出

```python
['abc', 'abc']
```

#### > count

无限迭代, 注意设置跳出条件.

```python
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
return iterable
```

* start: `int`, 迭代的起始值
* step: `int`, 迭代的步长, 正数表示正向增长, 负数表示反向增长

**代码示例**

```python
def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step
```

#### > cycle

无限循环迭代, 注意跳出条件

```python
def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
return iterable
```

* iterable: `iterable`, 需要循环迭代的可迭代对象

**代码示例**

```python
def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element
```

## 1.3 过滤迭代

#### > compress

筛选迭代, 类似`filter`

```python
def compress(data, selectors):
    """
    compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    """
return iterable
```

* data: `iterable`, 需要过滤的可迭代参数
* selectors: `iterable`, 过滤规则, 经过`bool`运算后为`True`的将会被保留

**类似**

```python
def compress(data, selectors):
	return filter(lambda x: x[0], zip(selectors, data))
```

#### > dropwhile

阻断式获取未满足条件的当前元素及其以后的全部元素

```python
def dropwhile(predicate, iterable):
	# dropwhile(lambda x: x < 0, [-1, -2, 1, -1, -2]) ==> 1, -1, -2
return iterable
```

* predicat: `fucntion`, 需要进行筛选的条件
* iterable: `iterable`, 需要筛选的可迭代对象

**类似代码**

```python
def dropwhile(predicate, iterable):
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x
```

#### > takewhile

类似`dropwhile`, 但是是获取之前的全部元素

**类似代码**

```python
def takewhile(predicate, iterable):
    # takewhile(lambda x: x < 0, [-1, -2, 1, -1, -2]) --> -1, -2
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break
```

#### > filterfalse

类似`filter`, 区别在于判断时, 对条件进行取反操作.



