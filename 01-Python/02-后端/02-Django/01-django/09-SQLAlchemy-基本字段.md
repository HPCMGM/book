# 1. SQLalchemy

**注意**:

* Django2.1不再支持MySQL5.5，必须5.6版本以上, 报错信息如下:

  ```python
    File "C:\Users\hpcm\Envs\test\lib\site-packages\django\db\migrations\recorder.py", line 69, in ensure_schema
      raise MigrationSchemaMissing("Unable to create the django_migrations table (%s)" % exc)
  django.db.migrations.exceptions.MigrationSchemaMissing: Unable to create the django_migrations table ((1064, "You have an error in your S
  QL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(6) NOT NULL)' at line 1"))
  ```

  解决方案:

  * 将Django降级到2.0.0

    ```python
    pip install django==2.0.0
    ```


## 1.1 ORM框架

Object Relation Mapping(ORM), 数据库对象关系映射

将数据库中的表, 字段等转化成Python的对象, 直接通过对象去操作数据库. 

* 屏蔽了不同数据库的sql语言的差异
* 牺牲了Python对象向数据库转化时间, 和sql语句转化时间

## 1.2 安装mysql驱动

```python
pip install pymysql
```

## 1.3 配置

### 1.3.1 驱动

```python
import pymysql

pymysql.version_info = (1, 4, 13, "final", 0)  # 强制指定客户端版本
pymysql.install_as_MySQLdb()
```

### 1.3.2 数据库

修改`setting.py`中`DATABASES`参数

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '10.0.0.10',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'dong10',  # 数据库用户密码
        'NAME': 'test',  # 数据库名字
        'OPTIONS': {'isolation_level': None}
    }
}
```



## 1.4 操作命令

### 1.4.1 生成迁移文件

```python
python manage.py makemigrations
```

### 1.4.2 同步到数据库

```python
python manage.py migrate
```

### 1.4.3 查看全部迁移记录

```python
python manage.py showmigrations
```

### 1.4.3 版本回退

```python
python manage.py migrate app_name version
```

# 2. 字段

## 2.1 类型字段

`id`字段默认会自动创建, 无需进行再次创建, 创建后可以用`id`或者`pk`字段都可以查询到

| 字段             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| AutoField        | 自动增长                                                     |
| BooleanField     | 布尔类型                                                     |
| NullBooleanField | 支持Null, True, False三种                                    |
| CharField        | 字符串  max_length限时长度                                   |
| TextField        | 大文本(一般超过4000字符)                                     |
| IntegerField     | 整形                                                         |
| DecimalField     | 十进制浮点型,  参数max_digits为总位数，参数decimal_places为小数位数 |
| FloatField       | 浮点数                                                       |
| DateField        | 日期, 参数: auto_now(每次保存时自动记录时间), auto_now_add(创建时自动保存)  两个参数相互排斥, 只能二选一 |
| TimeField        | 时间, 参数同上                                               |
| DateTimeField    | 日期时间, 参数同上                                           |
| FileField        | 上传文件字段                                                 |
| ImageField       | 继承FileField, 对上传内容进行校验                            |

## 2.2 字段限制

| 参数           | 说明                                                   |
| -------------- | ------------------------------------------------------ |
| null           | 默认False(非空), 字段可以设置null                      |
| blank          | 默认False(非空白), 字段设置什么都行, 但是必须需要设置. |
| db_column/name | 数据库中字段名称, 如果不指定使用属性名                 |
| db_index       | 是否为字段创建索引, 默认False                          |
| default        | 默认值                                                 |
| primary_key    | 主键, 默认False                                        |
| unique         | 唯一, 默认False                                        |

## 2.3 外键限制

外键默认使用的字段是`on_delete`

| 参数        | 说明                                      |
| ----------- | ----------------------------------------- |
| CASCADE     | 删除主表关联删除约束表                    |
| PROTECT     | 抛出异常禁止删除                          |
| SET_NULL    | 将约束表中约束字段改为null(需要null_True) |
| SET_DEFAULT | 将约束表中约束字段改为默认(需要有默认值)  |
| SET()       | 删除主表并给约束表中约束字段指定值        |
| DO_NOTHING  | 不做任何操作, 抛出异常                    |

**实例**

```python
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class MyModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
```

## 2.4 HelloWorld

```python
from django.db import models
class Book(models.Model):
    # Django中不用设置主键, 自动生成主键id, 可以使用id/pk(primary key)查询
    b_title = models.CharField(max_length=20, verbose_name="书名")
    class Meta:
        # Django中如果不设置表名, 默认以app名字_小写模型类作为名字
        db_table = "tb_books"              # 表名
        verbose_name = "图书"              # 自定义字段名字
        verbose_name_plural = verbose_name # 开启自定义字段
        def __str__(self):
            return self.b_title  # 让输出是书名  这里不能使用repr
```

# 3. 操作

## 3.1 增删改

### 3.1 增加

* 单个

  ```python
  t = Table.objects.create()
  ```
---

  ```python
  t = Table()
  t.save()
  ```

* 批量

  ```python
  t_list = []
  for _ in range(10):
      t = Table()
      t_list.append(t)
  Table.objects.bulk_create(t_list)
  ```


### 3.1.2 删除

* 单个删除

  ```python
  t = Table.objects.get()
  t.delete()
  ```

* 批量删除

  ```python
  Table.objects.all().delete()
  Table.objects.filter().delete()
  ```

### 3.1.3 修改

* 单个

  ```python
  t = Table.objects.get()
  t.name = xx
  t.save()
  
  t = Table.objects.all().first()
  t.name = xx
  t.save()
  ```

  

* 批量

  ```python
  Table.objects.filter().update(name=xxx)
  ```

  

## 3.2 查询

ORM查询存在惰性

实例

```python
tables = Table.objects.all()   # 未访问数据库
print(tables)  # 获取到的是查询语句
[table for talbe in tables]  # 获取orm查询集对象
```

### 3.4.1 查询方法

#### F/Q

* F对象

  表中字段运算后, 与其他字段进行对比

  ```python
  Table.objects.filter(num1__gt=F(num2) * 2)
  # where num1 > num2 * 2
  ```

* Q对象

  或且非操作(&|~)

  ```python
  Table.objects.filter(Q(num1__gt=20) | Q(num2__gt=5))
  # where num1 > 20 or num2 > 5
  
  Table.objects.filter(~Q(id=3))
  # where id!=3
  ```

  

#### 查询

| 方法     | 返回      | 说明                                                         |
| -------- | --------- | ------------------------------------------------------------ |
| get      | any       | 主键查询. 主键为id/pk                                        |
| all      | list(any) | 返回一个查询集, 转化后为list, 全部查询, 默认限制查询21个, 即limit=21 |
| filter   | list(any) | 返回一个查询集, 转化后为list , 过滤查询                      |
| order_by | list(any) | 返回一个查询集, 转化后为list, 排序查询                       |
| exclude  | list(any) | 返回一个查询集, 转化后为list, 取反查询                       |
| exists   | bool      | 判断查询集是否存在数据                                       |

#### 聚合

聚合函数调用需要使用`appregate`方法

| 方法 | 返回 | 说明   |
| ---- | ---- | ------ |
| Avg  | dict | 平均数 |
| Max  | dict | 最大数 |
| Min  | dict | 最小数 |
| Sum  | dict | 求和   |

**实例**

```python
from django.db.models import Sum
Table.objects.aggregate(Sum("t_num"))

# 返回
# {"t_num__sum": 3}
```

#### 关联查询

filter(对方类名__对方属性\_\_条件=xxx)

filter(约束字段__对方属性\_\_条件=xxx)

```python
Table.objects.filter(tb_table1__name__contains="test")
```



### 3.4.2 查询过滤

| 方法                                                     | 作用                                                     | 实例                                                         |
| -------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------ |
| exact/iexact                                             | 等于, 等价于使用`=`号<br>增加符号`i`表示不区分大小写匹配 | id_exact=1<br>id=1                                           |
| contains/icontains                                       | 包含某个字<br/>增加符号`i`表示不区分大小写匹配           | name__contains="name"                                        |
| startswith/endswith<br>istartswith/iendswith             | 以某个字开头/结尾<br/>增加符号`i`表示不区分大小写匹配    | name__startswith="n"                                         |
| in                                                       | 范围查询                                                 | id__in=[1, 3, 4, 5]                                          |
| gt/gte                                                   | 大于/大于等于                                            | id__gte=8                                                    |
| lt/lte                                                   | 小于/小于等于                                            | id__lte=8                                                    |
| isnull                                                   | 判断是否为空                                             | name__isnull=False                                           |
| datetime/date/year/month/day/week_day/hour/minute/second | 时间操作                                                 | login_year=1980  等于1980年<br>login_gte=date(1980, 2, 2)  大于1980年 |



## 3.3 自定义查询集

**注意:**  一经修改, objects管理器将会失效.

### 3.3.1 查询集

```python
class SomeTableManager(models.Manager):
    def all(self):
        # 让all方法继承filter方法, 并给filter传递参数
        return super().filter(is_delete=False)
    
    def create_table(self, title, pub_date):
        # 创建模型类对象: self.model
        st = self.model()
        st.filed = title
        st.save()
        return st
    
    def get_queryset(self):
        """此函数, 会过滤查询集. 通过此方法可以过滤被删除的信息"""
        return super().get_queryset().filter(id_delete=False)
```



### 3.3.2 激活查询集

```python
class SomeTable(models.Model):
    """orm模型"""
    query = TableManager()
    # 还可以定义系统自带的查询集, 达到两用的效果
    objects = models.Manager()
    
SomeTable.query.all()    # 受查询集的影响
SomeTable.objects.all()  # 不受查询集的影响
SomeTable.query.create_table("xx", "xx")
```
