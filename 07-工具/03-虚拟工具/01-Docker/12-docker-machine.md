# 1. 安装

docker-machine, 在虚拟机中启动一个小巧的linux并自带一个docker

https://docs.docker.com/machine/install-machine/#install-machine-directly

网页版docker: `docker payground`, 登录即可使用

# 2. 使用

```bash
docker-machine create demo  # 安装docker, 命名为demo
docker-machine ls   # 列出所有的docker
docker-machine ssh demo  # 登录demo中
docker-machine stop demo  # 停止demo
docker-machine rm demo   # 删除demo
```

# 3. 配置

## 3.1 全局变量配置

```bash
docker-machine env demo  #查询全局变量
eval $(docker-machine env demo)  # 设置全局变量
docker-machine env --unset   # 取消变量
eval $(docker-machine env --unset)  # 取消并设置变量
```

## 3.2 操作aliyun配置

1. 下载aliyun驱动

   ```bash
   https://github.com/AliyunContainerService/docker-machine-driver-aliyunecs
   ```

2. 将文件改名并放入如下路径

   ```bash
   /usr/local/bin/docker-machine-driver-aliyunecs
   ```

3. 测试是否安装成功

   ```bash
   docker-machine create -d aliyunecs --help
   ```

4. 获取aliyun的AccessKey

   ```bash
   创建AccessKey会显示secret_key 只显示一次, 注意保存
   ```

5. 利用docker-machine启动阿里云docker

   ```bash
   docker-machine create -d aliyunecs --aliyunecs-io-optimized=optimized --aliyunecs-instance-type=ecs.c5.large(选择自己的实例类型) --aliyunecs-access-key-id=LTAIPoRNN2dtRazR(实例的access_key) --aliyunecs-access-key-secret=VWasyt5MnYwI52GH66wkygQQ5Lv&uV(实例的secret_key) --aliyunecs-region=cn-qingdao(实例的位置) demo
   ```

   