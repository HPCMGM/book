# 1. 数据库读写分离

为了提高数据库的读写效率, 对分布式数据库高效的利用, 可以进行读写分离

## 1.1 自动实现读写分离

### 1.1.1 setting配置

```python
# 数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'meiduo'  # 数据库名字
    },
    'slave': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 8306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'meiduo'  # 数据库名字
    }
}
```

### 1.1.2 设置分发规则

```python
class MaterSlaveRouter(object):
    """数据库主从读写分离"""

    def db_for_read(self, model, **hints):
        """读取数据库"""
        # 也可以多个数据库随机性读取
        return "slave"

    def db_for_write(self, model, **hints):
        """写入数据库"""
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return True
```

## 2.2 手动实现

只需要在orm编写是指定对应的数据库即可

```python
Users.objects.using("slave").create(xxx)
Users.objects.filter(xx).using("default").first()
```

