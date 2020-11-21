# 1. 发送TCP

## 1.1 TCP服务端

接受客户端请求信息

```python
# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2020/5/15 15:37
import socket


ip_port = "0.0.0.0", 1050
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 端口复用
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定ip及端口
sock.bind(ip_port)
# 配置连接上限
sock.listen(128)
print("服务已启动: {}".format(ip_port))
while True:
    client_sock, client_ip_port = sock.accept()
    print("用户 {} 已接入!".format(client_ip_port))
    msg = client_sock.recv(1024)
    print(msg.decode())
    if msg == b"q":
        break
    client_sock.send(msg)
    client_sock.close()
sock.close()
```

## 1.2 TCP客户端

发往服务端客户信息

```python
# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2020/5/15 15:43
import socket

ip_port = "19.19.19.52", 1050
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ip_port)
sock.send("11你好xx".encode())
sock.close()
```