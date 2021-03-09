# 1. beautifulsoup4

## 1.1 安装

```python
pip install beautifulsoup4
```

## 1.2 使用

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "lxml")                  # 获取html数据  制定解析器名字lxml
soup = BeautifulSoup(open("index.html"), "lxml")    # 获取文件数据
soup.prettify()      # 格式化输出对象内容
soup.a.contents      # 子标签a以列表形式输入
soup.a.children      # 子标签a以生成器形式输出
soup.a.descendants   # 递归子标签a以生成器形式输出

############## 标签操作 ##################
soup.title           # 获取title标签
soup.head            # 获取head标签
soup.name            # 获取标签名
soup.p.attrs         # 获取p标签中的属性
soup.p.get("href")   # 获取p标签中的href属性
soup.p["class"]      # 获取p中的class名
# soup.p.get("class")
soup.p["class"]="xx" # 修改class名
del soup.p["class"]  # 删除属性

############## 文本操作 ##################
soup.p.string        # 获取文本数据, 不包括注释数据
soup.p.get_text()
```

## 1.3 文档树

#### > find_all

```python
def find_all(name, attrs, recursive, text, **kwargs):
return soup
```

* name: `str`, 标签名称, 支持正则`re.compile("^b")`, 多个标签以列表形式传入
* attrs: `str`, 属性选择
* text: `str`, 搜索内容中包含text的标签, 可以传入列表, 正则
* kwargs: 
  * class_ = "sister"
  * id="link2"

#### > find

类似find_all, 选择第一个.

```python
soup.find()  # 查找网页中第一个符合匹配的结果
soup.find("a", {"class" : "link"}).get_text()   # .string
soup.find("a", {"class" : "link"}).get("href")  # .attrs["href"]

soup.find_all() # 查找网页中所有符合匹配的结果列表
soup.find_all("a", {"class" : "link"})[0].get_text()  # .string
soup.find_all("a", {"class" : "link"})[0].get("href")  # .attrs["href"]
```

#### > select

````python
soup.select("title")          # 选择title标签
soup.select(".t")             # 选择class = "t"的标签
soup.select("#t")             # 选择id = "t"的标签
soup.select("p #t")           # 选择p中id = "t"的标签
soup.select("p > a")          # 选择p中的a标签
soup.select("a[class=\"s\"]") # 选择a中class = "s"的标签
soup.select()# 查找网页中所有符合匹配的结果列表 （使用CSS Selector语法）
soup.select(".link")[0].get_text()             # .string
soup.select("a[class='link']")[0].get("href")   # .attrs["href"]
````

