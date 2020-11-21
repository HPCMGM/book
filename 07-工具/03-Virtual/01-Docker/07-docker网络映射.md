# 1. docker端口映射

将docker80端口映射到本机80端口

```bash
docker run -d --name web -p 80:80 nginx
```

测试

```bash
curl localhost
```

# 2. docker网络搭建

## 2.1 网络接口veth

相当于插口, 将两个网络进行连接

### 2.1.1 NET NameSpace(nets)接口

网络空间, 可以模拟多个网络设备的通讯

```bash
ip netns list  # 查看全部网络空间
ip netns delete name  # 删除指定网络空间
ip netns add name   # 增加网络空间
```

### 2.1.2 veth接口创建

```bash
ip netns exec test ip link set dev veth-test up   # 在网络空间test中启动一个veth-test的veth接口
ip netns exec test ip a   # 查看test网络空间中的全部ip
ip netns exec test ip addr add 192.168.1.1/24 dev veth-test  # 设置veth-test接口ip
```

实例

1. 创建两个网络空间

   ```bash
   ip netns test1
   ip netns test2
   ```

2. veth连接两个命名空间

   ```bash
   ip link add veth-test1 type veth peer name veth-test2
   ```

3. 将两个接口分别进行互联操作

   ```bash
   ip link set veth-test1 netns test1
   ip link set veth-test2 netns test2
   ```

4. 设置veth的ip

   ```bash
   ip netns exec test1 ip addr add 192.168.1.2/24 dev veth-test1
   ip netns exec test2 ip addr add 192.168.1.3/24 dev veth-test2
   ```

5. 启动veth

   ```bash
   ip netns exec test1 ip link set dev veth-test1 up
   ip netns exec test2 ip link set dev veth-test2 up
   ```

6. 测试ip连通性

   ```bash
   ip netns exec test1 ping 192.168.1.3
   ```

## 2.2 docker使用veth接口

### 2.2.1 docker网络查看

```bash
docker network ls
```

下载工具

```bash
sudo apt -y install bridge-utils
```

查看docker的veth挂载详情信息

```bash
brctl show
```

查看docker内部网络详细信息

```bash
docker network inspect bridge
```

### 2.2.2 docker绑定veth接口

调用veth接口时, 有点像DNS一样

1. 创建container 1

   ```bash
   docker run -d --name test1 busybox /bin/sh -c "while true;do sleep 3600;done"
   ```

2. 创建container 2, 并绑定veth

   ```bash
   docker run -d --name test2 --link test1 busybox /bin/sh -c "while true;do sleep 3600;done"
   ```

3. 当前ip情况如下

   ```bash
   test1 ip: 172.17.0.3
   test2 ip: 172.17.0.2
   ```

4. 测试链接情况

   ```bash
   docker exec -it test1 /bin/sh
   >>> ping 172.17.0.2  # 能ping通
   >>> ping test2       # 能ping通
   >>> exit
   
   docket exec -it test2 /bin/sh
   >>> ping 172.17.0.3  # 能ping通
   >>> ping test1       # 不能通
   ```

所以link创建的ip, 只是单向的, 使用的是默认的bridge

### 2.2.3 docker手动创建bridge

1. 删除其他测试的container

   ```bash
   docker rm $(docker stop $(docker ps -aq))
   ```

2. 创建网络bridge

   ```bash
   docker network create -d bridge test_work
   brctl show  # 查看创建效果
   ```

3. 运行container(默认连接在bridge上), 并指定test_work绑定

   ```bash
   docker run -d --name test3 --network test_work busybox /bin/sh -c "while true;do sleep 3600;done"
   # 对于运行中的docker, 也可以进行添加
   docker network connect test_work test2  # 将test_work添加到container名字为test2的上
   ```

4. 查看当前网络情况

   ```bash
   docker network inspect bridge
   docker network inspect test_work
   ```

5. 测试网络连通性

   ```bash
   docker exec -it test3 /bin/sh
   >>> ping test1  # 不通
   >>> ping test2  # 连通
   docker exec -it test2 /bin/sh
   >>> ping test1  # 连通
   >>> ping test3  # 连通
   docker exec -it test1 /bin/sh
   >>> ping test2  # 连通
   >>> ping test3  # 不通
   说明:
       <1> docker 创建的网络默认添加DNS
       <2> container拥有多个网络时可以连接两个网络段的ip/dns
   ```

   

## 2.3 桥接模式

与宿主机公用同一个ip

```bash
docker run -d --name web --network host nginx
```

查看container的ip

```bash
docker network inspect bridge  # ip为空
docker exec web /bin/sh ip a   # ip数据与主机相同
```

查看宿主机ip

```bash
ip a
```

示例

创建一个flask与redis通讯的应用

1. 创建redis container

   ```bash
   docker run -d --name redis redis  # 创建docker container
   ```

2. 创建dockerfile

   ```dockerfile
   COPY 3.py /app/app.py
   WORKDIR /app
   RUN pip install flask redis
   EXPOSE 5000
   CMD ["python", "app.py"]
   ```

3. 编译dockerfile

   ```bash
   docker build -t hpcmgm/flask .
   ```

4. 运行flask程序, 并与redis通讯

   ```bash
   docker run -d -p 5000:5000 --link redis -e REDIS_HOST=redis --name flask-redis hpcmgm/flask
   ```

5. 测试

   ```bash
   curl localhost:5000
   ```

   

