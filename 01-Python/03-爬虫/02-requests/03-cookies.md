```python
import requests
post_url = "http://www.baidu.com/login"
headers = {"User-Agent": "xxx"}
forn_dict = {
    "user_name": "xxx",
    "password": "xxx"
}
# 实例化session进行cookie的自动保存
send = requests.session()
# 获取到cookie自动保存, 这里不接受返回数据
send.post(post_url, headers=headers, data=form_dict)
# 获取其他页面的数据
response = send.get(url, headers=headers)
with open("test2.html", "w") as f:
    f.write(response.content)
```

