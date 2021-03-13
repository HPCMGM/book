# 1. 格式

## 1.1 压缩

### 1.1.1 格式获取

```python
def get_archive_formats()
```

返回值: list



**示例一**

* 代码

  ```python
  import shutil
  
  print(shutil.get_archive_formats())
  ```

* 结果

  ```bash
  [('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"), ('tar', 'uncompressed tar file'), ('xztar', "xz'ed tar-file"), ('zip', 'ZIP file')]
  ```



### 1.1.2 自定义格式

```python
def register_archive_format(name, function, extra_args=None, description='')
```

返回值: None

* name: `str`, 自定义的压缩格式
* function: `function`, 压缩函数
* extra_args: `[(key, value)]`, 函数调用时需要提供的参数, 默认会使用`make_archive`的全部参数
* description: 对该压缩格式的描述信息



### 1.1.3 删除格式

```python
def unregister_archive_format(name)
```

返回值: None

* name: `str`, 需要删除的压缩格式



## 1.2 解压

### 1.2.1 格式获取

```python
def get_unpack_formats()
```

返回值: list



**示例一**

* 代码

  ```python
  import shutil
  
  print(shutil.get_unpack_formats())
  ```

* 结果

  ```bash
  [('bztar', ['.tar.bz2', '.tbz2'], "bzip2'ed tar-file"), ('gztar', ['.tar.gz', '.tgz'], "gzip'ed tar-file"), ('tar', ['.tar'], 'uncompressed tar file'), ('xztar', ['.tar.xz', '.txz'], "xz'ed tar-file"), ('zip', ['.zip'], 'ZIP file')]
  ```

  

### 1.2.2 自定义格式

```python
def register_unpack_format(name, extensions, function, extra_args=None, description='')
```

返回值: None

* name: `str`, 自定义的解压格式
* extensions: `list`, 支持的解压文件的后缀列表, 例如: `[".zip", ".bz2"]`
* function: `function`, 自定义解压的函数
* extra_args: `[(key, value)]`, 自定义函数需要的参数
* description: `str`, 函数的描述信息

### 1.2.3 删除格式

```python
def unregister_unpack_format(name)
```

返回值: None

* name: 需要删除的格式



# 2. 压解文件

使用此功能需要Python条件: 

* Python >= 3.2
* 安装依赖包: `zlib`(zip压缩),`tar`(gz压缩), `bz2`(bz2压缩)
* xz压缩要求:  安装`lzma`模块, 且Python >= 3.5

## 2.2 压缩

```python
def make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0, dry_run=0, owner=None, group=None, logger=None)
```

返回值: None

* base_name: `str/path`,  压缩文件名(无需设置后缀, 后缀会自动添加)
* format: `str`, 压缩格式, 目前支持: `zip`, `tar`, `gztar`, `bztar`, `xztar`
* root_dir: `str/path`,  需要压缩的目录. 真正压缩路径由root_dir + base_dir控制
* base_dir: `str/path`, 压缩生成的文件路径, 相对路径.
* verbose: 参数已废弃
* dry_run: `bool`,  True表示, 只打印日志, 不创建压缩文件
* owner: `str`, 使用哪个拥有者创建压缩文件, 默认当前
* group: `str`, 使用哪个归属组创建压缩文件, 默认当前
* logger: `logger对象`



**示例一**

* 代码

  ```python
  import shutil
  import logging.config
  
  config_logging = {
      # 此处为logger的配置, 由于比较多, 已经省略
  }
  
  logging.config.dictConfig(config_logging)
  
  logger = logging.getLogger("info")
  
  base_name = r"E:\project\code\test\t_shutil\compress\test"  # 生成文件名称
  format_type = "gztar"  # 压缩格式
  root_dir = r"E:\project\code\test\t_check_time"  # 需要压缩的目录
  base_dir = r"apps\common"  # 压缩生成的文件路径, 相对路径.
  verbose = True  # 此参数已废弃, 为了向下兼容, 还是需要保留的.
  dry_run = False  # True表示, 只打印日志, 不创建压缩文件
  owner = "appgess"  # 创建者, 经过测试好像没有卵用
  group = "appgess"  # 归属组, 经过测试好像没有卵用
  logger = logger  # 日志记录
  
  shutil.make_archive(base_name, format_type, root_dir, base_dir, verbose, dry_run, owner, group, logger)
  ```

* 压缩结果

  ```bash
  (test) [appgess@localhost t_shutil]$ ll /home/appgess/test.tar.gz   # 权限查看
  -rw-rw-r--. 1 appgess appgess 5510 Aug  7 10:31 /home/appgess/test.tar.gz
  (test) [appgess@localhost t_shutil]$ python -m tarfile -l /home/appgess/test.tar.gz  # 归档目录查看 
  apps/common/ 
  apps/common/login_ssh_do.py 
  apps/common/pycrypt.py 
  apps/common/sender.py 
  apps/common/tasks_status_redis.py 
  apps/common/__pycache__/ 
  apps/common/__pycache__/pycrypt.cpython-37.pyc 
  (test) [appgess@localhost t_shutil]$ 
  ```

  

## 2.2 解压

```python
def unpack_archive(filename, extract_dir=None, format=None)
```

* filename: `str/path`, 需要解压的文件
* extract_dir: `str/path`, 需要解压的位置
* format: `str`, 解压使用的格式, 目前支持: `zip`, `tar`, `gztar`, `bztar`, `xztar`



**示例一**

* 代码

  ```python
  import shutil
  
  filename = "/home/appgess/test.tar.gz"  # 需要解压的文件
  extract_dir = "/home/appgess/a"  # 解压的路径
  format_type = "gztar"  # 解压的格式
  
  shutil.unpack_archive(filename, extract_dir, format_type)
  ```

* 解压结果

  ```python
  (test) [appgess@localhost t_shutil]$ tree /home/appgess/a
  /home/appgess/a
  └── apps
      └── common
          ├── login_ssh_do.py
          ├── __pycache__
          │   └── pycrypt.cpython-37.pyc
          ├── pycrypt.py
          ├── sender.py
          └── tasks_status_redis.py
  
  3 directories, 5 files
  (test) [appgess@localhost t_shutil]$
  ```


