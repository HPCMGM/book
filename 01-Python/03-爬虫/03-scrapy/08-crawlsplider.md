# 1. crawlspider

* spider 手动解析, 并发送清楚
* crawlspider: 框架进行自动解析和发送请求, 只需要指定爬取规则即可, 专门为整站抓取而设计, 类似flask的路由模式



```python
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

rules = [
    Rule(LinkExtractor(allow=r"Items/"), process_links=func, callback=func, fllow=True),
]
```

## 1.1.  Rule

```python
def __init__(self, link_extractor=None, callback=None, cb_kwargs=None, follow=None, process_links=None, process_request=None):
return rule
```

* link_extractor: `LinkExtractor`, 为正则规则, 
* callback: `func`, 回调函数, 当请求完成后, 会执行此函数对响应数据进行解析, 此函数名称不能为`parse`, 此函数为系统函数.
* cb_kwargs: `kwargs` callback的kwargs参数,
* follow: `bool`, 如果callback非空, allow默认为None, 如果callback为空, allow默认为False
* process_link:`func`, 对url进行预处理的函数
* process_request: ``

## 1.2 LinkExtractor

```python
def __init__(self, allow=(), deny=(), allow_domains=(), deny_domains=(), restrict_xpaths=(),
                 tags=('a', 'area'), attrs=('href',), canonicalize=False,
                 unique=True, process_value=None, deny_extensions=None, restrict_css=(),
                 strip=True, restrict_text=None):
```

* allow: `str/list`, 允许的正则规则, 支持一个或多个
* deny: `str/list`, 过滤的正则规则, 优先执行allow, 其次为deny, 支持一个或多个
* allow_domains: `str/list`, 允许访问的域名, 支持一个或多个
* restrict_xpaths: `str/list`, xpath提取, 支持一个或多个
* tags: `str/list`, 提取标签, 支持一个或者多个

```python
创建规则: link = LinkExtractor(allow=(r"xxx"))
            过滤: link.extract_links(response)
```

