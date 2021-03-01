# 1. FastDFS

C语言编写的分布式文件管理系统. 

## 1.1 特点

* 考虑冗余文件备份
* 负载均衡
* 线程库容机制
* 高可用, 高性能

## 1.2 架构

* Tracker server(调度服务器)

  管理集群, 每个tracker节点低位平等, 手机Storage集群状态

* Storage Server(存储服务器)

  真实保存文件, Storage分为很多的组. 每个组之间保存的文件是不同的. 每组内部可以有很多程勇, 组成成员内部保存的内容是一样的, 成员地位平等, 没有主从概念.

  ```python
  group1 /M00 /02 /44/ wKgDrE34E8eAAAAAAAAasfsfaFSD.sh
  ```

  * 组名: `group1`, 文件上传后所在的storage组名称.
  * 虚拟磁盘路径: `/M00`, storage配置的虚拟路径, 与磁盘选项store_path*对应, 如果配置的store_paht0则是M00, 如果配置store_path1则是M01, 依次类推
  * 数据两级目录: `/02/44`, storage服务器会在每个虚拟磁盘下, 创建两级目录用于存储文件
  * 文件名称: `wKgDrE34E8eAAAAAAAAasfsfaFSD.sh`,  文件名称创建是根据: 时间, 名称, 服务器ip地址, 文件创建时间戳, 文件大小, 随机数, 文件拓展名等信息生成的.

# 2. Docker部署

## 2.1 拉取镜像

### 2.1.1 在线拉取

```python
docker image pull delron/fastdfs
```

### 2.1.2 官方镜像包

官方进行下载太慢了, 我这里提供了打包后的官方包: 

[百度下载](https://pan.baidu.com/s/1_h71riGd2wfJ3PgYFjZybQ )[密码: hpcm]

## 2.2 运行容器

如果不能运行, 则删除`/usr/data/fastdfs/storage/data`中的`fdfs_storaged.pid`文件, 然后重新运行

### 2.2.1 tracker运行

```python
docker run -dti --network=host --name tracker -v /home/appgess/Desktop/fastdfs/tracker:/var/fdfs delron/fastdfs tracker
```

### 2.2.2 storage运行

```python
docker run -dti --network=host --name storage -e TRACKER_SERVER=10.0.0.13:22122 -v /home/appgess/Desktop/fastdfs/storage:/var/fdfs delron/fastdfs storage
```

## 2.3 使用

1. 安装`fdfs-client`拓展包

   ```python
   pip install fdfs-client-py3
   pip install mutagen
   pip install requests
   ```

2. 配置`client`配置文件[conf](image/26-FastDFS/client.conf)

   修改部分:

   ```python
   base_path=xxx        # FastDFS存放日志的目录
   tracker_server=xx    # tracker 服务器ip:22122
   ```

3. 上传使用

   ```python
   from fdfs_client.client import Fdfs_client
   
   client = Fdfs_client("client.conf")
   res = client.upload_by_filename(r"xx")  # 上传文件 绝对路径
   res = client.upload_by_buffer("xx")    # 上传二进制流
   ```

4. 访问

   ```python
   curl localhost:8888/group/xxx
   ```

   

