# 1. http协议

超文本传输协议（HyperText Transfer Protocol）是一种应用层协议

# 2. 请求报文

## 2.1 请求行(Request line)

```python
GET / HTTP/1.1\r\n 
```

**说明:**

 1. 提交方式 

    GET: 

    POST:

    PUT:

    DELETE:

    OPTION:

    HEAD:

 2. 统一资源定位符

    /xx
    
 3. 协议及版本号
   
    HTTP/1.1

## 2.2 请求头(Request head)

```python
Host: www.baidu.com:80\r\n
# IP:端口或者域名, 必须有这个 下面的不是必须的
Connection: keep-alive\r\n
# 长连接--1.1基本都是长连接
Upgrade-Insecure-Requests: 1\r\n
# 表示可以接受http格式数据
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36\r\n
# 用户代理: 系统版本和浏览器版本
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n
# 接受汇总: 表示能接受什么类型
Accept-Encoding: gzip, deflate\r\n
# 可以接受的压缩方式
Accept-Language: zh-CN, zh; q=0.9\r\n
# 可以接受的语言类型, 优先级高的为1, 其次0.9
\r\n
# 换行符  后面还有请求体
```

## 2.3 请求体(Request body)

```python
需要发送的内容
```

# 3. 响应报文

## 3.1 响应行(Response line)

```python
HTTP/1.1 200 OK\r\n
```

**说明:**

 1. 协议及版本号

    HTTP/1.1

 2. 状态码

    2xx: 成功

    3xx: 重定向

    4xx: 请求失败

    5xx: 服务器异常

 3. 状态码的解释

    ok

## 3.2 响应头(Response head)

```python
Connection: Keep-Alive
# 长连接
Content-Encoding: gzip
# 压缩类型
Content-Type: text/html; charset=utf-8
# text(大类)/html(小类)
Date: Wed, 14 Mar 2018 09:52:48 GMT
# 服务器上次开启时间
Server: BWS/1.1
# 服务器名字
```

## 3.3 响应体(Response body)

```python
回应内容本体
```

# 4. HTTP通讯

## 4.1 浏览器

```python
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("www.baidu.com", 80))

# 创建请求报文
request_line = "GET / HTTP/1.1" + "\r\n"
request_head = "Host: www.baidu.com" + "\r\n\r\n"
request_body = "xx"
request_data = request_line + request_head + request_body

c.send(request_data.encode())
response_data = c.recv(5*1024).decode()

# 解析相应报文
res = response_data.split("\r\n\r\n")
response_line, response_head = res[0].split("\r\n", 1)
response_body = res[1:]
print(response_line)
print(response_head)
print(response_body)
```

## 4.2 服务器

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:hpcm
# datetime:19-3-6 下午4:25
import os
import re
import socket
from threading import Thread


# noinspection PyTypeChecker
class HttpServer(object):
    """创建HTTP服务器"""
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip_port = "", 8888
        self.block_list = []
        self.base_path = os.path.dirname(__file__)

    def set_socket(self):
        """设置服务器"""
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server.bind(self.ip_port)
        self.server.listen(128)

    def scheduler(self, client, ip_port):
        """中心调度"""
        if ip_port[0] in self.block_list:
            client.close()
            return
        request_data = client.recv(5 * 1024).decode()
        if not request_data:
            client.close()
            return
        try:
            request_headers, request_body = request_data.split("\r\n")
        except ValueError:
            request_headers = request_data
            request_body = ""
        request_line, *request_head = request_headers.split("\r\n")
        method, path, protocol = request_line.split()
        if not protocol.startswith("HTTP"):
            client.send("Not support {} protocol!".format(protocol).encode())
            client.close()
            return
        if re.findall(r"\.\w+?$", path, re.S):
            # 静态文件
            response_line, response_head, response_body = self.static_file(client, path, request_head, request_body)
        else:
            # 动态资源
            if method == "GET":
                response_line, response_head, response_body = self.get_method(client, path, request_head, request_body)
            elif method == "POST":
                response_line, response_head, response_body = self.post_method(client, path, request_head, request_body)
            else:
                client.send("Not support {} method!".format(method).encode())
                client.close()
                return
        response = response_line + "\r\n" + response_head + "\r\n\r\n" + response_body
        client.send(response.encode())
        client.close()

    def static_file(self, client, path, request_head, request_body):
        """处理静态文件"""
        response_line = "HTTP/1.1 200 OK"
        response_head = "Content-Type: text/html; charset=utf-8\r\nServer: BWS/1.1\r\nConnection: Keep-Alive"
        try:
            print("get static file...")
            with open(os.path.join(self.base_path, path[1:]), "r") as f:
                content = f.read()
            return response_line, response_head, content
        except FileNotFoundError:
            response_line = "HTTP/1.1 400 NotFountFile"
            return response_line, response_head, "Not found file in path: {}".format(path)

    def get_method(self, client, path, request_head, request_body):
        response_line = "HTTP/1.1 200 OK"
        response_head = "Content-Type: text/html; charset=utf-8\r\nServer: BWS/1.1\r\nConnection: Keep-Alive"
        try:
            print("method get for url...")
            with open(os.path.join(self.base_path, path[1:-1]), "r") as f:
                content = f.read()
            return response_line, response_head, content
        except FileNotFoundError:
            response_line = "HTTP/1.1 400 NotFountFile"
            return response_line, response_head, "Not found file in path: {}".format(path)

    def post_method(self, client, path, request_head, request_body):
        print(request_head)

    def start(self):
        """启动"""
        self.set_socket()
        print("server is start...")
        try:
            while True:
                client_info = self.server.accept()
                t = Thread(target=self.scheduler, args=client_info)
                t.start()
        except KeyboardInterrupt:
            print("server is stop!")
            self.server.close()


if __name__ == "__main__":
    hs = HttpServer()
    hs.start()
```

