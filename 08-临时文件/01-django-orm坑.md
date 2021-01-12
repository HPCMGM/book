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

ForeignKey

```python
class A():
	a = ForeignKey()
```

* to: 指向需要关联的表名
* on_delete: 联动删除时的处理方式
* related_name: 关联查询外键表时, 联动查询时的字段: X.related_name
* related_query_name: 反向查询时, 联动查询时的字段: A.related_query_name
* limit_choices_to: 类似普通字段中的choice, 用于admin中等渲染成select表单控件
* parent_link: 是否将外键表中的字段, 直接平移到本对象中调用.
* db_column: 关联字段, 相当关联查询时的where tb_a.a = tb_b.b中的a
* to_field: 被关联的字段, 默认为主键(id). 相当关联查询时的where tb_a.a = tb_b.b中的b