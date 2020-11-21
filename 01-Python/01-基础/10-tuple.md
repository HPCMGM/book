# 1. tuple

## 1.1 简介

元组类似列表, 但定义后不可修改, 支持拆包, 组包

```python
In [1]: a, b = 1, 2
In [2]: print(a, b)
1 2

In [3]: a, b = b, a
In [4]: print(a, b)
2 1
```

## 1.2 定义

```python
In [60]: a_tuple = (1, 2, 3)
In [61]: a_tuple
Out[61]: (1, 2, 3)

In [62]: a_tuple = 1, 2 , 3,
In [63]: a_tuple
Out[63]: (1, 2, 3)

In [64]: a_tuple = (1,)
In [65]: a_tuple
Out[65]: (1,)
```

## 1.3 场景运用

* 函数中的组包, 拆包

  ```python
  def foo(*args):  # *args就是利用元组的组包
      return 1, 2   # 返回值1, 2利用元组组包自动形成(1, 2)返回
  foo(*(1, 2, 4))  # *(1, 2, 4)就是利用元组的拆包
  ```

* 变量交换

  ```python
  In [1]: a, b = 1, 2
  In [2]: print(a, b)
  1 2
  
  In [3]: a, b = b, a
  In [4]: print(a, b)
  2 1
  ```

* 占位符拆包

  ```python
  In [7]: price = 8
  In [8]: weight = 5
  In [9]: a_tuple = (price, weight)
  
  In [10]: print("price: %s, weight: %s" % a_tuple)
  price: 8, weight: 5
  ```

# 2. 常见操作

元组的操作和list类似, 只不过设置修改原数据的方法不可用.

## 2.1 查询

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
In [18]: a_tuple = [1, 2, 1]
In [19]: a_tuple.index(1)
Out[19]: 0
```

#### > count

统计某个元素在元组中存在的个数

```python
def count(self, x):
return int
```

* x: `obj`, 需要统计的元素

示例

```python
In [29]: a_tuple = (1, 2, 1, 3, 1, 1)
In [31]: a_tuple.count(1)
Out[31]: 4
```

## 2.2 其他操作

支持索引取值, 支持`+`, 但是不支持`+=`

## 2.3 特殊操作

元组虽然是不可变类型, 但是元组内的可变类型还是可以改变的

```python
In [66]: a_tuple = (1, [1, 2])
In [67]: a_tuple[1].append(3)

In [68]: a_tuple
Out[68]: (1, [1, 2, 3])
```



