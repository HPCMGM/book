# 1. 缓存

## 1.1 安装

```python
pip install drf-extensions
```

## 1.2 hellword

## 1.3 配置信息

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://10.0.0.12:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

REST_FRAMEWORK_EXTENSIONS = {
    # 缓存时间
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60,
    # 缓存存储
    'DEFAULT_USE_CACHE': 'default',
}

```



# 2. 使用

## 2.1 普通使用

普通函数构建的视图函数, 视图类, 直接装饰对应的函数即可

```python
class FooView(views.APIView):
    @cache_response(timeout=60*60, cache='default') # 缓存时间/redis库名
    def get(self, request, *args, **kwargs):
        pass
```

## 2.2 视图集

视图集由于修改了对应的状态, 所以框架也提供了相对应的`mixins`来使用

* ListCacheResponseMixin: 缓存动作`list`数据
* RetrieveCacheResponseMixin: 缓存动作`retrieve`数据
* CacheResponseMixin: 缓存动作`list+retrieve`数据

```python
class FooView(CacheResponseMixin, ReadOnlyModelViewSet):
    pass
```

