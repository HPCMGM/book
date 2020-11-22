# 1. 示例

```python
import csv
import logging

import cx_Oracle

from common.pycrypt import crypt

logger = logging.getLogger("info")


class Oracle(object):
    """oracle管理器"""

    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        try:
            self.password = crypt.decrypt(password)
        except Exception as e:
            logger.error(e)
            logger.info("password decrypt error!")
            exit(0)
        self.database = database
        self.ora = None
        self.cur = None

    def check_status(self, sql=None, assert_status=None):
        """执行状态监测"""
        if not [sql, assert_status]:
            return True
        try:
            self.cur.execute(sql)
        except Exception as e:
            logger.exception(e)
            return False
        if str(self.cur.fetchall()[0][0]) == assert_status:
            return True
        else:
            return False

    def to_csv_content(self, file_name, encode="gbk"):
        """将数据转换为csv格式"""
        csv_list = [[]]
        for i in self.cur.description:
            csv_list[0].append(i[0])
        for i in self.cur.fetchall():
            csv_list.append(i)
        with open(file_name, "w+", encoding=encode) as f:
            csv_obj = csv.writer(f)
            csv_obj.writerows(csv_list)
            logger.info("save file: {}".format(file_name))

    def execute_file(self, file_name, format_str=""):
        """执行文件内部sql语句"""
        with open(file_name, "r", encoding="utf-8") as f:
            sql = f.read()
        if format_str and "{}" in sql:
            sql = sql.format(format_str)
        self.cur.execute(sql)

    def __enter__(self):
        self.ora = cx_Oracle.connect(
            "{}/{}@{}:{}/{}".format(self.username, self.password, self.host, self.port, self.database),
            encoding="utf-8")
        self.cur = self.ora.cursor()
        logger.info("oracle {} connect success!".format(self.host))
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info("oracle {} connect close!".format(self.host))
        self.close()

    def close(self):
        self.cur.close()
        self.ora.close()

```

# 2. 示例

```python
# -*- coding: utf-8 -*-
# author:HPCM
# datetime:2019/8/22 9:16
import os
import csv
import logging
from datetime import datetime, timedelta

import cx_Oracle

from config import constants, conf, SettingLogging
from config.load import load_path
from common import holiday

SettingLogging().set_logger()

logger = logging.getLogger("info")


class Oracle(object):
    """oracle管理器"""

    def __init__(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.ora = None
        self.cur = None

    def __enter__(self):
        self.ora = cx_Oracle.connect(
            "{}/{}@{}:{}/{}".format(self.username, self.password, self.host, self.port, self.database),
            encoding="utf-8")
        self.cur = self.ora.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.cur.close()
        self.ora.close()


class GetDataMakeCSV(object):
    """获取数据生成csv"""

    def __init__(self, host=None, port=None, username=None, password=None, database=None):
        self.host = host or constants.ORACLE_HOST
        self.port = port or constants.ORACLE_PORT
        self.username = username or constants.ORACLE_USERNAME
        self.password = password or constants.ORACLE_PASSWORD
        self.database = database or constants.ORACLE_DATABASE
        self.current_time = datetime.now()
        self.start_time_str = None
        self.end_time_str = None
        self.save_file = None

    def start(self):
        """主控启动器"""
        self.set_time()
        self.get_data_save_csv()

    def set_time(self):
        """配置起始时间"""
        if constants.BEFORE_DAY > 0:
            self.current_time = (self.current_time - timedelta(days=constants.BEFORE_DAY))
        if not holiday.is_holiday(self.current_time) is True:
            logger.info("{} is holiday!".format(self.current_time))
            exit(0)
        i = 1
        while True:
            current_time = self.current_time - timedelta(days=i)
            if holiday.is_holiday(current_time) is not True:
                if self.end_time_str is None:
                    self.end_time_str = current_time.strftime("%Y%m%d")
                else:
                    self.start_time_str = current_time.strftime("%Y%m%d")
            if all([self.start_time_str, self.end_time_str]):
                break
            else:
                i += 1
        logger.info("start: {}, end: {}".format(self.start_time_str, self.end_time_str))

    def get_data_save_csv(self):
        """获取并生成文件"""
        lp = load_path.LoadPath(conf.BASE_DIR)
        sql_file_name = lp.absolute_path(os.path.join(conf.CONFIG_SQL_PATH, constants.JDC_SQL_NAME))
        save_file_name = lp.absolute_path(os.path.join(conf.CONFIG_CSV_SAVE_PATH, constants.JDC_SAVE_NAME))
        with open(sql_file_name, "r", encoding="utf-8") as f:
            sql = f.read()
        sql = sql.format(**{"start": self.start_time_str, "end": self.end_time_str})
        save_file_name = save_file_name.format(**{"start": self.start_time_str, "end": self.end_time_str})
        logger.info(sql)
        logger.info("will save: {}".format(save_file_name))
        csv_list = [[]]
        with Oracle(self.host, self.port, self.username, self.password, self.database) as cur:
            try:
                cur.execute(sql)
            except Exception as e:
                logger.info("SQL execute failed! sql: {}, error message: {}".format(sql, e))
            for i in cur.description:
                csv_list[0].append(i[0])
            for i in cur.fetchall():
                csv_list.append(i)
            logger.info("execute {} success!".format(sql_file_name))
        save_file_name = save_file_name.format(self.current_time.strftime("%Y%m%d"))
        logger.info("write file: {}".format(save_file_name))
        with open(save_file_name, "w+", encoding="gbk") as f:
            csv_obj = csv.writer(f)
            csv_obj.writerows(csv_list)
        self.save_file = save_file_name
        logger.info("file {} save success!".format(save_file_name))


if __name__ == '__main__':
    gdc = GetDataMakeCSV()
    gdc.start()
```

