# 1. yum

## 1.1 yum安装

默认Redhat是不能使用其他源的, 所以需要重装yum软件

1. 删除自带yum

   ```bash
   rpm -qa|grep yum|xargs rpm -e --nodeps
   ```

2. 下载yum软件

   注意选择对应的版本, 当前使用的版本为6

   ```bash
   wget http://mirrors.aliyun.com/centos/6/os/x86_64/Packages/rpm-4.8.0-59.el6.x86_64.rpm &&
   wget http://mirrors.aliyun.com/centos/6/os/x86_64/Packages/yum-metadata-parser-1.1.2-16.el6.x86_64.rpm &&
   wget http://mirrors.aliyun.com/centos/6/os/x86_64/Packages/python-urlgrabber-3.9.1-11.el6.noarch.rpm &&
   wget http://mirrors.aliyun.com/centos/6/os/x86_64/Packages/yum-3.2.29-81.el6.centos.noarch.rpm &&
   wget http://mirrors.aliyun.com/centos/6/os/x86_64/Packages/yum-plugin-fastestmirror-1.1.30-41.el6.noarch.rpm
   ```

3. 安装yum

   ```bash
   rpm -ivh *.rpm --force --nodeps  # 强制批量安装
   ```

   

## 1.2 yum常用方法

```bash
yum install -y python # 安装程序
yum -y update python  # 更新程序, 会改变系统/软件设置, 更新系统, 内核.
yum -y upgrade python # 更新程序, 不改变上述设置
yum -y update         # 整个系统更新, 升级
yum -y info python    # 查看程序详细信息
yum -y remove python  # 拆卸程序
yum search python     # 搜索相关程序包
yum grouplist  # 查看有哪些软件组包
yum groupinstall groupname  # 直接安装软件组包, 例如`yum groupinstall 'Development tools'`
```

* install: 安装包
* update: 升级, 如果不加包名, 这进行系统升级
* info: 查看安装包的作用
* provides: 通过安装后的软件, 查找安装包
* remove: 删除软件

# 2. Redhat系统注册

未激活的Redhat, 需要重新安装yum, 否则不能安装软件. 也可以直接激活, 但是不建议, 官方的软件包太少了, 激活后换源是不支持的. 所以不建议激活.

## 2.1 开发者账号注册

访问下列网站完成注册

```bash
https://developers.redhat.com/auth/realms/rhd/protocol/openid-connect/registrations?client_id=web&redirect_uri=http%3A%2F%2Fdevelopers.redhat.com%2Fblog%2F2014%2F06%2F26%2Frhel-7-is-for-developers%2F&state=8bc8e6d2-7dea-42c2-96da-c5e2e5755fca&nonce=eab2e0c7-b41d-44a9-99ad-0c2dbd5170a9&response_mode=fragment&response_type=code
```

## 2.2 账号登录激活

```bash
[root@localhost gcc-4.8.5]# subscription-manager register --username=565956231@qq.com --password=wdlRE4911? --auto-attach
The system has been registered with ID: 1b6c59d6-fb26-454d-ab37-fe14837f261c 
Installed Product Current Status:
Product Name: Red Hat Enterprise Linux Server
Status: Subscribed
```
