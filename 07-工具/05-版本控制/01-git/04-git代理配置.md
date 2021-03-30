修改ssh-key的密码

```shell
ssh-keygen -f id_rsa -p
```

其他操作

```shell
git config --list   # 查看配置列表

# 设置代理
git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy http://127.0.0.1:1080

# 取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy
```

