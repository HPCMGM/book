# 1. request

## 1.1 属性

请求数据, url, 方法, 协议, 端口, ip等数据提取

* 注意如果测试表单数据提交, 在没有完整配置session依赖的redis情况下, 最好把csrftoken的中间件关闭, 否则不能正常提交表单的

| 属性                      | 作用                                                         | 对应方法                                                     |
| ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `request.GET`             | GET请求参数提取                                              | 1. `get()`: 获取单个数据<br>2. `getlist()`: 获取列表数据<br>**可以参考flask中的GET提取方法** |
| `request.POST`            | 表单提交参数提取(除流数据外)                                 | 同上                                                         |
| `request.FILES`           | 表单中的流对象提取                                           | 同上                                                         |
| `request.body`            | bytes, 原始响应体数据                                        |                                                              |
| `request.method`          | str, 请求方法                                                |                                                              |
| `request.encoding`        | None/str, 请求头中的`charset`参数                            |                                                              |
| `request.environ`         | dict, 遵循`WSGI`协议的environ                                |                                                              |
| `request.headers`         | dict, 请求头部信息                                           |                                                              |
| `request.path`            | str, 请求资源路径(例`/users/`), 不含参数                     |                                                              |
| `request.scheme`          | str, 请求协议(例`http/https`)                                |                                                              |
| `request.content_param`   | dict, 请求头部中的`Content-Type`用`;`分开, 如果没有`;`则为空字典 |                                                              |
| `request.content_param`   | str, 从`request.content_param`中获取`charset`参数            |                                                              |
| `request.upload_handlers` | list, 上传文件解析使用的类, 一般可以用`FILE_UPLOAD_HANDLERS`去指定. |                                                              |




## 1.2 方法

| 方法                                                         | 说明                                                         | 参数                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `build_absolute_uri(location=None):`                         | 自动规整绝对资源路径                                         | `location`: str, 绝对路径                                    |
| `get_full_path(force_append_slash=False)`                    | 获取资源路径 <br>In [1] `http://localhost: 8000/aa/bb`<br>Out [1] `/aa/bb` | `force_apped_slash`:  bool, 是否追加尾部`/`                  |
| `get_full_path_info(force_append_slash=False):`              | 源码中和`get_full_path`调用一个函数                          | 同上                                                         |
| `get_host()`                                                 | 获取host:port<br>`127.0.0.1:8000`                            |                                                              |
| `get_port()`                                                 | 获取port<br>`8000`                                           |                                                              |
| `get_raw_uri():`                                             | 没有处理前的完整url<br>`http://127.0.0.1:8000/users/?a=b&b=%E4%BD%A0%E5%A5%BD` |                                                              |
| `is_ajax`()                                                  | 判断, 是否由`ajax`发送的请求, 比较的是:HTTP_X_REQUESTED_WITH字段是否等于XMLHttpRequest |                                                              |
| `is_secure()`                                                | 判断, 是否使用`https`协议                                    |                                                              |
| `get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)` | 获取cookie                                                   | `key`: cookie的键<br>`default`: 如果不存在, 则使用这个默认的值代替<br>`salt`: 加密的盐<br>`max_age`: 最大生存时间, 如果超过这个时间就会报错 |
| `parse_file_upload(self, META, post_data)`                   | tuple(POST QueryDict, FILESMultiValueDict)获取提交的表单流对象, | 这个是内部完成的参数无序自己配置                             |
| `read(size=0)`                                               | 读取流对象<br>request.POST或者request.body                   |                                                              |
| `readline(line)`                                             | 同上                                                         |                                                              |
| `readlines()`                                                | 同上                                                         |                                                              |
| `close()`                                                    | 文件读取完成后, 需要关闭流对象                               |                                                              |



# 2. 封装的对象

## 2.1 user

当前用户对象, 对应方法:

* check_password
* delete
* get_all_permissions
* get_group_permissions
* get_user_permissions
* get_username
* groups
* has_module_perms
* has_perm
* has_perms
* id
* is_active
* is_anonymous
* is_authenticated
* is_staff
* is_superuser
* pk
* save
* set_password
* user_permissions
* username

## 2.2 resolver_match

此对象主要用于获取当前用户调取当前的请求链

* app_name: app_name的名称
* app_name: app_name名称列表
* args: 传入视图函数中的args参数
* kwargs: 传输视图函数中的关键字参数
* func: 当前视图函数
* namespace: url命名空间
* route: 当前路由
* url_name: url命名
* view_name: 视图函数名称



