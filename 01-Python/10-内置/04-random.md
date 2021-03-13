# 1. random

## 1.1 单个

### 1.1.1 整形

#### > randrange()

从一个`range`中随机选取一个整数. 

```Python
def randrange(self, start, stop=None, step=1, _int=int):
	return int
```

* start: int, `range`中的起始值
* stop: int/None, `range`中的终止值
* step: int, `range`中的步长
* _int: function, 用于处理`start`/`stop`/`step`强制类型转换为整形 , 但是如果不是`int`类型, 会抛出`ValueError`异常

#### > randint()

左闭右闭区间中选取一个整数. 事实上`randint`是通过`randrange`实现的. 源码如下:

```Python
def randint(self, a, b):
	return self.randrange(a, b+1)
```

* a: int, 整数区间的起始值
* b: int, 整数区间的结束值. b必须大于a



### 1.1.2 小数

#### > random()

随机返回一个`[0.0, 1.0)`一个浮点数

```Python
def random(self)
	return float
```

#### > uniform()

随机选取一个区间中的一个小数.  实际上是利用`random()`实现的, 源码如下:

```Python
def uniform(self, a, b):
	return a + (b - a) * self.random()
```

* a: float/int, 起始位置
* b: float/int, 终止位置, 支持`a > b`和`a < b`

### 1.1.3 可迭代对象

#### > choice()

随机从一个**非空**队列中返回一个随机元素. 不得为空, 否则引发`IndexError`

```Python
def choice(self, seq):
    return obj
```

* seq: 支持切片的可迭代对象. 

## 1.2 批量

### 1.2.1 概率性

从序列中随机挑选指定数量的元素

#### > sample()

```Python
def sample(self, population, k):
	return list
```

* population: list/tuple/set, 需要选取的集合
* k: int, 选取的个数

可以用此函数打乱一个不可变序列

```Python
import random

a = (1, 2, 3, 4)
print(random.sample(a, k=len(a)))
```

输出

```Python
[2, 3, 1, 4]
```

#### > choices()

按照权重挑选一定数量的元素

```Python
def choices(self, population, weights=None, *, cum_weights=None, k=1):
    return list
```

* population: list/tuple/set, 需要挑选的序列
* weights: list/None, 为每个元素指定权重. `len(weights) == len(population)`必须成立
* cum_weights:  list/None. 累积权重. 如果`cum_weights`为`[10, 5, 30, 5]`, 那么就相当于`weights`为`[10, 15, 45, 50]`
* k: int, 选取的个数

示例

```Python
import random
random.choices(iter, weights, k)

l = [1, 2, 4, 5]
weight = [0.5, 0.6, 0.7, 0.8]
k = 3
print(random.choices(l, weight, cum_weights=None, k=3))
```

输出

```Python
[1, 4, 4]
```

## 2. 原序列操作

### 2.1 随机打乱

#### > shuffle()

在原来序列中进行打乱操作.

```Python
def shuffle(self, x, random=None):
    return None
```

* x: list/set, 需要打乱的序列
* random: func, 默认取得是`random.random()`, 即`[0, 1)`的随机数.

示例

```Python
import random
from functools import partial
a = [1, 2, 3, 4]
func = partial(random.uniform, 0, 1)
random.shuffle(a, func)
print(a)
```

输出

```Python
[4, 3, 1, 2]
```





