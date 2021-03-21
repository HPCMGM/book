```bash
4. 搭建私有hub:
    server:
        docker run -d -p 5000:5000 --restart always --name registry:2
    client
        测试网络连通性: telnet ip 5000
        添加server信任:
            sudo vim /etc/docker/daemon.json
            添加:
                {"insecure-registries": ["ip:5000"]}
            sudo vim /lib/systemd/system/docker.service
            [Service]中添加:
                EnvironmentFile=-/etc/docker/daemon.json
    4.1 push/pull:
        创建: docker build -t ip:5000/name .
            docker push ip:5000/name
            docker pull ip:5000/name
    4.2 查看:
        浏览器中:
            ip:5000/v2/_catalog

5. 上传镜像:
    docker login # 登陆账号密码
    docker push  # 提交数据
```





# 1. 配置

## 1.1 创建目录

创建目录用来保存密码认证和证书认证

```python
mkdir -p {/home/hpcm/docker/auth,/home/hpcm/docker/certs}
```

## 1.2 签名证书

修改openssl配置

`vim /etc/pki/tls/openssl.cnf`, 在`[ v3_ca ]`添加

```shell
[ v3_ca ]
subjectAltName = IP:192.168.50.132
```

## 1.3 创建证书

证书创建及更换需要重启docker`service docker restart`

```python

[root@localhost ~]# cd docker/auth
[root@localhost ~]# openssl req -newkey rsa:4096 -nodes -sha256 -keyout ssl.key -x509 -days 365 -out ssl.crt
Generating a 4096 bit RSA private key
...........................................................................................++
...........................................++
writing new private key to 'ssl.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:CN
State or Province Name (full name) []:GD
Locality Name (eg, city) [Default City]:SZ
Organization Name (eg, company) [Default Company Ltd]:GOLD
Organizational Unit Name (eg, section) []:JS
Common Name (eg, your name or your server's hostname) []:192.168.50.132:5000
Email Address []:
[root@localhost ~]# ls
anaconda-ks.cfg ssl.crt ssl.key

```

## 1.4 添加hup认证

添加认证账号密码, 可以创建多个

```python
docker run --entrypoint htpasswd registry:2 -Bbn appgess appgess >> /home/hpcm/docker/auth/htpasswd
```

 

# 2. docker registry

## 2.1 启动docker hup

```python
docker run -d -p 5000:5000 --restart=always -v /home/hpcm/docker/auth/:/auth/ -e "REGISTRY_AUTH=htpasswd" -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/ssl.crt -e REGISTRY_HTTP_TLS_KEY=/certs/ssl.key -v /home/hpcm/docker/certs:/certs/ --name dockerhup registry:2
```

## 2.2 登录

### 2.2.1 crt证书配置

将hup主机上的`/home/hpcm/docker/certs/ssl.crt`复制到客户端的`/etc/docker/certs.d/192.168.50.132:5000`下, 并取名为`ca.crt`, 注意此目录是不存在的需要自己创建

```python
scp /home/hpcm/docker/certs/ssl.crt root@192.168.50.129:/etc/docker/certs.d/192.168.50.132:5000
```

### 2.2.2 登录

```python
root@ubuntu:/etc/docker/certs.d/192.168.50.132:5000# docker login 192.168.50.132:5000
Username: appgess
Password: 
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store
Login Succeeded
root@ubuntu:/etc/docker/certs.d/192.168.50.132:5000# 
```