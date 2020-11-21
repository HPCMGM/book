# 1. 视图

## 1.1 视图函数

### 1.1.1 创建的视图

手动创建视图函数, 和flask模式差不多

```python
from django.http import HttpResponse
def index(request, *args, **kwargs):
    """主页"""
    if request.method == "GET":
        return HttpResponse("Get")
    elif request.method == "POST":
        return HttpResponse("Post")
    return HttpResponse("Method Not Allowed {}: {}".format(request.method, request.path), status=405)

```

### 1.1.2 路由配置

```python
urlpatterns = [
    url(r"/", index),
]
```



## 1.2 视图类

### 1.2.1 自动分发

视图类可以自动完成method的分发, 相关源码如下:

```python
	def as_view(cls, **initkwargs):
        """Main entry point for a request-response process."""
        ...

        def view(request, *args, **kwargs):
            ...
            return self.dispatch(request, *args, **kwargs)
			...
        return view
    
	def dispatch(self, request, *args, **kwargs):  # 动态分发请求
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    def http_method_not_allowed(self, request, *args, **kwargs):  # 不支持请求
        logger.warning(
            'Method Not Allowed (%s): %s', request.method, request.path,
            extra={'status_code': 405, 'request': request}
        )
        return HttpResponseNotAllowed(self._allowed_methods())
```

* 从源码中可以看出, dispatch函数为主要的分发函数, 配置在路由中必须是这个函数, 所以配置路由时候一定要先执行as_view,  才能获取到dispath.

### 1.2.2 视图类定义

```python
class RequestTest(View):
    """不同的请求使用不同的方法"""

    def get(self, request, *args, **kwargs):
        return HttpResponse("get")

    def post(self, request, *args, **kwargs):
        print(request.GET)
        return HttpResponse("post")
```

### 1.2.3 路由配置

```python
urlpatterns = [
    url(r"/", RequestTest.as_view(), name="test"),
]
```

# 2. 视图装饰

闭包

```python
def func1(view):
    def func2(request, *args, **kwargs):
        """xxx"""
        # 视图执行前, 需要执行的操作
        res = view(request, *args, **kwargs)
        # 视图执行后, 需要执行的操作
        return res

    return func2
```



## 2.1 隐式装饰

利用as_view方法的执行, 来实现装饰功能的完成

```python
class Handle1(View):
    """处理业务1"""

    def as_view(self, *args, **kwargs):
        view = super(Handle1, self).as_view(*args, **kwargs)
        view = func1(view)  # 调用闭包
        return view


class Handle2(View):
    """处理业务2"""

    def as_view(self, *args, **kwargs):
        view = super(Handle2, self).as_view(*args, **kwargs)
        view = func1(view)  # 调用闭包
        return view


class RequestMethod(Handle1, Handle2, View):  # 利用Python广式继承, 将掉as_view拖到View中执行
    """不同的请求使用不同的方法"""

    def get(self, request):
        return HttpResponse("get")

    def post(self, request):
        return HttpResponse("post")
```

## 2.2 类装饰

```python
@method_decorator(func1, name="dispatch")  # 使用于全部方法
# @method_decorator(func1, name="get")  # 使用于GET方法
# @method_decorator(func1, name="post")  # 使用于post方法
class RequestMethod(View):
    """不同的请求使用不同的方法"""

    def get(self, request):
        return HttpResponse("get")

    def post(self, request):
        return HttpResponse("post")
```

## 2.3 方法装饰

```python
class RequestMethod(View):
    """不同的请求使用不同的方法"""
    
	@method_decorator(func1)
    def get(self, request):
        return HttpResponse("get")

    def post(self, request):
        return HttpResponse("post")
```

## 2.4 url装饰

原理类似2.1, 直接通过影响as_view方法来实现装饰

```python
urlpatterns = [
    ...
    path(r"^request_method/$"), func1(request_method.as_view())
]
```



