# 1. 原生sqlalchemy

## 1.1 安装

```python
pip install sqlalchemy
pip install sqlalchemy-migrate
```

# 2. 数据迁移

## 2.1 配置

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

url = "mysql+mysqldb://root:dong10@localhost:3306/db_host?charset=utf8"
engine = create_engine(url)
Session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
# 直接使用sessionmaker则重新创建一个session, 使用scoped_session会获取一个, 如果没有则重新创建
db = Session()  # 用户数据库操作

Model = declarative_base()  # 用于模型创建
```

## 2.2 模型

```python
from sqlalchemy import Column, String, Integer, BigInteger, SmallInteger
注意: Interger为基类不能使用

class HostInfo(Model):
    """主机存储信息表"""
    __tablename__ = 'host_info'
    id = Column(SmallInteger(), primary_key=True, index=True)
    host = Column(String(64), unique=True, nullable=True)
    username = Column(String(128), nullable=True)
    _password = Column(String(128), nullable=True)
    base_path = Column(String(256), default="~")

    def __repr__(self):
        return 'host_info:%s' % self.host

    @property
    def password(self):
        return crypt.decrypt(self._password)

    @password.setter
    def password(self, pwd):
        # 设置password前进行加密
        self._password = crypt.encrypt(pwd)
```

## 2.3 迁移

### 2.3.1 数据库初始化

```python
# pip install sqlalchemy-migrate
from migrate.versioning import api

def db_init():
    """初始化, 此函数只能执行一次"""
    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        # 判断迁移文件是否存在
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
```

### 2.3.2 生成迁移文件

```python
def migrate():
    """生成迁移版本文件"""
    import types
    # 创建迁移文件版本
    Model.metadata.create_all(bind=engine)
    migration = os.path.join(SQLALCHEMY_MIGRATE_REPO, 'versions/%03d_migrate.py' % (
            api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO) + 1))

    # 创建旧版本
    tmp_module = types.ModuleType('old_model')
    # 创建旧模块
    old_model = api.create_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

    exec(old_model, tmp_module.__dict__)
    script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, tmp_module.meta,
                                              Model.metadata)
    with open(migration, 'w') as f:
        f.write(script)
    print("migration save as {}".format(migration))
```

### 2.3.3 更新到数据库

```python
def upgrade():
    """更新到数据库"""
    api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    print('Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)))
```

# 3. 模型操作

## 3.1 增加

```python
def add_info():
    """增加信息"""
    host_info = HostInfo()
    host_info.host = host
    host_info.username = username
    host_info.password = password
    host_info.base_path = base_path
    db.add(host_info)
    db.commit()
```



## 3.2 删除

```python
def delete_info():
    """删除信息"""
    db.query(HostInfo).filter(HostInfo.host == self.host).all()[0].delete()
```



## 3.3 修改

```python
def change_info(self):
    """修改信息"""
    host_info = db.query(HostInfo).filter(HostInfo.host == self.host).all()[0]
    print(host_info)
    host_info.password = self.password
    db.update(host_info)
    db.commit()
```



## 3.4 查询

```python
db.query(HostInfo).filter(HostInfo.host == self.host).all()[0]
其他用法和Flask-SQLAlchemy相似
```

