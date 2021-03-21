# 1. 程序运行

```bash
docker container [选项] 镜像/镜像ID
```

* run: 指定的image运行, 并生成一个container ID
* stop: 停止指定container
* restart: 重启container
* kill: 杀死container
* rm: 移除container, 需要先停止
* logs: 查看该container中的标准数据流
* inspect: 查看container的详细信息
* ls: 查看运行中的container
* commit: 保存当前状态container, 并生成对应的镜像

# 2. run

## 2.1 参数详解

```bash
docker container run [选项] 镜像名称
```

* -i: 交互式模式运行
* -t: 给镜像分配伪终端, 常于-i同时使用
* -d: 后台执行
* -p: 映射端口(本地端口:docker内部端口)
* -v: 目录映射(本地目录:docker目录)
* -e: 添加环境变量, 可以多次调用. 格式`-e PYTHON=/bin/bash/python`
* --name: 给容器命名
* --network=host: 将主机网络环境映射到主机中
* 

## 2.1 实例

1. 直接进入交互模式

   ```bash
   [root@localhost repos]# docker run -it centos /bin/bash  # 直接运行镜像, 并进入shell模式
   [root@91aef102099a /]# ls
   bin  dev  etc  home  lib  lib64  lost+found  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
   [root@91aef102099a /]# exit
   exit
   [root@localhost repos]#
   ```

   

2. 后台模式, 并进入shell

   ```bash
   [root@localhost repos]# docker run -d -it centos /bin/bash -c "while true; do echo 1111; sleep 1;done"  # 后台执行docker容器
   290d7607f4c8721f1337242b84bd15cdbe6ddf4e202efaa65d4b12e0f24d45c3
   [root@localhost repos]# docker container ls
   CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
   290d7607f4c8        centos              "bash -c 'while true…"   23 seconds ago      Up 22 seconds                           affectionate_shamir
   [root@localhost repos]# docker container exec -it 290d7607f4c8 /bin/bash  # 进入终端shell
   [root@290d7607f4c8 /]# exit
   exit
   [root@localhost repos]#
   ```

# 3. ls

## 3.1 参数详解

```bash
docker container ls[ ID/名称] [/bin/bash|exec][ -c 命令]
```

* -a: 展示全部container, 包含已经停止的, 默认只显示运行的.
* -p: 显示完整的ID编号, 默认只显示部分
* -q: 只显示ID, 不显示其他信息
* -f: 过滤查看指定状态的ID, `status=exited`表示查看已经退出的ID
* /bin/bash:  绑定指定shell, 给docker关联使用
* exec: 直接运行, 并进入shell交互模式
* -c: 前台直接用shell执行命令
* -d: 后台守护执行命令



# 4. logs

## 4.1 参数详解

```bash
docker logs id
```

# 5. stop

## 5.1 参数详解

```bash
docker container stop id
```

# 6. start

停止的的container, 使用start即可启动

## 6.1 参数详解

```bash
docker container start id
```



# 7. rm

## 7.1 参数详解

```bash
docker container rm id
```

* -f: 强制删除正在运行的container, 默认不可删除运行的docker

## 7.2 实例

### 7.2.1 批量删除

```bash
docker container $(docker container ls -aq)  # 删除全部
docker container $(docker container ls -qf "status=exited")  # 删除已经退出的ID
```

