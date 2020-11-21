# 1. paramiko

## 1.1 ssh

```python
impor paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, user, password)
stdin, stdout, stderr = ssh.exec_command("ls ~") # 发送终端指令 获取文件描述符
stdout.read() 使用read读取
ssh.close()
```

# 5. 异常错误

## 5.1 版本问题

* 错误信息

  ```python
  from cryptography.hazmat.bindings._openssl import ffi, lib
  ImportError: DLL load failed: 找不到指定的程序。
  ```

* 解决方案

  1. 降版本, paramiko的paramiko-1.17.4-py2.py3-none-any.whl 
  2. 加密库: pycrypto, wheel网站为:http://www.voidspace.org.uk/python/pycrypto-2.6.1/ 
     先安装加密库, 再安装paramiko轮子即可

## 5.2 编码异常

* 错误信息

  ```python
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.5/site-packages/paramiko-2.1.1-py3.5.egg/paramiko/file.py", line 327, in readlines
  File "/usr/local/lib/python3.5/site-packages/paramiko-2.1.1-py3.5.egg/paramiko/file.py", line 312, in readline
  File "/usr/local/lib/python3.5/site-packages/paramiko-2.1.1-py3.5.egg/paramiko/py3compat.py", line 148, in u
  UnicodeDecodeError: 'utf-8' codec can't decode byte 0xca in position 35: invalid continuation byte
  ```

* 解决方案

  本异常是由于, 目标机与当前机器的编码格式不一样导致编码异常.解决方案

  强制兼容`utf-8`与`gbk`两种编码方式 
  修改源码`paramiko/py3compat.py`文件中的`u`函数和`b`函数如下:

  ```python
  import threading
  encoding = {}
      def b(s):
          """cast unicode or bytes to bytes"""
          if isinstance(s, bytes):
              return s
          elif isinstance(s, str):
              return s.encode(encoding.get(threading.currentThread().ident, "utf8"))
          else:
              raise TypeError("Expected unicode or bytes, got {!r}".format(s))
  
      def u(s):
          """cast bytes or unicode to unicode"""
          if isinstance(s, bytes):
              coding = encoding.get(threading.currentThread().ident, None)
              if coding == "gbk":
                  r = s.decode(coding)
              else:
                  try:
                      r = s.decode("gbk")
                      encoding[threading.currentThread().ident] = "gbk"
                  except UnicodeDecodeError:
                      r = s.decode("utf8")
                      encoding[threading.currentThread().ident] = "utf8"
              return r
          elif isinstance(s, str):
              return s
          else:
              raise TypeError("Expected unicode or bytes, got {!r}".format(s))
  
  ```

  