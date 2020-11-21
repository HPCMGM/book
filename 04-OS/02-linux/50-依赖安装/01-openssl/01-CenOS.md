# 1. CenOS7

## 1.1 在线安装

1. yum install perl perl-devel

2. yum install gcc gcc-c++

3. perl 安装 Text::Template

   进入perl交互式前, 可能需要配置些东西, 直接使用`yes`即可

   ```shell
   [root@localhost openssl-1.1.0g]# perl -MCPAN -e "shell"
   ...
   export PATH="/root/perl5/bin:$PATH";
   
   Would you like me to append that to /root/.bashrc now? [yes] yes
   ...
   cpan[2]> install Text::Template
   ...
   Appending installation info to /usr/lib64/perl5/perllocal.pod
     MSCHOUT/Text-Template-1.59.tar.gz
     /usr/bin/make install  -- OK
   
   cpan[2]> exit
   Terminal does not support GetHistory.
   Lockfile removed.
   
   ```

4. 源码编译安装

   ```shell
   ./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl/conf
   ./config -t
   make depend
   make
   make test TESTS=test_sanity V=1
   make install
   
   vim /etc/ld.so.conf
   将 /usr/local/openssl/lib  #追加到尾部
   ldconfig  # 刷新lib
   
   测试:
   /usr/local/openssl/lib/openssl version -a
   ```



```python
    9  vi /etc/sysconfig/network-scripts/ifcfg-ens33 
   10  service network restart
   11  ping 10.0.0.2
   12  ping 10.0.0.1
   13  vi /etc/sysconfig/network-scripts/ifcfg-ens33 
   14  service network restart
   15  ping www.baidu.com
   16  vi /etc/sysconfig/network-scripts/ifcfg-ens33 
   17  service network restart
   18  ping www.baidu.com
   19  vim /etc/resolv.conf
   20  vi /etc/resolv.conf
   21  service network restart
   22  mnt /dev/cdrom /mnt
   23  mount /dev/cdrom /mnt
   24  ip a
   25  service network restart
   26  ping www.baidu.com
   27  iptables -F
   28  ip a
   29  ping www.baidu.com
   30  service network restart
   31  ping www.baidu.com
   32  ip a
   33  service sshd start
   34  reboot
   35  ls
   36  ip a
   37  ping www.baidu.com
   38  vim /etc/resolv.conf
   39  vi /etc/resolv.conf
   40  ping www.baidu.com
   41  ls
   42  exit
   43  ls
   44  mount /dev/cdrom /mnt
   45  ls
   46  cd /usr/local/packages/
   47  ls
   48  tar -zxf Python-3.5.2.tgz 
   49  cd Python-3.5.2
   50  ls
   51  vim Modules/Setup.dist 
   52  ./configure --prefix=/usr/local/python/python37 --enable-shared
   53  make -j 4
   54  yum install zlib zlib-devel
   55  ls
   56  cd ..
   57  cd Python-3.5.2
   58  ls
   59  mkdir devel
   60  yum install zlib zlib-devel
   61  yum install --downloadonly --downloaddir=./devel/ zlib zlib-devel
   62  yum reinstall --downloadonly --downloaddir=./devel/ zlib zlib-devel
   63  cd devel
   64  ls
   65  rpm zlib-devel-1.2.7-18.el7.x86_64.rpm -ihv
   66  cd ..
   67  make
   68  yum install --downloadonly --downloaddir=./devel/ libbz2 libbz2-devel
   69  yum search bz2
   70  yum search bzip2
   71  yum install --downloadonly --downloaddir=./devel/ bzip2 bzip2-devel
   72  rpm -ivh devel/bzip2-*
   73  make
   74  yum search curses
   75  yum install --downloadonly --downloaddir=./devel/ ncurses ncurses-devel
   76  yum reinstall --downloadonly --downloaddir=./devel/ ncurses ncurses-devel
   77  rpm -ivh devel/ncurses-*
   78  make
   79  yum search _curses_panel
   80  yum search curses_panel
   81  yum search curses
   82  yum -y reinstall zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite sqlite-devel readline-devel tk tk-devel gdbm gdbm-devel db4-devel libpcap-devel lzma xz xz-devel libuuid libuuid-devel libffi-devel --downloadonly --downloaddir=./devel/
   83  yum -y rinstall zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite sqlite-devel readline-devel tk tk-devel gdbm gdbm-devel db4-devel libpcap-devel lzma xz xz-devel libuuid libuuid-devel libffi-devel --downloadonly --downloaddir=./devel/
   84  yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite sqlite-devel readline-devel tk tk-devel gdbm gdbm-devel db4-devel libpcap-devel lzma xz xz-devel libuuid libuuid-devel libffi-devel --downloadonly --downloaddir=./devel/
   85  ls
   86  rpm -ivh devel/*
   87  make
   88  yum search tkinter
   89  yum install --downloadonly --downloaddir=./devel/ tkinter
   90  rpm -ivh devel/t*
   91  rpm -ivh devel/tix-8.4.3-12.el7.x86_64.rpm 
   92  rpm -ivh devel/t* --force --nodeps
   93  make
   94  yum search tk
   95  yum reinstall tk
   96  make
   97  yum reinstall tkinter
   98  make
   99  yum reinstall tkinter-devel
  100  yum reinstall tk-devel
  101  make
  102  ls
  103  yum install sqlite sqlite-devel
  104  make
  105  yum install readline
  106  yum install readline-devel
  107  make
  108  yum search ssl
  109  yum search openssl-devel
  110  yum install openssl-devel
  111  make
  112  yum install lzma
  113  yum install lzma-devel
  114  make
  115  yum search lzma
  116  yum search xz xz-devel
  117  yum install xz xz-devel
  118  make
  119  yum search gdbm
  120  yum install gdbm gdbm-devel
  121  make
  122  history

```

