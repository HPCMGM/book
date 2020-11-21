# 1. 用户信息恢复

## 1.1 家目录文件恢复

误删家目录文件恢复用户登录.

```bash
[root@localhost ~]# rm -rf /home/test/*
[root@localhost ~]# su test
bash-4.1$ exit  # 登录异常.....
exit
[root@localhost ~]# useradd test1
[root@localhost ~]# cp /home/test1/.bash* /home/test/
[root@localhost ~]# su test
[test@localhost root]$  # 正常切换
```

