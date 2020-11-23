作用: 

* 分离celery任务, 让指定的队列执行指定的任务

#### 配置信息

```python
CELERY_IMPORTS = {
    "celery_tasks.tasks.notify.tasks",
    "celery_tasks.tasks.kernel.tasks",
    "celery_tasks.tasks.docker.tasks",
    "celery_tasks.tasks.hotfix.tasks"
}

if settings.DEBUG is True:
    CELERY_IMPORTS.add("celery_tasks.tasks.test.tasks")

CELERY_QUEUES = (
    Queue('default', Exchange('default', type='direct'), routing_key='default'),
    Queue('hotfix', Exchange('hotfix', type='direct'), routing_key='hotfix'),
    Queue('builder', Exchange('builder', type='direct'), routing_key='builder'),
)
CELERY_ROUTES = {
    "hotfix": {
        'queue': 'hotfix',
        'routing_key': 'hotfix'
    },
}


app.conf.task_default_queue = "default"
app.conf.task_default_exchange = "default"
app.conf.task_default_routing_key = "default"
```

#### 函数调用

```python
tasks.publish_rpms_to_yum_repo.apply_async(args=(kwargs,), queue="hotfix", routing_key="hotfix")
```

#### 启动队列

```python
celery -A celery_task.main worker -l info -Q builder # builder 队列
celery -A celery_task.main worker -l info -Q hotfix # hotfix 队列
```

