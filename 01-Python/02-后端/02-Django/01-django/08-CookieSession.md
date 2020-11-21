# 1. cookie

cookie是基于`HttpResponseBase`进行操作的, 所有继承`HttpResponseBase`的类均可以用此方法操作

## 1.1 设置

### 1.1.1 参数

| 参数     | 类型     | 默认值  | 说明                                                         |
| -------- | -------- | ------- | ------------------------------------------------------------ |
| key      | str      |         | cookie的键                                                   |
| value    | str      | `""`    | cookie的值                                                   |
| max_age  | int      | `None`  | 常用这个参数, 存活最长时间(s), None表示关闭浏览器就过期      |
| expires  | datetime | `None`  | 达到什么时候过期, None表示关闭浏览器就过期                   |
| path     | str      | `'/'`   | 指定cookie在指定的url域中有效                                |
| domain   | str      | `None`  | cookie作用域名, 注意要在域名前加`"."`                        |
| secure   | bool     | `False` | True, cookie只能在`HTTPS`, `SSL`协议中被解析                 |
| httponly | bool     | `False` | True, cookie不允许js读取                                     |
| samesite | str      | `None`  | (Strict/Lax/None)<br>Strict: 表示禁用跨站cookie传输<br>Lax: 预加载有效<br>None: Cookie 只能通过 HTTPS 协议发送 |



### 1.1.2 实例

```python
def get(self, request):
    response = HttpReponse()
	response.set_cookie(key, value='', max_age=None, expires=None, path='/',
                   domain=None, secure=False, httponly=False, samesite=None)
    return reponse
```



## 1.2 获取

### 1.2.1 参数

此类型为`dict`, 支持其所有的方法

| 参数  | 类型 | 默认值 | 说明             |
| ----- | ---- | ------ | ---------------- |
| Slice |      |        | 支持字典切片语法 |
| get   |      |        |                  |
| items |      |        |                  |
| keys  |      |        |                  |
| pop   |      |        |                  |
| clear |      |        |                  |
| ...   |      |        |                  |

### 1.2.2 实例

```python
def del(self, request):
    request.COOKIES.get(key)
    request.COOKIES.clear()
    return reponse
```



## 1.3 删除

同上

# 2. session

session是由`request.session`对象来守护的.

## 2.1 对象操作

### 2.1.1  配置

如果要使用redis, 需要安装

```python
pip install django-redis==2.10.6
```

* 储存配置

  * 数据库:

    ```python
    SESSION_ENGINE = "django.contrib.sessions.backends.db"
    ```

  * redis:

    ```python
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    ```

  * redis与数据库混合储存

    优先redis

    ```python
    SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
    ```

* 配置server端缓存

  ```python
  CACHES = {
      "default": {
          "BACKEND": "django_redis.cache.RedisCache",
          "LOCATION": "redis://127.0.0.1:6379/1",
          "OPTIONS": {
              "CLIENT_CLASS": "django_redis.client.DefaultClient",
          }
      }
  }
  ```

* 使用缓存

  ```python
  SESSION_CACHE_ALIAS = "default"
  ```

  

### 2.1.2 方法

| 方法                   | 参数                                                         | 返回值 | 说明                                               |
| ---------------------- | ------------------------------------------------------------ | ------ | -------------------------------------------------- |
| splice                 | key, 切片操作                                                |        | 支持切片操作(设置/删除)                            |
| flush                  |                                                              |        | 清空缓存数据, 如果为混合缓存模式, 将会同步到数据库 |
| clear                  |                                                              |        | 清空缓存数据, 不会同步到数据库                     |
| clear_expired          |                                                              |        | 清空过期的session                                  |
| get                    | key: session键<br>default: 缺省值                            | any    | 获取session值                                      |
| get_session_cookie_age |                                                              | int    | 从配置文件中获取session_cookie_age的值             |
| create                 |                                                              |        | 创建缓存字段, 内部操作, 无需手动执行               |
| save                   |                                                              |        | 创建缓存字段, 内部操作, 无需手动执行               |
| has_key                | key: session键                                               | bool   | 检测session键, 是否存在                            |
| is_empty               |                                                              | bool   | 检测session是否为空                                |
| items                  |                                                              | item   | 返回key, value二元组的可迭代对象                   |
| keys                   |                                                              | keys   | 返回keys                                           |
| load                   |                                                              | dict   | 重载(redis/db)所有session, 并组包为dict            |
| pop                    | key, default=object()                                        | any    | 删除并返回一个session值                            |
| save                   |                                                              |        |                                                    |
| set_expiry             | value: timedelta/int/None, 设置超时时间, 如果为None, 表示立即失效 |        | 配置session过期时间                                |
| setdefault             | key, value                                                   | any    | 类似字典, 设置一个缺省值, 并返回设置后的value      |
| update                 | dict_                                                        |        | 类似字典, 批量添加key, value                       |
| values                 |                                                              | values | 返回values                                         |

### 2.1.3 属性

| 属性             | 返回值 | 说明                                                         |
| ---------------- | ------ | ------------------------------------------------------------ |
| accessed         | bool   | request的上下文中是否对session进行过访问                     |
| modified         | bool   | 是否session进行的任何操作                                    |
| cache_key        | str    | 由模块路径+32位的随机数组成的, 缓存数据的key                 |
| cache_key_perfix | str    | 模块路径, 默认为`"django.contrib.sessions.cache"`            |
| serializer       | object | session用于序列化的模块, 默认读取setting`SESSION_SERIALIZER` |
| session_key      | str    | 当前session 的key                                            |

## 2.2 实例

### 2.2.1 增加

```python
def ssession(request):
    res = HttpResponse("set session")
    request.session["key"] = 1
    return HttpResponse("set session")
```

### 2.2.2 查询

```python
def gsession(request):
    print(request.session.get("key"))
    return HttpResponse("get session")
```



### 2.2.3 删除

```python
ef dsession(request):
    request.session.clear()
    return HttpResponse("del session")
```

