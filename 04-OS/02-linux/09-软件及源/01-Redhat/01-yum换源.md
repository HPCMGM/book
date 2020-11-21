# 1. yum换源

## 1.1 在线源

源文件位置: /etc/yum.repos.d/*.repo

1. 删除源文件

   ```bash
   cd /etc/yum.repos.d
   rm -rf *.repo
   ```

2. 下载需要使用的源

   ```bash
   wget http://mirrors.aliyun.com/repo/Centos-6.repo  # 阿里云
   wget http://mirrors.163.com/.help/CentOS6-Base-163.repo # 网易
   ```

3. 修改变量

   下载的文件中, 存在两个变量

   * $releaserver: 系统版本号, `cat /etc/centos-release`
   * $basearch: 表示系统位数, `uname -r`

   如果发现系统版本和远程服务器版本不一致, 则手动进行修改.(一般服务器保存的是最新版本的数据)

   ```bash
   vim Centos-6.repo  #进入vim进行批量替换
   :%s/$releasever/6/g
   ```

4. 清理缓存, 即可使用

   ```bash
   yum clean all
   yum makecache
   ```

   

## 1.2 挂载ISO盘

### 1.2.1 开机自动加载

```bash
vim /etc/fstab
```

追加内容

```bash
/dev/sr0		/mnt		iso9660     defaults   0   0  # 或者
/dev/cdrom              /mnt                    iso9660 defaults        0 0
```

* /dev/cdrom: 需要挂载的盘符
* /mnt:  挂载的位置
* iso9660: iso盘格式
* defaults: 控制权限等问题
* 0  0: 是否进行开启检测  , 0表示不检测

### 1.2.2 挂载ISO盘

```bash
mount -a  # 挂载
umount /mnt/  # 卸载挂载
```

查看挂载内容

```bash
ls /mnt/
```

![image-20200710231223206](image/01-yum%E6%8D%A2%E6%BA%90/image-20200710231223206.png)

### 1.2.3 指定yum使用ISO

1. 清空源

   ```bash
   cd /etc/yum.repos.d/
   rm -rf *
   ```

2. 配置源

   ```bash
   vim test.repo
   ```

   增加如下内容

   ```bash
   [Redhat]
   name=Redhat-Server
   baseurl=file:///mnt
   enabled=1
   gpgcheck=0
   ```

   * name: 服务名称
   * baseurl: 指定使用源位置, 支持(file:///, http://, ftp://)等
   * enabled: 是否启用
   * gpgcheck: 是否使用公钥检查

3. 清空缓存, 并使用

   ```bash
   yum clean all
   yum install python-pip
   ```

   