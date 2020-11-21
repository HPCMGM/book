# 1. 镜像源

## 1.1 国内源

```bash
https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/  # 清华源
```

## 1.2 源修改

操作文件: `/etc/apt/sources.list`

```bash
mv /etc/apt/sources.list /etc/apt/sources.list_bak
vim /etc/apt/sources.list
```

将国内源更新到此文件中, 然后更新源

```bash
apt-get update
```

