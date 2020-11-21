# 1. CORS

Cross-origin resource sharing, CORS跨站资源共享.

## 1.1 允许跨域类型

允许在下列场景中使用跨域 HTTP 请求：

- 由 [`XMLHttpRequest`](https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest) 或 [Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) 发起的跨域 HTTP 请求。
- Web 字体 (CSS 中通过` @font-face `使用跨域字体资源), [因此，网站就可以发布 TrueType 字体资源，并只允许已授权网站进行跨站调用](http://www.webfonts.info/wiki/index.php?title=%40font-face_support_in_Firefox)。
- [WebGL 贴图](https://developer.mozilla.org/zh-CN/docs/Web/API/WebGL_API/Tutorial/Using_textures_in_WebGL)
- 使用 `drawImage` 将 Images/video 画面绘制到 canvas

## 1.2 跨域模式
CORS跨域请求有两种模式: 
* 简单模式

  * 请求类型

    HEAD/GET/POST

  * headers

    * Accept/Accept-Language/Content-Language/Last-Event-ID/DPR/Downlink/Save-Data/Viewport-Width/Width

    * Content-Type:

      只允许三种类型: application/x-www-form-urlencoded、multipart/form-data、text/plain

* 非简单模式

  只要没有满足简单模式的跨域请求, 均为非简单模式的操作

  比如`Content-Type: application/json`

# 2 简单模式

## 2.1 流程

* client发送跨域请求
* server回复client

## 2.1 headers

### 2.1.1 请求

| 字段   | 说明                                                         | 是否可选 |
| ------ | ------------------------------------------------------------ | -------- |
| Origin | 本次请求来自哪个源（协议 + 域名 + 端口）。服务器根据这个值，决定是否同意这次请求。 | 必填     |

### 2.1.2 响应

| 字段                             | 说明                                            | 是否可选 |
| -------------------------------- | ----------------------------------------------- | -------- |
| Access-Control-Allow-Origin      | 表示允许跨域的源可以有哪些, 所有的可以用`*`表示 | 必填     |
| Access-Control-Allow-Credentials | 表示是否允许发送Cookie, 默认是false             | 可选     |
| Access-Control-Expose-Headers    | 表示client可以读取的header字段                  | 可选     |

**说明**

* Access-Control-Expose-Headers

  默认只能读取6个字段: Cache-Control/Content-Language/Content-Type/Expires/Last-Modified/Pragma

* Access-Control-Allow-Credentials  

  需要server配置True, client中js才行:

  ```python
  var xhr = new XMLHttpRequest();
  xhr.withCredentials = true;
  ```

  并且Access-Control-Allow-Origin字段, 不能为`*`, 必须指明要发送的字段才能正常发送到server cookie

# 3. 非简单模式

## 3.1 流程

* client询问server允许的操作
* server回复client
* client获取允许的信息, 并按照要求发送信息
* server回复client

## 3.2 header

### 3.2.1 请求

| 字段                           | 说明                                     | 是否必填 |
| ------------------------------ | ---------------------------------------- | -------- |
| Origin                         | 本次请求来自哪个源（协议 + 域名 + 端口） | 必填     |
| Access-Control-Request-Method  | 需要的请求方法                           | 必填     |
| Access-Control-Request-Headers | 需要额外请求的头部信息字段               | 可选     |

### 3.2.2 响应

| 字段                             | 说明                                            | 是否必填 |
| -------------------------------- | ----------------------------------------------- | -------- |
| Access-Control-Allow-Origin      | 表示允许跨域的源可以有哪些, 所有的可以用`*`表示 | 必填     |
| Access-Control-Allow-Methods     | 表示允许跨域访问的方法                          | 必填     |
| Access-Control-Allow-Headers     | 表示允许额外增加的头部信息字段                  | 可选     |
| Access-Control-Allow-Credentials | 是否允许此请求跨域访问                          | 必填     |
| Access-Control-Max-Age           | 允许缓存此跨域数据最长时效                      | 可选     |

