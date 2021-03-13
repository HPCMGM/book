# 1. pickle

模块 pickle 实现了对一个 Python 对象结构的二进制序列化和反序列化。

## 1.1 序列化

### 1.1.1 序列化

#### > dumps

序列化, 并输出`bytes`类型.

```python
def dumps(obj, protocol=None, fix_imports=True):
return bytes
```

* obj: `object`, Python基本对象, 用于序列化操作
* protocol: `int`, 序列化版本, 负数表示最高版本, 目前用3
* fix_imports: `bool`, 设置为`True`且`protocol<3`时, 则使用`Python2`中的`dumps`

**示例**

```python
import pickle
class Test(object):
    def __init__(self):
        self.a = "ww"
        self.b = [1, 2]

t1 = Test()
t1.c = Test()

str_byte = pickle.dumps(t1)
d = pickle.loads(str_byte)
print(d.c)
```

输出

```python
b'\x80\x03c__main__\nTest\nq\x00)\x81q\x01}q\x02(X\x01\x00\x00\x00cq\x03h\x00)\x81q\x04}q\x05(X\x01\x00\x00\x00bq\x06]q\x07(K\x01K\x02eX\x01\x00\x00\x00aq\x08X\x02\x00\x00\x00wwq\tubh\x06]q\n(K\x01K\x02eh\x08h\tub.'
ww
```

#### > dump

序列化, 并输出到文件中保存.

```python
def dump(obj, file, protocol=None, fix_imports=True):
return None
```

* obj: `object`, Python基本对象, 用于序列化操作
* file: `file-object`, 文件流对象, 即`open("test.txt", "wb+")`即可.
* protocol: `int`, 序列化版本, 负数表示最高版本, 目前用3
* fix_imports: `bool`, 设置为`True`且`protocol<3`时, 则使用`Python2`中的`dump`

### 1.1.2 反序列化

#### > loads

反序列化, 将`bytes`转化为Python数据类型.

```python
def loads(s, fix_imports=True, encoding="ASCII", errors="strict"):
return object
```

* s: `bytes`, 由`dumps`产生的二进制流.
* fix_imports: `bool`, 设置为`True`且`protocol<3`时, 则使用`Python2`中的`loads`
* encoding: `str`,  编码方式
* errors: `int`, 如果编码错误后, 则进行的处理方案

#### > load

反序列化, 将文件保存的数据转化为Python数据类型

```python
def load(file, fix_imports=True, encoding="ASCII", errors="strict"):
return object
```

* file: `file-object`, 文件流对象, 即`open("test.txt", "rb")`即可.
* fix_imports: `bool`, 设置为`True`且`protocol<3`时, 则使用`Python2`中的`loads`
* encoding: `str`,  编码方式
* errors: `int`, 如果编码错误后, 则进行的处理方案

### 1.1.3 常量

#### - HIGHEST_PROTOCOL

最高版本

#### - DEFAULT_PROTOCOL

默认版本, python3当前为3

## 1.2 序列化原理

```python
class Test1:
    def __init__(self):
        self.d = 2

    def pt(self):
        print("test massage")
        return 2

    def __setstate__(self, state):
        """反序列化调用"""
        for k, v in state.items():
            setattr(self, k, v)
        return self

    def __getstate__(self):
        """序列化调用"""
        return self.__dict__


class Test:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.e = Test1().pt

    def __setstate__(self, state):
        for k, v in state.items():
            print(k, v)
            setattr(self, k, v)
        return self

    def __getstate__(self):
        return self.__dict__


b = pickle.dumps(Test())
print(b)
a = pickle.loads(b)
print(a.e())
```

