# 1. Manger

## 1.1 作用

Python程序开发完成后, 有时需要交给其他人来部署, 为了方便其他人部署. 最好不要让别人去更改内部代码, 所以最佳的方案就是使用命令行的时候, 指定运行参数来更改配置. 即解析命令行参数

```python
import sys

sys.argv
```

在flask-script中已经实现了自动解析的方法可以直接使用.

## 1.2 安装

```python
pip install flask-script
```

## 1.3 helloword

```python
from flask import Flask
from flask_script import Manager
app = Flask(__name__)

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
```

程序被托管运行后, 默认被注入两个参数:

* shell: 使用项目配置打开类似Python的交互环境

  ```python
  python application.py shell
  ```

* runserver: 启动项目

  ```python
  python application.py runserver
  
  -h HOST, --host HOST
  -p PORT, --port PORT
  --threaded
  --processes PROCESSES
  --passthrough-errors
  -d, --debug           enable the Werkzeug debugger (DO NOT use in production
                      code)
  -D, --no-debug        disable the Werkzeug debugger
  -r, --reload          monitor Python files for changes (not 100% safe for
                      production use)
  -R, --no-reload       do not monitor Python files for changes
  --ssl-crt SSL_CRT     Path to ssl certificate
  --ssl-key SSL_KEY     Path to ssl key
  ```

## 1.4 Manager

### 1.4.1 实例

```python
def __init__(
        self,
        app=None,  
        with_default_commands=None,
        usage=None,
        help=None, 
        description=None, 
        disable_argcomplete=False
)
```

* app: flask的实例化app
* with_default_commands: 配置默认的命令, 会自动加载两个命令: runserver, shell
* usage: 命令中的usage. 就是总述命令
* help: 帮助信息
* description: 信息描述
* disable_argcomplete: 是否禁用自动载入args

### 1.4.2 方法

* run

  ```python
  def run(self, commands=None, default_command=None)
  ```

  * commands

    dict, 和add_commad功能相同, 用来增加命令

  * default_command

    str, 让程序以默认参数运行, 如下:

  **实例:**

  ```python
  manager.run(default_command="runserver")
  ```

  即可在使用`python application.py`就可以直接运行服务了

* add_commad

  ```python
  def add_command(self, *args, **kwargs)
  ```

  * args:
    * name: cmd运行的参数
    * command: Command实例对象
  * kwargs:
    * namespace: 上级命令归属

  **实例:**

  ```python
  manager.add_command("sc1", ShellCMD(), namespace="name")
  manager.add_command("sc2", ShellCMD(), namespace="name")
  ```

  执行命令:

  ```python
  (test) E:\project\test\test> python application.py name --help
  positional arguments:
    {sc1,sc2}
      sc1       这里是 --help 中方法解释的地方
      sc2       这里是 --help 中方法解释的地方
  
  optional arguments:
    -?, --help  show this help message and exit
  ```

# 2. 配置运行参数

增加运行参数可以有两种模式 

## 2.1 继承配置

### 2.1.1 类方法

```python
from abc import ABC

from flask import Flask
from flask_script import Manager, Command, Option

class ShellCMD(Command, ABC):
    """这里是 --help 中方法解释的地方"""
    option_list = {
        Option("--name", "-n", dest="name", help="方法帮助 name"),
        Option("--age", "-a", dest="age", help="方法帮助 age")
    }

    def run(self, *args, **kwargs):
        """此方法将会接受cmd中传入的参数, 并在kwargs以关键词参数被传入"""
        print("传入参数为: {}, {}".format(args, kwargs))
        
manager = Manager(app)
manager.add_command("sc", ShellCMD(), namespace="test")

if __name__ == '__main__':
    manager.run()
```

### 2.1.2 实例配置

```python
class Test2(Command, ABC):
    """这里是 test2 --help 中方法解释的地方"""

    def get_options(self):
        return [
            Option("-n", "--name", dest="name", default="默认参数")
        ]

    def run(self, *args, **kwargs):
        """此方法将会接受cmd中传入的参数, 并在kwargs以关键词参数被传入"""
        print("传入参数为: {}, {}".format(args, kwargs))
```



## 2.2 装饰器配置

### 2.2.1 command

```python
@manager.command
def cmd1(name, age=None):
    """这是 --help 可以查询的地方"""
    print("传入参数为: {}, {}".format(name, age))
```

**说明:**

* 命令名

  cmd1, 即函数名称

* 命令的参数

  name, [age]. 即函数的参数, 位置参数为必填参数, 关键字参数为可选参数

命令调用:

```python
(test) E:\project\test\test> python application.py cmd1 --help
positional arguments:
  name

optional arguments:
  -?, --help         show this help message and exit
  -a AGE, --age AGE
```



### 2.2.2 option

```python
@manager.option("-n", "--name", help="这里是用help查到信息", dest="name", default="aa")
@manager.option("-a", "--age", help="这里是用help查到信息", dest="age")
def cmd2(*args, **kwargs):
    """这是 --help 可以查询的地方"""
    print("传入参数为: {}, {}".format(args, kwargs))
```

**说明:**

* 命令名

  cmd2, 即函数名称

* 命令的参数

  [name], [age]. 用此方法装饰的命令参数均为缺省参数 

# 3. 测试代码

```python
import os
import sys
from abc import ABC

from flask import Flask
from flask_script import Manager, Command, Option

base_dir = os.path.abspath(sys.path[0])
sys.path.insert(0, os.path.join(base_dir, "apps"))
sys.path.insert(0, base_dir)


app = Flask(__name__)
manager = Manager(app)


class Test1(Command, ABC):
    """这里是 test1 --help 中方法解释的地方"""
    option_list = {
        Option("--name", "-n", dest="name", help="方法帮助 name"),
        Option("--age", "-a", dest="age", help="方法帮助 age")
    }

    def run(self, *args, **kwargs):
        """此方法将会接受cmd中传入的参数, 并在kwargs以关键词参数被传入"""
        print("传入参数为: {}, {}".format(args, kwargs))


class Test2(Command, ABC):
    """这里是 test2 --help 中方法解释的地方"""

    def get_options(self):
        return [
            Option("-n", "--name", dest="name", default="你猜")
        ]

    def run(self, *args, **kwargs):
        """此方法将会接受cmd中传入的参数, 并在kwargs以关键词参数被传入"""
        print("传入参数为: {}, {}".format(args, kwargs))



@manager.command
def cmd1(name, age=None):
    """这是 --help 可以查询的地方"""
    print("传入参数为: {}, {}".format(name, age))


@manager.option("-n", "--name", help="这里是用help查到信息", dest="name", default="aa")
@manager.option("-a", "--age", help="这里是用help查到信息", dest="age")
def cmd2(*args, **kwargs):
    """这是 --help 可以查询的地方"""
    print("传入参数为: {}, {}".format(args, kwargs))


manager.add_command("sc1", Test1(), namespace="test")
manager.add_command("sc2", Test2(), namespace="test")

if __name__ == '__main__':
    manager.run(default_command="runserver")
```



