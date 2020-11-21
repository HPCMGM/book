# 1. [shadowsocks-R](https://github.com/shadowsocksr-backup)

## 1.1 环境配置

安装环境centos6, ssr客户端下载: [ssr客户端](https://github.com/shadowsocksr-backup)

## 1.2 更换内核

 

```
yum -y install wget && wget --no-check-certificate https://blog.asuhu.com/sh/ruisu.sh && bash ruisu.sh
```

## 1.3 网络加速

对网络进行加速处理, 二选一即可

### 1.3.1 锐速

 

```
wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/serverspeeder/master/serverspeeder-all.sh && bash serverspeeder-all.sh
```

### 1.3.2 bbr

 

```
wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh && chmod +x bbr.sh && ./bbr.sh
```

## 1.4 安装ssr

 

```
wget -q -N --no-check-certificate https://raw.githubusercontent.com/FunctionClub/SSR-Bash-Python/master/install.sh && bash install.sh
```

