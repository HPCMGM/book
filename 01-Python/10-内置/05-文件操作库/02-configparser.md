# 1. configparser

本模块主要用于读取配置文件, 如常见的`ini`等

## 1.1 示例

* 配置文件

  ```python
  # test.cfg
  [test]
  a = 1
  b = 2
  c = %(a)s+%(b)s
  # 相当于Python中格式化占位符: "{}+{}".format(a, b)
  ```

* 读取

  ```python
  from configparser import ConfigParser
  
  conf = ConfigParser()
  
  conf.read("test.cfg")
  
  print(conf.get("test", "a"))
  # "1"
  print(conf.get("test", "b"))
  # "1+2"
  print(conf.get("test", "c"))
  # "a + b"
  print(conf.get("test", "d"))
  # "1+2"
  #获取配置文件所有的section ['logging', 'mysql']
  #获取指定section下所有option ['host', 'port', 'user', 'password']
  #获取指定section下所有的键值对 [('host', '127.0.0.1'), ('port', '3306'), ('user', 'root'), ('password', '123456')]
  #获取指定的section下的option <class 'str'> 127.0.0.1
  ```

  

