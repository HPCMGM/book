# 1. requests

`requests`是Python中常用的网络爬虫工具, 是通过urllib3封装而成.支持

* Python2.6-Python3.5

使用时需要提前安装

```python
pip install requests
```



#### > request

```python
def request(method, url, **kwargs):
return Response
```

* method: `str`, 请求方式GET/PUT/POST/DELETE等
* url: `str`, 请求的url或者连带`query`参数等
* kwargs: 
  * headers
  * cookies
  * auth
  * proxies
  * hooks
  * 