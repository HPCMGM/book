# model数据加密

数据先加密再入库

```python
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    # 利用私有属性, 让外界无法访问
    _password = Colnumn("password", String(128))

    # 设置password为数据库字段名
    # 自动向模型对象中添加数据
    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict:
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)

    @property
    def password(self):
        return self._password

    # 通过装饰连接外部password
    @password.setter
    def password(self, password)
        # 设置password前进行加密
        self._password = generate_password_hash(password)

    def check_password(self, password):
        # 自动加密并以password和数据库中密码做校验, 返回布尔值
        return check_password_hash(self._password, password)
```

