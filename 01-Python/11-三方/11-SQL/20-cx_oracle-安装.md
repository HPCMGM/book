### 1. 驱动准备

1. 到官网下载`instantclient-basic`: https://www.oracle.com/cn/database/technologies/instant-client/downloads.html
2. 这里提供了版本: `11.2.0.4.0`的文件
   * [instantclient-basic-linux.x64-11.2.0.4.0](image/20-oracle-%E5%AE%89%E8%A3%85/instantclient-basic-linux.x64-11.2.0.4.0.zip)
   * [instantclient-basic-windows.x64-11.2.0.4.0](image/20-oracle-%E5%AE%89%E8%A3%85/instantclient-basic-windows.x64-11.2.0.4.0.zip)
   * [instantclient-sdk-linux.x64-11.2.0.4.0](image/20-oracle-%E5%AE%89%E8%A3%85/instantclient-sdk-linux.x64-11.2.0.4.0.zip)
   * [instantclient-sqlplus-linux.x64-11.2.0.4.0](image/20-oracle-%E5%AE%89%E8%A3%85/instantclient-sqlplus-linux.x64-11.2.0.4.0.zip)

### 2. 部署环境

#### windows

1. 解压

2. 配置环境, `PATH`中添加

   ```python
   ORACLE_HOME=instantclient-basic-win32-11.2.0.1.0\instantclient_11_2
   ```

#### linux

1. 解压

   ```python
   mkdir -p /opt/oracle
   cd /opt/oracle
   unzip instantclient-basic-linux.x64-11.2.0.4.0.zip
   ```

2. 安装依赖

   ```python
   yum install libaio
   ```

3. 创建连接

   ```python
   sh -c "echo /opt/oracle/instantclient_19_3 > /etc/ld.so.conf.d/oracle-instantclient.conf"
   ```

   刷新依赖

   ```python
   ldconfig
   LD_LIBRARY_PATH=/opt/oracle/instantclient_19_3:$LD_LIBRARY_PATH
   ```

4. 配置ora(选填, Python用不到)

   ```python
   mkdir -p /opt/oracle/instantclient_12_2/network/admin
   tnsnames.ora，sqlnet.ora或oraaccess.xml
   ```

   






