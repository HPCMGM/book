# 1. parse

## 1.1 非ASCII数据转义

### 1.1.1 转义

#### > quote

遵循http协议, 将非ASCII文本进行转义处理, 即将此符号进行`base64`转义, 输出格式为16进制, 并在前面加`%`. 用于http协议传输.

```python
def quote(string, safe='/', encoding=None, errors=None):
return str
```

* string: `str`, 需要转义的字符
* safe: `str`, 不需要转义的字符. 默认为: `/`
* encoding: `str`, 编码格式
* errors: `str`, 编码出现异常时处理方案.

**示例**

```python
print(urllib.parse.quote("/你好?", safe="/?"))
print(urllib.parse.quote("/你好?"))

import base64

def base_quote(s):
    es = base64.b16encode(s.encode()).decode()
    return "".join(["%" + es[i: i + 2] for i in range(0, len(es), 2)])

print(urllib.parse.quote("/你 好?", safe=""))
print(base_quote("/你 好?"))
```

输出

```python
/%E4%BD%A0%E5%A5%BD?
/%E4%BD%A0%E5%A5%BD%3F

%2F%E4%BD%A0%20%E5%A5%BD%3F
%2F%E4%BD%A0%20%E5%A5%BD%3F
```

#### > quote_plus

和`quote`一样. 不同之处在于:  空格`" "`转义为`+`, `safe`中默认参数不为`/`

```python
def quote_plus(string, safe='', encoding=None, errors=None):
return str
```

* string: `str`, 需要转义的字符
* safe: `str`, 不需要转义的字符.
* encoding: `str`, 编码格式
* errors: `str`, 编码出现异常时处理方案.

**示例**

```python
print(urllib.parse.quote_plus("/你 好?", safe="/"))
print(urllib.parse.quote("/你 好?", safe="/"))
```

输出

```python
/%E4%BD%A0+%E5%A5%BD%3F
/%E4%BD%A0%20%E5%A5%BD%3F
```

#### > quote_from_bytes

类似`quote`. 不同在于转义二进制流对象, 即接收的参数为`bytes`

```python
def quote_from_bytes(bs, safe=b"/"):
return str
```

### 1.1.2 转义还原

#### > unquote

`quote`的反函数, 用于转义的反解析. 

```python
def unquote(string, encoding='utf-8', errors='replace'):
return str
```

* string: `str`, 需要反转义的字符
* encoding: `str`, 编码格式
* errors: `str`, 编码出现异常时处理方案.

**示例**

```python
encode_str = urllib.parse.quote("你/?好", safe="?")
print(encode_str)
print(urllib.parse.unquote(encode_str))
```

输出

```python
%E4%BD%A0%2F?%E5%A5%BD
你/?好
```

#### > unquote_plus

`quote_plus`的反函数, 用于反解析.

```python
def quote_plus(string, encoding='utf-8', errors='replace'):
return str
```

* string: `str`, 需要反转义的字符
* encoding: `str`, 编码格式
* errors: `str`, 编码出现异常时处理方案.

#### > unquote_from_bytes

`unquote_from_bytes`的反函数, 用于反解析

```python
def quote_from_bytes(str):
return bytes
```

* string: `str`, 需要反转义的字符

## 1.2  url参数

### 1.2.1 Python转url参数

#### > urlencode

```python
def urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus):
return str
```

* query: `dict/items`, 字典或者为可迭代的二元组.
* doseq: `bool`, 如果`query`的中存在`list`类型, 是否为每个元素都设置一个`key`. `False`表示不设置.
* safe: `str`, `+`, `/`等特殊字符, 不进行编码操作.
* encoding: `str`, 编码格式
* errors: `str`, 编码产生异常时处理方案. `str.encode(encoding, errors)`
* quote_via: `str`, 编码调用函数, 默认`urllib.parse.parse_plus`

**示例**

```python
query_data = {
    "a": ["1", "2"],
    "b": "1",
    "c": "+"
}

print(urllib.parse.urlencode(query=query_data, doseq=True, safe="+"))
```

输出

```python
a=1&a=2&b=1&c=+
```

### 1.2.2 url参数转Python

#### > parse_qsl

```python
def parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace'):
return items
```

* qs: `str`, 需要解析的url字符串参数.
* keep_blank_values: `bool`, 表示是否将空白值视为空白字符串.
* strict_parsing:  `bool`, 表示如果解析出现异常, 是否引发异常. `False`表示忽略异常
* encoding: `str`, 编码格式
* errors: `str`, 编码出现异常时处理方案.

**示例**

```python
import urllib.parse

url_data = "a=1&a=2&b=1&c=+&e="

print(urllib.parse.parse_qsl(url_data, keep_blank_values=True))
print(urllib.parse.parse_qsl(url_data, keep_blank_values=False))
```

输出

```python
[('a', '1'), ('a', '2'), ('b', '1'), ('c', ' '), ('e', '')]
[('a', '1'), ('a', '2'), ('b', '1'), ('c', ' ')]
```

#### > parse_qs

内部是将`parse_qsl`的结果转化为字典.

```python
def parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace'):
return dict
```

* qs: `str`, 需要解析的url字符串参数.
* keep_blank_values: `bool`, 表示是否将空白值视为空白字符串.
* strict_parsing:  `bool`, 表示如果解析出现异常, 是否引发异常. `False`表示忽略异常
* encoding: `str`, 编码格式
* errors: `str`, 编码出现异常时处理方案.

**示例**

```python
print(urllib.parse.parse_qs(url_data))
```

输出

```python
{'a': ['1', '2'], 'b': ['1'], 'c': [' ']}
```

## 1.3 url操作

### 1.3.1 url拆分

#### > urlparse

将完整url, 解析为: 协议, 域名/IP:PORT, 资源路径, 参数, 锚点等信息

```python
def urlparse(url, scheme="", allow_fragments=True):
return ParseResult
```

* url: `str`, 需要解析的url
* scheme: `str`, 当前使用的协议
* allow_fragments: `bool`, 是否解析锚点符号`#`

**示例**

```python
import urllib.parse

url = "https://www.baidu.com/index?a=1&b=#aa"
print(list(urllib.parse.urlparse(url, allow_fragments=False)))
print(urllib.parse.urlparse("//www.baidu.com/你好/<bb>?a=1&b=2#aa", "https"))
```

输出

```python
['https', 'www.baidu.com', '/index', '', 'a=1&b=#aa', '']
ParseResult(scheme='https', netloc='www.baidu.com', path='/你好/<bb>', params='', query='a=1&b=2', fragment='aa')
```

### 1.3.2 url合并

#### > urlunparse

`urlparse`的反函数, 将协议, 域名/IP:PORT, 资源路径, 参数, 锚点等信息组合为完整的url

```python
def urlunparse(components):
return str
```

* components: `iterable`, 可迭代对象, 需要提供6个元素, 分别为: 协议, 域名/IP:PORT, 资源路径, 参数, 锚点信息.

**示例**

```python
print(urllib.parse.urlunparse(['https', 'www.baidu.com', '/index', '', 'a=1&b=#aa', '']))
```

输出

```python
https://www.baidu.com/index?a=1&b=#aa
```

### 1.3.3 url组合

#### > urljoin

按照http协议进行url路径组合

```python
def urljoin(base, url, allow_fragments=True):
return str
```

* base: `str`, url组合的基础路径
* url: `str`, url需要组合的路径. 有点类似`os.path.join`, 如果此参数以根路径开头, 则会覆盖`base`.
* allow_fragments: `bool`, 是否解析锚点`#`, 参见`urlencode`

**示例**

```python
print(urllib.parse.urljoin("http://www.baidu.com", "1.py"))
print(urllib.parse.urljoin("http://www.baidu.com", "/www.tencent.com"))
print(urllib.parse.urljoin("http://www.baidu.com", "//www.tencent.com"))
```

输出

```python
http://www.baidu.com/1.py
http://www.baidu.com/www.tencent.com
http://www.tencent.com
```



