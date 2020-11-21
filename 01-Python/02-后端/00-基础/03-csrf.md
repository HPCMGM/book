# 1. CSRF

CSRF(Cross Site Request Forgery), 跨站请求伪造. 

## 1.1 攻击原理

* client正常登陆后, 官方服务器配置cookie给client
* 在未销毁cookie情况下(一般是未关闭此页面), 用户访问钓鱼服务器
* 钓鱼服务器会诱导重定向到官方服务器的某个需要的页面. 此时client会携带完整的用户cookie信息, 服务器会认为是合法操作. 导致个人隐私泄露以及财产安全。

![img](01-CSRF.assets/CSRF%E6%94%BB%E5%87%BB%E8%BF%87%E7%A8%8B.png)
## 1.2 防范原理

使用CSRF进行防范, 原理:

* 官方服务端发送给client cookie时, 同时发送csrf_token字段
* 官方服务端在提供给client所有form表单等提交时, 都必须配置csrf_token字段
* 当form表单提交后, 通过获取cookie中的csrf_token与表单提交的csrf_token对比验证是否合法

注意:

* 由于浏览器是隔离每个服务器的cookie的, 一个钓鱼网站所以无法获取其他网站的cookie, 重定向可以使用cookie但是不能获取它的值
* 所以在对比表单中的csrf_token与cookie中的csrf_token是不一致的

# 2. 测试

## 2.1 攻击实现

### 2.1.1 官方

* web

  ```python
  from flask import Flask, render_template, make_response
  from flask import redirect
  from flask import request
  from flask import url_for
  
  app = Flask(__name__)
  
  
  @app.route('/', methods=["POST", "GET"])
  def index():
      if request.method == "POST":
          # 取到表单中提交上来的参数
          username = request.form.get("username")
          password = request.form.get("password")
  
          if not all([username, password]):
              print('参数错误')
          else:
              print(username, password)
              if username == 'laowang' and password == '1234':
                  # 状态保持，设置用户名到cookie中表示登录成功
                  response = redirect(url_for('transfer'))
                  response.set_cookie('username', username)
                  return response
              else:
                  print('密码错误')
  
      return render_template('login.html')
  
  
  @app.route('/transfer', methods=["POST", "GET"])
  def transfer():
      # 从cookie中取到用户名
      username = request.cookies.get('username', None)
      # 如果没有取到，代表没有登录
      if not username:
          return redirect(url_for('index'))
  
      if request.method == "POST":
          to_account = request.form.get("to_account")
          money = request.form.get("money")
          print('假装执行转操作，将当前登录用户的钱转账到指定账户')
          return '转账 %s 元到 %s 成功' % (money, to_account)
  
      # 渲染转换页面
      response = make_response(render_template('transfer.html'))
      return response
  
  if __name__ == '__main__':
      app.run(debug=True, port=9000)
  ```

* html

  * 登录html

    ```python
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>登录</title>
    </head>
    <body>
    
    <h1>我是网站A，登录页面</h1>
    
    <form method="post">
        <label>用户名：</label><input type="text" name="username" placeholder="请输入用户名"><br/>
        <label>密码：</label><input type="password" name="password" placeholder="请输入密码"><br/>
        <input type="submit" value="登录">
    </form>
    
    </body>
    </html>
    ```

  * 转账html

    ```python
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>转账</title>
    </head>
    <body>
    <h1>我是网站A，转账页面</h1>
    
    <form method="post">
        <label>账户：</label><input type="text" name="to_account" placeholder="请输入要转账的账户"><br/>
        <label>金额：</label><input type="number" name="money" placeholder="请输入转账金额"><br/>
        <input type="submit" value="转账">
    </form>
    
    </body>
    </html>
    ```

    

### 2.1.2 hack

* web

  ```python
  from flask import Flask
  from flask import render_template
  
  app = Flask(__name__)
  
  @app.route('/')
  def index():
      return render_template('hack_index.html')
  
  if __name__ == '__main__':
      app.run(debug=True, port=8000)
  ```

  

* html

  ```python
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
  </head>
  <body>
  
  <h1>我是网站B</h1>
  
  <form method="post" action="http://127.0.0.1:9000/transfer">
      <input type="hidden" name="to_account" value="999999">
      <input type="hidden" name="money" value="190000" hidden>
      <input type="submit" value="点击领取优惠券">
  </form>
  
  </body>
  </html>
  ```

  

## 2.2 防范实现

### 2.2.1 官方

* web修改

  ```python
  @app.route('/', methods=["POST", "GET"])
  def index():
      if request.method == "POST":
          # 取到表单中提交上来的参数
          username = request.form.get("username")
          password = request.form.get("password")
  
          if not all([username, password]):
              print('参数错误')
          else:
              print(username, password)
              if username == 'user' and password == 'pwd':
                  # 状态保持，设置用户名到cookie中表示登录成功
                  response = redirect(url_for('transfer'))
                  response.set_cookie('username', username)
                  return response
              else:
                  print('密码错误')
  
      return render_template('temp_login.html')
  
  
  @app.route('/transfer', methods=["POST", "GET"])
  def transfer():
      # 从cookie中取到用户名
      username = request.cookies.get('username', None)
      # 如果没有取到，代表没有登录
      if username is None:
          return redirect(url_for('index'))
  
      if request.method == "POST":
          to_account = request.form.get("to_account")
          money = request.form.get("money")
          # 取出表单中的 csrf_token
          form_csrf_token = request.form.get("csrf_token")
          print(form_csrf_token)
          # 取出 cookie 中的 csrf_token
          cookie_csrf_token = request.cookies.get("csrf_token")
          print(cookie_csrf_token)
          # 进行对比
          if cookie_csrf_token != form_csrf_token:
              return 'token校验失败，可能是非法操作'
          print('假装执行转操作，将当前登录用户的钱转账到指定账户')
          return '转账 %s 元到 %s 成功' % (money, to_account)
  
      # 生成 csrf_token 的值
      csrf_token = generate_csrf()
  
      # 渲染转换页面，传入 csrf_token 到模板中
      response = make_response(render_template('temp_transfer.html', csrf_token=csrf_token))
      # 设置csrf_token到cookie中，用于提交校验
      response.set_cookie('csrf_token', csrf_token)
      return response
  
  
  if __name__ == '__main__':
      app.run(host="0.0.0.0", port=5001)
  ```

  

* html增加

  ```python
  <form method="post">
      <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
      <label>账户：</label><input type="text" name="to_account" placeholder="请输入要转账的账户"><br/>
      <label>金额：</label><input type="number" name="money" placeholder="请输入转账金额"><br/>
      <input type="submit" value="转账">
  </form>
  ```

  

### 2.2.2 hack

不论是否增加csrf_token字段, 都无法访问.





