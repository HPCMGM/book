# 1. pycrypto

本模块用于对称性加密策略

## 1.1 安装

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

# 2. 字符加密

## 2.1 < DES

DES加密, 主要为固定加密密码块为8字节.DES对称性加密算法加密, 创建DES加密对象 

```python
def Crypto.Cipher.DES.new(key, mode, IV=8, nonce=None, segment_size=8, mac_len=None, initial_value=0, *args, **kwargs):
return Cipher
```

- key: bytes/bytearray/memoryview, 加密秘钥, 8字节
- mode: 加密算法的模式, 有MODE_(ECB, CBC, CFB, OFB, CTR, OPENPGP, EAX)
- IV: bytes, 加密初始化常量, 8字节
- nonce: bytes, 随机字符串
- segment_size: int, 分组时每组的大小
- mac_len: int, 身份表示的长度, 不能超过8
- initial_value: 计数器(Counter)

**示例**

```python
import base64
from Crypto.Cipher import DES

key = '-8B key-'
cipher = DES.new(key.encode(), DES.MODE_ECB)

# 加密
plaintext = 'sona si latine loqueris '
en_bytes = cipher.encrypt(plaintext.encode())
print(base64.b64encode(en_bytes).decode())
# 解密
en_bytes = base64.b64decode('cRmk7obU8qFH26ywMDvHC24YwioyLNsH'.encode())
print(cipher.decrypt(en_bytes).encode())
```

输出

```python
cRmk7obU8qFH26ywMDvHC24YwioyLNsH
sona si latine loqueris
```

### 2.1.1 加解密

#### > encrypt

加密.

```python
def encrypt(self, plaintext, output=None):
return bytes
```

* plaintext: `bytes`, 需要进行加密的二进制字符串
* output: `bytesarray/memoryview`, 需要保存的位置

**示例**

```python
import base64
from Cryptodome.Cipher import DES

key = '-8B key-'
cipher = DES.new(key.encode(), DES.MODE_ECB)

# 加密
a = bytearray(24)
b = bytearray(24)
plaintext = 'sona si latine loqueris '
with open("test.txt", "wb+") as f:
    en_bytes = cipher.encrypt(plaintext.encode(), a)
    print(a)
    b_bytes = cipher.encrypt(plaintext.encode())
    print(b_bytes)
    # base64.b64decode('cRmk7obU8qFH26ywMDvHC24YwioyLNsH'.encode())
    de_bytes = cipher.decrypt(b_bytes)
    print(de_bytes)
    de_bytes = cipher.decrypt(b_bytes, b)
    print(de_bytes)
    print(b)
```

输出

```python
bytearray(b'q\x19\xa4\xee\x86\xd4\xf2\xa1G\xdb\xac\xb00;\xc7\x0bn\x18\xc2*2,\xdb\x07')
b'q\x19\xa4\xee\x86\xd4\xf2\xa1G\xdb\xac\xb00;\xc7\x0bn\x18\xc2*2,\xdb\x07'
b'sona si latine loqueris '
None
bytearray(b'sona si latine loqueris ')
```

#### > decrypt

解密.

```python
def decrypt(self, ciphertext, output=None):
return bytes
```

* ciphertext: `bytes`, 需要进行解密的二进制字符串
* output: `bytesarray/memoryview`, 需要保存的位置

### 2.1.2 加密方式

#### - MODE_ECB

可使用参数

* key: `bytes/bytearray/memoryview`, 加密秘钥, 必须为8位

* mode: 加密算法的模式, `MODE_ECB`

加密数据

* 长度应该是8字节的倍数

**示例**

```python
import base64
from Crypto.Cipher import DES

key = '-8B key-'
cipher = DES.new(key.encode(), DES.MODE_ECB)

# 加密
plaintext = 'sona si latine loqueris '
en_bytes = cipher.encrypt(plaintext.encode())
print(base64.b64encode(en_bytes).decode())
# 解密
en_bytes = base64.b64decode('cRmk7obU8qFH26ywMDvHC24YwioyLNsH'.encode())
print(cipher.decrypt(en_bytes).encode())
```

输出

```python
cRmk7obU8qFH26ywMDvHC24YwioyLNsH
sona si latine loqueris
```

#### - MODE_CBC

可使用参数

* key: `bytes/bytearray/memoryview`, 加密秘钥, 必须为8位
* mode: 加密算法的模式, MODE_CBC
* iv: 初始化向量, 必须为8位

加密数据
* 长度应该是8字节的倍数

**示例**

```python
import base64
from Crypto.Cipher import DES

key = '-8B key-'
cipher = DES.new(key.encode(), DES.MODE_CBC)
plaintext = 'sona si latine loqueris '
en_bytes = cipher.encrypt(plaintext.encode())
iv_bytes = cipher.iv
en_str = base64.b64encode(en_bytes).decode()
b64_iv = base64.b64encode(iv_bytes).decode()
print("加密后:", en_str)
print("初始化异或字符串: ", b64_iv)

en_bytes = base64.b64decode(en_str.encode())
iv = base64.b64decode(b64_iv.encode())
cipher = DES.new(key.encode(), DES.MODE_CBC, iv=iv)
de_str = cipher.decrypt(en_bytes).decode()
print("解密后: ", de_str)
```

输出

```python
加密后: cH5KDlHiBOQjL8ritbNjyymzg6dTPXLT
初始化异或字符串: SY5AWI516eI=
解密后: sona si latine loqueris 
```

#### - MODE_CFB

- 可使用参数
  - key: `bytes/bytearray/memoryview`, 加密秘钥, 必须为8位
  - mode: 加密算法的模式, MODE_CFB
  - iv: 初始化向量, 必须为8位
  - segment_size: 分割明文与密文的位数, 默认8位=1字节, 必须为8的倍数
- 加密数据
  - 长度无限制

**示例**

```python
import base64
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)
cipher =DES.new(key,DES.MODE_CFB, iv=key, segment_size=16)
plaintext = 'sona si latine loqueris '
en_bytes = cipher.encrypt(plaintext.encode())
iv_bytes = cipher.iv
en_str = base64.b64encode(en_bytes).decode()
b64_iv = base64.b64encode(iv_bytes).decode()
print("加密后:", en_str)
print("初始化异或字符串: ", b64_iv)

en_bytes = base64.b64decode(en_str.encode())
iv = base64.b64decode(b64_iv.encode())
cipher =DES.new(key, DES.MODE_CFB, iv=iv, segment_size=16)
de_str = cipher.decrypt(en_bytes).decode()
print("解密后: ", de_str)
```

输出

```python
加密后: HlkZVL69cDwHK4NvwMi7pdkxlQzpnoOq
初始化异或字符串: ZJ2nLn39kd0=
解密后: sona si latine loqueris 
```

#### - MODE_OFB

- 可使用参数
  - key: `bytes/bytearray/memoryview`, 加密秘钥, 必须为8位
  - mode: 加密算法的模式, MODE_OFB
  - iv: 初始化向量, 必须为8位
- 加密数据
  - 长度无限制

**示例**

```python
import base64
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_OFB, iv=key)
plaintext = 'sona si latine loqueris '
en_bytes = cipher.encrypt(plaintext.encode())
iv_bytes = cipher.iv
en_str = base64.b64encode(en_bytes).decode()
b64_iv = base64.b64encode(iv_bytes).decode()
print("加密后:", en_str)
print("初始化异或字符串: ", b64_iv)

en_bytes = base64.b64decode(en_str.encode())
iv = base64.b64decode(b64_iv.encode())
cipher = DES.new(key, DES.MODE_OFB, iv=iv)
de_str = cipher.decrypt(en_bytes).decode()
print("解密后: ", de_str)
```

输出

```python
加密后: MsbxVYSVmBos206Blu6lA1aCY1iy9xMu
初始化异或字符串: 4TlvNnfS5kQ=
解密后: sona si latine loqueris 
```

#### - MODE_CTR

- 可使用参数
  - key: `bytes/bytearray/memoryview`, 加密秘钥, 必须为8位
  - mode: 加密算法的模式, MODE_CTR
  - nonce: `bytes`, 固定随机数的值, 长度为0~块大小-1(7), 与参数`counter`互斥
  - initial_value: `int`, 计数器的初始值, 与参数`counter`互斥
  - counter: 自定义计数器对象`Crypto.Util.Counter.new()`, 与参数`nonce/initial_value`互斥
- 加密数据
  - 长度无限制

**示例**

```python
import base64
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)
nonce = get_random_bytes(7)
cipher = DES.new(key, DES.MODE_CTR, nonce=nonce, initial_value=20)
plaintext = 'sona si latine loqueris '
en_bytes = cipher.encrypt(plaintext.encode())
en_str = base64.b64encode(en_bytes).decode()
print("加密后:", en_str)


en_bytes = base64.b64decode(en_str.encode())
cipher = DES.new(key, DES.MODE_CTR, nonce=nonce, initial_value=20)
de_str = cipher.decrypt(en_bytes).decode()
print("解密后: ", de_str)
```

输出

```python
加密后: NOUj8/LXzaHy3VB0kD3IOJue+Gp0NXu/
解密后: sona si latine loqueris 
```

#### - MODE_OPENPGP

- 可使用参数
  - key: `bytes/bytearray/memoryview`, 加密秘钥, 必须为8位
  - mode: 加密算法的模式, MODE_OPENPGP
  - iv: 初始化向量, 必须为8位
- 加密数据
  - 长度无限制

**示例**

```python
import base64
from Crypto.Cipher import DES

key = b"\xedy,\xbb\xc0\xd1A\x17"
cipher = DES.new(key, DES.MODE_OPENPGP, iv=key)
plaintext = 'sona si latine loqueris '
en_bytes = cipher.encrypt(plaintext.encode())
IV = cipher.IV
en_str = base64.b64encode(en_bytes).decode()
print("加密后:", en_str)


en_bytes = base64.b64decode(en_str.encode())
cipher = DES.new(key, DES.MODE_OPENPGP, iv=IV)
de_str = cipher.decrypt(en_bytes[2:])[8:]
print("解密后: ", de_str.decode())
```

输出

```python
加密后: f+3baaFhuc9L1eYHUBQPfumbzAyA3nf7XPRVnR9zLLsvHQ==
解密后: sona si latine loqueris 
```

#### - MODE_EAX

- 可使用参数
  - key: `bytes/bytearray/memoryview`,  加密秘钥, 必须为8位
  - mode: 加密算法的模式, MODE_EAX
  - nonce: `bytes`, 随机字符串
  - mac_len: `int`, MAC标签的期望长度, 默认8
- 加密数据
  - 长度无限制

**示例**

```python
import base64
from Crypto.Cipher import DES

key = b"\xedy,\xbb\xc0\xd1A\x17"
nonce = b"abcdef"
cipher = DES.new(key, DES.MODE_EAX, nonce=nonce, mac_len=DES.block_size)
plaintext = 'sona si latine loqueris'
en_bytes = cipher.encrypt(plaintext.encode())
en_str = base64.b64encode(en_bytes).decode()
print("加密后:", en_str)

en_bytes = base64.b64decode(en_str.encode())
cipher = DES.new(key, DES.MODE_EAX, nonce=nonce, mac_len=DES.block_size)
de_str = cipher.decrypt(en_bytes)
print("解密后: ", de_str.decode())
```

输出

```python
加密后: QHJFCtqN0ioTaQRoLGxoQG3OSbPuG8A=
解密后: sona si latine loqueris
```

## 2.2 < AES

### 2.2.2 加密方式



# 2. 文本加密

## 2.1 RSA

### 2.1.1 秘钥生成



### 2.1.2 加解密





