# 1. 准备环境

## 1.1 清理依赖

清理不正常的依赖关系

```bash
yum install yum-utils -y
yum clean all
package-cleanup --dupes # 列出
package-cleanup --cleandupes # 清理
package-cleanup --problems # 清理损坏的包
```

## 1.2 更新yum核心

```bash
yum update -y
```

## 1.3 安装依赖

安装gcc编译需要的依赖

 

```bash
yum install gcc gcc-c++
yum install glibc-static libstdc++*
yum install flex* bison*
```

# 2. 安装gcc

## 2.1 准备安装包

 

```bash
wget ftp://gcc.gnu.org/pub/gcc/releases/gcc-4.8.5/
tar -zxf gcc-4.8.5.tar.bz2 -C /usr/local/src
cd /usr/local/src/gcc-4.8.5
```

下载一些必备的依赖程序

 

```bash
两种方法任选一种
# 方法1. 使用给定的脚本
./contrib/download_prerequisites 

# 方法2. 手动完成下载:  # 需要在gcc目录中执行
wget ftp://gcc.gnu.org/pub/gcc/infrastructure/mpfr-2.4.2.tar.gz
wget ftp://gcc.gnu.org/pub/gcc/infrastructure/gmp-4.3.2.tar.gz
wget ftp://gcc.gnu.org/pub/gcc/infrastructure/mpc-0.8.1.tar.gz

tar -zxf mpfr-2.4.2.tar.gz
tar -zxf gmp-4.3.2.tar.gz
tar -zxf mpc-0.8.1.tar.gz

ln -sf mpfr-2.4.2 mpfr
ln -sf gmp-4.3.2 gmp
ln -sf mpc-0.8.1 mpc
```

## 2.1 安装

### 2.1.1 编译安装

 

```bash
#跳转到编译后的程序文件存放目录
mkdir /usr/local/build/gcc-4.8.5 -p
cd /usr/local/build/gcc-4.8.5

/usr/local/src/gcc-4.8.5/configure --enable-checking=release --enable-languages=c,c++ --disable-multilib
#编译gcc源程序, 如果中途中断后执行, 修复后依赖需要再次执行, make distclean 和 ./configure xx
make -j4
make install
```

### 2.2.2 切换依赖

 

```bash
cp /usr/local/lib64/libstdc++.so.6.0.19 /usr/lib64 
mv /usr/lib64/libstdc++.so.6 /usr/lib64/libstdc++.so.6_bak
ln -s /usr/lib64/libstdc++.so.6.0.19 /usr/lib64/libstdc++.so.6
```