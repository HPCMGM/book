# request

`request`为客户端请求信息的封装, 可以使用这个对象来提取需要的参数

# 1.  请求数据
## 1.1 url

`request.args`, 用于提取url中的参数. 方法参见`ImmutableMultiDict`

**示例:**

```python
request.args.get("a")
request.items()
```

## 1.2 form表单

form表单数据包含两种数据提取方法

```python
<!DOCTYPE html>
<html>
    <body>
        <form action="/items" action="upload" method="post" enctype="multipart/form-data">
            <input type="checkbox" name="test" value="1"/>
            <input type="checkbox" name="test" value="2"/>
            <input type="checkbox" name="test" value="3"/>
            <input type="file" name="file" /><br />
            <input type="submit" value="Upload" />
        </form>
    </body>
</html>
```



### 1.2.1 `request.form`

提取文本数据, 一般`text`, `textarea`, `password`, `radio`等标签. 方法参见`ImmutableMultiDict`

```python
request.form.get("test")   # 1
request.form.getlist("test")  # ['1', '2']
```

### 1.2.2 `request.files`

提取文件(文件/图片等流数据)数据, 一般`file`等标签. 方法参见`ImmutableMultiDict`.

获取到的将是`FileStorage`类型数据. 具体数据提取方法参见`FileStorage`

```python
request.files.get("file")   # <FileStorage: 'netspeed.py' ('text/plain')>
```

**注意:**

* 要想提取到文件, 前端必须使用`enctype="multipart/form-data"`
* 可以用`request.close()`来关闭本次访问的全部文件流对象

## 1.3 url+form

同时获取表单和url参数

`request.values` = `request.args` + `request.form`

```python
    def values(self):
        args = []
        for d in self.args, self.form:
            if not isinstance(d, MultiDict):
                d = MultiDict(d)
            args.append(d)
        return CombinedMultiDict(args)
```



## 1.4 json

`request.json`, dict类型. 直接可以使用

```python
{'a': [1, 2, 3]}
<class 'dict'>
```

## 1.5 cookies

`request.cookies`, 格式为字典, 获取客户端的cookies

## 1.6 body源数据

`request.data`, 获取body源数据, bytes

```python
b'{\n\t"a": [1, 2, 3]\n}'
```
## 1.7 无法解析的数据

`request.stream`,  flask无法解密的数据, 封装在stream中(不破坏格式), 只能获取一次

## 1.8 其他数据

`request.environ`, 客户端的全部信息, 此数据是即将送往wsgi中处理的第一个参数

```python
{'wsgi.version': (1, 0), 'wsgi.url_scheme': 'http', 'wsgi.input': <_io.BufferedReader name=632>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'wsgi ... T_LANGUAGE': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 'werkzeug.request': <Request 'http://localhost:5000/abc/dtc/abc/?date=2020' [GET]>}
```

# 2. 请求头部

## 2.1 请求头

`request.headers`, `<class 'werkzeug.datastructures.EnvironHeaders'>`, 方法类似`ImmutableMultiDict`. 包含了客户端全部的headers信息

```python
 Host: localhost:5000
 Connection: keep-alive
 Pragma: no-cache
 Cache-Control: no-cache
...
 Sec-Fetch-User: ?1
 Sec-Fetch-Dest: document
 Accept-Encoding: gzip, deflate, br
 Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
```

## 2.2 请求行
```python
curl http://localhost:5000/abc/dtc/abc/?date=2020
        
@app.route("/abc/dtc/<string:b>/")
def index1(b):
    return b
```
### 2.2.1 url数据

* `request.url`

  获取完整url

  ```python
  http://localhost:5000/abc/dtc/abc/?date=2020
  ```

* `request.path`

  获取资源路径

  ```python
  /abc/dtc/abc/
  ```

* `request.url_root/request.host_url`

  url的根路径. 由于两者最终调用的方法均为`uri_to_iri`, 所以输出均一样

  ```python
  def get_current_url(root_only=False, host_only=False)  # 两者都会调用这个函数
      if host_only:
          return uri_to_iri("".join(tmp) + "/")  # 经过此函数后会提取出来根路径
      ...  # 中间会拼接完整的url
      return uri_to_iri("".join(tmp))  # 经过此函数后会提取出来根路径, 和中间的内容没有什么关系
  ```

  ```python
  http://localhost:5000/
  ```

* `request.url_rule`

  url的正则规则, 如果没有配置则为`request.path`

  ```python
  /abc/dtc/<string:b>/
  ```

* `request.base_url`

  不包含url参数的url

  ```python
  http://localhost:5000/abc/dtc/abc/
  ```

* `request.url_charset`

  解析url时使用的字符集, 默认为`utf-8`

* `request.host`

  获取url中的host和port

  ```python
  localhost:5000
  ```
  

### 2.2.2 协议及方法

| 功能         | 函数             |
| ------------ | ---------------- |
| 获取协议     | `request.scheme` |
| 获取请求方法 | `request.method` |



**说明:**

* HTTP 1.0
  * GET: 请求页面并返回实体
  * POST: 提交数据
  * HEAD: 获取headers
* HTTP 1.1
  * OPTIONS: 查询服务器性能
  * PUT: 提交并修改数据
  * PATCH: 补充PUT方法, 对已知资源进行更新
  * DELETE: 删除数据
  * TRACE: 回显, 用于测试或诊断
  * CONNECT: HTTP/1.1 协议中预留给能够将连接改为管道方式的代理服务器

# 4. 使用的类

## 4.1 ImmutableMultiDict

request中多次采用了不可变字典, 来封装客户端传递的数据, 实例中只使用了`request.args`做演示.

类型`ImmutableMultiDict`, 不可变字典, 不能对其修改, 否则抛出

```python
TypeError: 'ImmutableMultiDict' objects are immutable
```

由于不可变类型, 不能使用增删改操作, 所以不可用方法没有展示.

**方法:**

* **get(self, key, default=None, type=None)**

  获取一个key对应的value, 如果参数对应的值是list, 只能获取到list的第一个元素

  * key: 键
  * default: 如果没有取到值, 这使用此数据做填充
  * type: 将获取到值, 按照type转换为该类型

  ```python
  http://www.baidu.com/?key=1&key=2&key=3
      
  request.args.get("key")  # 1
  ```

  

* **getlist(self, key, type=None)**

  获取一个key对应的value, 可以获得全部参数

  * key: 键
  * type: 类型转换

  ```python
  http://www.baidu.com/?key=1&key=2&key=3
      
  request.args.getlist("key")  # ["1", "2", "3"]
  ```

* **items(self, multi=False)**

  获取key, value的二元组的可迭代对象.

  * multi: 类似get与getlist的区别, False一个元素/True一个列表

  ```python
  http://www.baidu.com/?key=1&key=2&key=3
      
  list(request.args.items(False))  # [('key', '1')]
  list(request.args.items(True))  # [('key', '1'), ('key', '2'), ('key', '3')]
  ```

* **keys(self)**

  返回keyview(dict_keyiterator), 类似字典获取keys

  ```python
  http://www.baidu.com/?key=1&key=2&key=3
      
  list(request.args.keys())  # ["key"]
  ```

* **lists(self)**

  返回Generator,  迭代出来为二元组(key, 完整的values)

  ```python
  http://www.baidu.com/?key=1&key=2&key=3
      
  list(request.args.lists())  # [('key', ['1', '2', '3'])]
  ```

* **values(self)**

  返回Generator, 迭代出来key对应的第一个value

  ```python
  http://www.baidu.com/?key=1&key=2&key=3
      
  list(request.args.values())  # ['1']
  ```

* **listvalues(self)**

  返回Generator, 迭代出来key对应完整的value

  ```python
  http://www.baidu.com/?key=1&key=2&key=3
      
  list(request.args.values())  # [('1', '2', '3')]
  ```

* **to_dict(flat=True)**

  返回dict, 将不可变字典转换成普通字典

  * flat: 转化时是否只提取 value的第一个元素, True提取一个/False完整转化

  ```python
  http://www.baidu.com/?key=1&key=2&key=3
      
  list(request.args.to_dict())  # {"key": "1"}
  ```

  

## 4.2 FileStorage

主要用于文件流对象的读取

* **read**

  此方法是由`storage.stream.read()`简化来的

* **save(self, dst, buffer_size=16384)**

  保存文件

  * dst: str, 保存文件的路径
  * buffer_size: 缓冲区大小.

  ```python
  file_storage = request.files.get("file")
  file_storage.save("test.py")
  ```

  

* **content_length/content_type**

  源码为

  ```python
  @property
  def content_length(self):
      return int(self.headers.get("content-length") or 0)
  
  @property
      def content_type(self):
          """The content-type sent in the header.  Usually not available"""
          return self.headers.get("content-type")
  ```

  一般浏览器上传文件不会携带此参数的, 所以是获取不到真正的答案的

* **filename**

  文件名称

  ```python
  hosts.yml
  ```

* **headers**

  文件相关的头部信息

  ```python
  Content-Disposition: form-data; name="file"; filename="hosts.yml"
  Content-Type: application/octet-stream
  ```

* **mimetype**

  文件类型

  ```python
  application/octet-stream
  ```

* **mimetype_params**

  将`=`类型的参数字典化

  ```python
  text/html; charset=utf-8
  ----转化----
  {"charset": "utf-8"}
  ```

* **name**

  对象名称

  ```python
  file
  ```

* **close(self)**

  关闭流对象, 源码

  ```python
  def close(self):
      try:
          self.stream.close()
      except Exception:
          pass
  ```

  

* **stream**

  文件流对象, 源码

  ```python
  self.stream = stream or BytesIO()
  ```

  