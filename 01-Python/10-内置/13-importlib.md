# 1. importlib

本模块主要用于导入各种包

#### > import_module

动态导入模块

```python
def import_module(name, package):
return module
```

* name: `str`, 模块名称, 不能是变量
* package: `str`, 需要到入的包, 路径分隔符用`.`隔开

**示例**

```python
test = importlib.import_module("test", "test.t_importlib")
a = getattr("a", test, None)
```

#### > reload

模块重载, 热更新

```python
def reload(module):
return module
```

* module: `Python_param`, 需要重载的模块变量, 不能为字符串

#### > invalidate_caches

```python
import os, sys, shutil

if os.path.exists('tempdir'):
    shutil.rmtree('tempdir')
os.mkdir('tempdir')
sys.path.append('tempdir')
with open('tempdir/tempmod1.py', 'w') as f:
    ...
import tempmod1
print(tempmod1)
import importlib
importlib.invalidate_caches()  # 刷新路径
# import time
# time.sleep(0.05)             # 延迟
with open('tempdir/tempmod2.py', 'w') as f:
    ...
import tempmod2
print(tempmod2)

# 结论:
动态创建的模块, 加载过后的路径需要刷新缓存, 或者延迟一段时间才能重新识别该路径中的模块, 具体时间取决于系统
```

