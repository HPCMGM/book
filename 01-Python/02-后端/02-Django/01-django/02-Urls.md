# 1. 路由

## 1.1 Django路由原理

Django使用的路由管理模式为列表管理.

最终的路由信息大概如下:

```python
[
    (url, views_func, namespace, name...),
    (url, views_func, namespace, name...),
    ...
]
```

总路由列表位置(默认): `project/project/urls.py`

## 1.2 路由解析流程

路由的解析流程, 是按照**总路由**从上之下, 依次解析, 如果上层路由没有严格使用正则, 可能会屏蔽下层路由的使用

**实例**:

```python
urlpatterns = [
    url(r"/abc/", view.abc),
    url(r"/abc/abc", view.abc.abc)  # 此url永远无法解析到
]
```



# 2. 正向解析

## 2.1 路由列表

总路由列表

```python
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 后台站点管理端
]
```

列表中的url产生每一项都是一一对应的关系.

默认总路由中会有一个后台站点管理系统url.

## 2.2 路由映射

路由参数url最终参数信息:

```python
def _path(route, view, kwargs=None, name=None, Pattern=None):
```

* route: 带正则的url信息

* view:  

  * 视图函数

    视图函数必须接受一个request对象

    ```python
    def index(request):
        return HttpResponse("helloword")
    ```

  * 基于`as_view`方法的视图类

    继承View并重写需要的方法, 来开起该方法

    ```python
    class RequestTest(View):
        """不同的请求使用不同的方法"""
    
        def get(self, request):
            return HttpResponse("get")
    
        def post(self, request):
            return HttpResponse("post")
    ```

    

  * include:

    由include函数产生的一个三元组, 其中inclue函数参数如下:

    ```python
    def include(arg, namespace=None):
    ```

    * arg:

      * urlconf_module: 子路由模块路径

      * app_name: 

        子路由名称, 也是默认命名空间名称, 主要是在源码中出现了:

        `namespace=namespace or app_name`, 

        只需要在子路由文件中定义此字段即可

        ```python
        from django.conf.urls import url
        
        from user.views import index, RequestTest
        
        app_name = "user"
        
        urlpatterns = [
            url("/test/$", RequestTest.as_view(), name="index"),
            url(r"/", index, name="test"),
        ]
        ```

    * namespace: 命名空间, 用于反向路由查找, 不得重复, 否则后面的配置无效

* kwargs: 用于视图函数增加的关键字参数

  ```python
  # url.py
  urlpatterns = [
      url("/test/$", RequestTest.as_view(), name="index"),
      url(r"/", index, {"a": "b"}, name="test"),
  ]
  
  # view.py
  def index(request, *args, **kwargs):
      """主页"""
      print(args, kwargs)  # () {'a': 'b'}
      return HttpResponse("Hello world")
  ```

  

* name: 一一对应关系, 对当前url进行命名, 不得重复, 但是不会报错.

* Pattern: 路由正则对象, 默认使用`functools.partial`指定关键字对象增加, 不用操作

  ```python
  url = partial(_path, Pattern=RegexPattern)
  ```

# 3. 反向解析

## 3.1 reverse

反向查找主要利用reverse函数实现, 模板中使用url实现

```python
def reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)
```

* viewname: 

  * url命名指定

    `url`影响参数: name

    只会寻找存在的, 如果不存在, 直接报错

    ```python
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
    	url("^aa/", view.as_view, name="aa"),
        url("^bb/", view.as_view, name="aa")
    ]
    ############################
    reverse("aa")
    # /aa/
    出现重复的url命名, 则会优先选用最上层url
    ```

  * 命名空间调用链式

    `url`影响参数:  app_name, namespace

    ```python
    # project/urls.py
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
    	url("^aa/", include("user.urls", namespace="user1")),
        url("^bb/", include("class.urls", namespace="class1"))
    ]
    
    # project/user/urls.py
    app_name = "school"
    urlpatterns = [
        url("aa/", include("dome.urls", namespace="user1")),
    ]
    
    # project/class/urls.py
    app_name = "school"
    urlpatterns = [
        url("bb/", include("dome.urls", namespace="user1")),
    ]
    # project/dome/urls.py
    app_name = "dome"
    urlpatterns = [
        url("dd/", view.as_view, name="aa")
    ]
    ####################################
    映射字典将会是:
        {
            "school": ["user1", "class1"]
        }
    reverse("class1:user1:aa")  # /bb/bb/dd  一般情况下  用这个就行了
    
    reverse("school:user1:aa", current_app="dome:user1") # /bb/bb/dd
    如果和当前请求的url, 在相同的链路上, 也可以使用当前相对路径进行操作
    reverse("school:user1:aa", current_app=request.resolver_match.namespace)
    # /bb/bb/dd
    ```

    

* urlconf: 指定urls模块路径, 默认为`project/urls.py`

* args: 

  重定向到视图函数后, url中正则参数的位置, args与kwargs不能共存

  ```python
  # url: /user/(henan)/
  def index(request, city)
  	...
  # 此时args中参数只能配置一个, 用来表示city
  # 注意args中的参数, 不需要进行处理, 进行进过quote()
  ```

* kwargs: 

  重定向到视图函数后, 增加关键字参数, args与kwargs不能共存, 直接使用关键字指定参数的数值

  ```python
  def index(request, city):
      ...
  # kwargs = {"city": henan}, 直接可以把参数传递到city中去
  ```

* current_app: 

  * viewname决定选择的app_name, viewname是按照`":"`正向遍历
  * current_app决定选择的namespace, current_app是按照`":"`反向遍历

  ```python
  {
      # 在urls中定义的app_name的集合
      app_name1: [namespace1, namespace2],
      app_name2: [namespace1, namespace2]
  }
  ```

# 4. 重定向

## 4.1 redirect

```python
def redirect(to, *args, permanent=False, **kwargs)
```

* to

  参数必须为以下三类:

  * model: 一个带有`get_absolute_url()`方法的类
  * reverse: reverse的结果
  * url: 路由中的url

* *args: 

  重定向时候, 指定视图函数的位置参数, 仅在位置参数生效时有用

* permanent:

  此重定向是否为永久重定向, 表示该url被弃用, 永久重定向到下个url中

* **kwargs:

  重定向时候, 指定视图函数的关键字参数, 仅在关键字参数生效时有用

## 4.2 实例

* url重定向

  ```python
  def get(self, request, *args, **kwargs):
  	param = urllib.parse.urlencode(kwargs)
  	return redirect("/users/login/?{}".format(params))
  ```

* view重定向

  ```python
  class Users(View):
      """用户登录授权"""
  
      def get(self, request, *args, **kwargs):
          return redirect(Users)
      
      @staticmethod
      def get_absolute_url():  # 此方法必须为静态方法
          """"""
          return "login"  # 返回的url将会和当前url叠加
      
  # 假设当前url为: http://localhost/user
  # 则重定向为: http://localhost/user/login
  # 也可以直接用完整url: http://www.baidu.com/  这样就不会叠加了
  
  ```

# 5. url参数解析

## 5.1 位置参数

* url

  ```python
  r"^weather/(beijing)/(2020)/$"
  ```

  

* views

  ```python
  def weather(request, city, years):  # 一定要一一对应
      print(city, years)  # beijing 2020
  ```

  

## 5.2 关键字参数

* url

  ```python
  r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$'
  ```

  

* views

  ```python
  def weather(request, years, city):
  	print(years, city)  # 2020 beijing
  ```






