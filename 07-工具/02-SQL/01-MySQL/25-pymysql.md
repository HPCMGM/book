# 示例

```python
import pymysql


class Mysql(object):
    def __init__(self):
        self.con = None
        self.cur = None
        self.cur_dict = None

    def __enter__(self):
        self.con = pymysql.connect(
            host="192.168.190.128",
            port=3306,
            user="root",
            password="dong10",
            database="db_name",
            charset="utf8"
        )
        self.cur = self.con.cursor()
        self.cur.cur_dict = self.con.cursor(cursor=pymysql.cursors.DictCursor)
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.cur.close()
            self.con.close()
        except pymysql.err.Error:
            pass


class ExeSql(object):
    def __init__(self):
        self.cur = None
        self.effect_row = None

    def get_dict(self, sql, sql_format=None):
        with Mysql() as cur:
            self.cur = cur.cur_dict
            return self.result(sql, sql_format)

    def get(self, sql, sql_format=None):
        with Mysql() as self.cur:
            return self.result(sql, sql_format)

    def result(self, sql, sql_format):
        self.effect_row = self.cur.execute(sql, sql_format)
        if not self.effect_row:
            return None
        return self.cur.fetchall()


cor = ExeSql()
# noinspection SqlDialectInspection
c = cor.get_dict("select * from tb_name where id > %s", [5])
print(c)
```

