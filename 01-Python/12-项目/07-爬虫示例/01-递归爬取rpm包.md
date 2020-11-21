递归爬取rpm依赖包, 防止下载rpm依赖问题

```python
#!/usr/bin/env python
# encoding: utf-8
# author: HPCM
# time: 19-5-1 上午12:56
# file: rpm_splder.py
import os
import time
from queue import Queue
from hashlib import sha1

import requests
from lxml import etree
import gevent
from gevent.monkey import patch_all

patch_all()


down_libs = "lzma-libs pyliblzma xz-devel"


class DownloadLibs(object):
    """依赖下载"""

    def __init__(self, libs):
        self.libs = libs
        self.base_url = "https://pkgs.org/download/"
        self.fingerprint = set()
        self.status = 0
        self.queue = Queue(100)

    def send_request(self, url_depth_name):
        """获取lib"""
        url, *depth_name = url_depth_name
        s = sha1()
        s.update(url.encode())
        fp = s.hexdigest()
        if fp in self.fingerprint:
            return
        self.status += 1
        print("[REQUEST] ===> {}".format(url))
        res = requests.get(url, verify=False)
        self.fingerprint.add(fp)
        self.scheduler(res, url_depth_name)

    def scheduler(self, res, url_depth_name):
        url, depth, name = url_depth_name
        obj = etree.HTML(res.content)
        try:
            if url.endswith(".html"):
                return self.parse_second_page(obj, (depth, name))
            elif any(filter(lambda x: url.endswith(x), [".rpm", ".zip", ".gz", ".tar", ".xz"])):
                return self.download_lib(res.content, (name, url))
            else:
                return self.parse_first_page(obj, (depth, name))
        finally:
            self.status -= 1

    def parse_first_page(self, obj, depth_name):
        """解析一级页面"""
        [self.queue.put((url, *depth_name)) or print("[FIRST] <==={}".format(url)) for url in
         obj.xpath("//div[@class=\"card-header collapsed distro-centos\"]/..//a/@href") if
         url.startswith("https://centos.pkgs.org/6/centos-x86_64/") and url.endswith("x86_64.rpm.html")]

    def parse_second_page(self, obj, depth_name):
        """解析二级页面"""
        if depth_name[0] is True:
            [self.queue.put((url, False, depth_name[1])) or print("[SECOND] <==={}".format(url)) for url in
             obj.xpath("//table[@class=\"table table-bordered-2 table-hover table-sm1 table-striped\"][3]//td/a/@href") if not url.endswith("(64bit)")]
        self.queue.put(
            (obj.xpath("//table[@class=\"table table-bordered-2 table-hover table-sm1\"]//tr[2]/td/a/@href")[0], False,
            depth_name[1]))

    def download_lib(self, res, path_url):
        """"""
        path, url = path_url
        name = url.split("/")[-1]
        current_path = os.path.join(os.getcwd(), path)
        if not os.path.exists(current_path):
            os.system("mkdir {}".format(current_path))
        with open("{}/{}".format(path, name), "wb") as f:
            f.write(res)
        print("[DOWNLOAD] <==== {}".format(name))

    def first_request(self):
        """爬虫入口"""
        [self.queue.put((self.base_url + path, True, path)) or print("[FIRST] <==={}".format(path)) for path in
         self.libs.split()]

    def loop_request(self):
        """无限请求"""
        t_list = []
        while True:
            if not self.queue.empty():
                t = gevent.spawn(self.send_request, self.queue.get())
                t.start()
                t_list.append(t)
            else:
                time.sleep(5)
                if self.status == 0 and self.queue.empty():
                    break
        [t.join() for t in t_list]

    def start(self):
        """启动器"""
        [os.system("rm -rf {}".format(path)) for path in os.listdir(os.getcwd()) if os.path.isdir(path)]
        self.first_request()
        self.loop_request()


if __name__ == "__main__":
    dl = DownloadLibs(down_libs)
    dl.start()
```

