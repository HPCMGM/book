```python
from flask import abort

abort(400)  # 异常抛出
@app.errorhandler(404)  # 异常拦截




from flask import abort

@app.route("/<a>")
def handler(a):
    if a == 0:
        # 抛出异常
        abort(400)
    return "success"

@app.errorhandler(404)
def error(e):
    """异常拦截"""
    return "错误提示信息! %s" % e


```

实例



```python
from flask import Flask, request, make_response, url_for, redirect, abort
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class Regex(BaseConverter):
    def __init__(self, url, *args):
        super().__init__(url)
        self.url = url
        self.regex = args[0]


app.url_map.converters["re"] = Regex


@app.route("/<re(r'\w+'):a>", endpoint="aaa", methods=["GET", "POST", "OPTIONS"])
def index(a):
    print(a)
    print(request.args)
    response = make_response("If you get this page means your service is success!", 400)
    response.headers = {
        "content-type": "text/html; charset=utf-8",
        "Server": "hpcm server"
    }
    return response


@app.route("/buy/<int(2):aa>")
def demo(aa):
    print(aa)
    if aa > 15:
        return redirect("http://www.baidu.com/")
    return redirect(url_for("jd", param=aa))


@app.route("/jd", endpoint="jd")
def demo2():
    return "这里是jd, 传递过来的参数为%s" % request.args.get("param")


@app.errorhandler(404)
def error(e):
    return "错误提示信息! %s" % e


@app.route("/error")
def ab():
    abort(400)


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True, host="0.0.0.0", port=8000)
```

