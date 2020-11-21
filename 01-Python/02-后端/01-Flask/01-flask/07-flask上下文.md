# 1. flask上下文

flask中的request只能应用于request当前请求的对象的上下文环境中(理解成全局变量，在视图函数中直接使用可以取到当前本次请求)

其中存在于上下文中的变量有: `current_app`, `request`, `session`, `g`

如果是用户发送请求时, Flask会自动将上下文环境对象压入栈中, 如果是自己手动调用, 则不会, 在调用以上变量时:
首先会获取栈顶的上下文环境对象, 并把上下文环境对象转化为app对象, 如果没有将上下文环境对象压栈时, 会抛出异常.

![image-20200528234957942](07-flask%E4%B8%8A%E4%B8%8B%E6%96%87.assets/image-20200528234957942.png)

# 2. 解决

在非上下文环境要想使用该对象, 必须手动压栈

```python
from flask import Flask, current_app
app = Flask(__name__)
ctx = app.app_context()   # 获取app的上下文环境对象
ctx.push()                # 手动压栈
print(current_app.config["DEBUG"])  # 成功获取app配置信息
ctx.pop()                 # 出栈  需要保证完整的上下文环境
```

