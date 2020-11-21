# 1. Elasticsearch

## 1.1 docker镜像创建

### 1.1.1 获取镜像

1. 在线拉取

   ```python
   docker pull delron/elasticsearch-ik:2.4.6-1.0
   ```

2. 获取离线镜像

   [本地下载](image/05-elasticsearch-%E5%AE%8C%E6%95%B4%E9%85%8D%E7%BD%AE/delron_elasticsearch.tar.gz)    [百度云](https://pan.baidu.com/s/1D5v0gfPhWBgwioQ_kaAc_A): hpcm
   
   ```python
   docker load -i elasticsearch-ik-2.4.6_docker.tar
   ```

### 1.1.2 运行容器

运行docker前, 需要配置一下elasticsearch的配置文件[下载](image/05-elasticsearch-%E5%AE%8C%E6%95%B4%E9%85%8D%E7%BD%AE/config.rar)

需要将配置文件中`config/dlasticsearch.yml`中, 修改为自己的`ip`

```python
network.host: 10.0.0.12
```

启动容器

```python
docker run -dti --network=host --name=elasticsearch -v /usr/data/elasticsearch/config:/usr/share/elasticsearch/config delron/elasticsearch-ik:2.4.6-1.0
```

## 1.2 Django项目接入

```python
pip install django-haystack==2.8.0
pip install drf-haystack==1.8.1
pip install elasticsearch==2.4.1
pip install django-rest-framework==0.1.0
```

### 1.2.1 模型创建

```python
# model.py
from django.db import models

# Create your models here.
class TableFoo1(models.Model):
    name = models.CharField(max_length=30, default="")
    desc = models.TextField(default="")

    class Meta:
        db_table = "tb_foo1"
```

### 1.2.2 索引创建

创建索引类

```python
# search_indexes.py
from haystack import indexes

from . import models

class Foo1Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.IntegerField(model_attr="id")
    name = indexes.CharField(model_attr="name")
    desc = indexes.CharField(model_attr="desc")

    def get_model(self):
        return models.TableFoo1

    def index_queryset(self, using=None):
        return self.get_model().objects
```

创建索引字段, 固定格式:

```Python
templates/search/indexes/{app_name}/{model_name(小写)}_text.txt
```

即

```python
templates/search/indexes/foo/tablefoo1_text.txt
```

向文件中加入需要需查询的字段

```jinja2
{{ object.name }}
{{ object.desc }}
```

### 1.2.3 序列化器

```python
# file: serializers.py
from drf_haystack.serializers import HaystackSerializer

from .search_indexes import Foo1Index


class Foo1Serializer(HaystackSerializer):
    class Meta:
        index_classes = [Foo1Index]
        fields = ["name", "desc"]
```

### 1.2.4 路由视图

```python
from drf_haystack.viewsets import HaystackViewSet

from .models import TableFoo1
from .serializers import Foo1Serializer


class Foo1SearchViewSet(HaystackViewSet):
    """Foo1搜索"""
    index_models = [TableFoo1]
    serializer_class = Foo1Serializer
```

视图

```python
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = []
router = DefaultRouter()
router.register('search', views.Foo1SearchViewSet, basename="test")
urlpatterns += router.urls
```

### 1.2.5 settings配置

#### 1.2.5.1 rest版本兼容调整

向`rest_framework.pagination`注入`_get_count`方法.

```python
import rest_framework.pagination

def _get_count(queryset):
    """
    Determine an object count, supporting either querysets or regular lists.
    """
    try:
        return queryset.count()
    except (AttributeError, TypeError):
        return len(queryset)

rest_framework.pagination._get_count = _get_count
```

#### 1.2.5.2 查询配置

```python
INSTALLED_APPS = [
    ...
    "rest_framework",
    "haystack",

    "foo",
]

....

# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://10.0.0.12:9200/',  # 此处为elasticsearch运行的服务器ip地址，端口号固定为9200
        'INDEX_NAME': 'db_test',  # 指定elasticsearch建立的索引库的名称
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
```

### 1.2.6 索引重建

```python
python manage.py rebuild_index
```

### 1.2.7 至此完结测试

```python
http://localhost:8000/foo/search/?name=t1
http://localhost:8000/foo/search/?desc=by
```

