# 1. DNS

## 1. 1 DNS协议
   DNS(Domain Name System, 域名系统),.
   DNS 可以被称为一种协议，也可以被称为一种系统，或一种服务。DNS 简单来说就是将域名和 IP 地址相互映射的一个分布式数据库，能够使人们更方便地访问互联网。DNS 使用 TCP 和 UDP 的 53 端口。

## 1.2 分支树

![图片描述](03-DNS%E5%8D%8F%E8%AE%AE.assets/5e6afa7d0001b14f13080836.png)

* **说明**
  1. 一级域名

     ```python
     .cn, .com, .org ...
     ```
  
  2. 二级域名
  
     ```python
     baidu.com, centos.org, github.com ...
     ```
  
  3. 三级域名及以下
  
     ```
     www.baidu.com, www.github.com ...
     www.cn.7.new.super.google.cn ...
     ```
  
     

## 1.3 域名解析

* 域名解析

  域名解析(Domain Name Resolution), 从域名得知 IP 地址的转换过程。域名的解析工作由 DNS 服务器完成。

* 域名反向解析

  反向解析(Reverse Resolution)或反向DNS(Reverse DNS),   IP 地址转换为域名的协议



# 2. DNS服务器

搭建主从DNS服务器, 管理域名:  network.cn

## 2.1 搭建

### 2.1.1 ubuntu16.04

1. 安装Bind9

   ```python
   apt-get -y install bind9
   ```

   

2. 配置Bind9

   * DNS主服务

     ```python
     vim /etc/bind/named.conf.local
     ```

     添加:

     ```python
     zone "network.cn" {
         type master;  # 主服务
         file "/etc/bind/db.network.cn";
         allow-transfer { 192.168.0.2; };
     };
     ```

     检查语法:

     ```python
     named-checkconf /etc/bind/named.conf.local  # 不报错即可
     ```

     配置`network.cn`:

     ```
     cp db.local db.network.cn
     vim db.network.cn
     ```

     **说明**:

     1. A: 主机名与一个 IPv4 地址匹配
     2. AAAA: 主机名与一个 IPv6 地址匹配
     3. CNAME: 指向另一个主机名的别名(alias)
     4. NS: 定义DNS服务器
     5. MX: 定义邮件服务器
     6. PTR:  IP对应的主机名, A的反向记录(IP反向解析)
     7. SOA: 区域信息

     配置如下:
     
     ```python
     $TTL 604800     ; 1 week  生存时间
     $ORIGIN network.cn.		; $ORIGIN 起源, 可选变量, 后面的@符号将会使用到这个参数, 如果没有定义则会使用/etc/bind/named.conf.local中的值
     @       IN SOA  ns1.network.cn. admin.network.cn. (		; SOA(Start Of Authority, 授权的开始), 包含主域名服务器和域名管理员电子邮箱, 末尾需要使用.
                                  2020031601 ; Serial 序列号
                                  3600       ; Refresh (1 hour), 记录从主服务更新到从服务器的时间
                                  3000       ; Retry (50 minutes), 从服务器等待重试时间重间隔
                                  4233600    ; Expire (7 weeks), 从服务器尝试与从服务器联系的时长
                                  604800 )   ; Negative Cache TTL (1 week), 否定缓存生存时间, 如果DNS没有解析到对应IP, 将会把错误记录缓存的时长
     
     @               IN      NS      ns1.network.cn.  ; 表示ns1.network.cn 是 network.cn 的一个域名服务器
     @               IN      NS      ns2  ; 相当于ns2.network.cn.
     @               IN      MX      10 mx1  ; 10为权重, 数字越低表示优先级越高
     @               IN      MX      20 mx2
     ns1             IN      A       192.168.0.1
     ns2             IN      A       192.168.0.2
     mx1             IN      A       192.168.0.3
     mx2             IN      A       192.168.0.4
     tuto            IN      A       192.168.0.5
     www             IN      A       192.168.0.6
     blog            IN      CNAME   www
     ```
     语法检测:
     ```python
named-checkzone network.cn db.network.cn  # 没有报错说明此配置无语法错误
     ```
   * DNS从服务

     1. 配置Bind9

        ```python
     vim /etc/bind/named.conf.local
        ```

        配置从设置:
     
        ```python
     zone "network.cn" {
            type slave;
         file "/var/cache/bind/db.network.cn";
            masters { 192.168.0.1; };
        };
        ```
     
        检查语法错误:
     
        ```python
     named-checkconf named.conf.local  # 没有异常说明语法正确
        ```

   * 配置反向解析
   
     1. 配置主服务

        ```python
     vim /etc/bind/named.conf.local
        ```
        增加配置如下:
        ```python
     zone "0.168.192.in-addr.arpa." {
                type master;
             file "/etc/bind/db.192.168.0";
        };
        ```
        检查语法
     
        ```python
     named-checkconf named.conf.local
        ```
        配置DB:
        
        ```python
        vim db.192.168.0
        ```
        内容如下:
        ```python
        $TTL 604800     ; 1 week
        $ORIGIN 0.168.192.in-addr.arpa.
        @       IN SOA  ns1.network.cn. admin.network.cn. (
                                        2020031601 ; Serial
                                        3600       ; Refresh (1 hour)
                                        3000       ; Retry (50 minutes)
                                        4233600    ; Expire (7 weeks)
                                        604800  )  ; Negative Cache TTL (1 week)
        
        @               IN      NS        ns1.network.cn.
        @               IN      NS        ns2.network.cn.
        1               IN      PTR       ns1.network.cn.
        2               IN      PTR       ns2.network.cn.
        3               IN      PTR       mx1.network.cn.
        4               IN      PTR       mx2.network.cn.
        5               IN      PTR       tuto.network.cn.
        6               IN      PTR       www.network.cn.
        ```
        检查语法
        ```python
        named-checkzone 0.168.192.in-addr.arpa. db.192.168.0
        ```

1. 启停配置

   ```python
   systemctl restart bind9
   systemctl status bind9
   ```


## 2.2 检测

### 2.2.1 配置DNS服务器

```python
vim /etc/resolv.conf
```

配置:

```python
nameserver 127.0.0.1
options edns0
```

### 2.2.2 检测

* host
  ```python
  host -t type name [server]
  ```
  type:
  ​	可取的值为 NS，A，MX，CNAME，等等
  
  name:
  ​	指定要查询的域名
  
  server:
  
  ​	可选, 指定DNS服务器. 如果没有设置, 则读取/etc/resolv.conf

直接执行:

```python
host -t ns network.cn  # 获取DNS服务器
host -t a ns2.network.cn  # 通过DNS获取IP

```

