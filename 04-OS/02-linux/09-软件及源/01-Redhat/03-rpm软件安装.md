# 1. rpm

Redhat Packages Manger(RPM软件包管理), 虽然打上Redhat标签, 但是为开放式的, OpenLinux, SUSE, Turbo Linux等linux都采用此软件包管理, rpm使用时容易出现依赖问题, 所以推荐使用yum, 会自动解决依赖关系.

## 1.1 常用方法

```bash
rpm [参数] *.rpm
```

* -i: install, 安装rpm包
* -U: 升级包
* -v: 显示附加消息, 提供更详细消息
* -V: 校验已安装的软件包的hash值
* -h: 安装时输出`###`等互动标记
* --nodeps: 安装, 或者删除时忽略依赖
* --force: 强制安装
* -e: 删除安装包

* -q: query查询rpm安装包
  * a: 查询全部安装包
  * f: 通过文件名查询rpm
  * i: 显示已经安装的rpm软件包的详细信息
  * l: list, 查询软件包文件安装的位置
  * p: 查询未安装软件包的相关信息
  * -R: 查询软件包的依赖性



## 1.1 rpm常用组合

### 1.1.1 安装

```bash
rpm -ivh /mnt/Packages/python-2.6.6-51.el6.x86_64.rpm  # 本地安装
rpm -ivh http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm  # 安装epel拓展源

rpm -ivh *.rpm --force --nodeps  # 忽略依赖关系, 并强制安装
```



### 1.1.2 查询

```bash
[root@localhost ~]# rpm -qf `which find`  # 通过路径查询安装的rpm包
findutils-4.4.2-6.el6.x86_64

[root@localhost ~]# rpm -qpl /mnt/Packages/python-2.6.6-51.el6.x86_64.rpm # 查询软件包安装后将会生成那些文件
warning: /mnt/Packages/python-2.6.6-51.el6.x86_64.rpm: Header V3 RSA/SHA256 Signature, key ID fd431d51: NOKEY
/usr/bin/pydoc
/usr/bin/python
/usr/bin/python2
/usr/bin/python2.6
/usr/share/doc/python-2.6.6
/usr/share/doc/python-2.6.6/LICENSE
/usr/share/doc/python-2.6.6/README
/usr/share/man/man1/python.1.gz
```

### 1.1.3 修改检测

检测rpm包安装后, 是否文件被修改.

```bash
[root@localhost ~]# rpm -V findutils-4.4.2-6.el6.x86_64  # 指定rpm检测
[root@localhost ~]#

[root@localhost ~]# rpm -Vf `which find`  # 指定路径检测
[root@localhost ~]#

[root@localhost ~]# rpm -qaV  # 自动扫描全部rpm并检测
prelink: /usr/bin/rhythmbox: at least one of file's dependencies has changed since prelinking
S.?......    /usr/bin/rhythmbox
```

* 5:  md5值, 校验失败
* S: 文件长度, 校验失败
* L: 链接路径, 校验失败
* T: 文件修改日期, 校验失败
* D: 设备信息, 校验失败
* U: 用户创建者, 校验失败
* G: 用户组, 校验失败
* ?: 不可读文件
* c: 配置文件, 校验失败
* d: 普通文件
* g: 增加了文件
* l: 授权文件
* r: 描述文件



### 1.1.4 删除

删除安装包, 尽量不要删除依赖关系.

```bash
rpm -e --nodeps python  # 删除Python, 不删除相关依赖
```

删除后, 检查

```bash
rpm -qa python
```

### 1.1.5 升级

```bash
rpm -Uvh xxx.rpm
```

一般情况下, 直接升级会升级失败, 因为有大量的依赖包也许要升级.

#### 1.1.5.1 依赖关系解决

```bash
[root@localhost ~]# rpm -ivh /mnt/Packages/mariadb-server-5.5.65-1.el7.x86_64.rpm 
error: Failed dependencies:
	mariadb(x86-64) = 1:5.5.65-1.el7 is needed by mariadb-server-1:5.5.65-1.el7.x86_64
	perl(DBI) is needed by mariadb-server-1:5.5.65-1.el7.x86_64
	perl-DBD-MySQL is needed by mariadb-server-1:5.5.65-1.el7.x86_64
	perl-DBI is needed by mariadb-server-1:5.5.65-1.el7.x86_64
[root@localhost ~]# rpm -ivh /mnt/Packages/mariadb-5.5.65-1.el7.x86_64.rpm 
```

依赖安装

```bash
rpm -ivh /mnt/Packages/mariadb-5.5.65-1.el7.x86_64.rpm
rpm -ivh /mnt/Packages/perl-DBD-MySQL-4.023-6.el7.x86_64.rpm
rpm -ivh /mnt/Packages/mariadb-server-5.5.65-1.el7.x86_64.rpm 
```

* 直接使用此网站查询, 来解决依赖关系 : http://www.rpmseek.com/index.html