# 1. 内置说明

* BASE_DIR:  项目根目录

  ```python
  BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
  ```

* SECRET_KEY

  秘钥, 用于csrf/登录等鉴权认证, 必须设置而且要保密.

  ```python
  SECRET_KEY = 'ij%&yqiwel1+ofck2of#g45z+0q(#u_-wxxgpz$juje8r_z))c'
  ```

* DEBUG:

  是否开启调试模式, True为开启, 异常全部输出到页面, 检测代码变动并重载项目.

  ```python
  DEBUG = True
  ```

* ALLOWED_HOSTS

  限制ip/域名访问, 指定可以访问的host, 域名.

  ```python
  ALLOWED_HOSTS = ["127.0.0.1"]  # 只能当前主机进行访问
  ```

* INSTALLED_APPS

  激活需要使用的app, 如果没有激活则不会开启对应的功能. 所以每次创建app后一定要先添加app

  ```python
  INSTALLED_APPS = [
      'django.contrib.admin', # 后台站点
      'django.contrib.auth', # 权限认证
      'django.contrib.contenttypes',  # 模型控制
      'django.contrib.sessions',  # session
      'django.contrib.messages',  # 模板消息推送
      'django.contrib.staticfiles', # 静态文件
      "user.apps.UserConfig"
  ]
  ```

* MIDDLEWARE

  中间件控制, 执行顺序是由上到下,  数据返回是由下到上

  ```python
  MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      # 'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
  ]
  ```

* ROOT_URLCONF

  指定url路由所在模块, 需要可以用`__import__()`导入的

  ```python
  ROOT_URLCONF = 'config.urls'
  ```

* TMEPLATES

  模板控制参数

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

* WSGI_APPLICATION

  指定wsgi模块所在的路径, 需要可以用`__import__()`导入

  ```python
  WSGI_APPLICATION = 'config.wsgi.application'
  ```

* DATABASES

  数据库配置, 默认为sqlite

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      }
  }
  ```

* AUTH_PASSWORD_VALIDATORS

  用户密码认证系统.

  ```python
  AUTH_PASSWORD_VALIDATORS = [
      {
          'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
      },
      {
          'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
      },
  ]
  ```

* LANGUAGE_CODE
  项目语言类型, 默认英文, 中文为: `'zh-hans'`, 会对后台站点页面有很大的影响

  ```python
  LANGUAGE_CODE = 'en-us'  # 'zh-hans'
  ```

* TIME_ZONE

  时区配置, 默认为UTC. 中国时区可以使用: `Asia/Shanghai`

  ```python
  TIME_ZONE = 'UTC'  # 'Asia/Shanghai'
  ```

* USE_I18N

  是否让项目支持国际化, 影响: 语言/时区

  ```python
  USE_I18N = True
  ```
  
* USE_L10N

  设置为True，则区域设置指定的格式具有更高的优先级

  ```python
  USE_L10N = True
  ```

* USE_TZ

  使用系统时区

  ```python
  USE_TZ = True
  ```

* STATIC_URL 

  静态文件url配置

  ```python
  STATIC_URL = '/static/'
  ```



# 2. 数据库

## 2.1 配置

### 2.1.1 sqlite

* sqlite

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      }
  }
  ```
### 2.1.2 mysql

使用数据库前, 注意引擎声明

```python
from pymysql import install_as_MySQLdb:
install_as_MySQLdb()
```
然后配置文件如下:
```python
DATABASES = {
    "default": {
            "ENGINE": "django.db.backends.mysql",
            "HOST": "localhost",
            "PORT": 3306,
            "USER": "django_project",
            "PASSWORD": "dong10",
            "NAME": "db_Django_project"
        }
}
```

### 2.1.3 redis

```python
CACHES = {
            "default": {
                "BACKEND": "django_redis.cache.RedisCache",
                "LOCATION": "redis://127.0.0.1:6379/0",
                "OPTIONS": {
                    "CLIENT_CLASS": "django_redis.client.DefaultClient",
                }
            },
            "session": {  # 重新指定一个库是给admin站点使用的
                "BACKEND": "django_redis.cache.RedisCache",
                "LOCATION": "redis://127.0.0.1:6379/1",
                "OPTIONS": {
                    "CLIENT_CLASS": "django_redis.client.DefaultClient",
                }
            }
        }
```

## 2.2 缓存配置

### 2.2.1 session

```python
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"  # 取值于CACHES
```



# 3. 路径

## 3.1 静态文件

### 3.1.1 静态文件读取配置

**注意**: 当Django参数DEBUG配置为False时, 将会禁用web访问静态文件的权限, 所以需要使用nginx做负载.

```python
STATIC_URL = '/static/'  # 指定静态文件url前缀
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'user'),  # 指定静态文件读取路径
]

#####################  配置路由  ##########################################
# urls.py
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path(r'static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    path(r"admin/", admin.site.urls),
]
#####################  静态文件访问  ##########################################

# 也可以直接这样追加静态路由
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
# http://127.0.0.1:8000/static/index.html  即可访问./statics/index.html文件
```

* STATIC_URL: 静态文件url前缀配置

* STATIC_ROOT: 指定静态文件存放根目录

* STATICFILES_DIRS:

  指定静态文件存放目录, 也可以这样配置:

  ```python
  STATICFILES_DIRS = [
      ("user", os.path.join(BASE_DIR, 'user/img')),  # 指定静态文件读取路径
  ]
  # http://127.0.0.1:8000/static/user/index.html  即可访问./statics/user/img/index.html文件
  ```


### 3.1.2 项目静态文件采集

收集项目中全部的静态文件, 用于nginx动静分离

```Python
# setting.py
# 指定静态文件的输出路径
STATICS_ROOT = os.path.join(os.path.dirname(BASE_DIR), "front/static")
```

命令行执行如下命令, 开始对静态文件进行采集

```bash
python manage.py collectstatic
```

## 3.2 模板文件

### 3.3 日志配置

```python
LOGGING = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'verbose': {
                    'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
                },
                'simple': {
                    'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
                },
            },
            'filters': {
                'require_debug_true': {
                    '()': 'django.utils.log.RequireDebugTrue',
                },
            },
            'handlers': {
                'console': {
                    'level': 'DEBUG',
                    'filters': ['require_debug_true'],
                    'class': 'logging.StreamHandler',
                    'formatter': 'simple'
                },
                'file': {
                    'level': 'INFO',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': os.path.join(BASE_DIR, "logs/running.log"),  # 日志文件的位置
                    'maxBytes': 300 * 1024 * 1024,
                    'backupCount': 10,
                    'formatter': 'verbose'
                },
            },
            'loggers': {
                'django': {  # 定义了一个名为django的日志器
                    'handlers': ['console', 'file'],
                    'propagate': True,
                },
            }
        }
```



# 4. 权限

## 4.1 CORS

跨域请求, 白名单配置

```Python
ALLOWED_HOSTS = ["xxx.hpcm.site", "api.hpcm.site", "127.0.0.1"]
CORS_ORTGIN_WHITELIST = (
    '127.0.0.1:8080',
    'localhost:8080',
    "xxx.hpcm.site:8080",
    "xxx.hpcm.site"
)
```

配置完成即可跨域访问

# 5. DRF

## 5.1 日志处理

```python
 REST_FRAMEWORK = {
                # 异常处理
                'EXCEPTION_HANDLER': 'utils.exceptions.exception_handler',
            }
```





