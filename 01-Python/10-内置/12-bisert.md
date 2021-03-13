# 1. bisect

本模块主要用于 **有序序列** 的操作. 比如优选插值, 索引查找等.

## 1.1 查询索引

#### > bisect_right

获取一个插入数据合适的位置, 以保证序列的**有序性**. 如果序列中存在于已知插入的数据重复, 则优先插入到右侧. 相当于为`list.insert`提供第一个参数

```python
def bisect_right(a, x, lo=0, hi=None):
return index
```

* a: `order array`, 有序的序列
* x: `object`, 需要插入的值
* lo: `index`, 选择起始索引位置
* hi: `index`, 选择终止索引位置

#### > bisect_left

获取一个插入数据合适的位置, 以保证序列的**有序性**. 如果序列中存在于已知插入的数据重复, 则优先插入到左侧. 相当于为`list.insert`提供第一个参数

```python
def bisect_left(a, x, lo=0, hi=None):
```

* a: `order array`, 有序的序列
* x: `object`, 需要插入的值
* lo: `index`, 选择起始索引位置
* hi: `index`, 选择终止索引位置

**示例**

```python
import bisect
data = [1, 2, 3, 7, 10]
print(bisect.bisect_left(data, 2))   # 按照该索引进行插入则会保证序列的有序性
data.insert(1, 2)
print(data)
del data[1]
print(bisect.bisect_left(data, 2, 3, 5))  # 按照该索引进行插入则会保证序列data[2:5]的有序性
data.insert(3, 2)
print(data[3:5])
del data[1]
print(bisect.bisect_right(data, 2))  # 按照该索引进行插入则会保证序列的有序性
```

输出

```python
1
[1, 2, 2, 3, 7, 10]
3
[2, 7]
3
```

#### > bisect

`bisect=bisect_right`, 所以参见`bisect_right`

本方法还可以用作范围取值.

**示例**

```python
import bisect
# 实现范围性枚举.
# 0 - 50 ==> level_1
# 50-70  ==> level_2
# 70-90  ==> level_3
# 90-∞ ==> level_4

a_list = [50, 70, 90]  # 三个分割点
b_list = ["level_1", "level_2", "level_3", "level_4"]  
# 四个分割段  注意len(a_list) != len(b_list), b_list相当于一条线段被len(a_list)分割后, 所对应的值

print(b_list[bisect.bisect(a_list, 39)])
print(b_list[bisect.bisect(a_list, 66)])
print(b_list[bisect.bisect(a_list, 80)])
print(b_list[bisect.bisect(a_list, 100)])
```

输出

```python
level_1
level_2
level_3
level_4
```

#### > insort_left

相当于帮你执行了`insert`, 即`a.insert(bisect.bisect_left(a, x), x)`

#### > insort_right

相当于帮你执行了`insert`, 即`a.insert(bisect.bisect_right(a, x), x)`

#### > insort

同`insort_left`

## 1.2 常用实例

### 1.2.1 查询索引

由此可见`bisect`查询索引是比较快的, 但是需要处理的必须是有序序列.

```python
import bisect
import random

a_list = [random.randint(0, 200) for _ in range(100000)]
a_list.sort()


def index_i():
    return a_list.index(100)


def binary_search_bisect(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None


def bisect_i():
    return binary_search_bisect(a_list, 100)


import time

count = 10000

print(index_i())
print(bisect_i())
s1 = time.time()
for _ in range(count):
    index_i()
s2 = time.time()
for _ in range(count):
    bisect_i()
s3 = time.time()

print("index: {}".format(s2 - s1))
print("bisect: {}".format(s3 - s2))
```

输出

```python
49864
49864
index: 7.404245853424072
bisect: 0.00892019271850586
```

### 1.2.1 其他操作

```python
def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError
```





