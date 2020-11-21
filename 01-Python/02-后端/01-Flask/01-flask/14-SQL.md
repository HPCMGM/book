# 1. flask-sqlalchemy

将数据库中的关系和数据映射成Python对象

* 优点
  * 面向对象编程, 不需要面向数据库编写sql语句
  * 数据模型与数据库的解耦, 屏蔽了不同数据库操作上的差异
* 缺点
  * 相比较直接使用SQL语句操作数据库,有性能损失
  * 对象的操作转换成SQL语句,根据查询的结果转化成对象, 在映射过程中有性能损失.

## 1.1 安装

中文文档链接: http://docs.jinkan.org/docs/flask-sqlalchemy

```python
pip install flask-sqlalchemy
```

如果连接mysql, 还需要下载

```python
pip install flask-mysqldb
pip install pymysql
```

数据迁移管理

```python
pip install flask-migrate
```

**注意**:

在模型创建前一定要先声明使用的引擎, 否则会出现异常:

```python
from pymysql import install_as_MySQLdb
install_as_MySQLdb()
```

## 1.2 helloword

```python
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    # 全局配置
    SECRET_KEY = "hello_world"
    DEBUG = True
    # mysql配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:dong10@localhost:3306/db_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

    SERVER_NAME = "0.0.0.0:8000"


app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class User(db.Model):
    __talbe__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return 'User:'.format(self.username)
    
@app.route("/select")
def select():
    """查询"""
    return User.query()

manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
```

## 1.3 数据库迁移

### 1.3.1 作用

* 开发中直接修改模型, 需要同步到sql数据库. 最直接的是直接在数据库中修改, 但是会导致数据丢失
* 使用框架迁移可以保证数据追踪, 回滚等操作
* flask-migrate自带cmd管理工具, 可以直接附加在flask-script上执行

### 1.3.2 命令操作

一般最常用的是前三个.

1. `python application.py db init`

   创建migrations文件夹，所有迁移文件都放在里面, 只需要执行一次即可, 后续更改不用在执行

2. `python application.py db migrate -m "本次改动的版本号"`

   生成本次操作的版本号, 为了以后出错可以回滚操作

3. `python application.py db upgrade`

   将模型操作同步到数据库中.

4. `python application.py db history`

   查看全部历史版本

5. `python application.py db downgrade/upgrade 版本号`

   版本回退操作

## 1.4 配置文件

```python
# 绑定数据库
SQLALCHEMY_DATABASE_URI = "mysql://username:password@ip:port/db_name"
	# mysql+pymysql://username:password@127.0.0.1:3306/test
	# postgresql://scott:tiger@localhost/mydatabase
	# - oracle://scott:tiger@127.0.0.1:1521/sidname
	# sqlite:////absolute/path/to/foo.db
# 绑定多个数据库
SQLALCHEMY_BINDS = {
	"db1": "mysql://username:password@ip:port/db_name",
    "db2": "sqlite:////path/to/appmeta.db"
}
# 是否开启查询语句显示
SQLALCHEMY_ECHO=False
# 是否读取每一句查询语句的具体信息(利用flask_sqlalchemy.get_debug_queries()语句/执行时长等)
SQLALCHEMY_RECORD_QUERIES=False # 测试/debug=True默认自动打开的
# 是否禁用UNICODE编码
SQLALCHEMY_NATIVE_UNICODE=False
# 数据库连接池, 默认5
SQLALCHEMY_POOL_SIZE=5
# 数据库连接池超时(s), 默认10
SQLALCHEMY_POOL_TIMEOUT=10
# 数据库连接收回(s), Mysql默认2小时, 其他8小时
SQLALCHEMY_POOL_RECYCLE=2 * 60 * 60
# 超出连接池最大值可创建的额外连接数, 使用后将会被抛弃
SQLALCHEMY_MAX_OVERFLOW
# 是否关闭信号追踪:
	# https://blog.csdn.net/weixin_42225318/article/details/80984198
	注: flask提供了信号追踪的接口(flask.signals最后几行), 需要先安装pip install blinker
    用途: 
        1. 检测各种请求钩子的调用, 并返回调用对象处理结果
        2. sqlalchemy对信号支持, 检测数据库的增删改操作, 并返回操作对象和list[(操作对象, "insert/delete/update")]
        3. 关闭可以提高服务器性能
        4. 对两个装饰函数有用:
            before_models_committed/models_committed
SQLALCHEMY_TRACK_MODIFICATIONS=False
```

# 2. 字段

## 2.1 字段

| 类型名       | python中类型      | 说明                                                |
| :----------- | :---------------- | :-------------------------------------------------- |
| Integer      | int               | 普通整数，一般是32位                                |
| SmallInteger | int               | 取值范围小的整数，一般是16位                        |
| BigInteger   | int或long         | 不限制精度的整数                                    |
| Float        | float             | 浮点数                                              |
| Numeric      | decimal.Decimal   | 普通整数，一般是32位                                |
| String       | str               | 变长字符串                                          |
| Text         | str               | 变长字符串，对较长或不限长度的字符串做了优化        |
| Unicode      | unicode           | 变长Unicode字符串                                   |
| UnicodeText  | unicode           | 变长Unicode字符串，对较长或不限长度的字符串做了优化 |
| Boolean      | bool              | 布尔值                                              |
| Date         | datetime.date     | 时间                                                |
| Time         | datetime.datetime | 日期和时间                                          |
| LargeBinary  | str               | 二进制文件                                          |

## 2.2 字段控制

| 选项名      | 说明                                              |
| :---------- | :------------------------------------------------ |
| primary_key | 如果为True，代表表的主键                          |
| unique      | 如果为True，代表这列不允许出现重复的值            |
| index       | 如果为True，为这列创建索引，提高查询效率          |
| nullable    | 如果为True，允许有空值，如果为False，不允许有空值 |
| default     | 为这列定义默认值                                  |

## 2.3 表间控制

| 选项名         | 说明                                                         |
| :------------- | :----------------------------------------------------------- |
| backref        | 在关系的另一模型中添加反向引用                               |
| primary join   | 明确指定两个模型之间使用的联结条件                           |
| uselist        | 如果为False，不使用列表，而使用标量值                        |
| order_by       | 指定关系中记录的排序方式                                     |
| secondary      | 指定多对多关系中关系表的名字                                 |
| secondary join | 在SQLAlchemy中无法自行决定时，指定多对多关系中的二级联结条件 |

## 2.4 示例

### 2.4.1 一对多

#### 2.4.1.1 模型

```python
class ObjectOne(db.Model):
    """一"""
    __tablename__ = 'obj_one'
    id = db.Column(db.Integer, primary_key=True)
    one_name = db.Column(db.String(64), unique=True, index=True)
    one_to_more = db.relationship("ObjectMore", backref="one_to_more")
    
    
class ObjectMore(db.Model):
    """多"""
    __tablename__ = 'obj_more'
    id = db.Column(db.Integer, primary_key=True)
    more_name = db.Column(db.String(64), unique=True, index=True)
    more_to_one = db.Column(db.Integer, db.ForeignKey('obj_one.id'))
```

#### 2.4.1.2 增删改查

* 增

  ```python
  ********************one************************
  >>> one1 = ObjectOne(one_name="one_1")
  >>> db.session.add(one1)
  >>> db.session.commit()
  >>> one1
  <ObjectOne: one_1>
      
  ********************more************************
  >>> more_1 = ObjectMore(more_name="more_1", more_to_one=one1.id)
  >>> db.session.add_all([more_1])
  >>> db.session.commit()
  >>> more_1
  <ObjectMore: more_1>
  ```

  

* 删

  删除时由于外键约束, 是不能直接删除One的一方, 只能先清理More后才能进行删除

  ```python
  ********************one************************
  obj_one = ObjectOne.query.get(uid)
  ObjectMore.query.filter_by(more_to_one=uid).delete()
  db.session.delete(obj_one)            
  db.session.commit()
  ********************more************************
  obj_more = ObjectMore.query.get(uid)            
  db.session.delete(obj_more)
  db.session.commit()
  ```

  

* 改

  ```python
  >>> obj_one_list = ObjectOne.query.filter_by(one_name="one_1")
  >>> obj_one_list[0].one_name="one_edit_1"
  >>> db.session.commit()
  >>> ObjectOne.query.filter_by(one_name="one_1")[0]
  <ObjectOne: one_edit_1>
  ```

  

* 查

  ```python
  ********************one to more************************
  >>> oo = ObjectOne.query.get(uid)
  >>> oo.one_to_more
  [<ObjectMore: more_3>]
  >>> oo.one_to_more[0].more_name
  'more_3'
  ********************more to one************************
  >>> om = ObjectMore.query.get(uid)
  >>> om.one_to_more
  <ObjectOne: one_2>
  >>> om.one_to_more.one_name
  'one_2
  ```

#### 2.4.1.3 示例代码

```python
# -*- coding:utf-8 -*-
# author: HPCM
# time: 2020/4/8 18:54
# file: t_flask.py
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    # 全局配置
    SECRET_KEY = "hello_world"
    DEBUG = False
    # mysql配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:dong10@19.19.19.11:3306/db_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)


class ObjectOne(db.Model):
    __tablename__ = 'obj_one'
    id = db.Column(db.Integer, primary_key=True)
    one_name = db.Column(db.String(64), unique=True, index=True)
    one_to_more = db.relationship("ObjectMore", backref="one_to_more")

    def __repr__(self):
        return '<ObjectOne: {}>'.format(self.one_name)

    def __str__(self):
        return '<ObjectOne: {}>'.format(self.one_name)


class ObjectMore(db.Model):
    __tablename__ = 'obj_more'
    id = db.Column(db.Integer, primary_key=True)
    more_name = db.Column(db.String(64), unique=True, index=True)
    more_to_one = db.Column(db.Integer, db.ForeignKey('obj_one.id'))

    def __repr__(self):
        return '<ObjectMore: {}>'.format(self.more_name)

    def __str__(self):
        return '<ObjectMore: {}>'.format(self.more_name)


@app.route("/add")
def add():
    """增加"""
    one1 = ObjectOne(one_name="one_1")
    one2 = ObjectOne(one_name="one_2")
    one3 = ObjectOne(one_name="one_3")
    db.session.add(one1)  # 提交一个
    db.session.add_all([one2, one3])  # 提交多个
    db.session.commit()  # 只有commit才能存入到数据库

    more_1 = ObjectMore(more_name="more_1", more_to_one=one1.id)
    more_2 = ObjectMore(more_name="more_2", more_to_one=one1.id)

    more_3 = ObjectMore(more_name="more_3", more_to_one=one2.id)

    db.session.add_all([more_1, more_2, more_3])
    db.session.commit()
    return "add success!"


@app.route("/delete/<string:mt>/<int:uid>")
def delete(mt, uid):
    """删除"""
    print(mt, uid)
    if mt == "one":
        obj_one = ObjectOne.query.get(uid)
        if not obj_one:
            return "{} 不存在!"
        try:
            ObjectMore.query.filter_by(more_to_one=uid).delete()
            db.session.delete(obj_one)
            db.session.commit()
            return "delete {} success!".format(uid)
        except Exception as e:
            db.session.rollback()
            print(e)
            return "delete {} failed!".format(uid)
    else:
        try:
            obj_more = ObjectMore.query.get(uid)
            db.session.delete(obj_more)
            return "delete {} success!".format(uid)
        except Exception as e:
            db.session.rollback()
            print(e)
            return "delete {} failed!".format(uid)


@app.route("/edit/<int:uid>")
def edit(uid):
    """编辑"""
    print(uid)
    obj_one = ObjectOne.query.get(uid)
    if not obj_one:
        return "{} 不存在!"
    print(obj_one.one_name)
    obj_one.one_name = "one_edit_{}".format(uid)
    db.session.commit()
    return "edit success!"


@app.route("/select/<string:mt>/<int:uid>")
def select(mt, uid):
    """查询"""
    print(mt, uid)
    if mt == "one":
        if uid == 0:
            res = ObjectOne.query.filter_by(id=uid + 2)
            oo = res[0]
        else:
            oo = ObjectOne.query.get(uid)
        print(dir(oo))
        print(oo.one_to_more[0].more_name)
        return str(oo.one_to_more)
    else:
        om = ObjectMore.query.get(uid)
        print(dir(om))
        return om.one_to_more.one_name


manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run(default_command="runserver")

```



### 2.4.2 多对多

#### 2.4.2.1 模型创建

```python
tb_relationship_more_more = db.Table(
    # 三方关系表
    "tb_relationship_more1_more2",
    db.Column('more1', db.Integer, db.ForeignKey('more1.id')),
    db.Column('more2', db.Integer, db.ForeignKey('more2.id')),
)


class ObjectMore1(db.Model):
    __tablename__ = 'more1'
    id = db.Column(db.Integer, primary_key=True)
    more1_name = db.Column(db.String(64), unique=True, index=True)
    more1_to_more2 = db.relationship(
        "ObjectMore2", secondary=tb_relationship_more_more, backref="more2_to_more1"
    )

    def __repr__(self):
        return '<ObjectOne: {}>'.format(self.more1_name)

    def __str__(self):
        return '<ObjectOne: {}>'.format(self.more1_name)


class ObjectMore2(db.Model):
    __tablename__ = 'more2'
    id = db.Column(db.Integer, primary_key=True)
    more2_name = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<ObjectMore: {}>'.format(self.more2_name)

    def __str__(self):
        return '<ObjectMore: {}>'.format(self.more2_name)
```



#### 2.4.2.2 增删改查

* 增

  ```python
  ********************more1_to_more2************************
  In [13]: more1_1 = ObjectMore1(more1_name="more1_1")
   ...: more1_2 = ObjectMore1(more1_name="more1_2")  # 也可使用关键字参数配置
      # ObjectMore1(more1_name="more1_2", more1_to_more2=[more2_2, more2_3])
      # ObjectMore2(more2_name="more2_2", more2_to_more1=[more1_2, more1_3])
   ...: 
   ...: more2_1 = ObjectMore2(more2_name="more2_1")
   ...: more2_2 = ObjectMore2(more2_name="more2_2")
   ...: more2_3 = ObjectMore2(more2_name="more2_3")
  
   ...: more1_1.more1_to_more2 = [more2_1, more2_2]
   ...: more1_2.more1_to_more2 = [more2_2, more2_3]
   ...: db.session.add_all([more1_1, more1_2, more2_1, more2_2, more2_3])
   ...: db.session.commit()
  In [14]: ObjectMore1.query.all()
  Out[14]: [<ObjectOne: more1_1>, <ObjectOne: more1_2>]
  In [15]: ObjectMore2.query.all()
  Out[15]: [<ObjectMore: more2_1>, <ObjectMore: more2_2>, <ObjectMore: more2_3>]
      
  ********************more2_to_more1************************
  more2_1.more2_to_more1 = [more1_1, more1_2]# 其他的均一样
  ```

  

* 删

  删除任意一方, 需要同时将其关联的另一方同时删除, flask是维护一张三方表, 再删除一方会自动清理三方表, 实现同时删除另一方

  ```python
  In [40]: more2_3 = ObjectMore2.query.filter_by(more2_name="more2_3")[0]
      
  In [41]: db.session.delete(more2_3)
  
  In [42]: db.session.commit()
      
  In [43]: ObjectMore2.query.filter_by(more2_name="more2_3")[:]
  Out[43]: []
  ```

  

* 改

  ```python
  In [24]: more1_1_list = ObjectMore1.query.filter_by(more1_name="more1_1")
      ...: more1_2_list = ObjectMore1.query.filter_by(more1_name="more1_2")
      ...: more1_1 = more1_1_list[0]
      ...: more1_2 = more1_2_list[0]
      ...:
      ...: more2_3_list = ObjectMore2.query.filter_by(more2_name="more2_3")
      ...: more2_3 = more2_3_list[0]
          
  In [25]: more2_3.more2_to_more1 = [more1_1, more1_2]
      ## 也可以使用list模式操作
      ## more2_3.more2_to_more1.append(more1_2)
      ## more2_3.more2_to_more1.remove(more1_2)
      ...
  In [26]: db.session.commit()
  ```

  

* 查

  ```python
  ********************more1_to_more2************************
  In [31]: more1_1 = ObjectMore1.query.filter_by(more1_name="more1_1")[0]
  
  In [32]: more1_1
  Out[32]: <ObjectOne: more1_1>
  
  In [33]: more1_1.more1_to_more2
  Out[33]: [<ObjectMore: more2_2>, <ObjectMore: more2_1>, <ObjectMore: more2_3>]
  
  ********************more2_to_more1************************
  In [28]: more2_3 = ObjectMore2.query.filter_by(more2_name="more2_3")[0]
      
  In [29]: more2_3
  Out[29]: <ObjectMore: more2_3>
  
  In [30]: more2_3.more2_to_more1
  Out[30]: [<ObjectOne: more1_1>, <ObjectOne: more1_2>]
  
  ```

  

```python

```



# 3. 数据库信号

## 3.1 执行前

```python
@models_committed.connect_via(app)
def models_committed(a, changes):
    """对数据库的增删该操作进行捕获处理"""
    print(a is app, changes)
```

## 3.2 执行后

```python
@before_models_committed.connect_via(app)
def models_committed(a, changes):
    """两个数据一模一样, 一个是操作后的, 一个是操作前的"""
    print(a is app, changes)
```

## 3.3 获取慢查询

```python
@app.after_request
def after_request(response):
    """在每次查询后, 获取慢查询记录"""
    for query in get_debug_queries():
        # if query.duration >= 0.001:  # 用时判断
        print(
                ('\nContext:{}\nSLOW QUERY: {}\nParameters: {}\n'
                 'Duration: {}\n').format(query.context, query.statement,
                                          query.parameters, query.duration))
    return response

```



## 3.4 测试代码

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:hpcm
# datetime:19-6-17 下午4:32
from flask import Flask, request
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy, models_committed, before_models_committed

app = Flask(__name__)


class Config(object):
    # 全局配置
    SECRET_KEY = "hello_world"
    DEBUG = False
    # mysql配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:dong10@localhost:3306/db_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_RECORD_QUERIES = False


app.config.from_object(Config)
db = SQLAlchemy(app)


class Number(db.Model):
    __tablename__ = "number_test"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return 'class:%s' % self.name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


@app.route("/a")
def query():
    page = int(request.args.get("page", 1))
    ns = Number.query.order_by(Number.id.desc()).paginate(page=page, per_page=3).items
    return str([n.name for n in ns])


@app.route("/b")
def add_one():
    n1 = Number()
    n1.name = "test_{}".format("111")
    n2 = Number()
    n2.name = "test_{}".format("111")
    db.session.add_all([n1, n2])
    db.session.commit()
    return "success!"


@models_committed.connect_via(app)
def models_committed(a, changes):
    """对数据库的增删该操作进行捕获处理"""
    print(a is app, changes)


@before_models_committed.connect_via(app)
def models_committed(a, changes):
    """两个数据一模一样, 一个是操作后的, 一个是操作前的"""
    print(a is app, changes)
    
    
@app.after_request
def after_request(response):
    """在每次查询后, 获取慢查询记录"""
    for query in get_debug_queries():
        # if query.duration >= 0.001:  # 用时判断
        print(
                ('\nContext:{}\nSLOW QUERY: {}\nParameters: {}\n'
                 'Duration: {}\n').format(query.context, query.statement,
                                          query.parameters, query.duration))
    return response


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
```

# 4. 数据库模型操作

对模型的增删改查操作

## 4.1 增删改

**注意:**

	* sqlalchemy默认是开启事务的
	* 要想数据变更生效必须执行`db.session.commit`

### 4.1.1 增

* 单个

  ```python
  foo = Foo(name=1)
  # db.session.add(foo)
  db.session.commit()
  ```

  

* 批量

  ```python
  foo1 = Foo(name1)
  foo2 = Foo(name2)
  # db.session.add_all([foo1, foo2])
  db.session.commit()
  ```

  

### 4.1.2 删

```python
foo1 = Foo.query.get(id=1)
# foo1.delete()
# db.session.delete(foo1)
db.session.commit()
```



### 4.1.3 改

```python
foo1 = Foo.query.get(1)
# foo1.name = foo_edit_1
db.session.commit()
```



## 4.2 查

| 方法         | 说明                                              |
| ------------ | ------------------------------------------------- |
| filter       | 模糊查询                                          |
| filter_by    | 等值查询                                          |
| limit        | 限制行数                                          |
| offset       | 偏移查询                                          |
| order_by     | 排序查询                                          |
| group_by     | 分组查询                                          |
| all          | 执行并获取结果[list]                              |
| first        | 执行并获取第一个结果                              |
| first_or_404 | 执行并获取第一个结果, 如果没有则返回404错误       |
| get          | 以主键查询, 执行并获取结果                        |
| get_or_404   | 以主键查询, 执行并获取结果, 如果没有则返回404错误 |
| count        | 统计返回结果的数量                                |
| paginate     | 返回一个Paginate对象, 用于翻页查询                |
| distinct     | 对输出的结果进行去重处理                          |

* filter_by

  ```python
  In [15]: ObjectMore1.query.filter_by(more1_name="more1_1").all()
  Out[15]: [<ObjectOne: more1_1>]
  ```

* filter

  ```python
  ## 开头匹配/末尾匹配, startswith/endswith
  In [17]: ObjectMore1.query.filter(ObjectMore1.more1_name.startswith("more1")).all()
  Out[17]: [<ObjectOne: more1_1>, <ObjectOne: more1_2>]
  
  ## 不等于
  In [18]: ObjectMore1.query.filter(ObjectMore1.more1_name!="more1_1").all()
  Out[18]: [<ObjectOne: more1_2>]
  
  ## 大于/等于/小于 >=/==/<=/>/<  或者__gt__()....
  In [22]: ObjectMore1.query.filter(ObjectMore1.more1_name<="more1_1").all()
  Out[22]: [<ObjectOne: more1_1>]
  
  ## 多个匹配 in_/notin_
  In [24]: ObjectMore1.query.filter(ObjectMore1.more1_name.in_(["more1_1"])).all()
  Out[24]: [<ObjectOne: more1_1>]
  
  ## 包含匹配 contains
  In [25]: ObjectMore1.query.filter(ObjectMore1.more1_name.contains(["_1"])).all()
  Out[25]: [<ObjectOne: more1_1>]
  
  ## 正则匹配 like/notlike
  In [33]: ObjectMore1.query.filter(ObjectMore1.more1_name.like("%2")).all()
  Out[33]: [<ObjectOne: more1_2>]
  
  ## 区间查询 between
  In [36]: ObjectMore1.query.filter(ObjectMore1.more1_name.between("more1_1", "more1_2")).all()
  Out[36]: [<ObjectOne: more1_1>, <ObjectOne: more1_2>]
  
  ## 空查询, is_/isnot
  In [40]: ObjectMore1.query.filter(ObjectMore1.more1_name.isnot(None)).all()
  Out[40]: [<ObjectOne: more1_1>, <ObjectOne: more1_2>]
  ```

* order_by

  ```python
  ## 排序查询 desc/asc  降序/升序
  In [42]: ObjectMore1.query.order_by(ObjectMore1.more1_name.desc()).all()
  Out[42]: [<ObjectOne: more1_2>, <ObjectOne: more1_1>]
  
  ## 函数 desc/asc  降序/升序
  In [3]: from sqlalchemy import desc, asc
  In [4]:  ObjectMore1.query.order_by(desc("more1_name")).all()
  Out[4]: [<ObjectOne: more1_2>, <ObjectOne: more1_1>]
  ```

* limit

  ```python
  In [10]:  ObjectMore1.query.limit(1).all()
  Out[10]: [<ObjectOne: more1_2>]
  ```

* offset

  ```python
  In [36]: for i in range(5):
      ...:     print("第 {} 页为: {}".format(i + 1, ObjectMore1.query.order_by(asc("id")).offset(2*i).limit(2).all()))
  
  第 1 页为: [<ObjectOne: more1_1>, <ObjectOne: more1_2>]
  第 2 页为: [<ObjectOne: more1_3>, <ObjectOne: more1_4>]
  第 3 页为: [<ObjectOne: more1_5>, <ObjectOne: more1_6>]
  第 4 页为: [<ObjectOne: more1_7>, <ObjectOne: more1_8>]
  第 5 页为: [<ObjectOne: more1_9>, <ObjectOne: more1_10>]
  
  ```

* distinct

  ```python
  In [48]: ObjectMore1.query.distinct("id").all()
  Out[48]:
  [<ObjectOne: more1_9>,
   <ObjectOne: more1_8>,
   <ObjectOne: more1_7>,
   ...]
  ```

* group_by

  ```python
  In [49]: ObjectMore1.query.group_by("id").all()
  Out[49]:
  [<ObjectOne: more1_9>,
   <ObjectOne: more1_8>,
  ...]
  ```

  

## 4.3 分页

调用paginate可以实现数据分页

```python
def paginate(self, page=None, per_page=None, error_out=True, max_per_page=None)
```

* page: 页数
* per_page: 每页数量
* error_out: 出现异常是否拦截
* max_per_page: 每页最大限制

返回Paginate对象

* query: 需要查询的对象
* page: 当前页数
* per_page: 一页含有个数
* total: 查询出的未分页的全部结果
* item: 当前页的结果集
* pages: 全部结果能分多少页
* prev(error_out): 上一页的Paginate对象
* prev_num: 上一页页数
* has_prev: 是否含有上一页
* next(error_out): 下一页对象
* next_num: 下一页页数
* has_next: 是否含有下一页
* iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2): jinjia模板渲染的分页:

```python
{% macro render_pagination(pagination, endpoint) %}
  <div class=pagination>
  {%- for page in pagination.iter_pages() %}
    {% if page %}
      {% if page != pagination.page %}
        <a href="{{ url_for(endpoint, page=page) }}">{{ page }}</a>
      {% else %}
        <strong>{{ page }}</strong>
      {% endif %}
    {% else %}
      <span class=ellipsis>…</span>
    {% endif %}
  {%- endfor %}
  </div>
{% endmacro %}
```









