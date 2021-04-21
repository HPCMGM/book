# 1. Request

```python
def __init__(self, url, callback=None, method='GET', headers=None, body=None,
                 cookies=None, meta=None, encoding='utf-8', priority=0,
                 dont_filter=False, errback=None, flags=None, cb_kwargs=None):
return Response
```

* url: `str`, 请求的url
* callback: `func`, 请求完成后回调的函数
* method: `str`, 请求的方法
* headers: `dict`, 请求时响应头部信息, 注意headers中不包含Cookies
* body: `str`, 响应体内容
* meta: ``
* encoding: `str`, 编码集
* priority: ``
* dont_filter: `bool`, 是否进行指纹判重, False表示不进行判重
* errback: `func`, 如果请求报错, 则会回调的函数
* flags: ``
* cb_kwargs: ``

# 2. Response

```python
def __init__(self, url, status=200, headers=None, body=b'', flags=None, request=None):
return response
```

* url: `str`, 请求的url
* status: `int`, 响应码
* headers: `dict`, 响应头部信息
* body: `bytes`, 响应体信息
* flags: ``
* resquest: `Request`, 请求对象