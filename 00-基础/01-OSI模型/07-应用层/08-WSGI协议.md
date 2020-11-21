# 1. URL种类

## 1.1 静态

访问的文件在服务端是真实存在的, 一般以*.html, *.jpg等形式存在

```python
http://www.baidu.com/index.html
http://www.baidu.com/index.html?a=1&b=2
```



## 1.2 动态

访问的url, 是不存在的, 调用本地代码, 对数据进行修改, 再把处理后的信息发送出来

```python
http://www.baidu.com/api/news
http://www.baidu.com/api/news?a=1&b=2
```

## 1.3 伪静态

看起来像静态url, 但是也是逻辑地址，不存在物理地址

```python
http://www.baidu.com/index.html
http://www.baidu.com/index.html?a=1&b=2
```

# 2. WSGI协议

不修改服务器和架构代码而确保可以在多个架构下运行web服务器. 让服务器不在处理数据, 将所有的请求发送给指定WSGI来处理, 直接提供数据即可.

## 2.1 WSGI框架

```python
def application(environ, start_response):
    """遵循wsgi协议的应用程序"""
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return response_body
```

### 2.1.1 传入参数

* environ(字典)

  包含客户端访问时携带的所有信息

  ```python
  {
      "HTTP_ACCEPT_LANGUAGE": "zh-cn",
      "wsgi.file_wrapper": <built-infunctionuwsgi_sendfile>,
      "HTTP_UPGRADE_INSECURE_REQUESTS": "1",
      "uwsgi.version": b"2.0.15",
      "REMOTE_ADDR": "172.16.7.1",
      "wsgi.errors": <_io.TextIOWrappername=2mode="w"encoding="UTF-8">,
      "wsgi.version": (1,0),
      "REMOTE_PORT": "40432",
      "REQUEST_URI": "/",
      "SERVER_PORT": "8000",
      "wsgi.multithread": False,
      "HTTP_ACCEPT": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "HTTP_HOST": "172.16.7.152: 8000",
      "wsgi.run_once": False,
      "wsgi.input": <uwsgi._Inputobjectat0x7f7faecdc9c0>,
      "SERVER_PROTOCOL": "HTTP/1.1",
      "REQUEST_METHOD": "GET",
      "HTTP_ACCEPT_ENCODING": "gzip,deflate",
      "HTTP_CONNECTION": "keep-alive",
      "uwsgi.node": b"ubuntu",
      "HTTP_DNT": "1",
      "UWSGI_ROUTER": "http",
      "SCRIPT_NAME": "",
      "wsgi.multiprocess": False,
      "QUERY_STRING": "",
      "PATH_INFO": "/index.html",
      "wsgi.url_scheme": "http",
      "HTTP_USER_AGENT": "Mozilla/5.0(Macintosh;IntelMacOSX10_12_5)AppleWebKit/603.2.4(KHTML,likeGecko)Version/10.1.1Safari/603.2.4",
      "SERVER_NAME": "ubuntu"
  }
  ```

  

* start_response(函数)

  WSGI反向调用server来添加响应头部信息(响应行+响应头)

  ```python
  def start_response(self, status, headers):
      """此函数被usgi框架反向调用"""
      response_headers_default = [
          ("Date": time.time()),
          ("Server": "Python Mini Server")
      ]
      self.headers = [status, response_header_default + headers]
  ```

### 2.1.2 返回参数

* response_body

  经过数据处理后的响应体的数据

## 2.2 WSGI实现

### 2.2.1 服务端

```python
import time
import socket
import sys
import re
import multiprocessing


class WSGIServer(object):
    """定义一个WSGI服务器的类"""

    def __init__(self, port, documents_root, app):

        # 1. 创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2. 绑定本地信息
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("", port))
        # 3. 变为监听套接字
        self.server_socket.listen(128)

        # 设定资源文件的路径
        self.documents_root = documents_root

        # 设定web框架可以调用的函数(对象)
        self.app = app

    def run_forever(self):
        """运行服务器"""

        # 等待对方链接
        while True:
            new_socket, new_addr = self.server_socket.accept()
            # 创建一个新的进程来完成这个客户端的请求任务
            new_socket.settimeout(3)  # 3s
            new_process = multiprocessing.Process(target=self.deal_with_request, args=(new_socket,))
            new_process.start()
            new_socket.close()

    def deal_with_request(self, client_socket):
        """以长链接的方式，为这个浏览器服务器"""

        while True:
            try:
                request = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                print("========>", ret)
                client_socket.close()
                return

            # 判断浏览器是否关闭
            if not request:
                client_socket.close()
                return

            request_lines = request.splitlines()
            for i, line in enumerate(request_lines):
                print(i, line)

            # 提取请求的文件(index.html)
            # GET /a/b/c/d/e/index.html HTTP/1.1
            ret = re.match(r"([^/]*)([^ ]+)", request_lines[0])
            if ret:
                print("正则提取数据:", ret.group(1))
                print("正则提取数据:", ret.group(2))
                file_name = ret.group(2)
                if file_name == "/":
                    file_name = "/index.html"

            # 如果不是以py结尾的文件，认为是普通的文件
            if not file_name.endswith(".py"):

                # 读取文件数据
                try:
                    f = open(self.documents_root+file_name, "rb")
                except:
                    response_body = "file not found, 请输入正确的url"

                    response_header = "HTTP/1.1 404 not found\r\n"
                    response_header += "Content-Type: text/html; charset=utf-8\r\n"
                    response_header += "Content-Length: %d\r\n" % (len(response_body))
                    response_header += "\r\n"

                    response = response_header + response_body

                    # 将header返回给浏览器
                    client_socket.send(response.encode('utf-8'))

                else:
                    content = f.read()
                    f.close()

                    response_body = content

                    response_header = "HTTP/1.1 200 OK\r\n"
                    response_header += "Content-Length: %d\r\n" % (len(response_body))
                    response_header += "\r\n"

                    # 将header返回给浏览器
                    client_socket.send(response_header.encode('utf-8') + response_body)

            # 以.py结尾的文件，就认为是浏览需要动态的页面
            else:
                # 准备一个字典，里面存放需要传递给web框架的数据
                env = {}
                # 存web返回的数据
                response_body = self.app(env, self.set_response_headers)

                # 合并header和body
                response_header = "HTTP/1.1 {status}\r\n".format(status=self.headers[0])
                response_header += "Content-Type: text/html; charset=utf-8\r\n"
                response_header += "Content-Length: %d\r\n" % len(response_body)
                for temp_head in self.headers[1]:
                    response_header += "{0}:{1}\r\n".format(*temp_head)

                response = response_header + "\r\n"
                response += response_body

                client_socket.send(response.encode('utf-8'))

    def set_response_headers(self, status, headers):
        """这个方法，会在 web框架中被默认调用"""
        response_header_default = [
            ("Data", time.ctime()),
            ("Server", "my-python mini web server")
        ]

        # 将状态码/相应头信息存储起来
        # [字符串, [xxxxx, xxx2]]
        self.headers = [status, response_header_default + headers]


# 设置静态资源访问的路径
g_static_document_root = "./html"
# 设置动态资源访问的路径
g_dynamic_document_root = "./web"

def main():
    """控制web服务器整体"""
    # python3 xxxx.py 7890
    if len(sys.argv) == 3:
        # 获取web服务器的port
        port = sys.argv[1]
        if port.isdigit():
            port = int(port)
        # 获取web服务器需要动态资源时，访问的web框架名字
        web_frame_module_app_name = sys.argv[2]
    else:
        print("运行方式如: python3 xxx.py 7890 my_web_frame_name:application")
        return

    print("http服务器使用的port:%s" % port)

    # 将动态路径即存放py文件的路径，添加到path中，这样python就能够找到这个路径了
    sys.path.append(g_dynamic_document_root)

    ret = re.match(r"([^:]*):(.*)", web_frame_module_app_name)
    if ret:
        # 获取模块名
        web_frame_module_name = ret.group(1)
        # 获取可以调用web框架的应用名称
        app_name = ret.group(2)

    # 导入web框架的主模块
    web_frame_module = __import__(web_frame_module_name)
    # 获取那个可以直接调用的函数(对象)
    app = getattr(web_frame_module, app_name) 

    # print(app)  # for test

    # 启动http服务器
    http_server = WSGIServer(port, g_static_document_root, app)
    # 运行http服务器
    http_server.run_forever()


if __name__ == "__main__":
    main()
```

### 2.2.2 WSGI框架

* Flask 模式

  核心模式: 用闭包方式来自动添加映射关系

```python
import time
import os
import re

template_root = "./templates"

g_url_route = dict()

# ----------更新----------
def route(url):
    def func1(func):
        # 添加键值对，key是需要访问的url，value是当这个url需要访问的时候，需要调用的函数引用
        g_url_route[url] = func
        def func2(file_name):
            return func(file_name)
        return func2
    return func1


@route("/index.py")  # ----------更新----------
def index(file_name):
    """返回index.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        data_from_mysql = "暂时没有数据，请等待学习mysql吧，学习完mysql之后，这里就可以放入mysql查询到的数据了"
        content = re.sub(r"{% raw %}\{%content%\}{% endraw %}", data_from_mysql, content)

        return content


@route("/center.py")  # ----------更新----------
def center(file_name):
    """返回center.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        data_from_mysql = "暂时没有数据,,,,~~~~(>_<)~~~~ "
        content = re.sub(r"{% raw %}\{%content%\}{% endraw %}", data_from_mysql, content)

        return content


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_name = environ['PATH_INFO']
    # ----------更新----------
    try:
        return g_url_route[file_name](file_name)
    except Exception as ret:
        return "%s" % ret
```

* Django模式

  核心模式: 路由列表存储映射关系

```python
import time
import os
import re

template_root = "./templates"

# 用来存放url路由映射
url_route = [
  ("/index.py", index_func),
  ("/center.py", center_func)
]

def index(file_name):
    """返回index.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        data_from_mysql = "暂时没有数据，请等待学习mysql吧，学习完mysql之后，这里就可以放入mysql查询到的数据了"
        content = re.sub(r"{% raw %}\{%content%\}{% endraw %}", data_from_mysql, content)

        return content

def center(file_name):
    """返回center.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        data_from_mysql = "暂时没有数据,,,,~~~~(>_<)~~~~ "
        content = re.sub(r"{% raw %}\{%content%\}{% endraw %}", data_from_mysql, content)

        return content


def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    file_name = environ['PATH_INFO']
    try:
        for k, v in url_route.items():
            if k == file_name:
                return url_route[file_name](file_name)
        else:
            raise("Not found url: {}".format(file_name))
    except Exception as ret:
        return "%s" % ret
```



  

  