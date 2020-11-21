# 1. DHCP协议

## 1.1 IP的获取

主机刚开始连接网络时, 是没有IP的.  所以需要先获取IP:

手动配置:

​		静态IP(statc), 自己手动设置

自动获取: 

​		动态IP(dynamic), 通过DHCP(Dynamic Host Configuration Protocol)服务器获取IP

## 1.2 DHCP获取IP

由于主机接入网络时, 没有IP地址不能发送IP数据报. 但是有MAC地址, 所以可以发送以太网帧. 和arp协议寻找指定ip的mac地址很类似:

* 第一步

  主机接入后, 利用mac地址发送到`ff:ff:ff:ff:ff:ff`广播帧. (DHCP DISCOVER 帧)

* 第二步

  DHCP服务器收到广播后, 回复一个帧.(DHCP OFFER 帧), 此帧包含了IP, 掩码, 有时会有默认网关, DNS等.

* 第三步

  主机收到以太网帧后, 广播发送请求帧(DHCP REQUREST 帧). 表示接受这个OFFER的分配.

* 第四部

  DHCP服务器收到广播后, 发送确认帧(DHCP ACK帧). 表示同意这个OFFER的租约.

值得注意的是, 通过DHCP服务器获取到的IP是有时效性的. 到达一定的时长后会被自动回收或者续租.

# 2. DHCP服务器搭建
首先关闭防火墙, 或者添加UDP策略
## 2.1 centos6

### 2.1.1  安装

   `yum install dhcp -y`

### 2.1.2 配置

1. 配置网卡

   ```python
   cp /etc/sysconfig/network-scripts/ifcfg-eth0 /etc/sysconfig/network-   scripts/ifcfg-eth0:1
   vim /etc/sysconfig/network-scripts/ifcfg-eth0:1
   ```

   配置如下:

   ```python
   DEVICE=eth0:1
   HWADDR=00:0C:29:AD:F8:B7
   TYPE=Ethernet
   UUID=d60f7bad-0f18-420a-8e19-3e361f8ffed4
   ONBOOT=yes
   NM_CONTROLLED=yes
   BOOTPROTO=static
   IPADDR=10.10.10.1
   NETMASK=255.255.255.0
   ```
   设置网卡:
   `vim /etc/sysconfig/dhcpd`
   配置如下:
   
   ```python
   DHCPDARGS=eth0:1     #指定在eth0:1虚接口上提供dhcpserver服务
   ```

2. 配置DHCP服务器

   ```python
   vim /etc/dhcp/dhcpd.conf
   ```
   修改配置如下:

   ```python
   ddns-update-style interim;      #表示dhcp服务器和dns服务器的动态信息更新模式
   ignore client-updates;          #忽略客户端更新
   subnet 10.10.10.0 netmask 255.255.255.0 {        #意思是我所分配的ip地址所在的网段为192.168.145.0 子网掩码为255.255.255.0
     range 10.10.10.100 10.10.10.200;            #租用IP地址的范围
     option domain-name-servers 8.8.8.8,114.114.114.114;
     option domain-name "example.org";
     option routers 10.10.10.1;                    #路由器地址，这里是当前 dhcp 机器的IP地址
     option subnet-mask 255.255.255.0;                  #子网掩码
     default-lease-time 600;                            #默认租约时间
     max-lease-time 7200;                              #最大租约时间
   #host myhost {                                      #设置主机声明
   #hardware ethernet 08:00:27:2C:30:8C;            #指定dhcp客户的mac地址
   #fixed-address 192.168.145.155;                  #给指定的mac地址分配ip
   # }
   }
   ```

### 2.1.3 开启DHCP服务
```
service dhcpd start
或者:
/etc/init.d/dhcpd start

如果未正常启动可以查看日志:
tail -n 200 /var/log/messages
```
### 2.1.4 配置开机自启
```python
chkconfig dhcpd on 
```
## 2.2 Ubuntu16.04

### 2.2.1 安装

   `apt-get install -y  isc-dhcp-server`

### 2.2.2 配置 

   1. 指定监听网卡

      `vim /etc/default/isc-dhcp-server`

      配置如下

      ```python
      INTERFACESv4="enp0s3 enp0s4 enp0s5"  # 多个网卡用空格分卡   
      ```


  2. 配置DHCP信息

     `vim /etc/dhcp/dhcpd.conf`
     
     配置如下:
     
     ```python
     # option domain-name "example.org"  # 配置DNS解析服务器域名
     尾部追加:
     subnet 10.0.2.0 netmask 255.255.255.0 {
       range 10.0.2.10 10.0.2.100;
       option subnet-mask 255.255.255.0;
       option routers 10.0.2.254;
       option domain-name-servers 10.0.2.1;
     }
     ```
     
### 2.2.3 启停服务
```python
systemctl start/stop/restart isc-dhcp-server
systemctl status isc-dhcp-server
```

### 2.2.4 检测DHCP服务

1. 端口

   ```python
   netstat -naup | grep dhcp
   lsof -i udp:63
   ```

2. 抓包

   监听网卡

   ```
   tcpdump -i enp0s3
   ```

   利用客户端强制发送DHCP请求

   ```python
   dhclient enp0s3
   ```

   



