# 下载

```bash
wget https://ftp.gnu.org/gnu/glibc/glibc-2.17.tar.gz
```

# 编译安装

```bash
tar -xvf glibc-2.17.tar.gz
cd glibc-2.17
mkdir build
cd build
../configure --prefix=/usr --disable-profile --enable-add-ons --with-headers=/usr/include --with-binutils=/usr/bin
make -j4 && make install
```

# 变更连接

# 确认

```bash
ll /lib64/libc.so.6  # 软连接指向

strings /lib64/libc.so.6 |grep GLIBC_  #可用的glibc版本
```



