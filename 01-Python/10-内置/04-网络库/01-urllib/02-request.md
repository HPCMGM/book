# 1. request

## 1.1 请求构建

### < Request

请求信息构建.

```python
def __init__(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None):
return Request
```

* url: `str`, 访问的url
* headers: `str`, 请求头部信息
* origin_req_host: `str`, `Origin`的ip地址
* unverifialbe: `bool`, 是否进行证书验证.
* method: `str`, 请求方法

**示例**

```python
import urllib.request
import urllib.parse

request = urllib.request.Request("http://localhost:8000/www", data=urllib.parse.urlencode({"a": 1, "b": 2}, method="GET").encode())

with urllib.request.urlopen(request) as up:
    print(up.read().decode())  # 读取content内容
```

## 1.2 发送请求

#### > urlopen

向网站发送请求信息.

```python
def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, cafile=None, capath=None, context=None):
return Response
```

* url: `str/Request`, 建议使用`Request`, 不然没法设置`method`等方法
* data: `str`, 表单提交数据. 需要使用`urllib.parse.urlencode`编码
* timeout: `int`, 超时时间
* cafile: `str`, 配置单个证书位置
* capath: `str`, 配置证书路径
* context: `str`, 配置证书内容

**示例**

```python
import urllib.request
import urllib.error
import urllib.parse

try:
    with urllib.request.urlopen("http://localhost:8000/www", data=urllib.parse.urlencode({"a": 1, "b": 2}).encode()) as req:
        print(req.read().decode())  # 读取content内容
        print(req.info())           # 读取headers内容(str)
        print(req.getheader("Content-Type"))
        print(req.geturl())         # 读取url内容
        print(req.getcode())        # 读取返回码
except urllib.error.HTTPError as e:
    # 当返回码为400时, 可以通过捕获异常获取信息
    print(e.read().decode())
    print(e.info())
```

输出

```python
If you get this page means your service is success!
Server: hpcm server
content-type: text/html; charset=utf-8
Content-Length: 51
Date: Tue, 23 Apr 2019 02:34:50 GMT


text/html; charset=utf-8
http://localhost:8000/www
```

## 1.3 爬虫三池

爬虫中基本反爬手段, 登录浏览器类型, ip地址, cookie的身份.

### 1.3.1 User-Agent

用于headers中的浏览器型号伪装

[User-Agent.py](image/02-request/User-Agent-list.py)

### 1.3.2 < ProxyHandler

IP池, 用于随机ip访问.

```python
def __init__(self, proxies=None):
return Handler
```

* proxies: `dict`, 代理信息. 例如: `{"http": "http://username:password@ip:port"}`

**示例**

```python
import urllib.request

# 其他hander使用方法相同
# *********************方法一(全局)**********************************
proxy_handler = urllib.request.ProxyHandler({"http": "http://username:password@ip:port"})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)  # 设置为全局, 即设置到urlopen中
request = urllib.request.Request("http://www.baidu.com")
urllib.request.urlopen(request).read()
# *********************方法二(直接使用)**********************************
proxy_handler = urllib.request.ProxyHandler({"http": "http://username:password@ip:port"})
opener = urllib.request.build_opener(proxy_handler)
request = urllib.request.Request("http://www.baidu.com")
opener.open(request).read()
```



### 1.3.3 < HTTPCookieProcessor

用户身份`cookie`维护, 防止过期

```python
def __init__(self, cookiejar=None):
return Handler
```

* cookiejar: `dict`, 默认`http.cookiejar.CookieJar()`.

**示例**

```python
import urllib.request
import urllib.parse
import http.cookiejar

from lxml import etree

form = {"staticpage": "https://www.baidu.com/cache/user/html/v3Jump.html",
        "charset": "UTF-8",
        "token": "57afd5e03e0d831b0fc760e4b83d7790",
        "tpl": "mn",
        "subpro": "",
        "apiver": "v3",
        "tt": "1556004351619",
        "codestring": "",
        "safeflg": "0",
        "u": "https://www.baidu.com/",
        "isPhone": "",
        "detect": "1",
        "gid": "8C477E5-50BF-4A0B-B35C-9407A10931DC",
        "quick_user": "0",
        "logintype": "dialogLogin",
        "logLoginType": "pc_loginDialog",
        "idc": "",
        "loginmerge": "true",
        "splogin": "rate",
        "username": "15516151135",
        "password": "e3f3LSZr7F+c2ENoSw8ELAESo+VTVZOw8+jCxY1qmehDckXO36OiRYHOqjC9WgDzRYFRk581SFyzL4wFujKo9cvRNS7ITDFNLhpCm8G/RD5rhAkApZgjnqRjQgPnVueVVZ3y4tO3P23Q7BYgP1d4tVJ0yttFnbwx0PqZ3ptkKNY=",
        "mem_pass": "on",
        "rsakey": "48aSagWK32CZA0Ri0iMFSRNDtbACMq4g",
        "crypttype": "12",
        "ppui_logintime": "53170",
        "countrycode": "",
        "fp_uid": "",
        "fp_info": "",
        "loginversion": "v4",
        "ds": "KMEXIVVXXXCAHzGcDVnSWeSn6VOSxKTavHtwHFFmmN5/2hFapvu0xIx9rWg6eIAG+sRkaZSA0A0LUhZoLDiPHjmETEgIekXPr6IMU5YMSRb8uCHTXS5Q5s15H9Zz7j312MPOXbMVv0MUFlICEWdo03/xJjzf/EsZ96w1GSgBx9ST8axC9aeSlIbG5CTYie44rPQ4/r7ed7T9qRczzkG0nxJWKLCxcGj1Rf/+Sd21Mwp268lpp7jjU2+h6bHLr3Ol87h9Vm0QevRTolw1AZDg99YQvDtzZ2RsbXYWm1ecIAiNC1K1zJQFWtnJfVPXdnCIoSImIBiqcLd6RsxDAd6noKOpB5UmjiLnhJ+6cLhZTvu7kkPaXfptNaVzzLbZ8OchDaRusKVic+oybxe8C+sdTdTiqgII91rmFq1aayfCgt8yPn7qgH8R/v6/ek35JQDnMgDuCaX2Sjn1Md/QfQIdTXFalq+0K8IDN+T+pwxm4/lPKkcBfDHfRPaPCsdyqelI98e+p5VG0KJubeNyVEcS/0nouTB39IUzqJS42qDRK7m+Ktv1Jj08cEODCbBW4zn5BsJk1J3ZjnaA373SRZedZ3x9g7UD28tBpkzmwZAQwQOm4MgJJNpPgkRKkazVvwYn6OdXVSsOIRKK2qRKSDmyuyCCLO21KqpGM6RyJJyqpI7CKi7f5R2sZvWOB2HcjSJ9wS2HQ06hOsFKwupgtL8oNfoMmcV328NPH0BuEWKpruckByDuYIiqtXSLJzZ/cereEygh8lSvo12R4kwLSdUx+oEk2eFt2CL1aMreA1areNunjSRKV9BONt6L7UTI7bT3gF3asS1rSFZRS0QBpJ9CtfiC/4AgQ+Hb5RhgMeWcxRsRCqCasuNZRIFZHg8eUbDUJu3XE4KDYJn6BHE5SOrDi8D7xsobAxYW4YRAw7/u/yAlsW5BX46jfFX0rJguaNTvzHBzFtQy2N9HD+jAmNpjG1nojJP916FmZb6W5zube2eHgN1GAu4Yaci+HrfYbtINsK/R6HQ2iVAMV8wQ8B5w6T6I5tRXbYhxLWFBdHZm1gVei/LhRqc5b86has375ovlq2YZl6/1/V0FJQhw8eZB9RbU5HA3ROyRblgZJkPDGvOKkNGjpWxsXk9j9IBU3htthRWKVJHtJXg7Kh/ey5yiLjfDh8E+8gAz5foU4+KCEWkiiwJuiwpn17C26tDx3nSSx1aAQTW+xEsVaVQmVZLXH3egb2y7DI7u5Kf3E3hlWL0v4lo7Im6VT18qaUOtCLX3",
        "tk": "4750Utcy1Bb63gH2McvTYkbvFiWQa6P3AvDT/wj4unfYIkpJKoURw0yPG56kVwOKLuvm",
        "dv": "tk0.93499462943878031556004298657@ssr0AsokqRBXrRBmwK8EpZokqRBXrRBmwx9PnxMmwwo0zKB0wR8Eva8PpZokqRrvp5FK6hErlMnp9tAavwAKlKC~ryEJpfO2wV5E8z54wR8mVgHLVRokvz9kqyMq__tr0qt5k8aokvx52wx9kIRMkIx91wa9EqR5ktKopFhE3H2tnKMAKhEnpZV8plMOJlcH0ryrnVcO~SgtXFgMkI~92wy9ktR8ECa91Vntnz4n3p9AKltnKhM8EhMAY9KIJKeHpHyIAhwOA6Z9aqxokvK82wy9kq-opFhE3H2tnKMAKhEnpZV8plMC0paCYHcCJFZ9PIYokva8mwx9PCYo4w_uUUDzU-sYUcCh-rh82wyokCaErbH0RwoP3a9k3z9kIy5Eta5kC-8k8V9En~8kqx8P3-9PnYhrbD4FxC48joylYHYCgIJpeO4ngI~lfoyVKBJFSOJSgOLt_Grd9aqR9PtR8EtY82wa9EvR8E3y8mwV8kGwokvz8PqR8Enw9mwz9Ev_",
        "traceid": "AA2ABC01",
        "callback": "parent.bd__pcbs__usvr84"}
headers = {
"Connection": "close",
"Content-Length": "2768",
"Content-Type": "application/x-www-form-urlencoded",
"Cookie": "BAIDUID=4296046C002606DDB6DED01A5ADB4182:FG=1; BIDUPSID=4296046C002606DDB6DED01A5ADB4182; PSTM=1550713766; MCITY=-340%3A; HOSUPPORT=1; UBI=fi_PncwhpxZ%7ETaJc6tARV41j-0xl98W2VVSobwQRe1%7EZtXPy6PUN6uq26ugrWh98CQQF0c4piUhh%7Eu7H9hX; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=28882_1467_28804_21079_18559_28768_28720_28832_28584_26350_22158; delPer=0; PSINO=7; locale=zh; USERNAMETYPE=1; SAVEUSERID=416cbf75a6be8a9c7dedc923e822f23b; HISTORY=8e73f3f0156dfaaa4e803238ab151ac484afa915584fa8252b2ab70f3ac81266fbc217c263d81d1298d746f856e0df833cbfd6; pplogid=4750Utcy1Bb63gH2McvTYkbvFiWQa6P3AvDT%2Fwj4unfYIkpJKoURw0yPG56kVwOKLuvm",
}

cookie = urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())
opener = urllib.request.build_opener(cookie)
urllib.request.install_opener(opener)
request = urllib.request.Request("https://passport.baidu.com/v2/api/?login", data=urllib.parse.urlencode(form).encode(), headers=headers, method="POST")
urllib.request.urlopen(request)
obj = etree.HTML(urllib.request.urlopen("http://www.baidu.com/").read())
print("用户名: {}".format(obj.xpath("//span[@class=\"user-name\"]/text()")))
```

## 1.4 异常类

#### < ContentTooShortError

`header`中的`Content-Type`长度与`data`不符

#### < HTTPError

Http响应码`4xx`报错

#### < URLError

url参数编码错误

# 2. 返回值

## 2.1 Request

## 2.2 Response

## 2.2 Handler





