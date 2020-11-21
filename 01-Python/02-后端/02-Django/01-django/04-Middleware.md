# 1. 默认

# 2. 自定义

注意:

* 中间件, 请求前执行, 顺序为从上到下
* 中间件, 响应后执行, 顺序为从下到上

## 2.1 准备中间件

```python
def middleware_begin(get_response):
    print("项目已启动!")   # 相当于flask中的 before_first_reuqest
    def middleware_after(request):
        print("访问视图函数前的预处理!")  # 相当于flask中的 before_request
        response = get_response(request)
        print("返回给client之前进行干预!")  # 相当于 after_request
        return response
    return middleware_after
```

## 2.2 载入中间件

```python
MIDDLEWARE = [
    'users.middleware.middleware_begin',
]
```

# 3. 项目启动时仅执行一次

1. 配置启动事宜

   ```python
   # 操作文件: /app/apps.py
   
   from django.apps import AppConfig
   
   
   class UsersConfig(AppConfig):
       name = 'users'
   
       def ready(self):
           print("only execute once!")
   ```

2. 设置需要加载的内容

   ```python
   # 操作文件: /app/__init__.py
   
   default_app_config = 'app.apps.AppConfig'
   ```

3. 安装APP

   ```python
   # 操作文件: /project/settings.py
   
   INSTALLED_APPS = [
       ...
       "app"
   ]
   ```

   



