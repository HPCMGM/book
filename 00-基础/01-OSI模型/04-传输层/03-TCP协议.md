# 1. TCP协议

## 1.1 介绍

TCP为传输控制协议(Transmission Control Protocol)

## 1.2 特点

* 相对稳定, 确保对方准确都到数据.
* 相对UDP而言TCP要慢
* web服务器都是使用tcp创建的
* 不能发送广播

# 2 报文

## 2.1 连接流程

### 2.1.1 建立连接

三次握手:

1. 客户端 请求服务端进行通讯. (A:  我要进行通讯, 收到请回复!)

   发送标志位为SYN(synchronous, 同步的), 请求建立连接. 

   数据中:

   ​	序列号sep(sequence number) = x

2. 服务端 同意客户端通信请求, 并请求与客户端通信.(B:  收到! 你能听到我说的话吗?)  

   收到数据:

   ​	序列号sep(sequence number) = x

   发送标志位为ACK(acknowledgement, 确认).  用来标记收到请求

   数据中:

   ​	确认号ack(acknowledgement number) = x + 1. 

   除此之外, 还需也许要发送SYN请求建立通讯, 请求建立连接. 

   数据中:

   ​	序列号sep(sequence number) = y

   所以发送到客户端的请求将由ACK+SYN组成.

3. 客户端 同意服务端通信请求. 发送标志位为ACK.(A: 能听到)  

   收到数据:

   ​	序列号sep(sequence number) = y

   ​	确认号ack(acknowledgement number) = x + 1. 

   发送标志位为ACK(acknowledgement, 确认). 用来标记收到请求

   数据中:

   ​	序列号sep(sequence number) = x + 1(没有增加)

   ​	确认号ack(acknowledgement number) = y + 1.

   ​	

为什么服务端需要请求客户端进行通讯(SYN)?

在网线的构造中, 发送方和接受方的网线是需要走不通的线路. TCP协议认为, 在一个方向上有通讯, 在另一个方向上也有通讯. 所以TCP是全双工(Full Duplex)的, 也可进行半双工通讯
所以三次握手的流程应该是这样的:

![img](03-TCP%E5%8D%8F%E8%AE%AE.assets/tcp%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B.png)


至此TCP通信已经成功建立的连接

### 2.1.2 连接的保持

经过三次握手, 双向通信已经建立了起来. 

客户端和服务端在通信时, 为确保每次的数据包都能准确的被对方所收到, 每次在发送本次数据时, 必须要确认(ACK)上次的数据已经收到,  并将ack(acknowledgement number) + 1

否则, 对方将重新补发上次的数据. 

如果接受到重复的数据包, 将会直接抛弃.

通讯过程:

1. 服务端 确认数据. 发送标志位为ACK.

   收到数据:

   ​	序列号sep(sequence number) = x + 1

   ​	确认号ack(acknowledgement number) = y + 1. 

   发送标志位为ACK(acknowledgement, 确认). 用来标记收到请求

   数据中:

   ​	序列号sep(sequence number) = y + 1

   ​	确认号ack(acknowledgement number) = x + 2.

2.  客户端 确认数据. 发送标志位为ACK.

   收到数据:

   ​	序列号sep(sequence number) = y + 1

   ​	确认号ack(acknowledgement number) = x + 2.

   发送标志位为ACK(acknowledgement, 确认). 用来标记收到请求

   数据中:

   ​	序列号sep(sequence number) = x + 2

   ​	确认号ack(acknowledgement number) = y + 2.

### 2.1.3 断开连接

通讯结束后必须要断开连接

1. 客户端  请求关闭. 

   收到数据:

   ​	序列号sep(sequence number) = x + k

   ​	确认号ack(acknowledgement number) = y + K.

   发送标志位为FIN(fin, 结束), 请求关闭连接

   数据中:

   ​	序列号sep(sequence number) = y + k

   ​	确认号ack(acknowledgement number) = x + K + 1.

2. 服务端  确认请求.

   收到数据:

   ​	序列号sep(sequence number) = y + k

   ​	确认号ack(acknowledgement number) = x + K + 1.

   发送数据:

   ​	发送确认数据ACK 

   ​	序列号sep(sequence number) = x + K + 1

   ​	确认号ack(acknowledgement number) = y + k + 1.

3. 服务端  请求关闭.

   由于数据传输可能正在继续不能立即断开, 所以关闭信号需要有一定的时间

   收到数据:

   ​	序列号sep(sequence number) = x + K + 1

   ​	确认号ack(acknowledgement number) = y + k + 1.

   发送数据:

   ​	发送确认数据ACK 

   ​	序列号sep(sequence number) = y + k + 1

   ​	确认号ack(acknowledgement number) = x + K + 2.

4. 客户端  确认请求.

   收到数据:

   ​	序列号sep(sequence number) = y + k + 1

   ​	确认号ack(acknowledgement number) = x + K + 2.

   发送数据:

   ​	发送确认数据ACK 

   ​	序列号sep(sequence number) = x + K + 2

   ​	确认号ack(acknowledgement number) = y + k + 2.

所以正常的通信全过程是这样的:

![img](03-TCP%E5%8D%8F%E8%AE%AE.assets/%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B%E3%80%81%E5%9B%9B%E6%AC%A1%E6%8C%A5%E6%89%8B.png)

## 2.2 报文信息

![img](03-TCP%E5%8D%8F%E8%AE%AE.assets/64380cd7912397ddb480a4110c5c4ab2d1a28709.jpeg)

**说明:**

1. 序号(sequence number)

   seq序号, 32位. 用来标记发送方的的数据包的序号

2. 确认号(acknowledgement number)

   ack序号, 32位. 用来确认seq的正常接收. 只有标志位为ACK时, ack序号才有效

3. 标志位(Flags)

   一共有6个标志位

   * URG: 紧急指针
   * ACK: 确认数据
   * PSH: 接收方尽快将报文交给应用层
   * RST: 重置连接
   * SYN: 请求连接
   * FIN: 释放连接

   *注意: 标志位的ACK和确认好的ack是不同的*



## 2.3 字节控制

* 局域网:

 1518(以太网帧) - 16(mac地址) - 帧类型(2) - IP数据报(20) - TCP头部信息(20) = 1460字节

* Internet: 

 标准MTU值(576) - IP数据报(20) - UDP头部信息(20) = 536字节

事实上tcp发送是没有上限控制的, 如果数据较大的话, 则会底层会自动分片发送. 数据越大标志着底层需要处理的时间越长, 可能会引起超时异常

