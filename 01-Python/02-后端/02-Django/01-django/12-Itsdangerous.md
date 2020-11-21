# 1. itesdangerous

主要用于加密的工具, 类似jwt.

## 1.1 安装

```bash
pip install itsdangerous
```

## 1.2 特点

与jwt相比, 可以对加密的token设置有效期, 其他都和jwt类似.

# 2. 配置

## 2.1 配置加密器

```python
from itsdanger import TimeJSONWebSignatureSerializer as Ser
# 实例化加密器: 可设置秘钥, 时间
ser = Ser(secret_key, expires=3600)  # 这里使用的为setting中的secret_key
```

## 2.2 加密内容

```python
# 加密数据, 返回的为二进制数据:
bytes_data = ser.dumps({"openid": openid})
encode_data = dytes_data.decode()
```

## 2.3 解密内容

```python
decode_data = ser.loads(encode_data)
```

## 2.4 常见异常

| 异常                            | 说明        |
| ------------------------------- | ----------- |
| `itsdangerous.SignatureExpired` | token过期   |
| `itsdangerous.BadSignature`     | token被修改 |
|                                 |             |









