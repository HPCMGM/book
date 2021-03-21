# 1. swarm(docker集群)

* 主节点创建

  ```bash
  docker swarm init --advertise-addr 10.0.0.11
  ```

  实例

  ```bash
  root@ubuntu:/etc/apt# docker swarm init --advertise-addr 10.0.0.11
  Swarm initialized: current node (m3firj3hmyl84e0wx2ff6psg4) is now a manager.
  
  To add a worker to this swarm, run the following command:
  
      docker swarm join --token SWMTKN-1-415z1uzj3bkendkjju9eqa42am58lyv20eu5pf86vkb4xl9vnl-d6batdh69p64tgmy19jhh3s6b 10.0.0.11:2377
  
  To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
  
  root@ubuntu:/etc/apt#
  ```

* 子节点创建

  ```bash
  docker swarm join --token SWMTKN-1-415z1uzj3bkendkjju9eqa42am58lyv20eu5pf86vkb4xl9vnl-d6batdh69p64tgmy19jhh3s6b 10.0.0.11:2377
  ```

  示例

  ```bash
  [root@localhost ~]# docker swarm join --token SWMTKN-1-415z1uzj3bkendkjju9eqa42am58lyv20eu5pf86vkb4xl9vnl-d6batdh69p64tgmy19jhh3s6b 10.0.0.11:2377
  This node joined a swarm as a worker.
  [root@localhost ~]#
  ```

* 查看加入的节点

  需要切换到主节点上才能执行查询操作

  ```bash
  docker node ls
  ```

  示例

  ```bash
  root@ubuntu:/etc/apt# docker node ls
  ID                            HOSTNAME                STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
  vs5tqav7f257ds3b2put0sitd     localhost.localdomain   Ready               Active                                  18.09.5
  m3firj3hmyl84e0wx2ff6psg4 *   ubuntu                  Ready               Active              Leader              19.03.13
  root@ubuntu:/etc/apt#
  ```

# 2. server(容器集群)

```bash
docker service create --name test busybox /bin/sh -c "while true;do sleep 3600;done"  # 创建
docker service ps test  # 查看
docker service rm test   # 删除
```

示例

一次性创建多个

```bash
docker service scale test=5  # 创建5个test, 负载均衡, 分布在三台服务器中
docker service ps test       # 可以参看到所有test
docker ps                    # 查看当前机器中的test
```

随机杀死一个

```bash
docker service rm -f c8b038f357b6  # 随机杀死worker/leader中的一个test
docker service ps test         # 还是5个test, 保证服务的开启有效性, 不会中断
```



# 3. 示例

## 3.1 wordpress搭建

负载均衡LVS使用VIP虚拟网络搭建wordpress

1. 创建网络

   ```bash
   docker network create -d overlay my-net
   ```

2. 创建mysql container

   ```bash
   docker service create --name mysql --network my-net --env   MYSQL_ROOT_PASSWORD=root --env MYSQL_DATABASE=wordpress --mount type=volume,source=mysql-data,destination=/var/lib/mysql mysql
   ```

3. 配置mysql

   ```bash
   docker exec -it mysql.1.zxd9kjpy9d228nlf7e7uj6qok /bin/sh
   >>> mysql -uroot -proot
   >>> ALTER USER 'root'@'%' IDENTIFIED BY 'root' PASSWORD EXPIRE NEVER;
   >>> ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
   >>> FLUSH PRIVILEGES;
   ```

4. 创建wordpress container

   ```bash
   docker service create --name wordpress -p 80:80 --network my-net --env  WORDPRESS_DB_PASSWORD=root --env WORDPRESS_DB_HOST=mysql wordpress
   ```

5. 测试

   ```bash
   curl localhost:80
   ```

   