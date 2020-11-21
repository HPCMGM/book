# 1. REST

Representational State Transfer(REST), 表现层状态转化

## 1.1 说明

* 每一种URL代表一种资源
* 客户端和服务器之间, 传递这种资源的某种表现层
* t通过四个动词完成状态转化: GET,POST,PUT,DELETE(PATCH, HEAD, OPTIONS)

## 1.2 REST需要遵循

### 1.2.1 方法控制

* GET /zoos：列出所有动物园
* POST /zoos：新建一个动物园（上传文件）
* GET /zoos/ID：获取某个指定动物园的信息
* PUT /zoos/ID：更新某个指定动物园的信息（提供该动物园的全部信息）
* PATCH /zoos/ID：更新某个指定动物园的信息（提供该动物园的部分信息）
* DELETE /zoos/ID：删除某个动物园
* GET /zoos/ID/animals：列出某个指定动物园的所有动物
* DELETE /zoos/ID/animals/ID：删除某个指定动物园的指定动物

### 1.2.2 url控制

* url 数据量表示

  * `http://localhost/api/names`: 对全部数据操作
  * `http://localhost/api/names/1`: 对单一数据操作

* 接口表示

  * `https://api.example.com`
  * `https://example.com/api`

* 接口版本

  * `https://www.example.com/api/1.0/demo`
  * `https://www.example.com/api/2.0/demo`

  github的控制是在Accept中:

  ```python
  Accept: vnd.example-com.demo+json; version=1.0
  ```

### 1.2.3 参数限制

* 数量

  limit=10, 返回记录数量

* 偏移量

  offset=10, 返回的数据需要偏移的数量

* 页数

  page=2, 需要返回第几页

* 页数限制

  per_page=100, 每页限制为100

* 排序字段

  sortby=name, 指定按照name字段进行排序

* 排序方式

  order=asc, 指定排序方式为正序

* 筛选条件

  name_type_id=1, 指定按照name字段, id=1操作

## 1.3 响应参数

### 1.3.1 响应码

- 200 OK - [GET]：服务器成功返回用户请求的数据
- 201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
- 202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
- 204 NO CONTENT - [DELETE]：用户删除数据成功。
- 400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作
- 401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
- 403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
- 404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
- 406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
- 410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
- 422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
- 500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。

### 1.3.2 响应信息

* 正常访问

  - GET /collection：返回资源对象的列表（数组）
  - GET /collection/resource：返回单个资源对象
  - POST /collection：返回新生成的资源对象
  - PUT /collection/resource：返回完整的资源对象
  - PATCH /collection/resource：返回完整的资源对象
  - DELETE /collection/resource：返回一个空文档

* 异常访问

  error被异常的键名替换

  ```python
  {
      error: "Invalid API key"
  }
  ```

### 1.3.2 超媒体

Hypermedia API, 返回结果中, 提供链接其他api的url.

实例

```python
{
  "message": "Requires authentication",
  "documentation_url": "https://developer.github.com/v3"
}
```

# 2. REST核心开发

## 2.1 模型对象

用于储存json, xml数据的Python对象模型

## 2.2 序列化

将 Python 对象转化为 json, xml等, 用于前端访问. 此过程为序列化

## 2.3 反序列化

将 json, xml等转化为 Python 对象, 用于后台使用. 此过程为反序列化.



