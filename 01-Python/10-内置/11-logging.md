# 1. 日志等级

## 1.1 日志等级

| 等级     | 数字 | 说明                                                       |
| -------- | ---- | ---------------------------------------------------------- |
| FATAL    | 60   | 系统异常, 例如: 系统奔溃.                                  |
| CRITICAL | 50   | 系统资源不足导致, 例如: 内存耗尽, 磁盘空间不足. 一般很少用 |
| ERROR    | 40   | 程序未按照预定运行, 发生错误.                              |
| WARNING  | 30   | 发生错误, 是人为因素导致错误. 如: 用户未按照指定信息输入   |
| INFO     | 20   | 日常请求及流程日志保留                                     |
| DEBUG    | 10   | 调试日志输出模式                                           |
| NOTSET   | 0    | 日志全部输出                                               |
* 开发或部署环境时是用`DEBUG`/`INFO`
* 应用上线时是用`WARNING`/`ERROR`/`CRITICAL`的级别来降低`I/O`压力和提高获取错误日志的效率

# 2. 日志配置

## 2.1 日志输出占位符


| 占位符           | 说明                                                     |
| ---------------- | -------------------------------------------------------- |
| `%(levelno)s`    | 日志级别数字(0/10/20/30/40/50)                           |
| `%(levelname)s`  | 日志级别的名称(NOTST/DEBUG/INFO/WARNGING/ERROR/CRITICAL) |
| `%(pathname)s`   | 输出函数所在目录, 相对路径                               |
| `%(filename)s`   | 输出函数所在文件名称                                     |
| `%(funcName)s`   | 当前函数名称                                             |
| `%(lineno)d`     | 当前所在行数                                             |
| `%(asctime)s`    | 当前时间                                                 |
| `%(thread)d`     | 线程id                                                   |
| `%(threadName)s` | 线程名称                                                 |
| `%(process)d`    | 进程号                                                   |
| `%(message)s`    | 日志信息                                                 |
## 2.2 日志处理器

| 处理器                | 作用                                       |
| --------------------- | ------------------------------------------ |
| `StreamHandler`       | 输出到流, 例如: `sys.stderr`, `sys.stdout` |
| `FileHandler`         | 输出到文件                                 |
| `BaseRotatingHandler` | 基本日志滚动                               |
| `RotatingHandler`     | 可设置日志量最大值的日志滚动               |
| `TimeRotatingHandler` | 可设置定时日志滚动                         |
| `SocketHandler`       | 远程(TCP/IP)日志记录                       |
| `DatagramHandler`     | 远程(UDP)日志记录                          |
| `SMTPHandler`         | 远程(SMTP)日志记录                         |
| `NTEventLogHandler`   | 远程(windows NT/ 2000/XP 事件)日志记录     |
| `HTTPHandler`         | 远程(HTTP的GET/POST)日志记录               |
| `SysLogHandler`       | 输出到系统日志中                           |
| `MemoryHandler`       | 输出到指定内存buffer中                     |



## 2.3 日志配置

### 2.3.1 普通配置

```Python
import logging
from logging.handlers import RotatingFileHandler


logging.basicConfig(level=logging.INFO)                                                          # 配置等级
file_handler = RotatingFileHandler("logs/run.log", maxBytes=1024 * 1024 * 100, backupCount=10)   # 配置文件路径/大小/数量
format_log = logging.Formatter("[%(levelname).4s] %(asctime)s P_%(process)d_T_%(thread)d <%(module)s:%(lineno)d>: %(message)s")# 配置输出格式
file_handler.setFormatter(format_log)                                                            # 载入输出格式
console = logging.StreamHandler()                                                                # 配置终端输出
console.setFormatter(format_log)                                                                 # 载入输出格式
logging.getLogger().addHandler(file_handler)                                                     # 配置到全局
logging.getLogger().addHandler(console)

# logging.config.dictConfig(LOGGING)
# logger = logging.getLogger("django")

logging.info("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info log.")
logging.log(logging.WARNING, "This is a warning log.")
logging.log(logging.ERROR, "This is a error log.")
logging.log(logging.CRITICAL, "This is a critical log.")
```

### 2.3.2 字典配置

```Python
import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(levelname).4s] %(asctime)s P_%(process)d_T_%(thread)d <%(module)s:%(lineno)d>: %(message)s"
        },
        'simple': {
            'format': "[%(levelname).4s] %(asctime)s P_%(process)d_T_%(thread)d <%(module)s:%(lineno)d>: %(message)s"
        },
    },
    # 'filters': {
    #     'require_debug_true': {
    #         '()': 'django.utils.log.RequireDebugTrue',
    #     },
    # },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            "stream": "ext://sys.stdout",
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "logs/running.log",  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            "level": "INFO",
            'handlers': ['console', 'file'],
            'propagate': True,
        },
    }
}
logging.config.dictConfig(LOGGING)
logger = logging.getLogger("django")

logger.info("This is a debug log.")
logger.info("This is a info log.")
logger.warning("This is a warning log.")
logger.error("This is a error log.")
logger.critical("This is a critical log.")

logger.log(logging.DEBUG, "This is a debug log.")
logger.log(logging.INFO, "This is a info log.")
logger.log(logging.WARNING, "This is a warning log.")
logger.log(logging.ERROR, "This is a error log.")
logger.log(logging.CRITICAL, "This is a critical log.")
```