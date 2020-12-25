# 1. lxml

## 1.1 xpath

xpath返回的永远是`list`



## 1.2 语法

| 表示形式            | 说明                                                 |
| ------------------- | ---------------------------------------------------- |
| nodename            | 选取此节点的所有子节点                               |
| /                   | 从根节点选取                                         |
| //                  | 相对节点选取                                         |
| .                   | 选取当前节点                                         |
| ..                  | 选取上级节点                                         |
|                     |                                                      |
| a                   | 选取  `a`标签                                        |
| a[@class="xx"]      | 选取  携带属性`class="xx"`的a标签                    |
| a/em                | 选取  a标签下的`em`标签                              |
| //a                 | 选取  当前页面的全部`a`标签                          |
| a//em               | 选取  当前页面中 a标签下的任意em标签                 |
| //@href             | 获取所有href属性值                                   |
|                     |                                                      |
| /a/em[1]            | 选取 a中第一个em标签, 按照文档流从上往下数, 只有一个 |
| /a/em[last()]       | 选取a中最后1个em标签                                 |
| /a/em[last()-1]     | 选取a中倒数第2个em标签                               |
| /a/em[position()<3] | 选取a中前2个em标签                                   |
| //a[@xx]            | 选取a中含有自定义属性xx的a标签                       |
| /a/em[bb>20]        | 选取a中em自定义属性  bb > 35 的元素                  |
| /a/em[bb>20]/p      | 选取a中em属性bb>35的p标签                            |
|                     |                                                      |
| *                   | 匹配任意节点                                         |
| @*                  | 匹配任意属性                                         |
| node()              | 统配任意类型的节点                                   |
|                     |                                                      |
| /a/*                | 选取a标签中的所有子标签                              |
| //*                 | 选取文档中的全部标签                                 |
| //a[@*]             | 选取文档中带有属性的a标签                            |
|                     |                                                      |
| //a/em \| //a/p     | 选取a标签中的em和p标签                               |
| //a \| //p          | 选取文档中的a和p标签                                 |
| /a/em/p \| //br     | 选取a标签下的em标签下的p标签或者全局中的br标签       |

## 2.2 运算符

| 表示形式 | 说明 |
| -------- | ---- |
| \|/or    | 或   |
| &/and    | 且   |
| !=       | 非   |
| <        | 小于 |
| >        | 大于 |
| +        | 加   |
| -        | 减   |
| div      | 除   |
| =        | 等   |
| mod      | 取余 |

# 2. XPath

```python
html_obj = etree.parse("test.html")  # 录入html文本
html_obj = etree.HTML(str_content)   # 录入字符串

a_list = html_obj.xpath("//a")  # 获取节点
result = a_list[0].text   # 获取第一个节点的内容
result = a_list[0].tag    # 获取第一个节点标签名(通过属性查找到标签名)

result = etree.tostring   # 修复文档, 补齐缺失的标签
```

**示例**

```python
from lxml import etree
import requests
html = request.get("www.baidu.com").content
html_obj = etree.HTML(html)       # 将html转化成HTML文档对象
url_list = html_obj.xpath("//a/@herf")    # 获取所有文档中的所有a标签中的herf属性, 列表
```

