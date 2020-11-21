# 1. linux配置

配置文件位置: `/etc/vsftpd.conf`

## 1.1 参数解析

## 1.2 实例配置

### 1.2.1 Ubuntu示例参考

1. 配置文件

   ```bash
   anonymous_enable=NO
   local_root=/home/python/ftp
   local_enable=YES
   chroot_list_enable=YES
   chroot_list_file=/etc/vsftd.chroot_list
   write_enable=YES
   ```

2. 创建文件

   ```bash
   vi /etc/vsftpd.chroot_list
   ```

3. 添加权限

   ```bash
   sudo chmod 555 ftp
   ```

