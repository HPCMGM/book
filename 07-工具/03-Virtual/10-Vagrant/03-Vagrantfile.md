# 1. 配置多节点

1. vagrantfile

   ```bash
   Vagrant.configure("2") do |config|
   
    (1..4).each do |i|
   
     config.vm.define "node#{i}" do |node|
   
     # 设置虚拟机的Box
     node.vm.box = "ubuntu/xenial64"
   
     # 设置虚拟机的主机名
     node.vm.hostname="node#{i}"
     config.vm.box_check_update = false
   
     # 设置虚拟机的IP
     node.vm.network "private_network", ip: "192.168.44.#{i}"
   
     # 设置主机与虚拟机的共享目录
     node.vm.synced_folder "~/Desktop/share", "/home/vagrant/share"
   
     # VirtaulBox相关配置
     node.vm.provider "virtualbox" do |v|
   
      # 设置虚拟机的名称
      v.name = "node#{i}"
   
      # 设置虚拟机的内存大小  
      v.memory = 2048
   
      # 设置虚拟机的CPU个数
      v.cpus = 1
     end
     end
    end
   end
   ```

2. 镜像源修改

   ```bash
   sudo vim /etc/apt/sources.list
   # 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
   deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
   # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted universe multiverse
   deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
   # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted universe multiverse
   deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
   # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
   deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
   # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted universe multiverse
   
   # 预发布软件源，不建议启用
   # deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
   # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-proposed main restricted universe multiverse
   ```

3. 安装必备软件

   ```bash
   sudo apt update && \
   sudo apt install -y python python3 python-pip python3-pip nmap libssl-dev openssh-server  ipython3 && \
   sudo -s && \
   apt install ipython ipython3
   
   # 设置root密码
   sudo passwd root
   ```

4. 安装ssh

   ```bash
   sudo vim /etc/ssh/sshd_config
   #PermitRootLogin yes
   #PasswordAuthentication yes
   ansible运行会报错: [WARNING]: sftp transfer mechanism failed on [19.19.19.244]. Use ANSIBLE_DEBUG=1 to see detailed information
   注释掉:  
   Subsystem      sftp    /usr/lib/ssh/sftp-server
   
   
   service sshd restart
   ```

5. 安装mysql

   ```bash
   sudo apt install -y mysql-server
   sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
   ```

   

