## 简介

### What

> # Oracle
>
> - 数据文件是数据库的物理存储单位，数据存储在表空间（由多个数据文件组成）
> - 表空间是数据文件的逻辑映射，一个数据库（特指整个数据库）在逻辑上被分成多个表空间（都包含system表空间）
> - 用户是在实例下建立的。不同实例中可以建相同名字的用户
> - 一个数据库schema可以存在于多个表空间，一个表空间里面可以有多个schema
>
> >数据文件 ----表空间                       
>
> A schema is a collection of database objects (used by a user.).
>
> Schema objects are the logical structures that directly refer to the database’s data.
>
> A user is a name defined in the database that can connect to and access objects.
>
> Schemas and users help database administrators manage database security.
>
> oracle database 由 多个 schema 组成
>
> schema 由 database objects 组成，如 tables，views, stored procedures等
>
> **Oracle 不能新创建一个 schema, 只能通过创建一个用户来创建 Schema, 且将用户名作为该 Schema 的 名字。各个Schema之间相互独立，一个User默认只能操作自己的Schema，除非他有相应的权限或者DBA权限，如果我们访问一个表时，没有指明该表属于哪一个schema中的，系统就会自动给我们在表上加上缺省的sheman名。**
>
> 
>
> - 数据文件是数据库的物理存储单位，数据存储在表空间（由多个数据文件组成）
> - 表空间是数据文件的逻辑映射，一个数据库在逻辑上被分成多个表空间（都包含system表空间）
> - 用户是在实例下建立的。不同实例中可以建相同名字的用户
>
> 创建过程： 表空间--->用户--->表;
> 所属关系： 表空间 包含 用户 和 表
>
> 
>
> - **用户**是用来连接数据库访问数据库
> - **模式**是数据库对象的集合。模式对象是数据库数据的逻辑结构。
> - 
>
> 一个汉字在Oracle数据库里占多少字节跟数据库的字符集有关，UTF８时，长度为三。







#### 定义

Oracle Database，又名 Oracle RDBMS，简称 Oracle。Oracle 数据库系统是美国 Oracle 公司（甲骨文）提供的以分布式数据库为核心的一组软件产品，是目前最流行的客户/服务器（client/server）或B/S体系结构的数据库之一，比如 SilverStream 就是基于数据库的一种中间件。Oracle 数据库是目前世界上使用最为广泛的数据库管理系统，作为一个通用的数据库系统，它具有完整的数据管理功能；作为一个关系型数据库，它是一个完备关系的产品；作为分布式数据库它实现了分布式处理功能，但它的所有知识，只要在一种机型上学习了Oracle知识，便能在各种类型的机器上使用它。

#### 数据文件（dbf）

数据文件是数据库的**物理存储单位**。数据库的**数据是存储在表空间中**的，真正是在某一个或者多个数据文件中，而一个表空间可以由一个或多个数据文件组成，一个数据文件只能属于一个表空间。一旦数据文件被加入到某个表空间后，就不能删除这个文件，如果要删除某个数据文件，只能删除其所属于的表空间才行。

**数据文件是数据库的物理存储单位，数据存储在表空间（由多个数据文件组成）**

#### 表空间

表空间：数据文件 = 1：n

数据库：表空间 = 1：n

> 数据库 和 表空间 可以看作是数据文件的高维抽象，是一个逻辑概念

表空间是Oracle对物理数据库上相关数据文件（ORA 或者DBF文件）的逻辑映射。一个数据库在逻辑上被划分成一到若干个表空间，每个表空包含了在逻辑上相关联的一组结构。每个数据库至少有一个表空间（称之为system表空间）。每个表空间由同一磁盘上的一个或多个文件组成，这些文件叫数据库文件（datafile）。一个数据文件只能属于一个表空间。

**表空间是数据文件的逻辑映射，一个数据库在逻辑上被分成多个表空间（都包含system表空间）**

#### 用户

用户是在实例下建立的。不同实例中可以建相同名字的用户。注：表的数据，是有用户放入某一个表空间的，而这个表空间会随机把这些表数据放到一个或者多个数据文件中。由于Oracle的数据库不是普通的概念，oracle是有用户和表空间对数据进行管理和存放的。但是表不是由表空间去查询的，而是由用户去查的。因为不同用户可以在同一个表空间建立同一个名字的表！这里区分就是用户了！

**用户是在实例下建立的。不同实例中可以建相同名字的用户**

#### 数据库和实例

Oracle数据库服务器由一个数据库和至少一个数据库实例组成。 数据库是一组存储数据的文件，而数据库实例则是管理数据库文件的内存结构。此外，数据库是由后台进程组成。

### Why

### 存储结构

#### 物理存储结构

物理存储结构是存储数据的纯文件。当执行一个 CREATE DATABASE 语句来创建一个新的数据库时，将创建下列文件：

  ● **数据文件**：数据文件包含真实数据，例如销售订单和客户等。逻辑数据库结构(如表和索引)的数据被物理存储在数据文件中。

  ● **控制文件**：每个 Oracle 数据库都有一个包含元数据的控制文件。元数据用来描述包括数据库名称和数据文件位置的数据库物理结构。

  ● **联机重做日志文件**：每个 Oracle 数据库都有一个联机重做日志，里面包含两个或多个联机重做日志文件。联机重做日志由重做条目组成，能够记录下所有对数据所做的更改。

除这些文件外，Oracle 数据库还包括如参数文件、网络文件、备份文件以及用于备份和恢复的归档重做日志文件等重要文件。

#### 逻辑存储结构

Oracle 数据库使用逻辑存储结构对磁盘空间使用情况进行精细控制。以下是 Oracle 数据库中的逻辑存储结构：

  ● **数据块(Data blocks)**：Oracle 将数据存储在数据块中。数据块也被称为逻辑块，Oracle 块或页，对应于磁盘上的字节数。

  ● **范围(Extents)**：范围是用于存储特定类型信息的逻辑连续数据块的具体数量。

  ● **段(Segments)**：段是分配用于存储用户对象(例如表或索引)的一组范围。

  ● **表空间(Tablespaces)**：数据库被分成称为表空间的逻辑存储单元。 表空间是段的逻辑容器。 每个表空间至少包含一个数据文件。







SYS：权限最高 

- 用户名：`sys as sysdba`

SYSTEM：次之

SCOTT：学习用账户



查看当前的监听器状态

```
C:\Users\Milo>lsnrctl status

LSNRCTL for 64-bit Windows: Version 11.2.0.1.0 - Production on 28-12月-2020 09:16:44

Copyright (c) 1991, 2010, Oracle.  All rights reserved.

正在连接到 (DESCRIPTION=(ADDRESS=(PROTOCOL=IPC)(KEY=EXTPROC1521)))
LISTENER 的 STATUS
------------------------
别名                      LISTENER
版本                      TNSLSNR for 64-bit Windows: Version 11.2.0.1.0 - Production
启动日期                  28-12月-2020 08:53:31
正常运行时间              0 天 0 小时 23 分 13 秒
跟踪级别                  off
安全性                    ON: Local OS Authentication
SNMP                      OFF
监听程序参数文件          E:\app\Milo\product\11.2.0\dbhome_1\network\admin\listener.ora
监听程序日志文件          e:\app\milo\diag\tnslsnr\LAPTOP-A88MNCD1\listener\alert\log.xml
监听端点概要...
  (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(PIPENAME=\\.\pipe\EXTPROC1521ipc)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=LAPTOP-A88MNCD1)(PORT=1521)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=127.0.0.1)(PORT=1521)))
服务摘要..
服务 "CLRExtProc" 包含 1 个实例。
  实例 "CLRExtProc", 状态 UNKNOWN, 包含此服务的 1 个处理程序...
服务 "orcl" 包含 1 个实例。
  实例 "orcl", 状态 READY, 包含此服务的 1 个处理程序...
服务 "orclXDB" 包含 1 个实例。
  实例 "orcl", 状态 READY, 包含此服务的 1 个处理程序...
命令执行成功
```



```sql

```





## 数据库的启动与关闭

### 数据库启动过程

涉及3个状态和3种文件

- NOMOUNT状态：该状态只打开了**数据库实例**，此时读取**参数文件**
- MOUNT状态：该状态ORACLE根据参数文件中**控制文件**的位置找到并打开控制文件，读取控制文件中各种参数信息，如数据文件和日志文件的位置等，但是此时并不打开数据文件
- OPEN状态：该状态数据库将打开**数据文件**并进行一系列的检查工作，这些检查工作用于数据恢复。

```sql
SQL> startup nomount
ORA-01081: 无法启动已在运行的 ORACLE - 请首先关闭它

sql>shutdown immediate关闭再进行

sql>startup nomount重新开启就可以了
```



### 数据库启动到NOMOUNT状态

```sql
SQL> startup
ORACLE 例程已经启动。

Total System Global Area 6580703232 bytes
Fixed Size                  2188128 bytes
Variable Size            3422555296 bytes
Database Buffers         3137339392 bytes
Redo Buffers               18620416 bytes
数据库装载完毕。
数据库已经打开。
```

### 数据库启动到MOUNT状态

1. 直接启动数据库到MOUNT状态
2. 如果数据库已经在NOMOUNT状态，使用指令alter database mount;

### 数据库启动到OPEN状态

```sql
SQL> alter database open;
```

### 关闭数据库

1. CLOSE：关闭数据文件，日志文件等
2. DISMOUNT：关闭控制文件
3. SHUTDOWN：关闭实例

