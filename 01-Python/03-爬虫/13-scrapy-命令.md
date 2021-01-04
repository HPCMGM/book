# 1. scrapy

## 1.1 bench

快速测试

## 1.2 fetch

快速抓取页面

## 1.3 genspider

创建爬虫

```python
scrapy genspider aa bb.com
```

* 创建aa爬虫, 并限制爬取域名必须为bb.com

## 1.4 runspider

运行爬虫

```python
scrapy runspider xx.py
```

* 指定运行爬虫文件xx.py

## 1.5 settings

获取配置数据

## 1.6 shell

交互式shell

## 1.7 startproject

创建爬虫项目

```python
scrapy startproject xx
```

* 创建xx项目

## 1.8 view

打开浏览器访问

```python
scrapy crawl test -o test.json
```

* 指定运行爬虫名称 test, 并按照指定格式保存