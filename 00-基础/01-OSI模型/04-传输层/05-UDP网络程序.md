# 1. 发送UDP

## 1.1 UDP服务端

用于接收UDP客户端请求.

```python
# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2020/5/15 9:53
import socket

ip_port = "19.19.19.52", 10010
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ip_port)
while True:
    msg, client_ip_port = sock.recvfrom(500 * 1024)
    print(len(msg))
    print(msg.decode(), client_ip_port)
sock.close()
```

## 1.2 UDP客户端

用于发送UDP报文的

```python
# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2020/5/15 9:49
import socket

ip_port = "111.230.227.23", 8002
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("1你好xx".encode(), ip_port)
sock.close()
```

## 1.3 广播

向一个网段广发请求. 只需要指定ip为发送网段的广播IP, 或者直接使用`<broadcast>`

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = "11.11.11.255", 11111
sock.sendto("message 测试!".encode(), ip_port)
```



