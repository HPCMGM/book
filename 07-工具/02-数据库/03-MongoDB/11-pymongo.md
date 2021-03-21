# 1. Pymongo

## 1.1 安装

```python
pip install pymongo
```

## 1.2 使用

```python
import pymongo
# 连接mongodb服务器
client = pymongo.MongoClient(host="localhost", port=27017)
# 进入admin进行权限校验
admin = client.admin
admin.authenticate("user_name", "password")
# 获取数据库集合(字典)
collection = client.admin.spider
# 查询到的结果为一个可迭代对象
print([i for i in collection.find().limit(10)])
```



