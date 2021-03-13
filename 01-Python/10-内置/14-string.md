# 1. 占位符

## 1.1 单个对象

```python
formatter = string.Formatter()
s1 = "aa{test.name}cc"
s2 = "aa{test.name!s:}cc"
s3 = "aa{test.name!r:}cc"
s4 = "aa{test.name!s:^8}cc"
s5 = "aa{test.name!s:#^8}cc"

Test = type("Test", (), {"name": "bb"})
test = Test()
string.Formatter().format(s1, test=test)    # 'aabbcc'
string.Formatter().format(s2, test=test)    # "aabbcc"
string.Formatter().format(s3, test=test)    # "aa'bb'cc"
string.Formatter().format(s4, test=test)    # 'aa   bb   cc'
string.Formatter().format(s5, test=test)    # 'aa###bb###cc'
```

## 1.2 多个对象

```python
Test = type("Test", (), {"name": "ww"})
test1, test2 = Test(), Test()
test2.name = "ss"
s = "aaaa{0.name!r:#^8}bb{1.name!r:@^8}bb{test.name!s:%^8}ccc"
string.Formatter().vformat(s, (test1, test2), {"test": test1})

输出: "aaaa##'ww'##bb@@'ss'@@bb%%%ww%%%ccc"
```

# 2. 模板操作

## 2.1 substitute

```python
substitute(*args, **kwargs):  # *args 不能传递参数, 内部传递self用的

t = string.Template("$who is ${name}\$${age}")
t.substitute(who="name", name="ss", age="aaa")

输出: 'name is ss\\${age}'
```

## 2.2 safe_substitute

```python
safe_substitute(*args, **kwargs):  # 使用方法和substitute, 但是没有参数它不会出错

t = string.Template("$who is ${name}\$${age}")
t.safe_substitute(who="name")

输出: 'name is ${name}\\${age}'    # 没有提供name参数不会报错
```

# 3. 常量

```python
ascii_letters						大小a-z
ascii_lowercase						a-z
ascii_uppercase						A-Z
digits						        0-9
hexdigits						    0-9 + a-f + A-F
octdigits						    0-7
punctuation						    符号
whitespace                          
printable                           全部
```

# 4. 函数

```python
capwords(str, sep): 以sep为分割的每个字符变大写

string.capwords("aaa bbb ccc, ddd eee", sep=" ")    # 'Aaa Bbb Ccc, Ddd Eee'
```

