# 1. MAC地址

## 1.1 概念

MAC 地址用于标识唯一的一个网卡，一台电脑会有一个或多个网卡，每个网卡都需要有一个唯一的 MAC 地址。


## 1.2 作用

借助 MAC 地址这个唯一标识，向网卡发送信息


## 1.3  mac地址编码

* 格式
 
 6字节的16进制编码表示, `ff:ff:ff:ff:ff:ff`

 前三位:  生产商购买IEEE（Institute of Electrical and Electronics Engineers)分配的序列
 
 后三位:  生产商自行分配的序列
 
* 个数
 
 16 ^ 6 = 2 ^ 48 ≈ 256000000000000
 
*  特殊的MAC地址
 
 `ff:ff:ff:ff:ff:ff`二进制位全为1的mac地址, 为广播地址(Broadcast Address)
