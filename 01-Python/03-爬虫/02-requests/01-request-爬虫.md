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
  * params
  * verify
  * cert
  * prefetch
  * adapters
  * stream
  * trust_env
  * max_redirects

# 2. 返回值

## 2.1 Response

#### - ok

判断, 响应是否成功. 状态码在400-600之间为False.

#### - status_code

获取当前请求的状态码

#### - is_redirect

判断, 是否进行重定向. 条件: location在headers中, 且状态码为301, 302, 303, 307, 308中的一个

#### - is_permanent_redirect

判断, 是否为永久重定向. 条件: location在headers中, 且状态码为301, 308中的一个

#### - next

获取重定向的url

#### - encoding

调用`text`时, 用来进行解码的字符集格式

#### - text

获取解码后的文本内容

#### - url

获取访问的url

#### - links

headers中的link

#### > iter_content

#### > iter_lines

#### > json

#### > raise_for_status

#### > close





