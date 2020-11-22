# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2018/12/7 13:50
from binascii import b2a_hex, a2b_hex

try:
    from Crypto.Cipher import AES
except ImportError:
    from Cryptodome.Cipher import AES


class Encryption(object):
    """AES对称加密"""

    def __init__(self, key, mode=None):
        # 将秘钥补齐16位
        self.key = self.parse_content(key[:16] if key and len(key) > 15 else key.ljust(16))
        self.mode = mode or AES.MODE_CBC
        self.aes = None

    def encrypt(self, content):
        """加密"""
        # 注意由于aes加密后会出现一些无法编码的字符, 所以使用b2a_hex转化为16进制, 或者使用base64进行编码
        self.aes = AES.new(self.key, self.mode, self.key)
        return b2a_hex(self.aes.encrypt(self.parse_content(content))).decode()

    def decrypt(self, content):
        """解密"""
        self.aes = AES.new(self.key, self.mode, self.key)
        return self.aes.decrypt(a2b_hex(content)).decode().strip()

    @staticmethod
    def parse_content(content):
        n = len(content) // 16 + 1 if len(content) % 16 else 0
        return content.ljust(16 * n).encode()
        

# -*- coding:utf-8 -*-
# author:HPCM
# datetime:2019/12/23 14:46
import time
import random
import base64

try:
    from Crypto.Cipher import AES
except ImportError:
    from Cryptodome.Cipher import AES


class Encryption(object):
    """AES对称加密"""

    def __init__(self, key=None, mode=None):
        # 将秘钥补齐16位
        self.key = self.split_16(key or "aaaaaaaaaaaaa").encode()
        self.mode = mode or AES.MODE_CBC
        self.aes = None

    def encrypt(self, content):
        """
        加密
        :param content: 需要加密的数据
        :return: 加密后的数据
        """
        # 注意由于aes加密后会出现一些无法编码的字符, 使用base64进行编码后在保存
        s = str(random.uniform(0, 1))[:3]
        e = str(int(time.time()))[-5:]
        self.aes = AES.new(self.key, self.mode, self.key)
        return base64.b64encode(self.aes.encrypt(self.add_16(s + "#" + content + "#" + e).encode())).decode()

    def decrypt(self, encrypt_content):
        """
        解密
        :param encrypt_content:加密的信息
        :return: 解密后数据
        """
        self.aes = AES.new(self.key, self.mode, self.key)
        content = self.aes.decrypt(base64.b64decode(encrypt_content)).decode().strip()
        return content[content.index("#")+1:content.rindex("#")]

    @staticmethod
    def split_16(content):
        """
        切割到长度为16位
        :param content: 需要截取或补充的str
        :return: 16位长度的字符串
        """
        return content[:16] if content and len(content) > 15 else content.ljust(16)

    @staticmethod
    def add_16(content):
        """
        将传入的参数增加到16的倍数
        :param content: 需要操作的str
        :return: 能被16整除的str
        """
        d, n = divmod(len(content), 16)
        return content.ljust(16 * (d + (n and 1)))


crypt = Encryption()

if __name__ == "__main__":
    crypt = Encryption()
    txt = crypt.encrypt("appgess")
    print(txt)
    print(crypt.decrypt(txt))


if __name__ == "__main__":
    crypt = Encryption("secret_key")
    txt = crypt.encrypt("aaaaaaaaaaaaaaaaaa")
    print(txt)
    print(crypt.decrypt(txt))
