# 1. 字体配置

1. 进入注册表

   ```bash
   计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Console\TrueTypeFont
   # 查看都有什么类型的字体
   ```

2. 配置字体

   ```bash
   chcp 437  # 修改字体
   ```

# 2. 关闭滴滴声音

以管理员权限运行cmd

```bash
sc config start=disabled
sc stop beep
```





