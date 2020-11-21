# 1. json

本模块主要用于与其他语言进行交互时, 进行数据类型进行转化, 序列化对象(不记录Python数据格式)

### 1.1.1 序列化

#### > dumps

将Python数据类型, 转化为json数据.

```Python
def dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw):
```

* obj: Python object, 需要序列化的Python对象
* skipkeys: bool, 是否跳过非Python基本对象()的处理, False表示不会跳过, 则会抛出`TypeError`异常
* ensure_ascii: bool, 表示是否使用ascii码的转换, 如果为False则会原样输出, 不在使用转义功能
* check_circular: bool, 表示是否逐个的引用标签(可以用id查看), 如果为`False`则会跳过验证
* allow_nan: bool, 表示是否转换标准`float`类型外的类型(`nan`, `info`, `-inf`), `False`表示不转换, 抛出`ValueError`异常
* cls: func, 指定序列化器, 用于非Python标准类型序列化
* indent: 0/数字/字符串, 缩进填充控制, `0/负数/''`只会增加换行符. None无缩进, 正数标书缩进1格.
* separators: tuple, json数据中的`:`与`,`的控制, 默认使用(",", ": ").
* default: function, 序列化之后, value不是基本类型, 将会递归调用`default`来序列化, 直至为标准类型为止
* sort_keys: bool, 是否对keys进行排序处理
* \*\*kw: 官方文档指出目前kw未设置任何参数.(2020-08-28, 改版于Python3.6)

#### > dump

将Python数据类型, 转化为json数据类型, 并储存到流中(含有`.write`方法的对象).

```Python
def dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw):
```

* fp: `file-like object`, 文本类型的流对象, 比如`open`, `socket`等. 含有`write`方法即可
* 其他方法同上

### 1.1.2 反序列化

#### > loads

将json数据, 转化为Python数据类型

```Python
def loads(s, *, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
```

* s: str, 需要转化为Python基本数据类型的字符串
* cls: function, 指定序列化器, 用于非Python标准类型反序列化
* object_hook: function, 
* parse_float: function, 浮点类型的解析方式, 默认使用`float`, 可以切换成其他类型, 例如`decimal.Decimal`
* parse_int: function, 整形类型的解析方式, 默认使用`int`
* parse_constant: 
* object_pairs_hook: function, 
* \*\*kw: 官方文档指出目前kw未设置任何参数.(2020-08-28, 改版于Python3.6)

#### > load

将文本类型的json数据, 转化为Python基本数据类型.

```Python
def load(fp, *, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
```

* fp: `file-like object`, 文本类型的流对象, 只需含有`read()`方法即可
* 其他方法同上

# 3. 常量