# 1. JWT

Json web token. 代替Session来进行身份验证的认证机制

django-framework也带有其他鉴权的接口. 

## 1.1 安装

```bash
pip install djangorestframework-jwt
```



## 1.2 特点

session:

* 保存在服务器中, 占用内存空间
* 使用分布式服务器, 不能获取到另一个服务器中的session
* session 的令牌储存于cookie中, 容易被截获, 安全性稍差

jwt:

* 构成简单, 不占用服务器空间, 便于传输
* 不需要保存回话, 易于拓展, 签发完成即可在任意服务器上使用
* 签发证书为一次性的, 相对安全

使用jwt的服务器, 需要支持跨域策略. 因为浏览器需要把token保存在请求头中发送给服务器. 所以cors需要支持`Access-Control-Origin: *`

注:

* jwt不是Python特有功能, 它支持各种语言(Java, JavaScript, NodeJS, PHP等)

## 1.3 JWT构造

### 1.3.1 header

```python
import json
import base64

header_data = {
    "type": "JWT",  # 声明类型
    "alg": "HS256"  # 声明使用的加密算法为HMAC SHA256
}
header = base64.b64encode(json.dumps(header_data).encode()).decode()
```

将其采用base64编码后, 组成第一部分

### 1.3.2 payload

一般payload中包含(建议但不强制):

* iss: jwt签发者
* sub: jwt所面向的用户
* aud: 接受jwt的一方
* exp: jwt过期时间, 这个时间要大于签发时间
* nbf: 定义jwt的启用时间
* iat: jwt的签发时间
* jti: jwt的唯一身份表示. 主要用作一次性token. 从而回避重放攻击

实例:

```python
import json
import base64

payload_data = {
    "sub": "Python",
    "name": "hpcm",
    "admin": True
}
payload = base64.b64encode(json.dumps(payload_data).encode()).decode()
```

将其采用base64编码后, 作为第二部分

### 1.3.3 signature

1. 将base64编码后的header + `.` + base64编码后的payload连接成字符串`string`

2. 使用header中声明的加密方式开始加盐加密

   ```Python
   import hashlib
   import base64
   
   encrypt = hashlib.pbkdf2_hmac("sha256", "string".encode(), salt="secret_key".encode(), iterations=1)
   signature = base64.b64encode(encrypt).decode()
   ```

最终第三部分为加密后的signature

### 1.3.4 组合

将三部分组合在一起即为jwt完整的token

```python
token = header + "." + payload + signature
```



# 2. JWT配置

## 2.1 setting 配置

```Python
# 配置rest-framework jwt验证
REST_FRAMEWORK = {  # 设置验证
    "DEFAULT_AUTHENTICATION_CLASS": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",  # 优先验证
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    )
}

# 配置jwt的有效期
import datetime
JWT_AUTH = {
    "JWT_EXPITATION_DELTA": datetime.timedelta(days=1),  # 设置有效期为一天
}
```

## 2.2 登录验证

### 2.2.1 前端传入配置

header中增加键值对: 

Authorzation: Bearner+token

即:

```javascript
fetch("api/user/1", {
    header: {
        "Authorization": "Bearner" + token
    }
})
```

### 2.2.2 JWT后台校验

jwt自带校验功能, 只需要插入指定url

```Python
url(r"auths/", obtain_jwt_token, name = "auths")
```

## 2.3 自定义校验

### 2.3.1 生成token

```python
def make_token(user):
    """给用户创建token"""
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token
```



### 2.3.2 校验token

```python
def jwt_response_payload_hander(token, user=None, request=None):
    """重写这个方法"""
    return {
        "token": token,
        "user_id": user.id,
        "username": user.username
    }
```

修改setting校验配置:

```python
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'utils.users.jwt_response_payload_handler',
}
```

其他不变即可

# 3. 安全说明

* 不得在jwt的header和payload放入敏感数据, 此部分数据可以被解密
* 不得泄露secret私钥, 对于整个项目极为重要
* 如果可以, 请使用https协议