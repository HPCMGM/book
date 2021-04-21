```python
# 可以自行多次
def process_item(self, item, spider):
    return item
```

重写管道, 用来保存图片

```python
def get_media_requests(self, item, info):
    yield scrapy.Request(item["image_url"])
    
def get_completed(self, results, item, info):
    old_name = IMAGES_STORE + [x["path"] for ok, x in results if ok]
    new_name = IMAGES_STORE + item["nick_name"] + ".jpg"
    item["image_path"] = new_name
    os.rename(old_name, new_name)
    return item
```

