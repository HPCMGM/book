# 1. list

## 1.1 简介

有序的元素组成的数据结构, 支持索引, 切片, 加, 乘等操作

## 1.2 定义

```python
a_list = ["a", "b", 1, 2]
a_list = list("a", "b", 1, 2)
```

# 2. 常见操作

## 2.1 修改

### 2.1.1 增加

#### > 符号操作

* `+`

  列表叠加操作, 此方法要比`append`要快

  ```python
  In [3]: a_list = [1, 2]
  In [4]: c_list = ["1", "2"]
  
  In [5]: a_list + c_list  # 直接+, 不会修改原列表, 可以用+=来修改原列表即: a_list += c_list
  Out[5]: [1, 2, '1', '2']
  ```

* `*`

  列表批量增加

  ```python
  In [9]: [1, 2] * 3
  Out[9]: [1, 2, 1, 2, 1, 2]
  ```

#### > append

在原列表尾部追加一个元素

```python
def append(obj):
return None
```

* obj: `object`, 向列表中增加的元素

示例

```python
In [5]: a_list = [1, 2]                                                                                     
In [6]: a_list.append([1, 3])                                                                                       
In [7]: a_list                                                                                               
Out[7]: [1, 2, [1, 3]]
```

#### > extend

在原列表尾部叠加一个列表

```python
def extend(iterable):
return None
```

* iterable: `iterable`, 需要想原列表追加的可迭代对象

示例

```python
In [7]: a_list = [1, 2, [1, 3]]
In [8]: a_list.extend([2, 5]) 

In [9]: a_list                                                                                               
Out[9]: [1, 2, [1, 3], 2, 5]
```

#### > insert

在原列表指定位置插入一个元素

```python
def insert(index, obj):
return None
```

#### > copy

列表浅copy, 深copy可以用模块`copy`中的`deepcopy`来操作.

```python
def copy(self):
return list
```

示例

```python
In [9]: a_list                                                                                               
Out[9]: [1, 2, [1, 3], 2, 5]

In [10]: a_list.copy()                                                                                      
Out[10]: [1, 2, [1, 3], 2, 5]
```

### 2.1.2 其他

#### > sort

对原列表进行排序操作

```python
def sort(self, *, key=None, reverse=False):
return None
```

* key: `function`, 此函数用于定义排序规则, 需要接受一个参数(list中的每一项), 返回一个可hash的参数用于比较排序
* reverse: `bool`, 是否倒序.

示例

```python
In [22]: a_list = ["a3", "abc1", "df8"] 
In [24]: a_list.sort(key=lambda x: int(x[-1]))                                                                      
In [25]: a_list                                                                                             
Out[25]: ['abc1', 'a3', 'df8']
```

#### > reverse

对原列表进行翻转操作.

```python
def reverse(self):
return None
```

示例

```python
In [34]: a_list
Out[34]: [1, 2, 1, 3, 1, 1]
In [35]: a_list.reverse()
In [36]: a_list
Out[36]: [1, 1, 3, 1, 2, 1]
```

## 2.2 切片

切片在`list`中可以进行增删改查操作, 常用格式:

```python
list[index]
list[start:end:sep]
```

* index: `int`, 索引取值, 负数表示反向索引值
* start: `int`, 起始索引值, 负数表示反向索引值
* end: `int`, 终止索引值, 负数表示反向索引值
* sep: `int`, 步长, 负数表示倒序

#### > 增加

```python
In [11]: a_list = [1]                                                                                       
In [12]: a_list[0:1]=[1, 2, 4]                                                                                      
In [13]: a_list                                                                                             
Out[13]: [1, 2, 4]
```

#### > 修改

```python
In [13]: a_list
Out[13]: [1, 2, 4]
    
In [14]: a_list[0] = 5                                                                                       

In [15]: a_list                                                                                             
Out[15]: [5, 2, 4]
```

#### > 删除

```python
In [15]: a_list                                                                                             
Out[15]: [5, 2, 4]
    
In [16]: del a_list[0],a_list[1:2]                                                                           
In [17]: a_list                                                                                             
Out[17]: [2]

```

#### > 查询

```python
In [18]: a_list = [1, 2, 3]                                                                                         
In [19]: a_list[1]                                                                                           
Out[19]: 2
```

#### > 浅copy

```python
In [20]: a_list[:]                                                                                           
Out[20]: [1, 2, 3]
```

## 2.3 查询

#### > index

从左边查询某个元素的索引值, 如果不存在则报错

```python
def index(self, sub, start=None, end=None):
return int
```

* sub: `obj`, 需要查找的元素
* start: `int`, 查找的起始位置
* end: `int`, 查找的结束位置

示例

```python
In [18]: a_list = [1, 2, 1]
In [19]: a_list.index(1)
Out[19]: 0
In [20]: a_list.index(1, 1, 2)
---------------------------------------------------------------------------
ValueError Traceback (most recent call last)
<ipython-input-20-cf6482135a39> in <module>
----> 1 a_list.index(1, 1, 2)
ValueError: 1 is not in list
In [21]: a_list.index(1, 1, 30)
Out[21]: 2
```

#### > count

统计某个元素在列表中存在的个数

```python
def count(self, x):
return int
```

* x: `obj`, 需要统计的元素

示例

```python
In [29]: a_list = [1, 2, 1, 3, 1, 1]
In [31]: a_list.count(1)
Out[31]: 4
```

## 2.4 删除

#### > remove

从左边查找指定的第一个元素, 找到后移除此元素, 没有找到则抛出异常

```python
def remove(self, object):
return None
```

* object: obj, 需要删除的元素

示例

```python
In [8]: a_list
Out[8]: ['4', 1, 2, '3', 'a', 'b', 'c']
In [9]: a_list.remove(1)
In [10]: a_list
Out[10]: ['4', 2, '3', 'a', 'b', 'c']
```

#### > pop

删除指定索引的元素, 并返回此元素值, 没有找到则抛出异常

```python
def pop(self, index=-1):
return object
```

* index: `int`, 需要删除的元素索引值

示例

```python
In [12]: a_list
Out[12]: ['4', 2, '3', 'a', 'b', 'c']
In [13]: a_list.pop(2)
Out[13]: '3'
In [15]: a_list
Out[15]: ['4', 2, 'a', 'b', 'c']
```



#### > clear

清空list

```python
def clear(self):
return None
```

示例

```python
In [15]: a_list
Out[15]: ['4', 2, 'a', 'b', 'c']
In [16]: a_list.clear()
In [17]: a_list
Out[17]: []
```

# 3. 列表操作

## 3.1 原序去重

列表去重, 并保证顺序不乱, 各个实现方式的效率如下

```python
import time
from collections import OrderedDict

ids = [1, 4, 3, 3, 4, 2, 3, 4, 5, 6, 1] + list(range(0, 1000))

def test1():
    ids_list = list(set(ids))
    ids_list.sort(key=ids.index)
    return ids_list

def test2():
    return OrderedDict().fromkeys(ids).keys()

def test3():
    new_li = []
    for i in ids:
        if i not in new_li:
            new_li.append(i)
    return new_li

def test4():
    ids_list = set(ids)
    return sorted(ids_list, key=ids.index)

count = 1000

st1 = time.time()
for _ in range(count):
    test1()
st2 = time.time()

for _ in range(count):
    test2()
st3 = time.time()

for _ in range(count):
    test3()
st4 = time.time()
```

输出

```python
set-list-sort: 5.71999979019
orderdict: 0.84500002861
new_list: 5.75
set-sorted: 5.69500017166
```

