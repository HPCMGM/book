# 1. Flask

## 1.1 app实例化

```python
from flask import Flask
app = Flask(__name__)
```

Flask对象`__init__`方法如下

```python
def __init__(
        self,
        import_name,
        static_url_path=None,
        static_folder='static',
        static_host=None,
        host_matching=False,
        subdomain_matching=False,
        template_folder='templates',
        instance_path=None,
        instance_relative_config=False,
        root_path=None
    )
```

**说明:**

* import_name

  实例化app所在路径, 一般使用`__name__`来自动识别. 此参数会用来动态的确定静态文件、模板文件位置等, 所以尽量使用`__name__`

* static_url_path

  静态文件的前缀, 默认等于`static_folder`

* static_folder

  静态文件名称

* static_host

  静态文件所在IP, 如果配置后需要设置`host_matching=True`和`static_folder`

* host_matching

  设置主机匹配的路由映射

* subdomain_matching

  子域名匹配

* template_folder

  模板文件夹

* instance_path

  读取实例包

* instance_relative_config

  是否配置实例文件夹

* root_path

  读取实例文件

## 1.2 路径问题

模板文件: $\__name__ + static_url_path + static_folder

静态文件: $\__name__ + template_folder

# 2. 视图函数

视图函数用于业务逻辑处理, 常见的增删改查等操作. 一般用装饰器来增加路由

```python
@app.route("/")
def index():
    import datetime
    return "<h1>{}</h1>".format(datetime.datetime.now())
```



# 3. 启动服务

web服务启用很简单, 只需要调用`app.run()`即可指定进入监听状态, 默认监听`127.0.0.1`的5000端口

```python
app.run()
```

方法参数如下

```python
app.run(self, host=None, port=None, debug=None, load_dotenv=True, **options)
```

**说明:**

* host

  指定监听的IP, 如果在`app.config["HOST"]`已经配置, 则此参数无效, 下列参数均是如此

* port

  指定监听的端口

* debug

  是否开启DEBUG模式

  1. 自动监听代码变动并重启服务,  
  2. 如果程序发生错误, 会在客户端输出详细日志
  3. 日志打印比较详细等

* load_dotenv

  运行环境控制

* options

  此参数处理在werkzeug.serving.run_simple中, 有以下参数

  * application
    WSGI协议中的app
  * use_reloader=False
    服务重启后是否重载模块
  * use_debugger=False
    是否开启werkzeug的debug模式
  * use_evalex=True
    是否启用异常推断功能
  * extra_files=None
    服务重新启动后, 重新加载其他的文件 list
  * reloader_interval=1
    重新加载的秒数限制
  * reloader_type='auto'
    stat/watchdog, 重载模式
  * threaded=False
    是否为每个请求开一个线程
  * processes=1
    是否为每一个请求开启一个进程，直到达到设置的并发进程的最大值
  * request_handler=None
    请求处理器, 默认值为BaseHTTPServer.BaseHTTPRequestHandler
  * static_files=None
    静态文件路径(list)
  * passthrough_errors=False
    如果出现异常是否直接挂掉服务(一般用于调试)
  * ssl_context=None
    ssl认证, type(cert_file, pkey_file)

