# 1. nmap

本模块用于侦探网络中的数据报.

linux命令

```python
ping -c 1 host  # 发送一个包   但是client会收到2个包
nmap -n -sP -PE 192.168.44.2  # 发送一个包, client收到1个包
 
tcpdump -np -i enp0s8 src host 192.168.44.2  # 监听网卡
```

python使用

```python
# 扫描当前局域网的全部主机信息
import nmap
nm = PortScanner()
# 扫描网段为192.168.44.x的全部主机信息
nm.scan("192.168.44.0/24", arguments="-n -sP -PE")
# 获取扫描后的全部hosts
all_hosts = nm.all_hosts()  # 获取全部主机
for host in all_hosts():
    print(nm.scan(hosts="192.168.111.128", arguments="-n -sP -PE"))
```

