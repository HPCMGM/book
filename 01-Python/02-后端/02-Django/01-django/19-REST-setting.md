# 1. 用户认证

## 1.1 认证

认证方式有两种配置方案

* 全局在`django.setting.py`中配置, 可以作用去全部视图函数
* 可以以在定义视图函数时加入`authentication_classes`来限制

### 1.1.1 认证配置

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',   # 基本认证
        'rest_framework.authentication.SessionAuthentication',  # session认证
    )
}
```

### 1.1.2 视图配置

```python
class ExampleView(APIView):
    permission_classes = (IsAuthenticated,)
    ...
```



# 2. 用户权限

## 2.1 权限

权限方式有两种配置方案

* 全局在`django.setting.py`中配置, 可以作用去全部视图函数
* 可以以在定义视图函数时加入`permission_classes`来限制

### 1.1.1 权限配置

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # 进行认证登录
        'rest_framework.permissions.AllowAny',  # 允许任何人
    )
}
```

### 1.1.2 视图配置

```python
class ExampleView(APIView):
    permission_classes = (IsAuthenticated,)
    ...
```

## 2.2 自定义权限

```python
class MyPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        """控制对obj对象的访问权限，此案例决绝所有对对象的访问"""
        return False

class BookViewSet(ModelViewSet):
    queryset = Book.query.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticated, MyPermission]
```



# 3. 限流

## 3.1 全局配置

```python
REST_FRAMEWORK = {
        'DEFAULT_THROTTLE_CLASSES': (
            'rest_framework.throttling.AnonRateThrottle',
            'rest_framework.throttling.UserRateThrottle'
        ),
        'DEFAULT_THROTTLE_RATES': {
            'anon': '100/day',    # 未登录用户
            'user': '1000/day'    # 登陆用户
        }
    }
```

* DEFAULT_THROTTLE_RATES

  可以使用`second`, `minute`, `hour`, `day`来指明周期

## 3.2 视图设置

```python
class ThrottleAPIView(APIView):
    throttle_classes = (UserRateThrottle, )
    ...
```



