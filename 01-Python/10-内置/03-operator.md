# 1. 运算法则

| 运算               | 句法                | 功能                                |
| ------------------ | ------------------- | ----------------------------------- |
| 加法               | `a + b`             | `add(a, b)`                         |
| 列表拼接           | `seq1 + seq2`       | `concat(seq1, seq2)`                |
| 同种可迭代对象拼接 | a +b                | iadd(a, b)                          |
| 是否包含           | `obj in seq`        | `contains(seq, obj)`                |
| 除法               | `a / b`             | `truediv(a, b)`                     |
| 整除               | `a // b`            | `floordiv(a, b)`                    |
| 按位和             | `a & b`             | `and_(a, b)`                        |
| 按位排他或         | `a ^ b`             | `xor(a, b)`                         |
| 按位反转           | `~ a`               | `invert(a)`                         |
| 按位或             | `a | b`             | `or_(a, b)`                         |
| 幂                 | `a ** b`            | `pow(a, b)`                         |
| 内存地址           | `a is b`            | `is_(a, b)`                         |
| 内存地址           | `a is not b`        | `is_not(a, b)`                      |
| 索引分配           | `obj[k] = v`        | `setitem(obj, k, v)`                |
| 索引删除           | `del obj[k]`        | `delitem(obj, k)`                   |
| 索引               | `obj[k]`            | `getitem(obj, k)`                   |
| 左移               | `a << b`            | `lshift(a, b)`                      |
| 取余               | `a % b`             | `mod(a, b)`                         |
| 乘法               | `a * b`             | `mul(a, b)`                         |
| 矩阵乘法           | `a @ b`             | `matmul(a, b)`                      |
| 相反数             | `- a`               | `neg(a)`                            |
| 否定（逻辑）       | `not a`             | `not_(a)`                           |
| 正                 | `+ a`               | `pos(a)`                            |
| 右转               | `a >> b`            | `rshift(a, b)`                      |
| 切片分配           | `seq[i:j] = values` | `setitem(seq, slice(i, j), values)` |
| 切片删除           | `del seq[i:j]`      | `delitem(seq, slice(i, j))`         |
| 切片               | `seq[i:j]`          | `getitem(seq, slice(i, j))`         |
| 字符串格式         | `s % obj`           | `mod(s, obj)`                       |
| 减法               | `a - b`             | `sub(a, b)`                         |
| bool方法调用       | `obj`               | `truth(obj)`                        |
| 比较               | `a < b`             | `lt(a, b)`                          |
| 比较               | `a <= b`            | `le(a, b)`                          |
| 比较               | `a == b`            | `eq(a, b)`                          |
| 比较               | `a != b`            | `ne(a, b)`                          |
| 比较               | `a >= b`            | `ge(a, b)`                          |
| 比较               | `a > b`             | `gt(a, b)`                          |
| 绝对值             | `abs(a, b)`         | `abs(a, b)`                         |
| 累积叠加           | `+=, *=, /=.....`   | `isub, imod....`                    |

# 2. operator

## 2.1 动态获取

### 2.1.1 属性方法

#### > attrgetter

批量获取属性或方法

```python
def attrgetter(*attrs):
return list/one
```

* `attrs`: `str`, 需要获取的方法, 支持多个和单个, 单个返回单个的属性和方法, 多个返回`list`

**示例**

```python
class Demo:
    def __init__(self):
        self.a = "a"
        self.b = "c"


class Test:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = Demo()

    def pt(self, a, b):
        print("do something", a, b)
        return self.a, self.b

# attrgetter批量获取对象属性
t = Test()
f = operator.attrgetter("c.a", "b", "a", "c.b", "pt")
print(f(t))
```

输出

```python
('a', 2, 1, 'c', <bound method Test.pt of <__main__.Test object at 0x000001F5B763FB00>>)
```

#### > methodcaller

直接获取并执行函数

```python
def methodcaller(name, /, *args, **kwargs):
return function_value
```

* args: `*args`, 不定长参数, 为函数的参数值
* kwargs: `**kwargs`, 不定长参数, 为函数的参数值

**示例**

```python
t = Test()
f = operator.methodcaller("pt", 3, 4)
print(f(t))
```

输出

```python
do something 3 4
(1, 2)
```

### 2.1.2 索引键值

#### > itemgetter

批量获取索引值对应的值

```python
def itemgetter(*items):
return one/list
```

* items: `index/key`,如果动态获取的为`list`, 则`items`为索引, 如果为`dict`, 则`items`为`key` . 支持单个或者多个

**示例**

```python
t_list = [1, 2, 3, 4, 5]
f = operator.itemgetter(1, 2, 3, 4)
print(f(t_list))
t_dict = {"a": 2, "b": 1, "e": 3}
print(operator.itemgetter("b")(t_dict))
print(sorted(t_dict.items(), key=operator.itemgetter(1)))
```

输出

```python
(2, 3, 4, 5)
1
[('b', 1), ('a', 2), ('e', 3)]
```

