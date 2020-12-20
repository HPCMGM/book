# 1. http协议

```python

```

# 2. url解析

RFC3986规定: url中只允许包含字母（a-zA-Z）、数字（0-9）、-_.~4个特殊字符以及所有保留字符。

## 2.1 url编码

将其他等非ASCII, 转化为有十六进制, 字母大写, 并用%分割后组成

### 2.1.1 解码

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

### 2.1.2 解码

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

# 3. 请求参数

## 3.1 query参数

### 3.1.1 编码.

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

### 3.1.2 解码

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

## 3.2 json参数

## 3.3 form参数





