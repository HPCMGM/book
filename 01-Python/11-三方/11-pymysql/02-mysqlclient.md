# 1. mysqlclient安装需要确保如下信息
1. 当前系统必须安装 `mysql`
2. 必须存在依赖
```python
yum install python-devel mysql-devel MySQL-python
```
3. 虚拟环境创建(注意, 此步骤一定要在依赖安装之后进行, 否则会出现, 不在虚拟环境安装是可以的, 进入虚拟环境后, 就无法安装mysqlclient, 显示Python头文件编译失败)
4. 安装mysqlclient
```python
pip install mysqlclient
```
