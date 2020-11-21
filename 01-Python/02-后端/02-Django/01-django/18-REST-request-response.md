# 1. Request

REST Framework 使用Parser解析器将数据按照Content-Type类型进行解析, 然后保存到Request对象中用于调度

其中Request方法对应如下

| 方法                   | 类型 | 说明                                              |
| ---------------------- | ---- | ------------------------------------------------- |
| `request.data`         | dict | 包含files, form, json(post, put, patch请求)的数据 |
| `request.query_params` | dict | get请求的url参数                                  |
|                        |      |                                                   |
|                        |      |                                                   |
|                        |      |                                                   |
|                        |      |                                                   |
|                        |      |                                                   |

# 2. Response

```python
class HTTPResponse: def __init__(self, content=b"", content_type=None, status=None, reason=None, charset=None)
```

* content: bytes, 需要发送的内容
* content_type:  str, 前端完整的Content-Type, 例如`application/json; charset=utf-8`
* status: int, 响应码, 此验证码会校验, 必须在[100, 599]之间
* reason: int, 响应码, 不校验验证码.
* charset: 要求前端的编码格式

## 2.2 响应码码表

```bash
1）信息告知 - 1xx
    HTTP_100_CONTINUE
    HTTP_101_SWITCHING_PROTOCOLS

2）成功 - 2xx
    HTTP_200_OK
    HTTP_201_CREATED
    HTTP_202_ACCEPTED
    HTTP_203_NON_AUTHORITATIVE_INFORMATION
    HTTP_204_NO_CONTENT
    HTTP_205_RESET_CONTENT
    HTTP_206_PARTIAL_CONTENT
    HTTP_207_MULTI_STATUS

3）重定向 - 3xx
    HTTP_300_MULTIPLE_CHOICES
    HTTP_301_MOVED_PERMANENTLY
    HTTP_302_FOUND
    HTTP_303_SEE_OTHER
    HTTP_304_NOT_MODIFIED
    HTTP_305_USE_PROXY
    HTTP_306_RESERVED
    HTTP_307_TEMPORARY_REDIRECT

4）客户端错误 - 4xx
    HTTP_400_BAD_REQUEST
    HTTP_401_UNAUTHORIZED
    HTTP_402_PAYMENT_REQUIRED
    HTTP_403_FORBIDDEN
    HTTP_404_NOT_FOUND
    HTTP_405_METHOD_NOT_ALLOWED
    HTTP_406_NOT_ACCEPTABLE
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED
    HTTP_408_REQUEST_TIMEOUT
    HTTP_409_CONFLICT
    HTTP_410_GONE
    HTTP_411_LENGTH_REQUIRED
    HTTP_412_PRECONDITION_FAILED
    HTTP_413_REQUEST_ENTITY_TOO_LARGE
    HTTP_414_REQUEST_URI_TOO_LONG
    HTTP_415_UNSUPPORTED_MEDIA_TYPE
    HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
    HTTP_417_EXPECTATION_FAILED
    HTTP_422_UNPROCESSABLE_ENTITY
    HTTP_423_LOCKED
    HTTP_424_FAILED_DEPENDENCY
    HTTP_428_PRECONDITION_REQUIRED
    HTTP_429_TOO_MANY_REQUESTS
    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS

5）服务器错误 - 5xx
    HTTP_500_INTERNAL_SERVER_ERROR
    HTTP_501_NOT_IMPLEMENTED
    HTTP_502_BAD_GATEWAY
    HTTP_503_SERVICE_UNAVAILABLE
    HTTP_504_GATEWAY_TIMEOUT
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED
    HTTP_507_INSUFFICIENT_STORAGE
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED
```

