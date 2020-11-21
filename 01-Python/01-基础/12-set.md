# 1. 集合

## 1.1 介绍

集合`set`, Python中的高级变量, 可以用来:

* 去重, 排序[注意: 本质上`set`是无序的, 排序只是附加的功能]
* 常见的算数运算: 交并补差集运算

在Python中, 集合内置有两种:

* 普通集合`set`

* 冰冻集合`forzenset`, 一经创建不可修改.

  **所以:** 冰冻集合支持此查询相关操作, 不可进行增改删操作!

## 1.2 定义

集合创建类似字典, 但是元素必须为可哈希值.

```python
In [1]: type({})
Out[1]: dict

In [3]: type({1,2, "3"})
Out[3]: set

In [4]: type({1,2, [1,2]})
---------------------------------------------------------------------------
TypeError Traceback (most recent call last)
<ipython-input-4-45e6ee0b6740> in <module>
----> 1 type({1,2, [1,2]})

TypeError: unhashable type: 'list'
```

冰冻集合创建

```python
In [6]: frozenset({1, 2,3 ,4 })
Out[6]: frozenset({1, 2, 3, 4})
```

# 2. 常见操作

## 2.1 增删改

### 2.1.1 增改

#### > add

在集合尾部增加一个元素

```python
def add(self, element):
return None
```

* element: `object`, 集合需要增加的元素

示例

```python
>>> a_set = {1, 2, 3}
>>> a_set.add((1, 3))
```

#### > copy

集合的浅copy, 类似dict/tuple等浅copy操作

### 2.1.2 删除

#### > remove

从左边开始查找到指定元素后, 删除改元素, 如果没有找到该元素会抛出`KeyError`异常

```python
def remove(self, element):
return None
```

* element: `object`, 集合中的元素

示例

```python
>>> a_set = {1, 2, 3}
>>> a_set.remove(2)
>>> a_set.remove(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 2
```

#### > discard

从左边开始查找到指定元素后, 删除改元素, 如果没有找到该元素不会抛出异常

```python
def discard(self, element):
return None
```

* element: `object`, 集合中的元素

示例

```python
In [7]: a_set = {1, 2, 3}
In [8]: a_set.discard(2)
In [9]: a_set.discard(2)
```

#### > pop

随机删除一个元素, 并把元素返回. 如果集合为空则抛出异常 

```python
def pop(self):
return object
```

示例

```python
In [14]: a_set = {1, 2, 3}
In [15]: a_set.pop()
Out[15]: 1
```

#### > clear

直接清空集合

```python
def clear(self):
return None
```

示例

```python
In [18]: a_set = {1, 2, 3}
In [19]: a_set.clear()

In [20]: a_set
Out[20]: set()
```

## 2.2 数学操作

### 2.2.1 交集

#### > intersection

获取两个集合的交集, 并返回

```Python
def intersection(self, s):
return set
```

* s: `set`, 需要求交集的集合

示例

```python
In [25]: a_set = {1, 2, 3}
In [26]: b_set = {2, 3, "b"}

In [27]: a_set & b_set
Out[27]: {2, 3}

In [29]: a_set.intersection(b_set)
Out[29]: {2, 3}
```

#### > intersection_update

获取两个集合的交集, 并赋值给第一个集合

```python
def intersection_update(self, s):
return None
```

* s: `set`, 需要求交集的集合

示例

```python
In [25]: a_set = {1, 2, 3}
In [26]: b_set = {2, 3, "b"}
    
In [30]: a_set.intersection_update(b_set)

In [31]: a_set
Out[31]: {2, 3}
```

#### > &

获取两个集合的交集, 并返回. 等同于`intersection`

### 2.2.2 并集

#### > union

求两个集合的并集, 并返回.

```python
def union(self, s):
return set
```

* s: `set`, 需要操作的集合

示例

```python
In [32]: a_set = {1, 2, 3}
In [33]: b_set = {2, 3, "b"}

In [34]: a_set | b_set
Out[34]: {1, 2, 3, 'b'}

In [35]: a_set.union(b_set)
Out[35]: {1, 2, 3, 'b'}

In [36]: a_set.update(b_set)

In [37]: a_set
Out[37]: {1, 2, 3, 'b'}
```

#### > update

类似`union`, 但是是在原集合上进行操作, 不返回结果

#### > |

等同于`union`



### 2.2.3 补集

#### > symmetric_difference

获取两个集合的补集, 并返回.

```python
def symmetric_difference(self, s):
return set
```

* s: `set`, 需要操作的集合

示例

```python
In [38]: a_set = {1, 2, 3}
In [39]: b_set = {2, 3, "b"}

In [40]: a_set ^ b_set
Out[40]: {1, 'b'}

In [41]: a_set.symmetric_difference(b_set)
Out[41]: {1, 'b'}

In [42]: a_set.symmetric_difference_update(b_set)

In [43]: a_set
Out[43]: {1, 'b'}
```

#### > symmetric_difference_update

类似`symmetric_difference`, 不同之处在于在原集合上进行操作, 不返回任何信息.

#### > ^

等同于`symmetric_difference`

### 2.2.4 差集

#### > difference

获取两个集合的差集, 并返回

```python
def difference(self, s):
return set
```

* s: `set`, 需要操作的集合

示例

```python
In [44]: a_set = {1, 2, 3}
In [45]: b_set = {2, 3, "b"}

In [46]: a_set-b_set
Out[46]: {1}

In [47]: a_set.difference(b_set)
Out[47]: {1}

In [48]: a_set.difference_update(b_set)

In [49]: a_set
Out[49]: {1}
```

#### > difference_update

类似`difference`, 不同之处在于, 操作原集合, 不返回任何信息

#### > -

等同于`difference`

### 2.2.5 包含判断

#### > issubset

判断, 原集合是否包含于s集合

```python
def issubset(self, s):
return bool
```

* s: `set`, 需要操作的集合

示例

```python
>>> a_set = {1 , 2, 4}
>>> b_set = {1, 2}
>>> a_set.issubset(b_set)
False
```

#### > issuperset

判断, s集合是否包含于原集合

```python
def issuperset(self, s):
return bool
```

* s: `set`, 需要操作的集合

示例

```python
In [1]: a_set = {1 , 2, 4}                                                                                   
In [2]: b_set = {1, 2}   
    
In [5]: a_set.issuperset(b_set)                                                                             
Out[5]: True
```

#### > isdisjoint

判断, 原集合与s集合中是否有交叉的元素

```python
def isdisjoint(self, s):
return bool
```

* s: `set`, 需要操作的集合

示例

```python
>>> a_set = {1 , 2, 4}
>>> b_set = {1, 2, 5}
>>> a_set.isdisjoint(b_set)
False
>>> c_set = {"a", "b"}
>>> a_set.isdisjoint(c_set)
True
```





