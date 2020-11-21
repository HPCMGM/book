# 1. Django-CORS

## 1.1 跨域请求

* 同源

  表示使用的协议, 域名和端口号是相同的

* 跨域

  * 浏览器的限制行为
  * 了安全限制一个源的js不能读写另一个源的资源
  * 通过src等标签嵌入url可以跨域, 但是js不能获取跨域页面中加载的数据

跨域请求是浏览器对js的一种限制策略, 想要突破这种限制, 可以使用

* cors

  cross-origin-resource sharing

* document.domain

* cross-document messaging

## 1.2 修改本地hosts

操作文件: `/etc/hosts`, 追加如下信息:

```bash
127.0.0.1    api.meiduo.site
127.0.0.1    www.meiduo.site
```

这样就可以直接通过域名的形式来访问当前主机了

## 1.3 安装cors

```bash
pip install django-cors-headers
```

# 2. cors配置

## 2.1 setting

```Python
# APP配置
INSTALLED_APPS = {
    ...
    "corsheaders", # 注册app
}

# 中间件配置
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware"  # 注意中间件应该放到最上面
    ...
]

# 白名单配置
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:8080',
    'localhost:8080',
    'www.meiduo.site:8080'
)

# 允许跨域携带cookie
CORS_ALLOW_CREDENTIALS = True

# 允许跨域访问的主机
ALLOWED_HOSTS = ["127.0.0.1", "api.meiduo.site"]  # 配置允许访问的主机
```

