# cpu使用率

# cpu消耗统计

```bash
psutil.cpu_times(percpu=False): return tuple
```

* percpu: bool, 是否显示每个cpu的消耗统计

返回参数:

* user: 用户空间时间消耗
* system: 系统空间时间消耗
* idle: 空闲时间
* nice: 当前用户执行进程, 真正在cpu上运行时长, 包含guest_nice
* iowait: io消耗时间, 不计入idle
* irq/interrupt: 硬件中断时间
* softirq: 软件中断时间
* steal:  其他用户使用cpu时长
* guest: 来宾用户使用cpu的时长
* guest_nice: 来宾用户运行的进程, 真正在cpu上运行时长
* dpc:  延迟调用时间