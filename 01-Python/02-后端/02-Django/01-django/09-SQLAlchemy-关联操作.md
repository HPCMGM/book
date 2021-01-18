# 1. 模型关联

## 1.1 一对一

* 一对一, 反向调用为`当前表的表名`

### 1.1.1 创建

```python
from django.db import models


# Create your models here.
class One1(models.Model):
    name = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'one1'  # 指明数据库表名

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


class One2(models.Model):
    name = models.CharField(max_length=20, null=True)
    to_one2 = models.OneToOneField(One1, on_delete=models.CASCADE, related_name="to_one1")

    class Meta:
        db_table = 'one2'  # 指明数据库表名

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name

```

### 1.1.2 操作

* 增加

  ```python
  o1 = One1()
  o1.name = "a1_1"
  o1.save()
  
  o2 = One2.objects.create(name="o2_1", to_one1=o1)
  o2.save()
  ```

  

* 删除

  ```python
  o1.delete()
  o2.delete()
  ```

  

* 查询

  ```python
  o1 = One1.objects.all()[0]
  print(o1.to_one1)
  o2 = One2.objects.all()[0]
  print(o2.to_one2)
  ```

  

* 修改

  ```python
  o1.to_one2.name = "one2_name1"
  o2.to_one1.name = "one1_name1"
  ```

  

## 1.2 一对多

一对多, 反向调用为`当前字段+'_set'`

### 1.2.1 Foreignkey

```python
def __init__(self, to, on_delete, related_name=None, related_query_name=None,
                 limit_choices_to=None, parent_link=False, to_field=None,
                 db_constraint=True, **kwargs):
    
# 示例sql
# orm对应关系: tb_a/TbA, tb_b/TbB
# select * from tb_a left join tb_b on tb_a.b_id=tb_b.a_id
```

* to: `obj/str`, model对象, 可以为字符串, 也可以为类对象, 示例中为: `TbB`
* on_delete: `function`, 当前字段删除时, 对约束表的影响, 一般选择有
  * models.CASCADE: 同时删除约束表对应的字段
  * models.PROTECT: 抛出异常, 禁止删除
  * models.SET_NULL: 将约束表中, 对应的字段改成`null`, 注意此时需要把`null=True`
  * models.SET_DEFAULT: 将约束表中, 对应的字段改成默认值, 注意此时`default`字段需要配置值
  * models.SET: 删除主表字段, 并给约束表赋予指定值
  * models.DO_NOTHING: 抛出异常, 不做任何操作
* related_name: `str`,  被约束表查询时的字段, 示例中可设置为`tb_a`, 这样就可以使用`TbB_obj.tb_a.all()`反向查询到对象集合
* related_query_name: `str`, 默认是使用当前字段的名称, 可设置为`tb_b`, 这样就可以使用`TbA_obj.tb_b`, 查询被约束的对象
* limit_choices_to: `items`,  restframework/admin等框架, 可以通过此字段, 渲染出来下拉菜单用于用户选择
* parent_link: `bool`, 是否将被约束的表中, 每个字段都映射到当前表中直接调用.
* to_field: `str`, 约束表中对应的关联字段名称, 示例中为`a_id`
* db_constraint: 
* kwargs:
  * db_column: 当前表中关联约束表的字段名称, 示例中为`b_id`

### 1.2.2 模型

```python
from django.db import models


# Create your models here.
class One(models.Model):
    name = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'one'  # 指明数据库表名

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


class More(models.Model):
    name = models.CharField(max_length=20, null=True)
    to_one = models.ForeignKey(One, on_delete=models.CASCADE, related_name="to_more")

    class Meta:
        db_table = 'more'  # 指明数据库表名

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
```



### 1.2.3 操作

* 增加

  ```python
  def create():
      one = One.objects.create(name="one1")
      more = More.objects.create(name="more1", to_one=one)  # 多绑定一
      one.save()
      more.save()
      
  def create():
      one = One.objects.create(name="one1")
      more = More.objects.create(name="more1")
      one.to_more.add(more1, more2)  # 一绑定多
      one.save()
      more.save()
  ```

* 修改

  ```python
  def edit():
      more1 = one.to_more.all()[0]
      more1.name = "more1_3"
      more1.save()
      more1 = More.objects.all()[0]
      one = more1.to_one
      one.name = "one1_3"
      one.save()
  ```

* 查询

  ```python
  def select():
      one = One.objects.all()[0]
      print(one.to_more.all()[0].name)
      more = More.objects.all()[0]
      print(more.to_one.name)
  ```

  

* 删除

  ```python
  def delete():
      more1 = More.objects.all()[0]
      one = more1.to_one
      more1.delete()
      one.delete()
  ```

  

## 1.3 多对多

### 1.3.1 ManyToManyField

* 多对多, 反向调用为`当前字段+'_set'`

### 1.3.2 模型

```python
from django.db import models


# Create your models here.
class Many1(models.Model):
    name = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'many1'  # 指明数据库表名

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return "<Many1: {}>".format(self.name)


class Many2(models.Model):
    name = models.CharField(max_length=20, null=True)
    to_more1 = models.ManyToManyField(Many1, related_name="to_more2")

    class Meta:
        db_table = 'many2'  # 指明数据库表名

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return "<Many2: {}>".format(self.name)
```

### 1.3.3 操作

* 增加

  ```python
  def create():
      more1 = Many1.objects.create(name="more1_1")
      more2 = Many2.objects.create(name="more2_1")
      more1.to_more2.add(more2)
      more2.save()
      more1.save()
  ```

* 查询

  ```python
  def select():
      more1 = Many1.objects.all()[0]
      print(more1.to_more2.all())
      more2 = Many2.objects.all()[0]
      print(more2.to_more1.all())
  ```

* 修改

  ```python
  def edit():
      more1 = Many1.objects.all()[0]
      more2 = more1.to_more2.all().first()
      more2.name = "more2_2"
      more2.save()
      
      more2 = Many2.objects.all()[0]
      more1 = more2.to_more1.all().first()
      more1.name = "more1_2"
      more1.save()
  ```

* 删除

  ```python
  def delete():
      more1 = Many1.objects.all()[0]
      more2 = more1.to_more2.all().first()
      more2.delete()
      more1.delete()
  ```

  

