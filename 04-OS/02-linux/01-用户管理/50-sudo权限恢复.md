# 1. sudo

## 1.1 sudo权限被改处理

1. 进入recovery模式, 选中root

2. 以读写模式挂载根目录

   ```bash
   mount -o remount rw /
   ```

3. 恢复权限

   ```bash
   chown -R root:root /usr  # 恢复文件归属
   chmod -R 755 /usr  # 恢复文件权限
   chmod 4755 /usr/bin/sudo  # 恢复sudo权限
   ```

4. 重启即可

   ```bash
   root
   ```

   