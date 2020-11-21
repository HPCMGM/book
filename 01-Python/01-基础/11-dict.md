# 1. dict

## 1.1 简介

1. "映射", "哈希","散列", "关系数组"都指字典
2. dict: {key: value} key是唯一的

注意: 官方说明Python>=3.7, dict会记录key的插入的顺序

## 1.2 定义

```python
In [10]: a_dict = {"a": 1, "b": 2}

In [11]: b_dict = dict(a=1, b=2)

In [12]: c_dict = dict([("a", 1), ("b", 2)])

In [13]: print(a_dict, b_dict, c_dict)
{'a': 1, 'b': 2} {'a': 1, 'b': 2} {'a': 1, 'b': 2}
```

## 1.3 应用场景

* 函数

  ```python
  In [1]: def foo(**kwargs):
     ...:     print(type(kwargs))
     ...:     print(kwargs)
     ...:
  
  In [2]: foo(a=2, b=3)
  <class 'dict'>
  {'a': 2, 'b': 3}
  ```

  

* 占位符

  ```python
  In [4]: a_dict = {
     ...: "a": 1,
     ...: "b": 2}
  
  In [5]: print("a is %(a)s" % a_dict)
  a is 1
  ```

  

# 2. 常用方法

## 2.1 切片

#### > 修改或增加

如果原字典中不存在, 则增加, 否则覆盖

```python
In [69]: a_dict = {"a": 1, "b": 2}
In [70]: a_dict["a"]=3

In [71]: a_dict
Out[71]: {'a': 3, 'b': 2}
```

#### > 删除

key不存在, 则会抛出异常

```python
In [17]: d_dict = {1: 2, 2: 3, 3: 4}
In [18]: del d_dict[1]

In [19]: d_dict
Out[19]: {2: 3, 3: 4}
```

#### > 取值

key不存在, 则会抛出异常

```python
In [14]: a_dict = {"a": 1, "b": 2}

In [15]: a_dict["a"]
Out[15]: 1
```



## 2.2 增改

#### > setdefault

增加k,v键值对, 如果存在, 不进行任何操作, 如果不存在, 则增加此键值对

```python
def setdefault(self, k, default):
return None
```

* k: `key`, 字典的key
* default: `obj`, 字典的value

示例

```python
>>> d_dict = {"a": 1, "b": 2}
>>> d_dict.setdefault("b", 3)
2
>>> d_dict.setdefault("e", 4)
4
>>> d_dict
{'b': 2, 'e': 4, 'a': 1}
```

#### > update

更新字典, 如果存在则覆盖.

```python
def update(self, kwargs):
return None
```

* kwargs: `dict`/`items`, 字典或者可转化为字典的可迭代对象

示例

```python
In [81]: a_dict = {"a": 1, "b": 2}
In [82]: b_dict = {"b": "33", "c": 1}
In [83]: a_dict.update(b_dict)

In [84]: a_dict
Out[84]: {'a': 1, 'b': '33', 'c': 1}
```

#### > fromkeys

增加一个拥有相同的`value`的字典

```python
def fromkeys(self, iterable, value):
return dict
```

* iterable: `iterable`, 字典的keys, 可迭代对象
* value: `object`, 新字典的value

示例

```python
>>> dict.fromkeys(("a", "b"), "1")
{'b': '1', 'a': '1'}
```

#### > copy

字典的浅copy

```python
def copy(self):
return dict
```

示例

```python
In [31]: {1:2, 3:4}.copy()                                                                                   
Out[31]: {1: 2, 3: 4}
```

## 2.3 删除

#### > pop

指定删除一个键值对.

```python
def pop(self, key, default=None):
return value
```

* key: `key`, 需要删除元素的key
* default: `value`, 如果不存在, 则使用default参数来代替, 防止引发异常

示例

```python
>>> d_dict = {"a": 1, "b": 2}
>>> d_dict.pop("a", 2)
1
>>> d_dict.pop("a", 2)
2
>>> d_dict.pop("a")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'a'
```

#### > popitem

随机删除一个键值对. Python3.7以后版本, 只会删除最后一次添加的键值对

```python
def popitem(self):
return tuple
```

示例

```python
>>> d_dict = {"a": 1, "b": 2}
>>> d_dict.popitem()
('b', 2)
>>> d_dict.popitem()
('a', 1)
>>> d_dict.popitem()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'popitem(): dictionary is empty'
```

#### > clear

清空字典

```python
def clear(self):
return None
```

示例

```python
>>> d_dict = {"a": 1, "b": 2}
>>> d_dict.popitem()
('b', 2)
>>> d_dict.popitem()
('a', 1)
>>> d_dict.popitem()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'popitem(): dictionary is empty'
```

## 2.4 查看

#### > keys

获取字典的全部keys

```python
def keys(self):
return dict_keys
```

示例

```python
In [71]: a_dict
Out[71]: {'a': 3, 'b': 2}

In [72]: a_dict.keys()
Out[72]: dict_keys(['a', 'b'])
```

#### > values

获取字典的全部values

```python
def values(self):
return dict_values
```

示例

```python
In [71]: a_dict
Out[71]: {'a': 3, 'b': 2}

In [73]: a_dict.values()
Out[73]: dict_values([3, 2])
```



#### > items

获取字典的全部k,v键值对

```python
def items(self):
return dict_items
```

示例

```python
In [71]: a_dict
Out[71]: {'a': 3, 'b': 2}

In [74]: a_dict.items()
Out[74]: dict_items([('a', 3), ('b', 2)])
```



#### > get

获取指定key的value值

```python
def get(self, key, default=None):
return value
```

* get: `key`, 需要获取字典的key
* default: `obj`, 如果key不存在, 则使用default作为value返回

示例

```python
In [78]: a_dict = {"a": 1, "b": 2}
In [79]: a_dict.get("a")
Out[79]: 1

In [80]: a_dict.get("c", 222)
Out[80]: 222
```

