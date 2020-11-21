```python

from flask import make_response, jsonify, json

# -----------方法一------------------------------------------------
response = make_response("content", status_code)
response.headers = {  # 
                "content-type": "text/html; charset=utf-8"/"application/json",
                # 浏览器需要以哪种格式格式解读
                "location": "www.baidu.com"  # 重定向
            }
# -----------方法二------------------------------------------------
return content, status_code, headers

# -----------json数据----------------------------------------------
@app.route("/")
def index():
    data = {
        name: "xxx",
        age: "xx"
    }  # 发给客户端的字典
    return jsonify(data)   # Context-Type: application/json

@app.route("/")
def index():
    date = {xx}
    return json.dumps(data) # context-Type: text/html







@app.route("/")
def index():
    response = make_response("aaaaaaaaaaaaaaaaa", 400)
    response.headers = {
        "content-type": "text/html; charset=utf-8",
        "Server": "hpcm server"
    }
    return response
```

