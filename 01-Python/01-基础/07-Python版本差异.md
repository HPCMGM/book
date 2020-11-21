# 1. 编码

## 1.1 编码类型

计算机存储单位换算:

```bash
8bits-->1024bytes->1024kb-->1024MB-->1GB
位        字节
```

编码类型

| 序号 | 类型    | 说明                                                  |
| ---- | ------- | ----------------------------------------------------- |
| 1    | ASCII   | 最初保存英文文字的码表, 一共127位, 1个字节            |
| 2    | Unicode | 万国码, 所有国家的编码都能解析 2个字节(生僻字4个字节) |
| 3    | UTF-8   | Unicode转化的, 长度可变 3个字节(生僻字4-6个字节)      |
| 4    | GBK     | 2个字节和Unicode编码不一致                            |

## 1.2 Python编码

### 1.2.1 各版本编码

Python2

> linux: utf-8
>
> windows: gbk

Python3

> 均为: Unicode

IPython

>均为: utf-8

### 1.2.1 编码转换

<table>
    <tr>
        <th>序号</th>
        <th>编码</th>
        <th>Python</th>
        <th>类型</th>
        <th>转码</th>
    </tr>
    <tr>
        <td rowspan="2">1</td>
        <td rowspan="2">str</td>
        <td>Python2</td>
        <td>二进制字符串, 通过Unicode转化的</td>
        <td>只能decode</td>
    </tr>
    <tr>
        <td>Python3</td>
        <td>Unicode形式, 字符串</td>
        <td>只能encode</td>
    </tr>
    <tr>
        <td rowspan="2">2</td>
        <td rowspan="2">byte</td>
        <td>Python2</td>
        <td>Unicode, 网络中获取到的数据类型</td>
        <td>只能encode</td>
    </tr>
    <tr>
        <td>Python3</td>
        <td>二进制</td>
        <td>只能decode</td>
    </tr>
</table>

# 2. 语法

| 序号 | 项目     | Python2                          | Python3         |
| ---- | -------- | -------------------------------- | --------------- |
| 1    | chatset  | `ASCII`不支持                    | `utf-8`         |
| 2    | str表现  | 二进制字符串                     | 字符串          |
| 3    | byte表现 | `Unicode`                        | 二进制字符      |
| 4    | 整形     | `long`, `int`                    | `int`           |
| 5    | print    | `print()`, `print ""`            | `print()`       |
| 6    | 输入     | `raw_input`自动识别类型, `input` | `input`         |
| 7    | 内置模块 | urllib, urllib.request           | urllib2, urllib |

