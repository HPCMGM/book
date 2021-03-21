# 1. docker-compose安装

## 1.1 在线安装

### 1.1.1 Ubuntu

```bash
curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
chmod +x /usr/local/bin/docker-compose && \
docker-compose --version
```

# 2. docker-compose配置

创建`docker-compose.yaml`文件

```bash
version: 3  # 表示版本号
services:   # 需要启动的container配置
	xxx
volumes:    # 路径映射配置
	xxx 
network:    # 网络配置
```

# 3. docker-compose命令

```bash
docker-compose built . # 创建image镜像
docker-compose up      # 交互式启动当前目录中`docker-compose.yml`文件
docker-compose up -d   # 后台启动
docker-compose up --scale web=3 -d  # 批量启动, 也可以批量减少
```



# 2. 示例

## 2.1 搭建wordpress

### 2.1.1 普通搭建

1. 下载mysql/wordpress

   ```bash
   docker pull mysql
   docker pull wordpress
   ```

2. 运行并配置mysql

   ```bash
   run -d --name mysql -v mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=wordpress mysql
   ```

   *注: mysql的具体配置参数参见: https://hub.docker.com/_/mysql/*

3. 处理php连接mysql密码错误 [重置密码即可]

   ```bash
   docker exec -it mysql /bin/bash
   >>> mysql - u root -p root
   >>> ALTER USER 'root'@'%' IDENTIFIED BY 'root' PASSWORD EXPIRE NEVER;
   >>> ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
   >>> FLUSH PRIVILEGES;
   ```

4. 配置wordpress

   ```bash
   docker run -d -p 80:80 --link mysql -e WORDPRESS_DB_HOST=mysql:3306 wordpress
   ```

   *注: wordpress配置参数参见: https://hub.docker.com/_/wordpress/*

5. 访问测试

   ```bash
   curl localhost
   ```

   

### 2.1.2 compose搭建

1. 配置yaml文件

   ```bash
   # docker-compose.yml
   version: "3"
   services:
       wordpress:
           image: wordpress
           ports:
               - 80:80
           environment:
               WORDPRESS_DB_HOST: mysql
               WORDPRESS_DB_PASSWORD: root
           networks:
               - my-bridge
       mysql:
           image: mysql
           environment:
               MYSQL_ROOT_PASSWORD: root
               MYSQL_DATABASE: wordpress 
           volumes:
               - mysql-data:/var/lib/mysql
           networks:
               - my-bridge
   volumes:
       mysql-data:
   networks:
       my-bridge:
           driver: bridge
   ```

2. 启动compose

   ```bash
   docker-compose up
   ```

3. 同样需要配置mysql密码问题

   ```bash
   docker exec -it mysql /bin/bash
   >>> mysql - u root -p root
   >>> ALTER USER 'root'@'%' IDENTIFIED BY 'root' PASSWORD EXPIRE NEVER;
   >>> ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
   >>> FLUSH PRIVILEGES;
   ```

4. 启动wordpress

   ```bash
   docker start wordpress
   ```

5. 访问并验证

   ```bash
   curl localhost
   ```

   

