# 1. uwsgi

本模块遵循WSGI协议, 用于Python web动态请求分发.

## 1.1 安装

```python
已经存在Python的环境中直接运行
pip install uwsgi
```

## 1.2 命令

```python
uwsgi uwsgi.ini  # 启动
killall -s INT uwsg  # 停止
```

## 1.3 配置文件

```python
[uwsgi]
master=true
http=:8000
home=/home/appgess/.virtualenvs/transmit
pythonpath=/home/appgess/.virtualenvs/transmit/bin/python
module=manager
chdir=/home/appgess/project/transmit
callable=app
processes=2
threads=4
buffer-size=65536
memory-report=true
env=python=/home/appgess/.virtualenvs/transmit/bin/python
pidfile=/home/appgess/server/transmit/uwsgi.pid

[uwsgi]
# 使用nginx连接时使用，Django程序所在服务器地址
socket=192.168.229.133:8001
# 直接做web服务器使用，Django程序所在服务器地址, 使用nginx时注释掉这个
# http=192.168.229.133:8001
# 项目目录
chdir=/home/python/Desktop/test
# 项目中wsgi.py文件的目录，相对于项目目录
wsgi-file=test/wsgi.py
# 进程数
processes=4
# 线程数
threads=2
# uwsgi服务器的角色
master=True
# 存放进程编号的文件
pidfile=uwsgi.pid
# 日志文件，因为uwsgi可以脱离终端在后台运行，日志看不见。我们以前的runserver是依赖终端的
daemonize=uwsgi.log
# 指定依赖的虚拟环境
virtualenv=/home/python/.virtualenvs/py3_django_1.11

uwsgi添加虚拟环境时  需要的路径指向为: bin/python之前  /home/appgess/.virtualenvs/test
```

