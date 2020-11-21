# 1. 拓展swap分区

Swap分区在系统物理内存不够用时, 可以从硬盘中分出一部分来供给使用

**注意**: 一般到这一步时, 尽量去加内存, 而不是划分.

```bash
mkswap /devices   # 格式转化
swapon /swap      # 激活/swap, 加入到swap分区中
vim /etc/fstab    # 增加开机自动挂载

#删除分区 
swapoff /swap
```

## 1.1 磁盘swap分区

### 1.1.1 增加磁盘分区

参见磁盘分区

### 1.1.2 格式转换

```bash
[root@localhost ~]# mkswap /dev/sdb2
Setting up swapspace version 1, size = 18873320 KiB
no label, UUID=70baa221-a908-4aee-823a-45086292fc79
[root@localhost ~]#
```

### 1.1.3 设置交换分区

```bash
[root@localhost ~]# free -m
              total        used        free      shared  buff/cache   available
Mem:            972         137         724           7         110         706
Swap:          2047           0        2047
[root@localhost ~]# swapon /dev/sdb2
[root@localhost ~]# free -m
              total        used        free      shared  buff/cache   available
Mem:            972         151         710           7         110         691
Swap:         20478           0       20478
[root@localhost ~]# 
```

### 1.1.4 关闭交换分区

```bash
[root@localhost ~]# swapoff /dev/sdb2
[root@localhost ~]# free -m
              total        used        free      shared  buff/cache   available
Mem:            972         137         724           7         110         705
Swap:          2047           0        2047
[root@localhost ~]#
```

## 1.2 文件增加swap分区

### 1.2.1 创建流文件

```bash
[root@localhost ~]# dd if=/dev/zero of=swap_file bs=1M count=500
500+0 records in
500+0 records out
524288000 bytes (524 MB) copied, 3.26677 s, 160 MB/s
[root@localhost ~]#
```

* dd: copy一个文件, 并且在copy同时进行指定转换
* if: 指定输入文件
* of: 指定输出文件
* bs: 设置读取/输出的块大小   , bytes
* count: 指定读取大小, bytes

### 1.2.2 转换文件

```bash
mkswap -f /root/swap_file  # 转换为swap文件
chmod 0600 swap_file       # 指定文件权限
free -m                    # 查看当前内存
swapon /root/swap_file     # 挂载swap
swapoff /root/swap_file    # 卸载swap
```

效果展示

```bash
[root@localhost ~]# mkswap -f /root/swap_file
mkswap: /root/swap_file: warning: wiping old swap signature.
Setting up swapspace version 1, size = 511996 KiB
no label, UUID=d1adedff-d839-4dbb-a559-45ed179c854a
[root@localhost ~]# chmod 0600 swap_file 
[root@localhost ~]# swapon /root/swap_file
[root@localhost ~]# free -m
              total        used        free      shared  buff/cache   available
Mem:            972         136         729           7         106         709
Swap:          2547           0        2547
[root@localhost ~]# swapoff /root/swap_file
[root@localhost ~]# free -m
              total        used        free      shared  buff/cache   available
Mem:            972         135         729           7         106         709
Swap:          2047           0        2047
[root@localhost ~]#
```



