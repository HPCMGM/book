# 自增长字段

字段id  为自增长字段, 必须设置为AutoField

否则在ORM无法判断id创建后应该为什么, 例如:

```python
obj = Tests.object.create()
```

或者

```python
obj = Tests()
obj.save()
```

无法获得id

```python
print(obj.id)
# None
```

