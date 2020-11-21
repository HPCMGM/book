# 3. 表单操作

## 3.1 模型

### 3.1.1 表单类型

用于表单模型创建

| 字段               | 说明                                    |
| ------------------ | --------------------------------------- |
| StringField        | 文本                                    |
| TextAreaField      | 文本域                                  |
| PasswordField      | 密码框                                  |
| HiddenField        | 隐藏文件字段                            |
| DateField          | 文本字段, 值为 datetime.date文本格式    |
| DateTimeField      | 文本字段, 值为datetime.datetime文本格式 |
| IntegerField       | 文本字段, 值为整数                      |
| DecimalField       | 文本字段, 值为decimal.Decimal           |
| FloatField         | 文本字段, 值为浮点数                    |
| BooleanField       | 复选框, 值为True和False                 |
| RadioField         | 一组单选框                              |
| SelectField        | 下拉列表                                |
| SelectMutipleField | 下拉列表, 可选多个值                    |
| FileField          | 文件上传字段                            |
| FieldList          | 一组指定类型的字段                      |

### 3.1.2 验证类型

用于限制用户对于指定的一些表单类型的数据提交

| 字段                     | 说明                                       |
| ------------------------ | ------------------------------------------ |
| DataRequired             | 非空                                       |
| EqualTo                  | 一致性                                     |
| Length                   | 字符串长度                                 |
| NumberRange              | 数字范围                                   |
| URL                      | 验证URL                                    |
| AnyOf                    | 输入值必须在设置的列表中                   |
| NoneOf                   | 输入信息不能在设置的列表中                 |
| render_kw{"key":"value"} | 使用字典形式传递html属性, 放在validators中 |



### 3.1.3 模型创建

要想创建表单模型, 必须开始app配置中的`SECRET_KEY`

* py文件配置

  ```python
  app.config["SECRET_KEY"] = "xx" # 必须配置私钥
  
  from flask_wtf import FlaskForm
  
  class RegisterForm(FlaskForm):
      """定义form表单类"""
      user_name = StringField(label="用户名: ", validators=[DataRequired("非空判断")])
      password = PasswordField(label="密码: ", validators=[DataRequired("非空判断")])
      rpassword = PasswordField(label="确认密码: ", validators=[DataRequired("非空判断"), EqualTo("password", "两次输入密码不一致")])
      submit = SubmitField(label="提交")
      
  
  from wtforms import From
  class xx(from):
      条件验证
      获取验证结果, 返回布尔类型from.validate()
  ```

  

* html文件配置

  ```python
  <form method="post">  # HTML创建form表单
  {{ form.csrf_token }}  # 在表单中添加CSRF token, 防止表单提交受到网络CSRF攻击
  {{ form.user_name.label }}  # form中的label
  {{ form.user_name }}  # txt文本框// 原理: 创建的实例对象将label参数以继承的方式传递给了Field类, 并重写了__str__魔法方法改为return self(), 直接调用魔法方法__call__, 而call方法返回的是一个浏览器渲染类的方法调用, 这就是为什么user_name.label能获取label的value, 而use_name只能输出txt文本框的原因 
  {% for error in form.user_name.errors %}  # 通过validators的验证后,将所有的错误error都放在了errors中, 所以这里需要循环遍历出error, 而不是在validators中
  {{ error }}
  {% endfor %}
  {{ form.submit }}
  </form>
  ```

  