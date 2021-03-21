# 2. 示例

## 2.1 具体操作

需求: 搭建docker分布式连接

环境: 使用virtualbox中的vagrant创建两台centos系统

1. 创建virtualbox系统环境

   配置启动文件: `vim vagrantfile`

   ```bash
   servers = {
           :hadoop1 => '192.17.0.2',
           :hadoop2 => '192.17.0.3',
           }
   
   Vagrant.configure("2") do |config|
   config.vm.box = "ubuntu/xenial64"
   config.vm.box_check_update = false
   
     servers.each do |server_name, server_ip|
       config.vm.define server_name do |server_config|
       server_config.vm.hostname = "#{server_name.to_s}"
       server_config.vm.network :private_network, ip: server_ip
               server_config.vm.provider "virtualbox" do |vb|
               vb.name = server_name.to_s
                   vb.memory = "2048"
                   vb.cpus = 1
            end
         end
     end
   end
   ```

2. 创建系统

   ```bash
   vagrant up  # 启动, 此过程比较漫长
   vagrant ssh hadoop1  # 登录机器1
   vagrant ssh hadoop2  # 登录机器2
   ```

3. 安装docker

   在两台机器上分别安装docker, 此过程略

4. 下载etcd

   两台都要执行

   ```bash
   wget https://github.com/coreos/etcd/releases/download/v3.0.12/etcd-v3.0.12-linux-amd64.tar.gz
   tar zxvf etcd-v3.0.12-linux-amd64.tar.gz
   cd etcd-v3.0.12-linux-amd64
   ```

5. 配置节点hadoop1

   ```bash
   nohup ./etcd --name docker-node1 --initial-advertise-peer-urls http://192.17.0.2/:2380 \
               --listen-peer-urls http://192.17.0.2:2380 \
               --listen-client-urls http://192.17.0.2:2379,http://127.0.0.1:2379 \
               --advertise-client-urls http://192.17.0.2:2379 \
               --initial-cluster-token etcd-cluster \
               --initial-cluster docker-node1=http://192.17.0.2:2380,docker-node2=http://192.168.205.11:2380 \
               --initial-cluster-state new &
   ```

6. 配置节点hadoop2

   ```bash
   nohup ./etcd --name docker-node2 --initial-advertise-peer-urls http://192.17.0.3:2380 \
               --listen-peer-urls http://192.17.0.3:2380 \
               --listen-client-urls http://192.17.0.3:2379,http://127.0.0.1:2379 \
               --advertise-client-urls http://192.17.0.3:2379 \
               --initial-cluster-token etcd-cluster \
               --initial-cluster docker-node1=http://192.17.0.2:2380,docker-node2=http://192.17.0.3:2380 \
               --initial-cluster-state new&
   ```

7. 查看运行状态

   ```bash
   [root@localhost ~]# ./etcdctl cluster-health
   member b8889e27b0c4c2cd is healthy: got healthy result from
   http://192.17.0.2:2379
   member ce8341085788e517 is unhealthy: got unhealthy result from
   http://192.17.0.3:2379
   cluster is degraded
   [root@localhost ~]# 
   ```

8. 配置docker

   * hadoop1

     ```bash
     sudo service docker stop && \
     sudo /usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock --cluster-store=etcd://192.17.0.2:2379 --cluster-advertise=192.17.0.2:2375 &
     ```

   * hadoop2

     ```bash
     sudo service docker stop && \
     sudo /usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock --cluster-store=etcd://192.17.0.3:2379 --cluster-advertise=192.17.0.3:2375 &
     ```

   做完此过程, 建议重新进入系统, 不然会有大量日志输出

9. 创建网络节点

   在两台机器上都执行.

   ```bash
   docker network ls  # 查看网络接口
   docker network create -d overlay deme   # 创建网络接口
   docker network inspect demo   # 查看网络接口详情
   ```

10. 测试

    测试一: 容器创建测试

    * hadoop1

      ```bash
      docker run -d --name test1 --net demo busybox sh -c "while true; do sleep 3600; done"
      ```

    * hadoop2

      ```bash
      执行相同的命令则无效, 提示名字重复
      ```

    测试二: 网络连通测试

    * hadoop1

      ```bash
      docker exec test1 ping test2 # ping通
      ```

    * hadoop2

      ```bash
      docker exec test2 ping test1 # ping通
      ```

      