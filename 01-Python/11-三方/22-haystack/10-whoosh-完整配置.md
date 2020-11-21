## 1. settings

```python
# app中增加: "haystack"

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'apps.users.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'  # 每次访问时进行索引更新
```

## 2. 创建索引类

文件定义规则:  app下创建`search_indexes.py` 

```python
from haystack import indexes
from .models import Many2, Many1


class Many1Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr="name")

    def get_model(self):
        return Many1

    def index_queryset(self, using=None):
        """用于update时索引更新"""
        return self.get_model().objects.all()


class Many2Index(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr="name")

    def get_model(self):
        return Many2
    def index_queryset(self, using=None):
        """用于update时索引更新"""
        return self.get_model().objects.all()
```

## 3. 定义索引字段

创建文件规则: `templates/search/indexes/{appname}/{tb_name}_text.txt`

* `templates/search/indexes/users/many1_text.txt`

  ```jinja2
  {{ object.name }}
  {{ object.description }}
  ```

* `templates/search/indexes/users/many2_text.txt`

  ```jinja2
  {{ object.name }}
  {{ object.description }}
  ```

## 4. 视图函数创建

```python
from haystack.forms import SearchForm
from haystack.views import SearchView
from apps.users.models import Many1, Many2
from django.http import JsonResponse
from django.views import View


class Many1Search(SearchView):

    def get_results(self):
        sqs = self.form.search()
        rsp = sqs.models(Many1)
        return rsp

    def create_response(self):
        context = self.get_context()
        a = [{"id": obj.id, "name": obj.name} for obj in context["paginator"].object_list]
        return JsonResponse({"data": a})

class Many2Search(View):

    def get(self, request):
        q = request.GET.get("q")
        sform = SearchForm({"q": q})
        posts = sform.search()
        posts = posts.models(Many1, )  # 指定搜索表
        posts_count = posts.count()
        posts = posts[1: 15]
        pub_info_list = []
        for i in posts:
            pub_info_list.append({"id": i.id, "name":i.name})
        return JsonResponse({"ret": pub_info_list})
```

## 5. url配置

```python
urlpatterns = [
    url("^search1/$", views.Many1Search()),
    url("^search2/$", views.Many2Search.as_view()),
    url("^search3/$", include("haystack.urls")),
]
```

# 6. 重建索引

也可使用`python manager.py rebuild_index`

```python
import logging
from collections import namedtuple

from haystack import connections
from haystack.management.commands.update_index import Command

class Logging(object):
    """xxx"""
    stdout = namedtuple("a", {"write": logging.warning})

class UpdateIndex(Logging, Command):

    pass


def clear_index():
    for backend_name in connections.connections_info.keys():
        backend = connections[backend_name].get_backend()
        backend.clear(commit=True)
    logging.warning("All documents removed.")

def update_index():
    UpdateIndex().handle()
    
    
def rebuild_index():
    clear_index()
    update_index()
```

