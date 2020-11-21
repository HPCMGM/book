# 1.  依赖安装

## 1.1 在线安装

### 1.1.1 Centos 6

```bash
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite sqlite-devel readline-devel tk tk-devel gdbm gdbm-devel db4-devel libpcap-devel lzma xz xz-devel libuuid libuuid-devel libffi-devel
```

### 1.1.2 Ubuntu 16.04

```bash
apt-get install -y gcc make \
build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl libncurses5-dev libncursesw5-dev xz-utils libffi-dev liblzma-dev python-dev pkg-config libusb-dev libusb-1.0-0-dev openssl tk tk-dev lzma libmysqlclient-dev
```

## 1.2 源码安装

### 1.2.1 sqlite

#### 1.2.1.1 sqlite安装

官方网站: [下载](https://www.sqlite.org/download.html)

```bash
wget https://www.sqlite.org/2020/sqlite-autoconf-3330000.tar.gz
tar -zxf sqlite-autoconf-3330000.tar.gz
cd sqlite-autoconf-3330000


./configure --prefix=/usr/local/sqlite
make -j3
make install
```

#### 1.2.1.2 Python编译

如果用此方式安装了sqlite3, 编译Python需要如下进行

```bash
LD_RUN_PATH=/usr/local/sqlite/lib ./configure LDFLAGS="-L/usr/local/sqlite/lib" CPPFLAGS="-I /usr/local/sqlite/include"


LD_RUN_PATH=/usr/local/sqlite/lib make -j3
LD_RUN_PATH=/usr/local/sqlite/lib make install
```

也可以修改原sqlite, 不影响Python编译的过程

```bash
mv /usr/bin/sqlite3 /usr/bin/sqlite3_old
cd /usr/local/sqlite/bin/
ln -s sqlite3 /usr/bin/sqlite3

vim /etc/profile
export LD_LIBRARY_PATH=/usr/local/sqlite/lib
source /etc/profile
```

### 1.2.2 ssl

#### 1.2.2.1 ssl安装

官方网站: [下载](https://www.openssl.org/source/)

* 下载

  ```bash
  wget https://www.openssl.org/source/openssl-1.1.1g.tar.gz
  mv openssl-1.1.1g.tar.gz /usr/local/Packages
  cd /usr/local/Packages
  tar -zxf openssl-1.1.1g.tar.gz
  ```

* 编译安装

  ```bash
  cd openssl-1.1.1g
  ./config --prefix=/usr/local/openssl
  ./config -t
  make depend
  make
  make test
  make install
  ```

* 编译过程中出错解决

  * 错误一

    ```bash
    Parse errors: No plan found in TAP output
    ```

    缺少perl相关依赖, 处理如下

    ```bash
    yum  install  perl-CPAN
    perl  -MCPAN  -e  shell
    ```

    然后页面出现如下

    ![image-20200909162239982](image/01-Linux%E5%AE%89%E8%A3%85/image-20200909162239982.png)

    然后一路回车即可, 直至页面出现如下信息, 即为完成, 输入`exit`退出即可

    ![image-20200909162407834](image/01-Linux%E5%AE%89%E8%A3%85/image-20200909162407834.png)

* 创建依赖关系

  ```bash
  cp libcrypto.so.1.1 /usr/local/lib
  cp libcrypto.so.1.1 /usr/local/lib64
  cp libcrypto.so.1.1 /usr/lib
  cp libcrypto.so.1.1 /usr/lib64
  
  cp libssl.so.1.1 /usr/local/lib
  cp libssl.so.1.1 /usr/local/lib64
  cp libssl.so.1.1 /usr/lib
  cp libssl.so.1.1 /usr/lib64
  ```

#### 1.2.2.2 Python编译处理

1. 开启openssl编译

   执行`make`后, 检查`Modules/Setup.dist`, 确保以下三行没有注释:

   ```python
   SSL=/usr/local
   _ssl _ssl.c \
           -DUSE_SSL -I$(SSL)/include -I$(SSL)/include/openssl \
           -L$(SSL)/lib -lssl -lcrypto
   ```

2. 重新执行编译安装

   ```bash
   ./configure --with-openssl=/usr/local/openssl
   ```

   

   执行完成后需要看到, 才为成功:

   ```bash
   --with-openssl  yes
   ```



### 1.2.3 uuid

#### 1.2.3.1 uuid安装

```bash

```

#### 1.2.3.2 Python编译

编辑Python的头文件
位置: `Modules/_uuidmodule.c`
将第11行:

```bash
  8 #include "Python.h"
  9 #ifdef HAVE_UUID_UUID_H
 10 #include <uuid/uuid.h>
 11 #elif defined(HAVE_UUID_H)
 12 #include <uuid.h>
 13 #endif
```

修改为:

```bash
else
```

安装此模块后需要重新执行

```bash
./configure
make
make install
```

### 1.2.4 libffi

#### 1.2.4.1 libffi安装

* 下载

  ```python
  wget ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz
  mv libffi-3.2.1.tar.gz /usr/local/Packages
  cd /usr/local/Packages
  tar -zxf libffi-3.2.1.tar.gz
  ```

* 安装

  ```python
  cd libffi-3.2.1
  ./configure
  make
  make install
  ```

* 参数配置

  ```python
  export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
  # 查找find / -name libffi.so.6, 将结果配置到LD_LIBRARY_PATH中
  export LD_LIBRARY_PATH=/usr/local/lib64
  ```

#### 1.2.4.2 Python编译

```bash

```



# 2. Python 安装

## 2.1 在线安装

## 2.2 源码安装

### 2.2.1 目录配置

```python
mkdir /usr/local/python
mkdir /usr/local/Packages
mv Python-3.7.2.tgz /usr/local/Packages
cd /usr/local/Packages
tar -zxf Python-3.7.2.tgz
cd Python-3.7.2
```

### 2.2.2 编译安装

```python
./configure --prefix=/usr/local/python/python37 --enable-shared --enable-optimizations

make -j4

make install
```

### 2.2.3 配置环境变量

```python
cp libpython*.so.1.0 /usr/lib
cp libpython*.so.1.0 /usr/lib64
cp libpython*.so.1.0 /usr/local/lib 
cp libpython*.so.1.0 /usr/local/lib64

# vim /etc/profile
# 增加
# PATH=$PATH:/usr/local/python/python37/bin

source /etc/profile
```

### 2.2.4 测试

运行一下命令, 如果不报错说明正常, 否则需要重新编译安装对应的依赖, 如果不许要此功能可以不用安装

```python
python3.7 -c "import ssl"
python3.7 -c "import ctypes"
python3.7 -c "import zlib"
python3.7 -c "import readline"
python3.7 -c "import lzma"
python3.7 -c "import uuid"
python3.7 -c "import tk"
python3.7 -c "import sqlite3"
```

# 3. 错误处理

## 3.1 openssl异常

* Python安装异常

  Python3.7.2 要求openssl/LibreSSL版本不得低于 1.0.2, 1.1, 或者LireSSL不得低于2.6.4

  ```python
  Python requires an OpenSSL 1.0.2 or 1.1 compatible libssl with X509_VERIFY_PARAM_set1_host().
  LibreSSL 2.6.4 and earlier do not provide the necessary APIs, https://github.com/libressl-portable/portable/issues/381
  ```
  
* pip使用异常

  缺少openssl

  ```python
  Ignoring ensurepip failure:pip required SSL/TLS
  ```

## 3.2 gcc异常

* 未安装gcc

  ```python
  configure:error: no accetable cc found in $PATH
  ```

* gcc rpm包: [下载](./01-Python.assets/gcc_rpm.tar.gz)

  ```bash
  rpm -ivh lib64gmp3-4.3.1-1mdv2010.0.x86_64.rpm
  rpm -ivh ppl-0.10.2-11.el6.x86_64.rpm
  rpm -ivh cloog-ppl-0.15.7-1.2.el6.x86_64.rpm
  rpm -ivh mpfr-2.4.1-6.el6.x86_64.rpm
  rpm -ivh cpp-4.4.7-4.el6.x86_64.rpm --force
  rpm -ivh kernel-headers-2.6.32-431.el6.x86_64.rpm
  rpm -ivh glibc-headers-2.12-1.132.el6.x86_64.rpm --nodeps --force
  rpm -ivh glibc-devel-2.12-1.132.el6.x86_64.rpm --force --nodeps
  rpm -ivh gcc-4.4.7-4.el6.x86_64.rpm --force --nodeps
  rpm -ivh libstdc++-devel-4.4.7-4.el6.x86_64.rpm --force --nodeps
  rpm -ivh gcc-c++-4.4.7-4.el6.x86_64.rpm --force --nodeps
  rpm -e --nodeps keyutils-libs-1.4-4.el6.x86_64
  rpm -ivh keyutils-libs-1.4-5.el6.x86_64.rpm
  rpm -ivh keyutils-libs-devel-1.4-5.el6.x86_64.rpm 
  rpm -ivh libsepol-devel-2.0.41-4.el6.x86_64.rpm 
  rpm -e --nodeps libselinux-utils-2.0.94-5.3.el6_4.1.x86_64
  rpm -Uvh libselinux-2.0.94-5.8.el6.x86_64.rpm
  rpm -ivh libselinux-devel-2.0.94-5.8.el6.x86_64.rpm
  rpm -e --nodeps krb5-libs-1.10.3-10.el6_4.6.x86_64
  rpm -ivh krb5-libs-1.10.3-42.el6.x86_64.rpm
  rpm -e --nodeps libcom_err-1.41.12-18.el6.x86_64
  rpm -ivh libcom_err-1.41.12-22.el6.x86_64.rpm 
  rpm -ivh libcom_err-devel-1.41.12-22.el6.x86_64.rpm
  rpm -ivh krb5-devel-1.10.3-42.el6.x86_64.rpm
  rpm -ivh zlib-devel-1.2.3-29.el6.x86_64.rpm 
  rpm -e --nodeps openssl-1.0.1e-15.el6.x86_64
  rpm -ivh openssl-1.0.1e-42.el6.x86_64.rpm 
  rpm -ivh openssl-devel-1.0.1e-42.el6.x86_64.rpm
  ```

## 3.3 Sqlite异常

* sqlite版本低

  需要更新版本

  ```python
  raise ImproperlyConfigured('SQLite 3.8.3 or later is required (found %s).' % Database.sqlite_version)
  django.core.exceptions.ImproperlyConfigured: SQLite 3.8.3 or later is required (found 3.6.20).
  ```
