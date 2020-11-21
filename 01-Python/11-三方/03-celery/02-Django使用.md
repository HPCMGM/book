# 1. 配置

## 1.1 写入配置

```python
# celery_tasks/config.py
broker_url = "redis://127.0.0.1/14"
result_backend = "redis://127.0.0.1/15"
SELERY_IMPORTS = {
    "celery_tasks.sms.aaa"  # 重新指定文件名
}
```



## 1.2 读取配置

```python
# celery_tasks/main.py
import django
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
django.setup()  # 读取django的运行环境

app = Celery("celery_tasks")
app.config_from_object("celery_tasks.config")
app.autodiscover_tasks(["celery_tasks.sms"])  # 自动添加任务
```

## 1.3 运行worker

```python
celery -A celery_tasks worker -l info
```

* -A:

  -A 表示读取celery_tasks.celery.py中的app, 如果需要重新指定的话, 可以直接指定到对应的文件: 

  ```python
  celery -A celery_task.main worker -l info
  ```