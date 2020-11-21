# 1. 常量属性

## 1.1 系统层面

### 1.1.1 平台类型

#### - platform

当前系统信息. `linux`/`windows`等

#### - byteorder

字节顺序指示符. 大端序为`big`, 小端序为`little`

## 1.2 Python内部

### 1.2.1 版本信息

#### - copyright

Python, 版权信息

#### - hexversion

Python, 解析器的版本值, 十六进制, 如0x020403F0

#### - version

Python, 版本信息

#### - implementation

`namespace`, 内部包含了`cache_tag`, `hexversion`, `name`, `version`等

**示例**

```python
In [2]: sys.implementation                                                                        
Out[2]: namespace(cache_tag='cpython-35', hexversion=50660080, name='cpython', version=sys.version_info(major=3, minor=5, micro=2, releaselevel='final', serial=0))
```

### 1.2.2 解析器内部

#### - maxsize

表示`Py_ssize_t`类型可设置的最大值

#### - maxunicode

表示`unicode`类型码点值最大值

### 1.2.3 交互常量

#### - ps1 

交互模式的符号 `>>>`

#### - ps2        

交互模式符号  ` ...`

# 2. 常量方法

## 2.1 系统层面

### 2.1.1 编码风格

#### > getdefaultencoding

编码格式, 从头部信息或者是当前系统的默认的编码格式

#### > getfilesystemencoding

文件路径编码格式, 从系统中获取

## 2.2 Python内部

### 2.2.1 递归深度

#### > getrecursionlimit

获取, 递归深度最大值.

```python
def getrecursionlimit():
return int
```

#### > setrecursionlimit

设置 递归深度的最大值

```python
def setrecursionlimit(limit):
return None
```

* limit: `int`, 需要设置的最大值

### 2.2.2 线程切换

#### > getswitchinterval

获取, 线程间切换时间. 单位: 秒

```python
def getswitchinterval():
return float
```

#### > setswitchinterval

设置, 线程间切换时间. 单位: 秒

```python
def setswitchinterval(interval):
return None
```

* interval: `float`, 需要设置的时间

# 3. 路径

## 3.1 Python路径

### 3.1.1 路径前缀

#### - base_prefix

Python解析器, 安装Python的目录的前缀, 默认值为`./Configure`中的`--prefix`参数.一般为`/usr/local`下.   不论虚拟环境还是真实环境, `base_exec_prefix`一直指向真实环境的`prefix`.    定值

#### - prefix

Python解析器, Python启动后, 会在执行`site.py`文件时检测当前环境, 如果为虚拟环境, 则`prefix`将会改变为虚拟环境的`prefix`.   变值

#### - base_exec_prefix

Python解析器, 安装的解析器目录的前缀, 默认值为`./Configure`中的`--exec-prefix`参数.一般为`/usr/local`下.   不论虚拟环境还是真实环境, `base_exec_prefix`一直指向真实环境的`exec_prefix`.    定值

#### - exec_prefix

Python解析器, Python启动后, 会在执行`site.py`文件时检测当前环境, 如果为虚拟环境, 则`exec_prefix`将会改变为虚拟环境的`exec_prefix`.    变值

### 3.1.2 Python所在位置

#### - executable

Python解析器, 所在的绝对路径.  

## 3.2 导包路径

#### - path

返回`list`, 当Python加载后, 此参数将会影响`import`和`from xx import xx`将会从哪里选取包及其导包路径的优先级. 

#### - builtin_module_names

返回`list`, 表示Python启动时预加载的模块内容

#### - modules

返回`dict`, 表示Python代码运行时, 所有的存储模块及路径.

# 4. 交互

## 4.1 标准流

### 4.1.1 标准流

#### - stdin

标准输入, 用于所有交互式输入, 包括`input`.

```python
return file-object
```

#### - stdout

标准输出, 用于所有交互式输出, 包括`print()`, `expression`, `input`的提示信息.

```python
return file-object
```

#### - stderr

标准错误输出, 用于所有交互式错误输出, 包括解析器本身异常, 代码异常导致的错误.

```python
return file-object
```

### 4.1.2 钩子

#### > displayhook

输出钩子, 将`value`输出到屏幕, 并存入到`builtins._`中.

```python
def displayhook(value):
return None
```

* value: `str`, 需要输出到屏幕之前的预处理信息.

#### > execpthook

异常钩子, 本函数会将所给的回溯和异常输出到 `sys.stderr` 中。

```python
def execpthook(type, value, traceback):
return None
```

* type: `异常类`, 引发异常的类
* value: `异常示例`, 引发异常的实例对象
* traceback: `回溯对象`, 回溯引发异常的过程对象. 

## 4.2 退出

### 4.2.1 异常

#### > exc_info

获取当前存在的异常三元组.

```python
def exc_info():
return (type, value, traceback)
```

### 4.2.1 退出

#### > exit

引发`SystemError`异常, 来终止程序运行, 一般只能终止当前线程, 想终止进程需要使用`os._exit()`.

```python
def exit(status):
return None
```

* status: `int`, 表示退出程序时的状态. [1-127], 0/正常, 1/其他错误, 2/命令行错误

**示例**

```python
import time
import multiprocessing

def son():
    import os, sys
    print("do stop")
    # os._exit(1)
    sys.exit(1)

def foo():
    import threading
    threading.Thread(target=son).start()
    time.sleep(2)
    print("thread over")


if __name__ == '__main__':
    multiprocessing.Process(target=foo).start()
    time.sleep(5)
    print(22222222222222222)

```

输出

```python
do stop
thread over
22222222222222222
```

#### > is_finalizing

判断, 解析器是否正在关闭.

```python
def is_finalizing():
return bool
```

## 4.3 参数传递

#### - argv

返回一个列表. 表示传递到Python中的所有参数. 

```python
(py35) [appgess@localhost ~]$ python test.py aa bb eee aa ggg
['test.py', 'aa', 'bb', 'eee', 'aa', 'ggg']
(py35) [appgess@localhost ~]$ python -c 'import sys;print(sys.argv)' aab cc ee ff
['-c', 'aab', 'cc', 'ee', 'ff']
(py35) [appgess@localhost ~]$ 
```

#### - \_xoptions

利用`X`向Python内部传递字典类型的参数, 返回一个字典

```python
hpcm@test$: python -Xa=b -Xc test.py
# test.py
import sys
print(sys._xoptions)
print(sys.argv)
```

输出

```python
{'a': 'b', 'c': True}
['test.py']
```

# 5. 内部

## 5.1 资源占用

#### > getsizeof

获取变量, 占用内存量. 单位: 字节

```python
def getsizeof(obj):
return int
```

* obj: `object`, 需要检测的对象

#### > intern

创建出内存地址引用相同的对象. 由此方法创建的`string`会常驻与变量字典中, 利于查找.

```python
def intern(string):
return obj
```

* string: `string`, 需要`copy`的字符串

**示例**

```python
>>> a = sys.intern("this massage is used by intern function")
>>> b = sys.intern("this massage is used by intern function")
>>> c = "this massage is used by intern function"
>>> d = "this massage is used by intern function"
>>> print(a is b)
True
>>> print(c is d)
False
>>> print(a is c)
False
>>>
```

