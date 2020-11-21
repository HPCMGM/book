# 1. 路径异常

## 1.1 import导入失败

### 1.1.1 错误场景

* main.py

  ```python
  import a
  ```

* a.py

  ```python
  import b
  ```

打包语法:

```python
pyinstaller -F main.py
```

打包完成后, 运行报错

```python
ModuleNotFoundError: No module named 'b'
```

### 1.1.2 解决方案

在入口文件中, 提前导入全部需要用到的包, 防止打包时未打入.

```python
# main.py
import a
import b
```

## 1.2 BASE_DIR偏移

### 1.2.1 错误场景

项目代码使用`BASE_DIR`作为根路径, 后期其他模块循环引用此参数来进行操作.

例如`Django`中`BASE_DIR = os.path.dirname(os.path.abspath(__file__))`

此时对项目进行打包时:

```python
pyinstaller -F manager.py
```

直接运行程序, 将会把路径偏移至, 临时路径, 导致所有的绝对路径不可用, 错误示例

```python
OSError: [Errno 2] No such file or directory: '/tmp/_MEJIOSNzGe/test.txt'
[100180] Failed to execute script run
```

### 1.2.2 解决方案

使用`sys.argv[0]`来代替`__file__`即

```python
BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
```

## 1.3 hook异常

### 1.3.1 场景描述

当前系统中存在多个虚拟环境, `pyinstaller`安装在默认环境中, 在虚拟环境中使用`pyinstaller`打包程序, 在可执行软件运行时会爆找不到模块的错误 

### 1.3.2 解决方案

在`pyinstaller`打包时要注意输出的日志中是否所有导入的模块的`hook`都存在, 如果不存在, 可能是当前环境引发的问题

