# 1. pip

Python拓展包管理工具, 默认是自带安装的. 如果没有安装, 则需要手动安装

## 1.1 pip源

由于国外的源下载数据比较慢, 所以在使用pip更新, 下载时最好使用国内源

|      源名称      | 地址                                      |
| :--------------: | ----------------------------------------- |
|      阿里源      | https://mirrors.aliyun.com/pypi/simple/   |
|   中国科技大学   | https://pypi.mirrors.ustc.edu.cn/simple/  |
|       豆瓣       | http://pypi.douban.com/simple/            |
|     清华大学     | https://pypi.tuna.tsinghua.edu.cn/simple/ |
| 中国科学技术大学 | http://pypi.mirrors.ustc.edu.cn/simple/   |

## 1.2 pip安装

pip依赖于`setuptools`, `wheel`, 所以需要安装三个包. 官方安装介绍: https://pip.pypa.io/en/stable/installing/

### 1.2.1 在线安装

* 下载`get_pip.py`

  ```python
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   # 此版本>=2.7
  curl https://bootstrap.pypa.io/2.6/get-pip.py  # 此版本<2.7
  ```

  

* 执行安装pip

  ```python
  python get_pip.py
  ```

* 安装依赖包

  ``````python
  pip install setuptools wheel -i https://mirrors.aliyun.com/pypi/simple/
  ``````

  

### 1.2.2 离线安装

如果需要在无法联网的环境来安装pip, 需要提前下载好需要安装的包

* 本地安装命令

  ```python
  python get-pip.py --no-index --find-links=/local/copies  # 从本地来查找需要安装的包
  ```

# 2. pip操作

## 2.1 安装

pip安装三方包可以选用不同的源, 如果官方包安装出错, 可以尝试使用轮子安装`*.whl`

https://www.lfd.uci.edu/~gohlke/pythonlibs/

| 序号 |      操作      | 命令                                                         |
| :--: | :------------: | ------------------------------------------------------------ |
|  1   |    在线安装    | `pip install -r requirements.txt`                            |
|  2   |      下载      | `pip download -d .\ -r ..\requirements.txt`                  |
|  3   |    离线安装    | `pip install --no-index --find-links=./ -r requirements.txt` |
|  4   | Python源码安装 | `python setup.py build && python setup.py install`           |



## 2.2 利用pip环境迁移

1. 打包依赖

   ```python
   pip freeze --all > requirements.txt
   ```

   

2. 查询机器支持的版本

   需要查看机器支持的类型, 要对应才能成功的做迁移

   ```python
   python -c "from pip._internal import pep425tags;print(pep425tags.get_supported())" # 64位查看可迁移的版本
   python -c "import pip;print(pip.pep425tags.get_supported())" # 32位查看可以迁移版本
   ```

   目标机器

   ```python
   [('cp35', 'cp35m', 'manylinux1_x86_64'), ('cp35', 'cp35m', 'linux_x86_64')....
   ```

   打包机器

   ```python
   [('cp35', 'cp35m', 'manylinux1_x86_64'), ('cp35', 'cp35m', 'linux_x86_64')....
   ```

   输出的三项为`(implementation, abi, platform)`, 如果打包机器为`cp27mu`, 就不能用于目标机器.否则会报错:

   ```python
   package.whl is not a supported wheel on this platform
   ```

   解决方法, 使用非二进制打包

   ```python
   pip download --no-binary=:all: package_name
   # --no-binary=:all: 对于包以及包的依赖包，都不使用二进制
   ```

   

3. 下载安装包

   ```python
   pip download --only-binary=:all: --platform=manylinux1_x86_64 --python-version 35 --implementation cp --abi cp35m -r requirements.txt -d ./packages/
   ```

   

4. 离线安装

   ```python
   pip install --no-index --find-links=./packages/ -r requirements.txt
   ```

   

# 3. pip安装包制作

```python
try:
    from pip.req import parse_requirements
except ImportError:
    from pip._internal.req import parse_requirements
from setuptools import find_packages, setup
with open("version.txt", "rb") as f:
    version = f.read().strip()
setup(
    name="module_name",
    version=version,
    description="This information will be invoked in the execution of help",
    packages=find_packages(exclude=[]),
    author="hpcm",
    author="hpcm@foxmail.com",
    license="Apache License V2",
    package_data={"": ["*.*"]},
    url="#",
    install_requires=[str(ir.req) for i in parse_requirements("requirements.txt", session=False),
                      zip_safe=False,
                      classifiers=[
                          "Programming Language :: Python",
                          "Operating System :: Microsoft :: Windows",
                          "Operating System :: Unix",
                          "Programming Language :: Python :: 2.7",
                          "Programming Language :: Python :: 3.4",
                          "Programming Language :: Python :: 3.5",
                          "Programming Language :: Python :: 3.6",
                          "Programming Language :: Python :: 3.7",
                      ]
)
```



# 4. 常见报错

## 4.1 升级异常

* 错误信息

  ```python
  ImportError: cannot import name main
  ```

* 解决方法

  原因为pip升级导致模块中函数变更引起, 需要修改正确

  `vim /usr/bin/pip3`

  ```python
  # sudo vim /usr/bin/pip3
  from pip import __main__
  if __name__ == '__main__':
      sys.exit(__main__._main())
  ```



## 4.2 编译环境异常

* 错误信息

  ```python
  unable to find vcvarsall.bat
  ```

  

* 解决方法

  编译时缺少部分依赖, 可以直接使用编译后的wheel, 需要版本对应

  ```python
  https://www.lfd.uci.edu/~gohlke/pythonlibs/
  ```

  




