# 1. Flask

## 1.1 Flask介绍

Python语言, 基于Werkzeug工具箱编写的轻量级Web开发框架.

Werkzeug

Flask本身相当于一个内核, 其他功能都需要外设框架

## 1.2 Flask拓展包

* Flask-SQLAlchemy: 数据库操作
* Flask-script: 脚本操作
* Flask-migrate: 数据库迁移操作
* Flask-Session: Session储存操作
* Flask-WTF: 表单操作
* Flask-Mail: 邮件操作
* Flask-Bable: 国际化和本地支持, 翻译操作
* Flask-Login: 用户登录操作
* Flask-OpenID: 认证操作
* Flask-RESTful: REST API工具
* Flask-Bootstrap: 集成前端Twitter Bootstrap框架
* Flask-Moment: 本地化时间
* Flask-Admin: 拓展管理接口框架



官方文档:

​	中文: http://docs.jinkan.org/docs/flask/

​	英文: http://flask.pocoo.org/docs/0.11/

## 1.3 hello word

flask创建web非常简单, 如下代码即可实现一个简单的web:

http://localhost:5000/

默认端口: 5000

```python
from flask import Flask
from datetime import datetime

# app实例化
app = Flask(__name__)

# view创建
@app.route("/")
def index():
    return "now time is: {}".format(datetime.now()), 200

if __name__ == '__main__':
    # 服务运行
    app.run(host="0.0.0.0", debug=True)
```

# 2. 模块说明

flask是由jinjia2 + Werkzeug组成

Werkzeug:  HTTP通信, 路由, 视图,  本质是遵循WSGI协议的socket的服务器.

jinjia2: WSGI, 模板引擎, 转化复杂的数据成字符串给客户端.

* 常见WSGI模块:

  * wsgiref
  * werkzeug
  * uwsgi

  