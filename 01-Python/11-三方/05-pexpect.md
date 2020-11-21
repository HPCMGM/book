# 1. pexpect

向cmd一样运行命令. 本模块只适用于linux, window虽然有pexpect-win可以安装使用, 但是存在很多bug

## 1.1 安装

```python
pip install pexpect
```

#### > run

直接运行, 用后销毁命令窗口

```python
import pexpect

result, status_code = pexpect.run(cmd, withexitstatus=1)
print(result.decode())  # 运行结果
print(status_code)      # 运行状态码, 0表示成功
```

#### > spawn

向命令行一样执行任务.

```python
ssh = pexpect.spawn("ssh {}@{}".format("hpcm", "localhost"))
i = ssh.expect("password", timeout=20)  # 正则匹配, $表示符号
if i == 0:
    ssh.sendline("password")              # 输入密码
    if ssh.expect(["#", "$"]) in [0, 1]:
        print("登陆成功!")

发送指令:
# send               会加一个\n
# sendline           不会加\n
# sendcontrol(char)  发送控制符
```

**管道失败执行**

```python
child = pexpect.spawn("ps aux | grep nginx")
i = child.expect([pexpect.EOF], timeout=10)
print(child.before.decode())

# **************************************************
error: garbage option

Usage:
 ps [options]

 Try 'ps --help <simple|list|output|threads|misc|all>'
  or 'ps --help <s|l|o|t|m|a>'
 for additional help text.

For more details see ps(1).
```

**正确示例**

```python
child = pexpect.spawn("/bin/sh -c 'ps aux | grep nginx | grep -v grep'")
i = child.expect([pexpect.EOF], timeout=10)
print(child.before.decode())


# **************************************************
root       1415  0.0  0.0 125080  1476 ?        Ss   08:40   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
root       1417  0.0  0.0 125444  3020 ?        S    08:40   0:00 nginx: worker process
root       1419  0.0  0.0 125444  3020 ?        S    08:40   0:02 nginx: worker process
root       1420  0.0  0.0 125444  3020 ?        S    08:40   0:03 nginx: worker process
root       1422  0.0  0.0 125444  3020 ?        S    08:40   0:02 nginx: worker process
```

#### > interact

直接以命令交互模式执行

```python
ssh = pexpect.spawn("ssh {}@{}".format("hpcm", "localhost"))
i = ssh.expect(["password", "continue connecting (yes/no)?"], timeout=20)
if i == 0:
    ssh.sendline("password")
    if ssh.expect(["#", "$"]) in [0, 1]:
        print("登陆成功!")
        ssh.interact()  # 获取命令窗口
```

#### - logfile

日志接管

```python
logfile = open("run.log", "wb")
ssh = pexpect.spawn("ssh {}@{}".format("hpcm", "localhost"))
try:
    ssh.logfile = log_file  # 该日志只记录运行结果, ssh.before中的数据
finanlly:
    logfile.close()
```





