# 1. Blueprint

## 1.1 说明

大型项目中, 需要多人配合开发, 每个人只能承包一部分内容, 所以需要分多个文件. 为了防止app实例化的模块, 不能重复导入, 使用蓝图注册可以防止重复实例化app. 

蓝图不能独立存在, 必须注册给app.

## 1.2 `Blueprint`

```python
def __init__(self,
    name,
    import_name,
    static_folder=None,
    static_url_path=None,
    template_folder=None,
    url_prefix=None,
    subdomain=None, 
    url_defaults=None, 
    root_path=None 
)
```

* name: 蓝图名称
* import_name: 蓝图路径, 由于该模块是被导入的, 所以使用\__name__即可
* static_folder: 静态文件夹名称
* static_url_path: 静态文件夹路径
* template_folder: 动态模板文件夹名称
* url_prefix: url路由前缀
* subdomain: 子域名
* url_defaults: url缺省值
* root_path: 读取实例文件

## 1.3 helloworld

```python
from flask import Blueprint, Flask

bp = Blueprint(
    name,                    # 蓝图的名称
    import_name,             # 蓝图路径, 由于该模块是被导入的, 所以使用__name__即可
    static_folder=None,      # 静态文件夹名称
    static_url_path=None,    # 静态文件夹路径
    template_folder=None,    # 动态模板文件夹名称
    url_prefix=None,         # url路由前缀
    subdomain=None,          # 子域名
    url_defaults=None,       # url缺省值
    root_path=None           # 读取实例文件
)

app = Flask(__name__)
app.register_blueprint(bp)
```



# 2. 项目分文件

## 2.1 目录结构

```python
project
├── application.py
└── apps
    └── user
        ├── __init__.py
        └── views.py

```



## 2.2 `__init__.py`

```python
from flask import Blueprint

bp_user = Blueprint("user", __name__, url_prefix="/user")

from .views import *
```

## 2.3 `views.py`

```python
from user import bp_user


@bp_user.route("/")
def index():
    return "sucess!"
```

## 2.4 `application.py`

```python
from flask import Flask

from user import bp_user

app = Flask(__name__)

app.register_blueprint(bp_user)

if __name__ == '__main__':
    print(app.url_map)
    app.run()
```

