# PyMySQL

python调用mysql的驱动.

# HelloWorld

示例一

```python
import pymysql
con = pymysql.connect(
    host="192.168.190.128",
    port=3306,
    user="root",
    password="dong10",
    database="db_name",
    charset="utf8"
)					# 连接数据库
cor = con.cursor()  # 获取游标
cor.execute(sql)    # 执行语句
cor.fetchall()      # 获取执行结果
cor.close()			# 关闭游标
con.close()			# 关闭数据库连接
```



