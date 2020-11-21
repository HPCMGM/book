# 1. 网络通讯三要素

* IP

  确定主机网络及物理位置

* 协议

  保证通讯数据正常无误

* 端口

  指明网络程序的地址

# 2. 套接字

套接字(socket),  应用程序可以通过它发送或接收数据，可对其进行像对文件一样的打开、读写和关闭等操作。套接字允许应用程序将I/O插入到网络中，并与网络中的其他应用程序进行通信。网络套接字是IP地址与端口的组合。

## 2.1 创建socket

```python
import socket
# 创建套接字
sock = socket.socket(AddressFamily, Type)
# 端口复用
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 关闭套接字(流对象)
sock.close()
```

**说明:**

* AddressFamily

  AF_INET: Internet通讯

  AF_UNIX: 同一台机器的进程通讯

* Type

  SOCK_STREAM: TCP通讯

  SOCK_DGRAM: UDP通讯

## 2.1 socket使用流程

1. 创建套接字
2. 使用套接字收发数据
3. 关闭套接字

