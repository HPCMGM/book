# 1. psutil

## 1.1 CPU

### 1.1.1 基本信息

#### > cpu_count

获取逻辑cpu个数

```python
def psutil.cpu_cout(logical=True):
return int
```

* logical: `bool`, 是否排除超线程cpu

**示例**

```python
print(psutil.cpu_cout)
# 获取可以使用的CPU个数
#len(psutil.Process().cpu_affinity())
```

输出

```python
4
```

#### > cpu_freq

CPU主频检测

```python
def psutil.cpu_freq(percpu=False):
return scpufreq
```

* percpu: `bool`, 是否检测每个cpu

**输出参数**

* current: 当前频率
* min: 最小频率
* max: 最大频率

**示例**

```python
print(psutil.cpu_freq)
```

输出

```python
scpufreq(current=2500.0, min=0.0, max=2501.0)
```

### 1.1.2 使用情况

#### > cpu_percent

实时获取cpu利用率百分比

```python
def psutil.cpu_percent(interval=None, percpu=False):
return float/tuple
```

* interval: `float`, 获取多少秒内的CPU平均使用率, 建议不要用`None`, 这样输出的不准确.
* percpu: `bool`, 是否获取每个CPU的信息, 默认展示全部CPU的均值.

**示例**

```python
print(psutil.cpu_percent(interval=0.1, percpu=True))
```

输出

```python
(100.0, 0.0, 0.0, 0.0)
```

#### > cpu_times

进程的执行过程, 消耗在不同位置的时间(秒)

```Python
def psutil.cpu_times(percpu=False):
return scputimes# 类似tuple
```

* percpu: `bool`, 是否显示每个cpu的消耗统计

**返回信息**:

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

**示例**

```python
print(psutil.cpu_times())
```

输出

```python
scputimes(user=17.34, nice=0.0, system=71.23, idle=13116.78, iowait=390.47, irq=0.0, softirq=11.34, steal=0.0, guest=0.0, guest_nice=0.0)
```

#### > cpu_times_percent

获取cpu在不同空间的时间占用率.

```python
def psutil.cpu_times_percent(interval=None, percpu=False):
return scputimes
```

* interval: `float`, 获取多少秒内的CPU平均时间使用率, 建议不要用`None`, 这样输出的不准确.
* percpu: `bool`, 是否获取每个CPU的信息, 默认展示全部CPU的均值.

**示例**

```python
print(psutil.cpu_times_percent(interval=1, percpu=False)
```

输出

```python
scputimes(user=25.0, nice=0.0, system=0.0, idle=75.0, iowait=0.0, irq=0.0, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)
```

#### > cpu_stats

获取CPU被调用的次数

```python
def psutil.cpu_stats():
return scpustats
```

**返回参数**

* ctx_switches: `int`, 启动后的上下文切换次数
* interrupts: `int`, 自引导以来的中断次数
* soft_interrupts: `int`, 自引导以来的软件中断次数(window/sunos始终为0)
* syscalls: `int`, 自引导以来系统调用次数(linux始终为0)

**示例**

```python
print(psutil.cpu_stats())
```

输出

```python
scpustats(ctx_switches=2640056184, interrupts=1686413903, soft_interrupts=0, syscalls=2247895862)
```

#### > getloadavg

获取CPU在1/5/15分钟内的负载量

```python
def psutil.getloadavg():
return tuple
```

**示例**

```python
print(psutil.getloadavg())
```

输出

```python
# (0.18, 0.16, 0.08)
```

## 1.2 MEM

#### > virtual_memory

获取系统内存使用情况

```python
def psutil.virtual_memory():
return svmem
```

**输出参数**

* total: 总物理内存
* available: 进程可使用的内存, total - available != used
* used: 使用的内存(仅供参考) total - used != free
* free: 可用内存(建议使用available, 只有window中两者才会相等)
* active: 使用内存(存在于ram中)
* inactive: 未标记为使用的内存
* buffers: 缓存文件系统元数据内存
* cached: 缓存动态数据
* slab: 缓存内核数据
* wired: 标记始终保留在RAM中的内存, 永远不能移动到硬盘中

**示例**

```python
print(psutil.virtual_memory())
```

输出

```python
svmem(total=25625251840, available=17741873152, percent=30.8, used=7883378688, free=17741873152)
```

#### > swap_memory

获取交换内存

```python
def psutil.swap_memory():
return sswap
```

**输出参数**

* total: 总交换内存(字节)
* used: 使用的交换内存
* free: 自由交换内存
* percent: 使用率
* sin: 系统从磁盘交换入的字节
* sout: 系统从磁盘交换出的字节

**示例**

```python
print(psutil.swap_memory())
```

输出

```python
sswap(total=1022357504, used=0, free=1022357504, percent=0.0, sin=0, sout=0)
```

## 1.3 DISK

#### > disk_partitions

获取分区信息

```python
def psutil.disk_partitions(all=False):
return list
```

* all: `bool`, 是否获取全部分区信息

**输出参数**

* device: 硬盘名称
* moutpoint: 挂载点
* sftype: 磁盘格式
* opts: 磁盘权限

**示例**

```python
print(psutil.disk_partions())
```

输出

```python
[sdiskpart(device='/dev/sda3', mountpoint='/', fstype='ext4', opts='rw,errors=remount-ro'),
 sdiskpart(device='/dev/sda7', mountpoint='/home', fstype='ext4', opts='rw')]
```

#### > disk_usage

获取磁盘/目录使用情况.

```python
def disk_usage(path):
return sdiskusage
```

* path: `str`, 指定需要获取占用情况的目录

**返回参数**

* total: 总空间
* used: 使用
* free: 空闲
* percent: 使用百分比

**示例**

```python
print(psutil.disk_usage(path))
```

输出

```python
sdiskusage(total=534773755904, used=294595985408, free=240177770496, percent=55.1)
```

#### > disk_io_counters

获取磁盘IO信息

```python
def psutil.disk_io_counters(perdisk=False, nowrap=True):
return sdiskio
```

* perdisk: `bool`, 是否获取每个磁盘的IO情况
* nowrap: `bool`, 是否确保数据一直往上叠加

**返回参数**

* read_count: 读取次数
* write_count: 写入次数
* read_bytes: 读取的字节数
* write_bytes: 写入的字节数
* read_time: 从磁盘读取时间
* write_time: 从磁盘写入时间
* read_merged_count: 合并读取数量
* write_merged_count: 合并写入数量

**示例**

```python
print(psutil.disk_io_counters(perdisk=False, nowrap=True))
```

输出

```python
sdiskio(read_count=431883, write_count=666695, read_bytes=9281397248, write_bytes=16847543296, read_time=362, write_time=602)
```

## 1.4 NET

#### > net_io_counters

获取网卡IO信息

```python
def psutil.net_io_counters(pernic=False, nowrap=True):
return snetio
```

* pernic: `bool`, 是否获取全部网卡的信息
* nowrap: `bool`, 是否保证数据在一直向上叠加

**输出参数**

* bytes_sent：发送的字节数
* bytes_recv：接收的字节数
* packets_sent：发送的包数
* packets_recv：接收的数据包数
* errin：接收时的错误总数
* errout：发送时的错误总数
* dropin：丢弃的传入数据包总数
* dropout：丢弃的传出数据包总数（macOS和BSD总是0）

**示例**

```python
print(psutil.net_io_counters(pernic=False, nowrap=True))
```

输出

```python
snetio(bytes_sent=25927970531, bytes_recv=7958826163, packets_sent=23659788, packets_recv=8450453, errin=0, errout=0, dropin=0, dropout=0)
```





