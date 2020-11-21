# 1. 修改查询返回id信息

```python
def get_identifier(s):
    return str(s.pk)
```

在`settings.py`中替换信息

```python
HAYSTACK_IDENTIFIER_METHOD = "users.tests.get_identifier"
```

# 2. 筛选查询结果集

```python
class GoodsSearchView(SearchView, View):

    def get_results(self):
        sqs = self.form.search()
        rsp = sqs.models(Many1)
        return rsp

    def create_response(self):
        context = self.get_context()
        return JsonResponse({"data": [obj.get_stored_fields() for obj in context["paginator"].object_list]})

    def get_status(self):
        return self.request.GET.get("is_delete", "0") == "1"  # 注意 此参数必须设置在 indexes, 否则什么都查不到

    def get_query_filters(self):
        filter_dict = {
            "is_delete": self.get_status()
        }
        print(self.get_status())
        return SearchQuerySet().filter(**filter_dict).order_by("-id")

    def __call__(self, request):
        pass

    def get(self, request):
        self.request = request
        self.form = self.build_form(form_kwargs={'searchqueryset': self.get_query_filters()})
        self.query = self.get_query()
        self.results = self.get_results()
        return self.create_response()
```

