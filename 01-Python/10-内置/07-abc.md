# 1. abc

本模块主要用于抽象类的创建

* 检查某个类是否存在某种方法
* 强制让子类必须实现某种方法
* 重写isinstance和issubclass所识别的魔法方法

## 1.1 抽象类

### < ABC

```python
# ABC register 让子类抽象继承父类, 但是不能调用父类方法
class Demo3(ABC):
    ...

class Demo5:
    pass

Demo3.register(Demo5)

print(isinstance(Demo5(), Demo3))  # 只是抽象为其子类, 不能调用父类的方法
print(issubclass(Demo5, Demo3))
# 输出**************************************
True
True


from abc import *

class Demo3(ABC):

    @classmethod
    def __subclasscheck__(cls, subclass):
        if cls is Demo3:
            if any("__getitem__" in p.__dict__ for p in subclass.__mro__):
                return True
            else:
                return False

class Demo5:
    def __getitem__(self, item):
        ...
    
Demo3.register(Demo5)
print(isinstance(Demo5(), Demo3))
print(issubclass(Demo5, Demo3))
# 输出**************************************
True
True
```

### < ABCMeta

```python
class Demo1(metaclass=ABCMeta):
    ...

class Demo2(Demo1):
    ...

class Demo4:
    pass

Demo2.register(Demo4)

print(isinstance(Demo4(), Demo2))  # 只是抽象为其子类, 不能调用父类的方法
print(issubclass(Demo4, Demo2))
# 输出**************************************
True
True
```

## 1.2 抽象方法

#### > abstractmethod

```python
import abc
class Demo(metaclass=abc.MetaClass):
    @abc.abstractmethod
    def get(self):
        pass
    
class Test(Demo):
    pass

Test()   # TypeError: Can't instantiate abstract class Test with abstract methods get
```

**自己实现一**

```python
method_list = []
def func1(fun):
    method_list.append(fun.__name__)
    def func2(*args, **kwargs):
        return fun(*args, **kwargs)
    return func2

class Demo(type):
    def __new__(mcs, *args, **kwargs):
        for name in filter(lambda x: x not in args[2], method_list):
            raise TypeError("Can't instantiate abstract class {} with abstract methods {}".format(args, name))
        return super().__new__(mcs, *args, **kwargs)

    @func1
    def get(self):
        pass

class Test(metaclass=Demo):
    pass

# 运行直接报错
```

**自己实现二**

```python
# 需要调用才能触发
class Demo(object):
    def get(self):
        raise AttributeError("Must set methods get!")

class Test(Demo):
    pass

t = Test()
t.get()    # AttributeError: Must set methods get!
```



