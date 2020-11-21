```python
# coding=utf-8
import os
import re

import requests
from lxml import etree


def get_dev(lib):
    """获取依赖项"""
    temp = os.path.join(os.getcwd(), "temp.lib")
    i = os.system("pip install {} > {}".format(lib, temp))
    if i == 0:
        with open(temp, "r") as f:
            content = f.read()
            print(content)
        os.remove(temp)
        res = re.findall(r"Installing collected packages: (.*)\n", content, re.S)
        if res:
            return res[0].split(", ")
        else:
            res = re.findall(r"Requirement already satisfied: (.+?)(?:(?:>=|==|!=).+?)? in", content, re.S)
            if res:
                return res


def get_page(lib):
    """获取页面"""
    res = requests.get("https://pypi.org/project/{}/#files".format(lib))
    if str(res.status_code).startswith("2"):
        obj = etree.HTML(res.content)
        try:
            libs = obj.xpath("//tbody/tr/td/a/@href")
            cp34 = [i for i in libs if i.endswith(".whl") and ("cp34" in i or "py2.py3" in i)]
            if cp34:
                return cp34.pop()
            else:
                return libs.pop()

        except:
            print(lib)


def download(url, lib):
    """下载安装包"""
    content = requests.get(url).content
    name = url.split("/").pop()
    if not os.path.exists(lib):
        os.mkdir(lib)
    with open(os.path.join(lib, name), "wb") as f:
        f.write(content)
    print("[DOWN] <=== {} success!".format(name))


def start(lib):
    """启动器"""
    devs = get_dev(lib)
    for dev in devs:
        file = get_page(dev)
        download(file, lib)


if __name__ == "__main__":
    start("paramiko")
```

