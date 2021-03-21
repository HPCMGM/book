# 1. VMware网络配置

* 打开虚拟网络编辑器

  ![190adf68-931c-45ea-b134-506849fbadeb](image/10-Nat%E9%85%8D%E7%BD%AE/190adf68-931c-45ea-b134-506849fbadeb.jpg)

* 随便选择一张虚拟网卡, 进行如下配置

  ![image-20200924221107830](image/10-Nat%E9%85%8D%E7%BD%AE/image-20200924221107830.png)

* 配置网关和IP范围

  ![image-20200924221411122](image/10-Nat%E9%85%8D%E7%BD%AE/image-20200924221411122.png)

# 2. 虚拟机配置

* 选择当前虚拟机, 配置使用的网卡

  ![image-20200924221559714](image/10-Nat%E9%85%8D%E7%BD%AE/image-20200924221559714.png)

![image-20200924221658840](image/10-Nat%E9%85%8D%E7%BD%AE/image-20200924221658840.png)

然后进入系统, 开始配置网卡

## 5.1 RedHat

操作文件: `/etc/sysconfig/network-scripts/ifcfg-eth0`

```bash
DEVICE=eth0
BOOTPROTO=static
HWADDR=00:0C:29:F1:99:61  # 此数据通过ifconfig中可以直接复制
IPV6INIT=yes
NM_CONTROLLED=yes
ONBOOT=yes
TYPE=Ethernet
UUID=d808f1da-912d-4ec2-a5a2-9280744bfa1d
USERCTL=no
IPADDR=19.19.19.12
NETMASK=255.255.255.0
GATEWAY=19.19.19.2
DNS1=8.8.8.8
DNS2=8.8.4.4
```

重启网卡

```bash
service network restart
```

能正常进行如下测试, 说明配置成功

```bash
# redhat内
ping www.baidu.com
ping 19.19.19.1
# 宿主机
ping 19.19.19.12
```





