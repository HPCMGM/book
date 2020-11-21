# 1. 远程配置

## 1.1 ubuntu

新增文件: `/etc/systemd/system/docker.service.d/override.conf `(路径和文件可能不存在, 创建即可)

添加如下信息

```ini
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix://var/run/docker.sock
ExecReload=/bin/kill -s HUP $MAINPID
TimeoutSec=0
RestartSec=2
Restart=always
```

重启网络和docker服务

```bash
systemctl daemon-reload
systemctl restart docker.service
```

远程连接测试

```bash
docker -H 10.0.0.11 info
```

输出如下, 说明连接成功.

![image-20200923212110091](image/05-docket%E9%85%8D%E7%BD%AE/image-20200923212110091.png)

