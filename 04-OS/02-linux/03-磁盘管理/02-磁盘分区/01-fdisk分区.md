# 1. fdisk

```bash
fdisk [选项] device
```

常用参数

```bash
   a   toggle a bootable flag
   b   edit bsd disklabel
   c   toggle the dos compatibility flag
   d   delete a partition  # 删除分区
   g   create a new empty GPT partition table
   G   create an IRIX (SGI) partition table
   l   list known partition types  # 查看分区类型
   m   print this menu  # 打印帮助列表
   n   add a new partition  # 增加新分区
   o   create a new empty DOS partition table
   p   print the partition table  # 显示分区表
   q   quit without saving changes  # 不保存退出
   s   create a new empty Sun disklabel
   t   change a partition's system id   # 改变分区类型
   u   change display/entry units
   v   verify the partition table
   w   write table to disk and exit  # 保存退出
   x   extra functionality (experts only)
```



## 1.1 增加分区

### 1.1.1 增加分区

```bash
[root@localhost ~]# fdisk /dev/sdb
Welcome to fdisk (util-linux 2.23.2).

Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): n  # 创建分区
Partition type:
   p   primary (0 primary, 0 extended, 4 free)  # 主分区
   e   extended									# 拓展分区
Select (default p): p  # 构建主分区
Partition number (1-4, default 1): 1    # 选择分区编号
First sector (2048-41943039, default 2048):   # 分区扇形引导位置
Using default value 2048
Last sector, +sectors or +size{K,M,G} (2048-41943039, default 41943039): # 设置分区大小, 指定的话可以用`+10G`表示
Using default value 41943039
Partition 1 of type Linux and of size 20 GiB is set

Command (m for help): p  # 查看分区信息

Disk /dev/sdb: 21.5 GB, 21474836480 bytes, 41943040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0xe92d2ec3

   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1            2048    41943039    20970496   83  Linux  # 新增加的分区信息

Command (m for help): w   # 保存并退出
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
[root@localhost ~]# fdisk /dev/sdb
Welcome to fdisk (util-linux 2.23.2).

Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): m
Command action
   a   toggle a bootable flag
   b   edit bsd disklabel
   c   toggle the dos compatibility flag
   d   delete a partition
   g   create a new empty GPT partition table
   G   create an IRIX (SGI) partition table
   l   list known partition types
   m   print this menu
   n   add a new partition
   o   create a new empty DOS partition table
   p   print the partition table
   q   quit without saving changes
   s   create a new empty Sun disklabel
   t   change a partition's system id
   u   change display/entry units
   v   verify the partition table
   w   write table to disk and exit
   x   extra functionality (experts only)

Command (m for help): n
Partition type:
   p   primary (0 primary, 0 extended, 4 free)
   e   extended
Select (default p): p
Partition number (1-4, default 1): 1    
First sector (2048-41943039, default 2048): 
Using default value 2048
Last sector, +sectors or +size{K,M,G} (2048-41943039, default 41943039): 
Using default value 41943039
Partition 1 of type Linux and of size 20 GiB is set

Command (m for help): p

Disk /dev/sdb: 21.5 GB, 21474836480 bytes, 41943040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0xe92d2ec3

   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1            2048    41943039    20970496   83  Linux

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
[root@localhost ~]# ls /dev/sdb*
/dev/sdb  /dev/sdb1
[root@localhost ~]
```

### 1.1.2 分区生效

未使用的分区, 无需此操作



使用的磁盘分区后, 提示如下:

```bash
WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
The kernel still uses the old table. The new table will be used at
the next reboot or after you run partprobe(8) or kpartx(8)
Syncing disks.
```

处理方案:

1. 重启(最好是重启)
2. `partx -a /dev/sdb` 重新获取分区表

```bash
[root@localhost bak]# ls /dev/sdb*  # 新创建的分区没有加载  
/dev/sdb  /dev/sdb1  /dev/sdb4
[root@localhost bak]# partx -a /dev/sdb  # 刷新当前分区表
partx: /dev/sdb: error adding partition 1
partx: /dev/sdb: error adding partition 4
[root@localhost bak]# ls /dev/sdb*   # 成功读取到分区信息
/dev/sdb  /dev/sdb1  /dev/sdb2  /dev/sdb4
[root@localhost bak]#
```

## 1.2 格式化磁盘

```bash
mkfs.ext4 -f /dev/sdb1  # 格式化为ext4文件系统
mkfs.xfs -f /dev/sdb1   # 格式化为xfs文件系统
```



## 1.3 删除分区

```bash
[root@localhost bak]# fdisk /dev/sdb
Welcome to fdisk (util-linux 2.23.2).

Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Command (m for help): d  # 开始删除分区
Partition number (1,2,4, default 4): 1  # 指定需要删除的分区
Partition 1 is deleted

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.

WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
The kernel still uses the old table. The new table will be used at
the next reboot or after you run partprobe(8) or kpartx(8)
Syncing disks.
[root@localhost bak]# ls /dev/sdb*
/dev/sdb  /dev/sdb1  /dev/sdb2  /dev/sdb4  # 磁盘未同步, 需要重启才能解决
[root@localhost bak]# reboot

WARNING! The remote SSH server rejected X11 forwarding request.
Last login: Sat Jul 18 09:44:09 2020 from 10.0.0.1
[root@localhost ~]# ls /dev/sdb*
/dev/sdb  /dev/sdb2  /dev/sdb4  # 已经正常
[root@localhost ~]#
```

