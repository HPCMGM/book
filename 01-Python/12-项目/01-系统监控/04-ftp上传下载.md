```python
# -*- coding:utf-8 -*-
# author: HPCM
# time: 2020/2/24 16:19
# file: pyftp.py
"""
本模块用于ftp的上传下载, 新增功能如下:
1. 选择性过滤掉部分文件
2. 断线重连, 续传
3. 可以同时上传下载文件夹

黑名单过滤为正则整行匹配:
    名称 规则 是否匹配
    abc abc 是
    abc ab 否
    abc ab.* 是
"""
import re
import os
import time
import ftplib
import logging

logger = logging.getLogger("info")


class Ftp(object):
    """ftp控制器"""

    def __init__(self, host, username, password, port=21, remote_encoding="utf-8", local_encoding="gbk"):
        self.fp = None
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.remote_encoding = remote_encoding
        self.local_encoding = local_encoding
        self.remote_sep = None
        self.local_sep = None
        self.timeout = 10
        self.login()

    def login(self):
        """ftp登录"""
        self.fp = ftplib.FTP()
        self.fp.connect(host=self.host, port=self.port)
        self.fp.encoding = self.remote_encoding
        print(self.fp.login(user=self.username, passwd=self.password))
        self.fp.set_pasv(False) # 设置主动模式
        self.select_sep()

    def select_sep(self):
        """切换sep"""
        if self.fp.encoding == "utf-8":
            self.remote_sep = "/"
        else:
            self.remote_sep = "\\"
        if self.local_encoding == "utf-8":
            self.local_sep = "/"
        else:
            self.local_sep = "\\"

    def walk_download_file(self, remote, local, blacks=None):
        """下载文件"""
        try:
            try:
                self.fp.cwd(remote)
                if not os.path.exists(local):
                    os.mkdir(local)
                for path in self.fp.nlst(remote):
                    is_continue = False
                    for _ in filter(lambda x: re.match(x + "$", path), blacks):
                        is_continue = True
                        break
                    if is_continue is True:
                        continue
                    if self.remote_sep in path:
                        path = path.split(self.remote_sep).pop()
                    r_path = remote + self.remote_sep + path
                    l_path = local + self.local_sep + path
                    self.walk_download_file(r_path, l_path, blacks)
            except ftplib.error_perm:
                for _ in filter(lambda x: re.match(x + "$", local), blacks):
                    return
                print("[DOWN] <=== {}".format(remote))
                with open(local, "wb") as f:
                    self.fp.retrbinary("RETR {}".format(remote), f.write)
        except (TimeoutError, ConnectionResetError):
            logger.warning("ftp timeout now, try connect!")
            self.close()
            time.sleep(self.timeout)
            self.login()
            self.walk_download_file(remote, local, blacks)

    def walk_upload_file(self, local, remote, blacks=None):
        """上传文件"""
        try:
            if os.path.isdir(local):
                try:
                    self.fp.mkd(remote)
                except ftplib.error_perm:
                    pass
                for path in os.listdir(local):
                    is_continue = False
                    for _ in filter(lambda x: re.match(x + "$", path), blacks):
                        is_continue = True
                        break
                    if is_continue is True:
                        continue
                    l_path = local + self.local_sep + path
                    r_path = remote + self.remote_sep + path
                    self.walk_upload_file(l_path, r_path, blacks)
            else:
                for _ in filter(lambda x: re.match(x + "$", local), blacks):
                    return
                print("[LOAD] ===> {}".format(local))
                with open(local, "rb") as f:
                    self.fp.storbinary("STOR {}".format(remote), f)
        except (TimeoutError, ConnectionResetError):
            self.close()
            logger.warning("ftp timeout now, try connect!")
            time.sleep(self.timeout)
            self.login()
            self.walk_upload_file(local, remote, blacks)

    def download(self, remote, local, blacks=None):
        """下载, 支持文件和文件夹同时进行, 支持断线重连"""
        local = local + self.local_sep + remote.split(self.remote_sep).pop()
        if not os.path.exists(local):
            os.makedirs(local)
        self.walk_download_file(remote, local, blacks or [])

    def upload(self, local, remote, blacks=None):
        """上传, 支持文件和文件夹同时进行, 支持断线重连"""
        if os.path.isdir(local):
            remote = remote + self.remote_sep + local.split(self.local_sep).pop()
        self.walk_upload_file(local, remote, blacks or [])

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()

    def close(self):
        """关闭并清理相关信息"""
        try:
            self.fp.close()
            del self.fp
        except Exception as e:
            logger.exception(e)
            logger.error("ftp close error!")
            pass


if __name__ == "__main__":
    with Ftp("19.19.19.13", "Administrator", "dong4911?", 21) as fp:
        # fp.upload(r"E:\project\test\t_snmp", "/Users/hpcm/Desktop/install", [])
        fp.download(r"/Users/hpcm/Desktop/install", ".", [])

```

