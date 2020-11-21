# 加密

数据加密主要分为以下几种类型:

* 对称性加密(Symmetric Key Encryption): 

  加密和解密使用的秘钥是同一个, 常见加密类型有:

  ```bash
  DES、3DES、DESX、IDEA、TDEA、RC2、RC4、RC5、RC6、AES、Blowfish
  ```

* 非对称加密(Asymmetric Key Encryption): 

  使用公钥加密, 使用私钥解密, 常见加密类型有:

  ```bash
  RSA、ECC（移动设备用）、Diffie-Hellman、El Gamal、DSA（数字签名用）
  ```

* 不可逆算法: 

  通过算法运算得到的加密数据, 不可进行反向解开.

  

# Base64编码

* 作用:

  在网络传递数据时, 可能由于双方的平台编码格式不一致, 导致数据在专递时出现乱码.