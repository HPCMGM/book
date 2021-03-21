# 1. ipvsadm

## 1.1 常用命令

```bash
ipvsadm -A -t xxx -s rr
ipvsadm -a -t xxx -r xxx -m
ipvsadm -a -t xxx -r xxx -m
```

* -A: 添加服务
* -t: tcp服务
* -s: 指定调度算法
* rr: 表示轮询算法
* -a: 表示添加从服务
* -r: 指定从服务ip
* -m: 指定lvs模式为Nat模式

# 2. NAT模式

## 2.1 准备工作

### 2.1.1 内网主机

准备内网主机: 

* 10.0.0.10
* 10.0.0.11
* 10.0.0.12(双网卡)

### 2.1.2 外网主机

准备外网主机:

* 10.0.1.12(双网卡, 内网为10.0.0.12)

### 2.1.3 Nginx服务

需要在两个内网主机上, 安装Nginx服务用于测试

1. 添加nginx源

   操作文件: `vim /etc/yum.repos.d/CentOS-Base.repo`, 内容替换如下:

   ```bash
   [nginx]
   name=nginx repo
   baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
   gpgcheck=0
   enabled=1
   ```

   清空缓存

   ```bash
   yum clean all
   ```

2. 安装Nginx

   ```bash
   yum install -y nginx
   ```

3. 修改静态文件

   操作目录: `vim /usr/share/nginx/html/index.html`,  在文本的末尾增加`<h1>当前主机的ip</h2>`用于鉴别访问的主机

   即:

   * 10.0.0.10应增加: `<h1>10.0.0.10</h2>`
   * 10.0.0.11应增加: `<h1>10.0.0.11</h2>`

4. 重启Nginx

   ```bash
   nginx -t restart
   ```



## 2.3 开始搭建

在负载主机上(10.0.0.12, 外网: 10.0.1.12)执行如下命令:

```bash
ipvsadm -A -t 10.0.1.12:80 -s rr
ipvsadm -at 10.0.1.12:80 -r 10.0.0.10 -m
ipvsadm -at 10.0.1.12:80 -r 10.0.0.10 -m
```

同时关闭三个主机的防火墙

```bash
iptables -F
```

## 2.4 测试

通过外网访问10.0.1.12, 或者在10.0.1.12上多次执行如下命令

```bash
curl 10.0.1.12 | grep "h1"
```

如果看到ip在轮询变动, 说明搭建成功

