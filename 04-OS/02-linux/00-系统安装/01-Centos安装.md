# 1. 无界面mini版

1. 下载

   ```bash
   http://mirrors.163.com/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-1810.iso
   ```

2. 安装

   ```bash
   安装-->install xxx -->system中的安装 -->设置root账号密码 --> 重启系统
   ```

3. 网络配置

   * 网卡激活

     ```bash
     vi /etc/sysconfig/network-scripts/ifcfg-ens33
     # 修改:
     ONBOOT=yes
     ```

   * DNS配置

     ```bash
     vi /etc/resolv.conf
     # 添加: 电信的
     nameserver 114.114.114.114
     ```

4. ssh设置root连接

   操作文件: `/etc/ssh/sshd_config`

   ```bash
   # 修改: 支持root连接
   PermitRootLogin yes
   ```

   关闭防火墙

   ```bash
   service firewalld stop  # 关闭防火墙
   systemctl disable firewalld.service  # 关闭防火墙开机自启
   ```

   重启ssh使其生效

   ```bash
   systemctl enable sshd  # 开启开机自启
   systemctl restart sshd.service  # 重启sshd
   ```

5. 修改开机界面时间等待

   ```bash
   vim /boot/grub2/grub.cfg
   修改 timeout的值即可
   timeout
   ```

6. yum源配置

   ```bash
   按照此网站进行:
   http://mirrors.163.com/.help/centos.html
       
   yum install -y vim wget net-tools
   ```

7. 安装vmtools

   ```bash
   mkdir /mnt/cdrom 			# 创建挂载点
   mount /dev/cdrom /mnt/cdrom	# 挂载ios
   cd /mnt/cdrom
   cp -R /mnt/cdrom/VMwareTool-xxx.tar.gz /home/xx/Desktop && cd /home/xx/Desktop
   tar -zxf VMwareTool-xxx.tar.gz
   cd vmware-tools-distrib
   
   yum -y install perl
   ./vmawre-install
   ```

8. 启用共享文件夹

   ```bash
   在vmware中配置好window中的共享文件wx_apps, 进入linux执行命令如下:
   vmware-hgfsclient   # 查看共享文件
   yum -y install open-vm-tools-devel
   vmhgfs-fuse .host:/wx_apps /root/xx/Code/05-wx_apps/wx_apps -o nonempty -o allow_other
       
   完成后如果出现
   d????????? ? ? ? ?            ? hgfs 无法访问, 这重启即可
   ```

9. 加入开机自启

   ```shell
   vim /etc/rc.d/rc.local
   
   # vmhgfs-fuse .host:/project /home/appgess/project -o nonempty -o allow_other &
   ```

   

