# Crypto

本模块用于文本文件加密操作。

市面常见加密方式：

* 对称加密方式(对称加密)：AES DES ARC4

* 散列值计算(单向加密)：MD5 SHA HMAC

* 公钥加密和签名(非对称加密)：RSA DSA

对称加密: 加解密都使用同一套秘钥

非对称加密: 加密使用公钥, 解密使用秘钥

单向加密: 加密之后无法再次解密出来明文

# 安装

`pycrypto`为原模块名称, 作者不再维护, 所以可用新模块`pycryptodome`或者`crypto`安装任意一个即可

* pycrypto

  ```python
  pip install pycrypto
  wheel: http://www.voidspace.org.uk/python/pycrypto-2.6.1/
  ```

* pycryptodome

  ```Python
  pip install pycryptodome
  # 模块安装完成后, 如果导入失败, 则需要在模块`Python\Lib\site-packages`中找到`crypto`文件夹, 改为`Crypto`即可
  ```

