# 1. Ansible

## 1.1 参数说明

```bash
ansible [-i 主机清单] [-f 进程数量] [group] [-m 模块名] [-a 需要执行的命令]
```

* -i: 指定hosts配置文件
* -f: 指定启用进程个数
* -m: 指定使用的模块名称(command/shell)
* -a:需要执行的命令/脚本路径
* 

### 1.1.1 主机配置

操作文件: `/etc/ansible/hosts`

* ansible_ssh_port: 指定当前主机ssh端口
* ansible_ssh_user: 指定username
* ansible_ssh_pass: 指定password

示例配置如下

1. 单个配置

   增加信息

   ```bash
   10.0.0.10 ansible_ssh_port=22 ansible_ssh_user=appgess ansible_ssh_pass=appgess
   ```

   

2. 分组配置

   ```bash
   [appgess]
   10.0.0.10 ansible_ssh_port=22 ansible_ssh_user=appgess ansible_ssh_pass=appgess
   10.0.0.13 ansible_ssh_port=22 ansible_ssh_user=appgess ansible_ssh_pass=appgess
   ```

如果主机是第一次运行则需要修改配置

位置: `/etc/ansible/ansible.cfg`

```bash
host_key_checking = False
```

否则会出现错误

```bash
10.0.0.10 | FAILED! => {
    "msg": "Using a SSH password instead of a key is not possible because Host Key checking is enabled and sshpass does not support this.  Please add this host's fingerprint to your known_hosts file to manage this host."
}
```



示例运行

```bash
[root@localhost ansible]# ansible -i /etc/ansible/hosts all -m ping  # 全部执行 appgess表示只执行group appgess
10.0.0.10 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    }, 
    "changed": false, 
    "ping": "pong"
}
...
```



## 1.2 命令执行

### 1.2.1 command命令

不支持管道命令, 重定向.  此参数为缺省值, 没有指定-m默认使用的就是command

```bash
ansible -i /etc/ansible/hosts all -m command -a "df -Th"
ansible -i /etc/ansible/hosts all -m command -a "uname -r"
ansible -i /etc/ansible/hosts all -m commadn -a "uptime"
```

### 1.2.2 shell命令

支持shell中的全部指令与方法

```bash
ansible -i /etc/ansible/hosts all -m shell -a "df -Th"
ansible -i /etc/ansible/hosts all -m shell -a "uname -r >> /tmp/df.txt"
ansible -i /etc/ansible/hosts all -m shell -a "source ~/.bashrc && ll / >> /tmp/ll.txt"
```

### 1.2.3 scripts

执行本地的脚本文件

```bash
ansible -i /etc/ansible/hosts all -m scripts -a "/root/test.sh"
```

### 1.2.4 copy

文件上传与下载, 类似scp

```bash
ansible -i /etc/ansible/hosts all -m copy -a "src=/root/test.sh dest=/tmp/ owner=root group=root mode=0744 force=yes"
```

### 1.2.5 stat

文件权限查询

```bash
ansible -i /etc/ansible/hosts all -m stat -a "path=/tmp/hello"
```

### 1.2.6 get_url

联网下载资源, 类似wget/curl操作

```bash
ansible -i /etc/ansible/hosts all -m get_url -a "url=http://www.baidu.com/ dest=/tmp/ mode=0744 force=yes"
```

### 1.2.7 yum

安装命令, 支持状态(latest, present, installed前三个表示安装, removed, absent后两个表示拆卸)

```bash
ansible -i /etc/ansible/hosts all -m yum -a "name=python-pip state=installed"
```

### 1.2.8 cron

向crontab中追加定时任务.

```bash
ansible -i /etc/ansible/hosts all -m cron -a "name='命令命名' minute='*/60' job='echo 222'"
```

### 1.2.9 service

操作服务器, 例如nginx, httpd等, 被启用的服务必须支持`service xxx start/stop`

状态设置: started, stopped, restarted, reloaded.

```bash
ansible -i /etc/ansible/hosts all -m service -a "name=nginx state=restarted"
```

### 1.2.10 sysctl

配置主机系统中, /etc/systcl.conf中的项目

```bash
ansible -i /etc/ansible/hosts all -m sysctl -a "name=net.ipv4.ip_forward value=1 reload=yes"
```

### 1.2.11 user

用户管理

```bash
ansible -i /etc/ansible/hosts all -m user -a "name=appgess state=persent"
ansible -i /etc/ansible/hosts all -m shell -a "echo appgess | passwd appgess --stdin"
```



# 2. Ansible-Playbook

## 2.1 参数说明

```bash
ansible-playbook [选项] [参数]

-name: environment
  remote_user: root
  hosts: all
  roles:
   -prev
```



## 2.2 yml文件参数

```yaml
- name: 任务的描述信息
  shell(-m的参数): echo 111  # 此参数只可以定义一个, 否则后面的将会覆盖前面的
  remote_user: root # 连接主机使用的用户
  become: yes # 是否进行用户切换
  bacome_method: su # 切换的用户的方法, 支持su/sudo/pbrun等, 默认用sudo
  bacome_user: appgess  # 需要切换到的用户
  hosts: appgess  # 需要执行的hosts的group
  vars:
   username: nginx  # 当前task中的变量
  roles: # 需要执行的二级yml文件, 需要放置在此文件的目录
   - nginx  # yml位置为: ./nginx/tasks/main.yml
   - mysql
   - python
  tasks:
   - name: 模板配置
     file: template: src=template.j2 dest=/etc/foo.conf
  notify: 
    - restart nginx   # -m的参数执行成功后执行此操作(只会执行一次), 没有执行成功则不会执行, notify会调用handlers中对应的名字, 支持多个
    - restart mysqld
  handlers:
    - name: restart nginx
      service(-m的参数): name=nginx state=restarted
    - name: restart mysqld
      service(-m的参数): name=mysqld state=restarted
  
```

## 2.3 示例

### 2.3.1 安装nginx

1. 目录结构

   ```bash
   [root@localhost test]# tree
   .
   ├── nginx
   │   └── tasks
   │       └── main.yml
   ├── prev
   │   └── tasks
   │       └── main.yml
   ├── server
   │   └── tasks
   └── site.yml
   ```

2. 入口文件

   `./site.yml`

   ```bash
   - name: nginx安装
       remote_user: root
       hosts: appgess
       roles:
         - prev
         - nginx
         - server
   ```

3. nginx安装

   `nginx/tasks/main.yml`

   ```bash
   - name: nginx安装
     shell: yum install xxx
   ```

4. 运行ansible

   ```bash
   ansible-playbook -i /etc/ansible/hosts ./site.yml
   ```

   

# 3. Ansible-doc

## 3.1 参数说明



```bash
ansible-doc [-l] [-s service]
```





## 2.2 示例

