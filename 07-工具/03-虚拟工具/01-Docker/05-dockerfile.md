# 1. dockerfile

用于镜像的制作

# 2. 语法

## 2.1 FROM

基于什么镜像开始制作镜像, 尽量选用官方镜像, 保证安全性

```dockerfile
FROM scratch   # 基础镜像
```

## 2.2 LABEL

用于信息描述

```dockerfile
LABEL maintainer="hpcmpc@gmail.com"      # 作者
LABEL version="1.0"					     # 版本号
LABEL description="This is description"  # 描述信息
```

## 2.3 RUN/CMD/ENTRYPOINT

用于`shell`的命令运行

* RUN, 镜像编译时执行
* ENTRYPOINT, container运行开始时执行
* CMD, container运行后执行

示例一

```dockerfile
RUN apt-get update && \
apt-get -y install vim && \
rm -rf /var/lib/apt/lists/*
# 注意使用\
# 注意清理缓存
```

示例二(shell格式)

```dockerfile
RUN apt-get -y install vim
CMD echo "hello docker"
ENTRYPOINT echo "hello docker"
```

实例三(Exec格式)

```dockerfile
RUN ["apt", "-y", "install", "vim"]
CMD ["/bin/echo", "hello docker"]
ENTRYPOINT ["/bin/echo", "hello docker"]
```



## 2.4 WORKDIR

切换工作目录

```dockerfile
WORKDIR /test
# 此代码相当于: mkdir /test && cd /test
```

## 2.5 ADD/COPY

将本地文件copy到docker镜像中去. 两者语法基本相似

```bash
ADD [--chown=<user>:<group>] <src>... <dest>
ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]
```

实例

```dockerfile
ADD --chown=55:mygroup files* /somedir/
ADD hello /
```

## 2.6 ENV

设置环境变量, 方便命令执行时使用

```dockerfile
ENV <key> <value>
ENV <key>=<value> ...
```

实例

```dockerfile
ENV myName="John Doe" myDog=Rex\ The\ Dog \
    myCat=fluffy

ENV myName John Doe
ENV myDog Rex The Dog
ENV myCat fluffy

ENV MYSQL_VERSION 5.6  # 设置常量
RUN apt -y install mysql-server="${MYSQL_VERSION}"&& \
rm -rf /var/lib/apt/lists/*
```

## 2.7 EXPOSE

端口映射,将本地端口映射docker中

```dockerfile
EXPOSE 80 80
```

