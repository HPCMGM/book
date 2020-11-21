# 1. ICMP
## 1.1 作用

ICMP(Internet Control Message Protocol), 互联网控制报文协议

* 用于在发生错误时自动指示错误

* 可以提供排查网络问题的工具

## 1.2 协议

ICMP报文头部包含: type和code

* type: 说明ICMP用途

* code: 说明ICMP消息的角色

> type=3表示状态目标不可达

> type=5表示ICMP重定向

> type=8表示请求消息

> type=0表示响应消息

> type=11表示超过生存时间TTL225

> code=0表示网络不可达, 1表示机器不可达

