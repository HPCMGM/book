# 1. 默认存储

```bash
docker run -d --name mysql_1 -e MYSQL_ALLOW_EMPTY_PASSWORD mysql
```

运行一个mysql

查看存储位置:

```bash
docker volume ls
# 此存储为临时存储, 删除及清空
```

强制移除运行中的mysql

```bash
docker container rm -rf mysql_1
```

# 2.  本地映射

运行并指定存储位置

```bash
docker
run -d --name mysql_1 -v mysql:/var/lib/mysql -e MYSQL_ALLOW_EMPTY_PASSWORD = True mysql
```

存储测试

```bash
docker exec -it mysql_1 /bin/bash
>>> mysql -u root
>>> create database demo charset=utf-8;
>>> exit
exit
```

删除container

```bash
docker rm -f mysql_1
```

重新运行container, 并指定存储位置, 为上次指定的存储位置

```bash
docker run -d --name mysql_2 -v mysql:/var/lib/mysql -e MYSQL_ALLOW_EMPTY_PASSWORD = True mysql
```

查看数据

```bash
docker exec -it mysql_2 /bin/bash
>>> mysql -u root
>>> show databases; 
```

如果数据库中存在`demo`数据库, 则说明测试通过