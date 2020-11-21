## 数据库

SQL(Structured Query Language)数据库主要用于

* 数据的存储
* 快速读写
* 保证数据的有效性
* 程序支持性好, 易拓展.

### 数据库特点

数据库特点:

* dql: 数据查询命令
* dml: 数据操作命令, 增删改查(CURD)
* ddl: 数据定义命令, 创建表, 数据库, 删除表, 数据库
* spl: 语句不区分大小写, 每条spl语句要加";"

数据库主要包括两种类型:

## 数据库类型

### 关系型数据库

关系型数据库RDMS(Relational Database Management System)

E-R设计模型  E 表示entry, 实体; R表示relationship, 关系;

特点:

* 记录: 行数据
* 字段: 数据列
* 数据表: 记录集合
* 数据库: 数据表集合
* 主键: 特殊字段, 用来标识记录的唯一性

主流数据库:

* Oracle
* MySQL
* MS SQL(Microsoft SQL)
* Sqlite
* DB2: ibm

### 非关系型数据库

离散型数据, mongodb爬虫开发的时候使用非关系性数据库