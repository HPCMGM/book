# 1. Redhat

## 1.1  redhat 6

1. 编辑启动引导, 以单用户模式启动系统(安全模式)

   ![image-20200714224556810](image/51-root%E5%AF%86%E7%A0%81%E9%87%8D%E7%BD%AE/image-20200714224556810.png)

2. 进入系统后, 可以直接进行密码修改, 修改完成后重启电脑, 

   * 下次启动无需修改系统引导, 系统将以默认的init启动电脑

   ```bash
   Telling INIT to go to single user mode.
   init: rc main process(1001) killed by TERM signal
   [root@localhost /]# echo "dong10" | passwd --stdin root
   Changing password for user root.
   passwd: all authentication tokens updated successfully.
   [root@localhost /]# reboot
   
   ```

# 2. CentOS

## 2.1 centos 7

1. 修改启动引导, 开机按e

   ![image-20200714231532796](image/51-root%E5%AF%86%E7%A0%81%E9%87%8D%E7%BD%AE/image-20200714231532796.png)

2. 重新挂载系统文件, 让密码可写入

   ```bash
   mount -o remount,rw /sysroot
   chroot /sysroot
   echo "dong10" | passwd --stdin root
   # 第一个exit, 表示退出系统文件可写状态
   exit
   # 第二个exit, 表示进入默认init状态, 一般是init 5
   exit
   ```

   

   ![image-20200714232334184](image/51-root%E5%AF%86%E7%A0%81%E9%87%8D%E7%BD%AE/image-20200714232334184.png)

