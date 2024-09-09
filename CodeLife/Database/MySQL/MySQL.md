## 概述

- 摆脱指针
- 完全限定列名：当引用的列可能出现二义性时，必须使用完全限定列名（表名.列名）
- 使用C/S模式
- 单双引号无区别
- 关键字不区分大小写, 数据区分大小写

### 关系与表

- 关系中不允许重复的元祖，而表中可以
- 关系中的元祖没有从上往下的顺序，而表中的行有从上往下的顺序
- 关系中的属性没有从左往右的顺序，而表中有
- 关系满足第一范式
- 关系是笛卡尔积的子集
- 关系具有封闭性，即运算的输入和输出都是关系
- 关系对关系运算符也是封闭的
  - 群：对+，-或*， / 封闭
  - 环：对+, -, * 封闭
  - 域：对+，-，*，/ 封闭

### 规范

- **SQL大小写不敏感，但是插入的数据大小区分，即对非关键字的字符加引号**
- 习惯：关键字大写，其他小写
  
- 字符串和日期使用引号括起来，数值不用

- 库名，表名小写，多个单词可以由下划线连接
- 列名小写，由**表名缩写+列名**组合，如customers表的id列，cust_id

### SQL种类

- DDL （data definition language）：create, drop, alter
- DML (data manipulation language)：select, insert, update, delete
- DCL (data control language)：commit，rollback， grant， revoke

### 汉字

一个汉字占多少长度与编码有关

1. UTF-8：一个汉字 = 3个字节，英文是一个字节
2. GBK： 一个汉字 = 2个字节，英文是一个字节
3. utf8mb4: 一个汉字 = 4个字节，英文是一个字节
   varchar(n) 表示n个字符，无论汉字和英文，MySql都能存入 n 个字符，仅实际字节长度有所区别。
   MySQL检查长度，可用 SQL 语句 SELECT LENGTH(fieldname) FROM tablename
   在 utf-8 字符集中，最多可以存储(65535 -2) / 3 = 21844 个汉字
   在 gbk 字符集中，最多可以存储(65535 - 2) / 2 = 32766 个汉字

### mysql命令行实用程序

- 命令以；结束，按Enter换行
- `quit` 或 `exit` 退出
- `help` 或 `\h`
  - `help select`

### 修改默认编码

修改用户文件夹下的my.ini

```mysql
[mysql]
no-beep

default-character-set=utf8

character-set-server=utf8
重新启动mysql
```

## 数据类型

### 串

分为定长串与变长串，使用单引号或双引号括起来

- char：长度固定，char(n)，存储**n个字符**，n = 1-255, 
  - 当保存char值时，在它们的右边填充空格以达到指定的长度
  - 当检索到char值时，尾部的空格被删除掉
-  varchar，长度可变，varchar(n)，存储**n个字符**，n = 0-255, 
  - varchar只保存时只保存需要的字符数，另加一个字节来记录长度
  - 根据实际存储的数据来分配最终的存储空间。
- enum：接受最多64k个串组成的一个预定义集合的某个串
- longtext：与text相同，最大长度为4GB
- set：接受最多64k个串组成的一个预定义集合的零个或多个串
- text：最大长度为64k的变长文本
- tinytext：0-255字节

### 数值

分为**有符号数值**和**无符号（unsigned）数值**

- bit，1-64位
- bigInt，
- boolean（bool）： 0，1
- decimal（dec）：精度可变的浮点值
- double：双精度
- float：单精度
- int：
- mediumint：
- real：4字节的浮点值
- smallint：0-65535
- tinyint，0-255

### 日期和时间

- date：yyyy-mm-dd
- time：hh:mm:ss
- datetime：yyyy-mm-dd hh:mm:ss
- timestamp：和datetime相同，范围小
- year：
  - 两位数： 70（1970）~69（2069）
  - 四位数：1901-2155

### 二进制

可存储任何数据，如图像，多媒体，字处理文档等

- tinyblob：255字节

- blob：最大长度为64kb
- mediumblob：最大长度为16MB
- longblob：最大长度为4GB

## 数据库和表

### 实践

```mysql
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| crashcourse        |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> use crashcourse;
Database changed

+-----------------------+
| Tables_in_crashcourse |
+-----------------------+
| customers             |
| orderitems            |
| orders                |
| productnotes          |
| products              |
| vendors               |
+-----------------------+
6 rows in set (0.00 sec)

mysql> show tables;
+-----------------------+
| Tables_in_crashcourse |
+-----------------------+
| customers             |
| orderitems            |
| orders                |
| productnotes          |
| products              |
| vendors               |
+-----------------------+
6 rows in set (0.00 sec)

mysql> show columns from customers;
+--------------+-----------+------+-----+---------+----------------+
| Field        | Type      | Null | Key | Default | Extra          |
+--------------+-----------+------+-----+---------+----------------+
| cust_id      | int(11)   | NO   | PRI | NULL    | auto_increment |
| cust_name    | char(50)  | NO   |     | NULL    |                |
| cust_address | char(50)  | YES  |     | NULL    |                |
| cust_city    | char(50)  | YES  |     | NULL    |                |
| cust_state   | char(5)   | YES  |     | NULL    |                |
| cust_zip     | char(10)  | YES  |     | NULL    |                |
| cust_country | char(50)  | YES  |     | NULL    |                |
| cust_contact | char(50)  | YES  |     | NULL    |                |
| cust_email   | char(255) | YES  |     | NULL    |                |
+--------------+-----------+------+-----+---------+----------------+
9 rows in set (0.00 sec)

mysql> describe customers;
+--------------+-----------+------+-----+---------+----------------+
| Field        | Type      | Null | Key | Default | Extra          |
+--------------+-----------+------+-----+---------+----------------+
| cust_id      | int(11)   | NO   | PRI | NULL    | auto_increment |
| cust_name    | char(50)  | NO   |     | NULL    |                |
| cust_address | char(50)  | YES  |     | NULL    |                |
| cust_city    | char(50)  | YES  |     | NULL    |                |
| cust_state   | char(5)   | YES  |     | NULL    |                |
| cust_zip     | char(10)  | YES  |     | NULL    |                |
| cust_country | char(50)  | YES  |     | NULL    |                |
| cust_contact | char(50)  | YES  |     | NULL    |                |
| cust_email   | char(255) | YES  |     | NULL    |                |
+--------------+-----------+-----

mysql> status
--------------
C:\Program Files\MySQL\MySQL Server 5.7\bin\mysql.exe  Ver 14.14 Distrib 5.7.31, for Win64 (x86_64)

Connection id:          11
Current database:       crashcourse
Current user:           root@localhost
SSL:                    Cipher in use is ECDHE-RSA-AES128-GCM-SHA256
Using delimiter:        ;
Server version:         5.7.31-log MySQL Community Server (GPL)
Protocol version:       10
Connection:             localhost via TCP/IP
Server characterset:    latin1
Db     characterset:    utf8
Client characterset:    utf8
Conn.  characterset:    utf8
TCP port:               3306
Uptime:                 55 min 2 sec

Threads: 3  Questions: 225  Slow queries: 0  Opens: 399  Flush tables: 1  Open tables: 357  Queries per second avg: 0.068

mysql> show processlist;
+----+------+-----------------+-------------+---------+------+----------+------------------+
| Id | User | Host            | db          | Command | Time | State    | Info             |
+----+------+-----------------+-------------+---------+------+----------+------------------+
|  2 | root | localhost:13306 | crashcourse | Query   |    0 | starting | show processlist |
+----+------+-----------------+-------------+---------+------+----------+------------------+
```

### 命令总结

```mysql
show databases;
use 数据库名;
show 表名

describe 表名; 
等价于
show columns from 表名;

status

show processlist;

delimiter 分隔符 -- 定义新的分隔符

# 查看字符编码
show variables like '%char%';

# 参看创建表的语句
show create table 表名;

# 修改字符集为utf-8
set character_set_database = utf8;
set character_set_server = utf8;
```

## 检索 Select

select 返回的数据的顺序无意义。

- 通配符 *：匹配所有列；
- `distinct 列名`：返回不同的行，必须放在列名前，对后面所有的字段均起作用
- `limit  起始索引， 长度`：从起始索引开始，返回其长度为n的行
- MySQL的行索引从0开始，
-    `order by 列名` ：排序输出
- `order by 列名1` 等价于 `order by 列名1 ASC` ，即默认为升序ASC
- `order by 列名1 DESC， 列名2 DESC`
- 表达式与常量

### limit

- `limit  起始地址， 长度`
  - MySQL的行索引从0开始，

```mysql
mysql> select prod_name from products;
+----------------+
| prod_name      |
+----------------+
| .5 ton anvil   |
| 1 ton anvil    |
| 2 ton anvil    |
| Detonator      |
| Bird seed      |
| Carrots        |
| Fuses          |
| JetPack 1000   |
| JetPack 2000   |
| Oil can        |
| Safe           |
| Sling          |
| TNT (1 stick)  |
| TNT (5 sticks) |
+----------------+
14 rows in set (0.00 sec)

mysql> select prod_name from products limit 5;
+--------------+
| prod_name    |
+--------------+
| .5 ton anvil |
| 1 ton anvil  |
| 2 ton anvil  |
| Detonator    |
| Bird seed    |
+--------------+
5 rows in set (0.00 sec)

mysql> select prod_name from products limit 5,5;
+--------------+
| prod_name    |
+--------------+
| Carrots      |
| Fuses        |
| JetPack 1000 |
| JetPack 2000 |
| Oil can      |
+--------------+
5 rows in set (0.00 sec)

mysql> select prod_name from products limit 1,1;
+-------------+
| prod_name   |
+-------------+
| 1 ton anvil |
+-------------+
1 row in set (0.00 sec)
```

### order by

- `order by 列名1` 等价于 `order by 列名1 ASC` ，即默认为升序ASC

- `order by 列名1 DESC， 列名2 DESC`

```mysql
mysql> select prod_name from products order by prod_name;
+----------------+
| prod_name      |
+----------------+
| .5 ton anvil   |
| 1 ton anvil    |
| 2 ton anvil    |
| Bird seed      |
| Carrots        |
| Detonator      |
| Fuses          |
| JetPack 1000   |
| JetPack 2000   |
| Oil can        |
| Safe           |
| Sling          |
| TNT (1 stick)  |
| TNT (5 sticks) |
+----------------+
14 rows in set (0.00 sec)

mysql> select prod_id, prod_price, prod_name
    -> from products
    -> order by prod_price, prod_name;
+---------+------------+----------------+
| prod_id | prod_price | prod_name      |
+---------+------------+----------------+
| FC      |       2.50 | Carrots        |
| TNT1    |       2.50 | TNT (1 stick)  |
| FU1     |       3.42 | Fuses          |
| SLING   |       4.49 | Sling          |
| ANV01   |       5.99 | .5 ton anvil   |
| OL1     |       8.99 | Oil can        |
| ANV02   |       9.99 | 1 ton anvil    |
| FB      |      10.00 | Bird seed      |
| TNT2    |      10.00 | TNT (5 sticks) |
| DTNTR   |      13.00 | Detonator      |
| ANV03   |      14.99 | 2 ton anvil    |
| JP1000  |      35.00 | JetPack 1000   |
| SAFE    |      50.00 | Safe           |
| JP2000  |      55.00 | JetPack 2000   |
+---------+------------+----------------+
14 rows in set (0.00 sec)

mysql> select prod_id, prod_price, prod_name
    -> from products
    -> order by prod_price, prod_name DESC;
+---------+------------+----------------+
| prod_id | prod_price | prod_name      |
+---------+------------+----------------+
| TNT1    |       2.50 | TNT (1 stick)  |
| FC      |       2.50 | Carrots        |
| FU1     |       3.42 | Fuses          |
| SLING   |       4.49 | Sling          |
| ANV01   |       5.99 | .5 ton anvil   |
| OL1     |       8.99 | Oil can        |
| ANV02   |       9.99 | 1 ton anvil    |
| TNT2    |      10.00 | TNT (5 sticks) |
| FB      |      10.00 | Bird seed      |
| DTNTR   |      13.00 | Detonator      |
| ANV03   |      14.99 | 2 ton anvil    |
| JP1000  |      35.00 | JetPack 1000   |
| SAFE    |      50.00 | Safe           |
| JP2000  |      55.00 | JetPack 2000   |
+---------+------------+----------------+
14 rows in set (0.00 sec)
```

### 结合

- `order by`子句位于`FROM`子句后，`LIMIT`子句位于`order by`之后

```mysql
# 查询最高价

mysql> select prod_price from products order by prod_price DESC limit 1;
+------------+
| prod_price |
+------------+
|      55.00 |
+------------+
1 row in set (0.00 sec)
```

### 表达式与常量

```mysql
mysql> select 7-3;
+-----+
| 7-3 |
+-----+
|   4 |
+-----+
1 row in set (0.04 sec)

mysql> select '中国';
+--------+
| 中国   |
+--------+
| 中国   |
+--------+
1 row in set (0.00 sec)
```

## 过滤 where

- `where 列名 算术操作符 值`：确定一个列是否包含特定的值
- `where 列名 IS NULL`
  - 当值为字符串时，使用单/双引号限定，与数值类型比较时不用
  - 算术操作符：`=, <>, !=, <，<=, >, >=, between num1 and num2`
- `where 列名 算术操作符 值 逻辑操作符 列名 算术操作符 值`
    - 逻辑操作符：`AND，OR, NOT`，AND优先级高于OR
    - 逻辑运算符对比较运算符等返回的真值进行操作
- `where 列名 in (值1， 值2)` 等价于 `where 列名=值1 OR 列名=值2`
  - IN执行速度比OR块
- `NOT`：否定后跟的所有的任何条件
  - `NOT IN, NOT BETWEEN, NOT EXISITS`
- 与字符比较时，按照字典顺序进行比较，即按照条目在字典中出现的顺序来进行排序
    - 以相同字符开头的单词比不同字符开头的单词更相近。
- 所有包含null的计算，结果都是null

### 谓词

定义: 返回值为真值的函数。

- LIKE
  - `where 列 like 字符串`
  - %：匹配0个，1个或多个字符
  - _：只能匹配一个字符
  - 不要将通配符位于搜索处的开始处，搜索最慢
- `列 BETWEEN 值1 AND 值2`
  - `值1<= 列<=值2`
- NOT
  - IS NULL, IS NOT NULL
  - IN, NOT IN
- EXISTS ：判读是否存在满足某种条件的记录
  - `EXISTS select * 子查询`：只关心记录是否存在，因此返回那些列都没有关系

### if

IF(expr1,expr2,expr3)相当于三元表达式if expr1=true? expr2: expr3

```mysql
mysql> select product_name, sale_price, if(sale_price<1000,'低',if(sale_price<4000, '中', '高')) as price from product;
+--------------+------------+-------+
| product_name | sale_price | price |
+--------------+------------+-------+
| T恤          |       1000 | 中    |
| 打孔器       |        500 | 低    |
| 运动T恤      |       4000 | 高    |
| 菜刀         |       3000 | 中    |
| 高压锅       |       6800 | 高    |
| 叉子         |        500 | 低    |
| 擦菜板       |        880 | 低    |
| 圆珠笔       |        100 | 低    |
+--------------+------------+-------+
8 rows in set (0.00 sec)

# 等价于下
SELECT
	product_name,
	sale_price,
CASE
		WHEN sale_price < 1000 THEN
		'低' 
		WHEN sale_price < 4000 THEN
		'中' ELSE '高' 
	END AS price 
FROM
	product;
```

### 实践

```mysql
mysql> select prod_name, prod_price from products where prod_name = 'fuses';
+-----------+------------+
| prod_name | prod_price |
+-----------+------------+
| Fuses     |       3.42 |
+-----------+------------+
1 row in set (0.00 sec)

mysql> select prod_name, prod_price from products where prod_name = "fuses";
+-----------+------------+
| prod_name | prod_price |
+-----------+------------+
| Fuses     |       3.42 |
+-----------+------------+
1 row in set (0.00 sec)

mysql> select cust_name, cust_email from customers where cust_email is null;
+-------------+------------+
| cust_name   | cust_email |
+-------------+------------+
| Mouse House | NULL       |
| E Fudd      | NULL       |
+-------------+------------+
2 rows in set (0.00 sec)

mysql> select prod_name, prod_price from products where vend_id=1002 or vend_id=1003 and prod_price >=10;
+----------------+------------+
| prod_name      | prod_price |
+----------------+------------+
| Detonator      |      13.00 |
| Bird seed      |      10.00 |
| Fuses          |       3.42 |
| Oil can        |       8.99 |
| Safe           |      50.00 |
| TNT (5 sticks) |      10.00 |
+----------------+------------+
6 rows in set (0.00 sec)

mysql> select prod_name, prod_price from products where (vend_id=1002 or vend_id=1003) and prod_price >=10;
+----------------+------------+
| prod_name      | prod_price |
+----------------+------------+
| Detonator      |      13.00 |
| Bird seed      |      10.00 |
| Safe           |      50.00 |
| TNT (5 sticks) |      10.00 |
+----------------+------------+
4 rows in set (0.00 sec)

#######################字符串类型比较############################

mysql> select * from chars;
+-----+
| chr |
+-----+
| 1   |
| 10  |
| 11  |
| 2   |
| 222 |
| 3   |
+-----+
6 rows in set (0.00 sec)

mysql> select * from chars where chr>2;
+-----+
| chr |
+-----+
| 10  |
| 11  |
| 222 |
| 3   |
+-----+
4 rows in set (0.04 sec)

mysql> select * from chars where chr>'2';
+-----+
| chr |
+-----+
| 222 |
| 3   |
+-----+
2 rows in set (0.00 sec)

mysql> select * from chars order by chr;
+-----+
| chr |
+-----+
| 1   |
| 10  |
| 11  |
| 2   |
| 222 |
| 3   |
+-----+
6 rows in set (0.00 sec)
########################null值的计算###################
mysql> select null+1;
+--------+
| null+1 |
+--------+
|   NULL |
+--------+
1 row in set (0.00 sec)
```

## case表达式

- 简单case表达式
- 搜索case表达式
- 区别：简单case表达式受到条件的约束，简单case表达式能办到的事，搜索case表达式都能
- 注意事项：
  - 统一各分支返回的数据类型
  - 不要忘记END
  - 养成写ELSE的习惯
    - 不写默认为NULL

```mysql
# 搜索case表达式
case when 求值表达式  then 表达式
	 when 求值表达式  then 表达式
	 ELSE 表达式
end

# 简单case表达式
case 表达式
	 when 求值表达式  then 表达式
	 when 求值表达式  then 表达式
	 ELSE 表达式
end


# 如果 when中的求值表达式为真，则返回THEN子句中的表示，case表达式结束
# 如果 when中的求值表达式为假，跳到下一个when子句中。
# 如果 when中的求值表达式都为假，执行ELSE中的子句，返回表达式的值

mysql> SELECT product_name,
    -> CASE WHEN product_type='衣服' THEN CONCAT('A: ',product_type)
    -> WHEN product_type='办公用品' THEN CONCAT('B: ',product_type)
    -> WHEN product_type='厨房用具' THEN CONCAT('C: ',product_type)
    -> ELSE NULL
    -> end as abc_product_type
    -> from product;
+--------------+------------------+
| product_name | abc_product_type |
+--------------+------------------+
| T恤          | A: 衣服          |
| 打孔器       | B: 办公用品      |
| 运动T恤      | A: 衣服          |
| 菜刀         | C: 厨房用具      |
| 高压锅       | C: 厨房用具      |
| 叉子         | C: 厨房用具      |
| 擦菜板       | C: 厨房用具      |
| 圆珠笔       | B: 办公用品      |
+--------------+------------------+
8 rows in set (0.00 sec)
```

### 简单case表达式

```mysql
case 表达式
	 when 求值表达式  then 表达式
	 when 求值表达式  then 表达式
	 ELSE 表达式
end

mysql> select * from PopTbl2;
+-----------+-----+------------+
| pref_name | sex | population |
+-----------+-----+------------+
| 东京      | 1   |        250 |
| 东京      | 2   |        150 |
| 佐贺      | 1   |         20 |
| 佐贺      | 2   |         80 |
| 德岛      | 1   |         60 |
| 德岛      | 2   |         40 |
| 爱媛      | 1   |        100 |
| 爱媛      | 2   |         50 |
| 福冈      | 1   |        100 |
| 福冈      | 2   |        200 |
| 长崎      | 1   |        125 |
| 长崎      | 2   |        125 |
| 香川      | 1   |        100 |
| 香川      | 2   |        100 |
| 高知      | 1   |        100 |
| 高知      | 2   |        100 |
+-----------+-----+------------+
16 rows in set (0.00 sec)

mysql> SELECT pref_name,sum( CASE sex WHEN '1' THEN population ELSE 0 END ) AS '男',
        sum( CASE sex WHEN '2' THEN population ELSE 0 END ) AS '女' 
        FROM poptbl2 
        GROUP BY pref_name;
+-----------+------+------+
| pref_name | 男   | 女   |
+-----------+------+------+
| 东京      |  250 |  150 |
| 佐贺      |   20 |   80 |
| 德岛      |   60 |   40 |
| 爱媛      |  100 |   50 |
| 福冈      |  100 |  200 |
| 长崎      |  125 |  125 |
| 香川      |  100 |  100 |
| 高知      |  100 |  100 |
+-----------+------+------+
8 rows in set (0.00 sec)
```

### 搜索case表达式

```mysql

mysql> select * from poptbl;
+-----------+------------+
| pref_name | population |
+-----------+------------+
| 东京      |        400 |
| 佐贺      |        100 |
| 德岛      |        100 |
| 爱媛      |        150 |
| 福冈      |        300 |
| 群马      |         50 |
| 长崎      |        200 |
| 香川      |        200 |
| 高知      |        200 |
+-----------+------------+
9 rows in set (0.04 sec)

mysql> SELECT
    -> CASE WHEN population < 100 THEN '01'
    ->  WHEN population >= 100 AND population < 200 THEN '02'
    ->  WHEN population >= 200 AND  population < 300 THEN '03'
    ->  WHEN population >= 300 THEN '04'
    -> ELSE NULL END as pop_class,
    -> COUNT(*) AS cnt
    -> FROM poptbl
    -> GROUP BY
    -> CASE WHEN population < 100 THEN '01'
    ->  WHEN population >= 100 AND population < 200 THEN '02'
    ->  WHEN population >= 200 AND  population < 300 THEN '03'
    ->  WHEN population >= 300 THEN '04'
    -> ELSE NULL END;
+-----------+-----+
| pop_class | cnt |
+-----------+-----+
| 01        |   1 |
| 02        |   3 |
| 03        |   3 |
| 04        |   2 |
+-----------+-----+
4 rows in set (0.00 sec)

#### 上式等价于下式 

mysql> SELECT
    -> CASE WHEN population < 100 THEN '01'
    ->  WHEN population >= 100 AND population < 200 THEN '02'
    ->  WHEN population >= 200 AND  population < 300 THEN '03'
    ->  WHEN population >= 300 THEN '04'
    -> ELSE NULL END as pop_class,
    -> COUNT(*) AS cnt
    -> FROM poptbl
    -> GROUP BY
    -> pop_class;
```

## 常用函数

### 算术函数

- 算术运算符：+，-，*，/
- `abs(), mod(被除数，除数)，round(数，位数)`

### 字符串函数

- `Concat('字符or列名', '字符or列名', '字符or列名', ...)`
- `char_length(字符串), replace(列名，old字符串, new字符串)`
- `lower(), upper()`
- `length()`
- `ltrim(), rtrim(), trim()` ：只能删除左右两端的空格
- `列名 as 别名`
- `列名 算术操作符 列名 as 别名`

```mysql
mysql> select Concat(vend_name, '(', vend_country,')') from vendors order by vend_name;
+------------------------------------------+
| Concat(vend_name, '(', vend_country,')') |
+------------------------------------------+
| ACME(USA)                                |
| Anvils R Us(USA)                         |
| Furball Inc.(USA)                        |
| Jet Set(England)                         |
| Jouets Et Ours(France)                   |
| LT Supplies(USA)                         |
+------------------------------------------+
6 rows in set (0.00 sec)


mysql> select prod_id, quantity, item_price, quantity*item_price as expanded_price from orderitems where order_num=20005;
+---------+----------+------------+----------------+
| prod_id | quantity | item_price | expanded_price |
+---------+----------+------------+----------------+
| ANV01   |       10 |       5.99 |          59.90 |
| ANV02   |        3 |       9.99 |          29.97 |
| TNT2    |        5 |      10.00 |          50.00 |
| FB      |        1 |      10.00 |          10.00 |
+---------+----------+------------+----------------+
4 rows in set (0.03 sec)


mysql> select now();
+---------------------+
| now()               |
+---------------------+
| 2020-11-09 13:22:50 |
+---------------------+
1 row in set (0.00 sec)


mysql> select trim(' a b ');
+---------------+
| trim(' a b ') |
+---------------+
| a b           |
+---------------+
1 row in set (0.00 sec)

mysql> select product_name,char_length(product_name) as len_str from product;
+--------------+---------+
| product_name | len_str |
+--------------+---------+
| T恤          |       2 |
| 打孔器       |       3 |
| 运动T恤      |       4 |
| 菜刀         |       2 |
| 高压锅       |       3 |
| 叉子         |       2 |
| 擦菜板       |       3 |
| 圆珠笔       |       3 |
+--------------+---------+
8 rows in set (0.00 sec)
```



### 日期

- 格式：yyyy-mm-dd
- `Date()`：提取列的日期部分 
- `year(), month()`：提取列的年份，月份部分 `yyyy, mm`
- `DATADIFF(expr, expr2)`：返回两个日期相减（expr1 − expr2 ）相差的天数
- `current_date`

```mysql
mysql> select * from orders where order_date='2005-09-01';
+-----------+---------------------+---------+
| order_num | order_date          | cust_id |
+-----------+---------------------+---------+
|     20005 | 2005-09-01 00:00:00 |   10001 |
+-----------+---------------------+---------+
1 row in set (0.00 sec)

mysql> select * from orders where date(order_date)='2005-09-01';
+-----------+---------------------+---------+
| order_num | order_date          | cust_id |
+-----------+---------------------+---------+
|     20005 | 2005-09-01 00:00:00 |   10001 |
+-----------+---------------------+---------+
1 row in set (0.00 sec)

mysql> select * from orders where date(order_date) between '2005-09-01' and '2005-09-30';
+-----------+---------------------+---------+
| order_num | order_date          | cust_id |
+-----------+---------------------+---------+
|     20005 | 2005-09-01 00:00:00 |   10001 |
|     20006 | 2005-09-12 00:00:00 |   10003 |
|     20007 | 2005-09-30 00:00:00 |   10004 |
+-----------+---------------------+---------+
3 rows in set (0.00 sec)

mysql> select * from orders where year(order_date) = 2005 and month(order_date) = 9;
+-----------+---------------------+---------+
| order_num | order_date          | cust_id |
+-----------+---------------------+---------+
|     20005 | 2005-09-01 00:00:00 |   10001 |
|     20006 | 2005-09-12 00:00:00 |   10003 |
|     20007 | 2005-09-30 00:00:00 |   10004 |
+-----------+---------------------+---------+
3 rows in set (0.00 sec)

mysql> select datediff('2020-11-16', '2020-10-10');
+--------------------------------------+
| datediff('2020-11-16', '2020-10-10') |
+--------------------------------------+
|                                   37 |
+--------------------------------------+
1 row in set (0.00 sec)
```

### 转换函数

- 类型转换：cast
  - `select cast('2019-12-14' as date) as date_col;`
- 值的转换：coalesce

### 聚集函数

- 定义：运行在行组上，计算和返回单个值的函数
- `AVG(), COUNT(), MAX(), MIN(), SUM()`, 可以在函数中使用`DISTINCT`，如`AVG(DISTINCT 列名)`
  - 聚集函数忽略列值为`NULL`的行，`COUNT(*)`除外
    - 四则运算中存在null，结果一定为null
  - `COUNT(*)`，统计表的函数，包括列值为`NULL`的行
  - `COUNT(column)`：对特定列统计函数，不包括列值为`NULL`的行
  - `COUNT(1)`：

```mysql
mysql> select cust_email from customers;
+---------------------+
| cust_email          |
+---------------------+
| ylee@coyote.com     |
| NULL                |
| rabbit@wascally.com |
| sam@yosemite.com    |
| NULL                |
+---------------------+
5 rows in set (0.00 sec)


mysql> select count(cust_email) from customers;
+-------------------+
| count(cust_email) |
+-------------------+
|                 3 |
+-------------------+
1 row in set (0.00 sec)

mysql> select  avg(prod_price) as avg_price from products where vend_id=1003;
+-----------+
| avg_price |
+-----------+
| 13.212857 |
+-----------+
1 row in set (0.00 sec)

mysql> select  avg(distinct prod_price) as avg_price from products where vend_id=1003;
+-----------+
| avg_price |
+-----------+
| 15.998000 |
+-----------+
1 row in set (0.00 sec)
```

## 分组

- `group by`：可以包含任意数目的列，可以嵌套
  - 如果分组列中具有`NULL`值，则`NULL`作为一个分组返回。如果有多行`NULL`值，将其分为一组
  - 必须出现在`where`子句之后，`order by` 子句之前

- `where`过滤行，指定行对应的条件，`having`过滤分组，指定分组对应的条件
- `where`在数据分组前过滤，`having`在数据分组后过滤

```mysql
# 只显示分组后的第一行
mysql> select * from products group by vend_id;
+---------+---------+--------------+------------+-------------------------------------------------+
| prod_id | vend_id | prod_name    | prod_price | prod_desc                                       |
+---------+---------+--------------+------------+-------------------------------------------------+
| ANV01   |    1001 | .5 ton anvil |       5.99 | .5 ton anvil, black, complete with handy hook   |
| FU1     |    1002 | Fuses        |       3.42 | 1 dozen, extra long                             |
| DTNTR   |    1003 | Detonator    |      13.00 | Detonator (plunger powered), fuses not included |
| JP1000  |    1005 | JetPack 1000 |      35.00 | JetPack 1000, intended for single use           |
+---------+---------+--------------+------------+-------------------------------------------------+
4 rows in set (0.00 sec)

mysql> select vend_id, count(*) as num_prods from products group by vend_id;
+---------+-----------+
| vend_id | num_prods |
+---------+-----------+
|    1001 |         3 |
|    1002 |         2 |
|    1003 |         7 |
|    1005 |         2 |
+---------+-----------+
4 rows in set (0.00 sec)

mysql> select vend_id, count(*) as num_prods from products group by vend_id having count(*) >=3;
+---------+-----------+
| vend_id | num_prods |
+---------+-----------+
|    1001 |         3 |
|    1003 |         7 |
+---------+-----------+
2 rows in set (0.00 sec)
```

### 分组排序

- 先分组，对分组后的结果进行排序。

```mysql
mysql> select order_num, sum(quantity*item_price) as ordertotal
    -> from orderitems
    -> group by order_num
    -> having ordertotal >= 50;
+-----------+------------+
| order_num | ordertotal |
+-----------+------------+
|     20005 |     149.87 |
|     20006 |      55.00 |
|     20007 |    1000.00 |
|     20008 |     125.00 |
+-----------+------------+
4 rows in set (0.00 sec)

mysql> select order_num, sum(quantity*item_price) as ordertotal
    -> from orderitems
    -> group by order_num
    -> having ordertotal >= 50
    -> order by ordertotal;
+-----------+------------+
| order_num | ordertotal |
+-----------+------------+
|     20006 |      55.00 |
|     20008 |     125.00 |
|     20005 |     149.87 |
|     20007 |    1000.00 |
+-----------+------------+
4 rows in set (0.00 sec)
```

### select子句书写顺序

1. select
2. from 
3. where
4. union
5. group by
6. having 
7. order by
8. limit

### select子句逻辑顺序

1. from
2. join on
4. where
5. group by
6. avg，sum，count等各种函数
7. having
8. select
9. distinct
10. order by(asc(升序),desc(降序))
11. LIMIT

```mysql
-- SQL执行顺序
FROM <left_table>
ON <join_condition>
<join_type> JOIN <right_table>
WHERE <where_condition>
GROUP BY <group_by_list>
HAVING <having_condition>

SELECT
DISTINCT <select_list>

ORDER BY <order_by_condition>
LIMIT <limit_number>
```

## 子查询

### 利用子查询过滤

```
mysql> select cust_id
    -> from orders
    -> where order_num in (select order_num
    ->                     from orderitems
    ->                     where prod_id = 'TNT2');
+---------+
| cust_id |
+---------+
|   10001 |
|   10004 |
+---------+
2 rows in set (0.02 sec)
```

### 子查询作为字段

```mysql
mysql> select cust_name, cust_state,
    -> (select count(*) from orders where cust_id=cust_id) as orders
    -> from customers
    -> order by cust_name;
+----------------+------------+--------+
| cust_name      | cust_state | orders |
+----------------+------------+--------+
| Coyote Inc.    | MI         |      5 |
| E Fudd         | IL         |      5 |
| Mouse House    | OH         |      5 |
| Wascals        | IN         |      5 |
| Yosemite Place | AZ         |      5 |
+----------------+------------+--------+
5 rows in set (0.02 sec)
```

## 联结 join

- 联结操作十分耗费资源与时间
- `列名 as 列别名，表名 as 表别名`
- `表1 left/right outer jion 表2 on 表1.列1=表2.列2`

### 交叉联结

笛卡尔积

### 内联结

- inner jion
  - 等值联结
  - 自然连接

```mysql
mysql> select vend_name, prod_name, prod_price
    -> from vendors, products
    -> where vendors.vend_id = products.vend_id
    -> order by vend_name, prod_name;
+-------------+----------------+------------+
| vend_name   | prod_name      | prod_price |
+-------------+----------------+------------+
| ACME        | Bird seed      |      10.00 |
| ACME        | Carrots        |       2.50 |
| ACME        | Detonator      |      13.00 |
| ACME        | Safe           |      50.00 |
| ACME        | Sling          |       4.49 |
| ACME        | TNT (1 stick)  |       2.50 |
| ACME        | TNT (5 sticks) |      10.00 |
| Anvils R Us | .5 ton anvil   |       5.99 |
| Anvils R Us | 1 ton anvil    |       9.99 |
| Anvils R Us | 2 ton anvil    |      14.99 |
| Jet Set     | JetPack 1000   |      35.00 |
| Jet Set     | JetPack 2000   |      55.00 |
| LT Supplies | Fuses          |       3.42 |
| LT Supplies | Oil can        |       8.99 |
+-------------+----------------+------------+
14 rows in set (0.00 sec)

mysql> select vend_name, prod_name, prod_price
    -> from vendors inner join products
    -> on vendors.vend_id = products.vend_id;
+-------------+----------------+------------+
| vend_name   | prod_name      | prod_price |
+-------------+----------------+------------+
| Anvils R Us | .5 ton anvil   |       5.99 |
| Anvils R Us | 1 ton anvil    |       9.99 |
| Anvils R Us | 2 ton anvil    |      14.99 |
| LT Supplies | Fuses          |       3.42 |
| LT Supplies | Oil can        |       8.99 |
| ACME        | Detonator      |      13.00 |
| ACME        | Bird seed      |      10.00 |
| ACME        | Carrots        |       2.50 |
| ACME        | Safe           |      50.00 |
| ACME        | Sling          |       4.49 |
| ACME        | TNT (1 stick)  |       2.50 |
| ACME        | TNT (5 sticks) |      10.00 |
| Jet Set     | JetPack 1000   |      35.00 |
| Jet Set     | JetPack 2000   |      55.00 |
+-------------+----------------+------------+
14 rows in set (0.00 sec)
```

### 自连接

- 子查询 ---> 联结

```mysql
mysql> select prod_id, prod_name from products where vend_id =
    -> (select vend_id from products where prod_id = 'DTNTR');
+---------+----------------+
| prod_id | prod_name      |
+---------+----------------+
| DTNTR   | Detonator      |
| FB      | Bird seed      |
| FC      | Carrots        |
| SAFE    | Safe           |
| SLING   | Sling          |
| TNT1    | TNT (1 stick)  |
| TNT2    | TNT (5 sticks) |
+---------+----------------+
7 rows in set (0.00 sec)

mysql> select p1.prod_id, p1.prod_name 
	-> from products as p1, products as p2
    -> where p1.vend_id = p2.vend_id and p2.prod_id = 'DTNTR';
+---------+----------------+
| prod_id | prod_name      |
+---------+----------------+
| DTNTR   | Detonator      |
| FB      | Bird seed      |
| FC      | Carrots        |
| SAFE    | Safe           |
| SLING   | Sling          |
| TNT1    | TNT (1 stick)  |
| TNT2    | TNT (5 sticks) |
+---------+----------------+
7 rows in set (0.00 sec)
```

### 外联结

```mysql
mysql> select c.cust_id, o.order_num 
    -> from customers as c left outer join orders as o
    -> on  c.cust_id = o.cust_id;
+---------+-----------+
| cust_id | order_num |
+---------+-----------+
|   10001 |     20005 |
|   10001 |     20009 |
|   10002 |      NULL |
|   10003 |     20006 |
|   10004 |     20007 |
|   10005 |     20008 |
+---------+-----------+
6 rows in set (0.01 sec)
```

## 组合查询

- `UNION, INTERSECT, EXCEPT`

执行多个查询，并将结果作为单个查询结果集返回，这些组合查询通常称为并（union）

- `UNION`必须由两条或两条以上的`SELECT`语句组成
- `UNION`中的每个查询必须包含**相同的列，表达式，或聚集函数（列名次序可不同）**
- 默认取消重复行，保留可使用`UNION ALL`

```mysql
mysql> select vend_id, prod_id, prod_price
    -> from products
    -> where prod_price <= 5
    -> UNION
    -> select vend_id, prod_id, prod_price
    -> from products
    -> where vend_id in (1001,1002)
    -> order by vend_id, prod_price;
+---------+---------+------------+
| vend_id | prod_id | prod_price |
+---------+---------+------------+
|    1001 | ANV01   |       5.99 |
|    1001 | ANV02   |       9.99 |
|    1001 | ANV03   |      14.99 |
|    1002 | FU1     |       3.42 |
|    1002 | OL1     |       8.99 |
|    1003 | TNT1    |       2.50 |
|    1003 | FC      |       2.50 |
|    1003 | SLING   |       4.49 |
+---------+---------+------------+
8 rows in set (0.02 sec)
```

## 数据操作

### 插入数据

```mysql
# 插入所有列值
insert [IGNORE] into 表名 values(值1，值2，...);
# IGNORE:忽略重复数据/唯一索引

# 插入特定列值
insert into 表名(列名1， 列名2，...) values(值1，值2，DEFAULT,...);

# 从其他表复制数据，列名数量相同
insert into 表名(列名1， 列名2，...) select子句

# 列名匹配, 没有value
insert into 表名 select子句
```

### 更新数据

```mysql
# 如果没有where子句，则修改整张表
update 表名 set 列名1 = 列值1,  列名2 = 列值2, ... where子句;

mysql> update customers set cust_email = 'elmer@fudd.com',  cust_name='The Fudds' where cust_id = 10005;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update customers set cust_email = NULL where cust_id = 10005;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

### 删除数据

```mysql
# 如果没有where子句，则删除表中所有行
delete from 表名 where子句;

# 速度比delete快
# 原理：删除原来的表并重新创建一个表
truncate 表名;
```

## 表操作

### 创建表

```mysql
create table 表名
(
    列名 数据类型， 约束
    表级约束
) ENGINE=InnoDB  charset=utf8;

# 约束:
NOT NULL, # 默认允许NULL
AUTO_INCREMENT = 100， # 从100开始，每增加一行自动递增，增量默认为1
DEFAULT 列值，
primary key,
unique
enum("列值1", "列值2", ...)

#表级约束
primary key(列名, ...)
unique key(列名, ...)
foreign key (列名) references 表名(列名)
# 子表引用父表,自动为父表的外键约束列创建索引
# 对父表进行update和delete时
# cascade：子表级联更新
# set null： 子表被更新为NULL值
# NO ACTION：抛出错误，不允许更改
# RESTRICT：抛出错误，不允许更改 default

mysql> create table person(
    -> id int,
    -> sex enum("male", "female"));
Query OK, 0 rows affected (0.04 sec)

mysql> insert into person select 1, "male";
Query OK, 1 row affected (0.01 sec)
Records: 1  Duplicates: 0  Warnings: 0

mysql> insert into person select 1, "boy";
ERROR 1265 (01000): Data truncated for column 'sex' at row 1
```

### 更改表

```mysql
# 增加列
alter table 表名 add [column] 列名， 数据类型;

# 删除列
alter table 表名 drop [column] 列名;

# 修改列属性
alter table 表名 modify [column] 列名, 数据类型;

# 定义外键
alter table 表名1
add constraint 外键名(fk_表名1_表名2)
foreign key(列名1) references 表名2(列名2)



mysql> alter table vendors add vend_phone char(20);
Query OK, 0 rows affected (0.07 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> alter table vendors drop vend_phone;
Query OK, 0 rows affected (0.11 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

### 删除表

```mysql
drop table 表名；
```

### 重命名表
```mysql
rename table 旧表名 to 新表名;
```

## 视图

- 定义：虚表，修改视图会修改原始表，因为数据库中只存放视图的定义（select语句），不存放视图对应的数据。
- 优点：
  - 重用SQL语句
  - 简化复杂的SQL操作
  - 使用表的组成部分而不是整个表
  - 保护数据。可以给用户授予表的特定部分的访问权限而不是整个表的访问权限
  - 更改数据格式和表示。视图可返回与底层表的表示和格式不同的数据
- 规则：
  - 视图名唯一，视图可以嵌套，可以和表一起使用
  - 不能有索引，触发器或默认值

```mysql
# 创建视图
create view 视图名 as select子句 [with check option];

# with check option: 对视图进行插入时，将禁止不满足视图的元祖插入。

# 参看创建视图的语句
show create view 视图名;

# 删除视图
drop view 视图名;


mysql> create table t(id int);
Query OK, 0 rows affected (0.07 sec)

mysql> create view v_t
    -> as select * from t where id < 10;
Query OK, 0 rows affected (0.05 sec)

mysql> insert into v_t select 20;
Query OK, 1 row affected (0.04 sec)
Records: 1  Duplicates: 0  Warnings: 0

mysql> select * from t;
+------+
| id   |
+------+
|   20 |
+------+
1 row in set (0.00 sec)

mysql> select * from v_t;
Empty set (0.00 sec)

mysql> alter view v_t
    -> as select * from t where id<10
    -> with check option;
Query OK, 0 rows affected (0.04 sec)

mysql> insert into v_t select 20;
ERROR 1369 (HY000): CHECK OPTION failed 'test.v_t'
```

## 触发器

只在执行`DELETE， INSERT， UPDATE`语句时才有触发器

## 事务

### 概念

- 事务(transaction)：一组SQL语句，逻辑上的一组操作，要么都执行，要么都不执行。；

- 特性

  - 原子性（Atomicity）：事务是最小的执行单位，不可分割

  - 一致性（consistency）：事务执行前后，数据保持一致
  - 隔离性（Isolation）：并发访问数据库时，一个用户的事务不被其他事务干扰
  - 持久性（durability）：事务提交后，对数据库中的数据的改变是永久的

- 开启事务：`START TRANSACTION | BEGIN`

- 回退(rollback)：指撤销指定SQL语句的过程；
  
- 只能回退`insert, update, delete`，不能回退`create,drop`;
  
- 提交(commit)：指将未存储的SQL语句结果写入数据库表；
  - 一般情况下，对数据表的操作时   隐含提交（implicit commit）
  - **在事务中，需要显式提交，一旦提交，无法rollback**
  
- 保留点(savepoint)：指事务处理中设置的临时占位符(placeholder)，你可以对它发布回退（与回退整个事务处理不同）
  - `savepoint 保留点名称`
  - `rollback to 保留点名称`
  - `release savepoint 保留点名称`
  
- 事务隔离级别

  - `set transaction 隔离级别`
  - `read uncommitted, read committed, repeatable read, serializable`

### 实践

```mysql
############################rollback#################################
mysql> select * from test;
+----+--------+
| id | name   |
+----+--------+
|  1 | 小明   |
+----+--------+
1 row in set (0.00 sec)

mysql> start transaction;
Query OK, 0 rows affected (0.00 sec)

mysql> delete from test;
Query OK, 1 row affected (0.01 sec)

mysql> select * from test;
Empty set (0.00 sec)

mysql> rollback;
Query OK, 0 rows affected (0.01 sec)

mysql> select * from test;
+----+--------+
| id | name   |
+----+--------+
|  1 | 小明   |
+----+--------+
1 row in set (0.00 sec)

############################commit#################################
mysql> select * from test;
+----+----------+
| id | name     |
+----+----------+
|  1 | xioaming |
+----+----------+
1 row in set (0.00 sec)

mysql> start transaction;
Query OK, 0 rows affected (0.00 sec)

mysql> delete from test;
Query OK, 1 row affected (0.00 sec)

mysql> commit;
Query OK, 0 rows affected (0.04 sec)

mysql> rollback;
Query OK, 0 rows affected (0.00 sec)

mysql> select * from test;
Empty set (0.00 sec)
```

## 字符集

- 字符集：字母和符号的集合
- 编码：某个字符集成员的内部表示
- 校对：规定字符如何比较的指令

```mysql
############################################修改默认字符编码#################################################
mysql> show variables like '%char%';
+--------------------------+---------------------------------------------------------+
| Variable_name            | Value                                                   |
+--------------------------+---------------------------------------------------------+
| character_set_client     | utf8                                                    |
| character_set_connection | utf8                                                    |
| character_set_database   | latin1                                                  |
| character_set_filesystem | binary                                                  |
| character_set_results    | utf8                                                    |
| character_set_server     | latin1                                                  |
| character_set_system     | utf8                                                    |
| character_sets_dir       | C:\Program Files\MySQL\MySQL Server 5.7\share\charsets\ |
+--------------------------+---------------------------------------------------------+
8 rows in set, 1 warning (0.00 sec)


mysql> set character_set_database=utf8;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> set character_set_server=utf8;
Query OK, 0 rows affected (0.00 sec)

mysql> show variables like '%char%';
+--------------------------+---------------------------------------------------------+
| Variable_name            | Value                                                   |
+--------------------------+---------------------------------------------------------+
| character_set_client     | utf8                                                    |
| character_set_connection | utf8                                                    |
| character_set_database   | utf8                                                    |
| character_set_filesystem | binary                                                  |
| character_set_results    | utf8                                                    |
| character_set_server     | utf8                                                    |
| character_set_system     | utf8                                                    |
| character_sets_dir       | C:\Program Files\MySQL\MySQL Server 5.7\share\charsets\ |
+--------------------------+---------------------------------------------------------+
8 rows in set, 1 warning (0.00 sec)

###########################################修改表的字符编码################################################

mysql> show create table test;
+-------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                              |
+-------+-------------------------------------------------------------------------------------------------------------------------------------------+
| test  | CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` char(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

mysql> alter table test character set utf8;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> show create table test;
+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                                                 |
+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| test  | CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` char(2) CHARACTER SET latin1 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
+-------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

mysql> alter table test modify column name char(2) character set utf8;
Query OK, 1 row affected (0.06 sec)
Records: 1  Duplicates: 0  Warnings: 0

mysql> show create table test;
+-------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                            |
+-------+-----------------------------------------------------------------------------------------------------------------------------------------+
| test  | CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` char(2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
+-------+-----------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
```

## 索引

索引可以增加查询的速度，但是过多的索引可能会降低应用程序的性能。InnoDB会根据表的使用情况自动为表生成哈希索引。

### B+树索引

- 高度平衡
- 非叶子节点不保存数据，只进行数据的索引；
- 叶子节点存放着所有的数据
- 所有叶子节点链接形成一个线性链表

> 高度平衡：左右子树高度之差<1

#### 聚集索引

聚集索引（clustered index）按照每张表的主键构造一颗B+树，叶子节点存放表的多个行记录数据，每个数据页通过一个双向链表进行链接。实际的数据页只能按照一颗B+树进行排序，所以每张表只能拥有一个聚集索引。

数据页上存放的是完整的每行的记录，非数据页的索引页，存放的仅仅是键值以及指向数据页的偏移量

> 键值：主键的值
>
> 数据页：叶子节点

聚集索引的存储并不是物理上连续的而是逻辑上连续的。因为：

- 数据页通过双向链表连接，页按照主键的顺序排序
- 每个页中的记录也是通过双向链表进行维护

优点：

- 对于主键的排序查找和范围查找速度非常快

#### 辅助索引

也称为非聚集索引（secondary index），叶子节点不包含行记录的全部数据，叶子节点包含键值，及索引行，索引行中包含一个书签（bookmark），该书签与行数据映射。所以书签就是相应行数据的聚集索引键。

#### 联合索引

对表上的多个列进行索引，联合索引本质上也是一颗二叉树

#### 覆盖索引

从辅助索引中就可以得到查询的记录，而不需要查询聚集索引中的记录

#### 索引管理

```mysql
alter table 表名
add {index | key}  [index_name]
[index_type] (key_part,...) [index_option] ...

create [unique] index index_name
[index_type]
on tbl_name (index_col_name, ...)

drop index index_name on tbl_name

show index from tbl_name
```

### 哈希索引

InnoDB使用哈希算法来对字典进行查找，采用链表方式解决冲突。哈希索引经哈希函数映射到一个哈希表中，对于字典类型的查找非常快速，但是对于范围查找就无能为力了

> 字典类型查找：select * from table where index_col='xxx'

### 全文检索

#### 倒排索引

## 锁

### 锁的类型

#### 针对行数据

- 共享锁（S Lock），允许**事务读一行数据**

  > S share，事务，读， 一行数据

- 排他锁（X Lock），允许**事务删除或更新一行**数据

> 只有 S 锁相互兼容，锁的对象是行记录

#### 针对表级别的锁

意向锁（Intention Lock），目的是为了在一个事务中揭示下一行将被请求得锁的类型

- 意向共享锁（IS Lock），事务想要获得一张表中某几行的共享锁
- 意向排他锁（IX Lock），事务想要获得一张表中某几行的排他锁

### 锁问题

#### 脏读

一个事务可以读到另外一个事务中**未提交**的数据，违反了数据库的隔离性

发生在READ UNCOMMITTED（读取未提交），InnoDB的默认事务隔离级别为READ REPEATABLE

#### 不可重复读

 一个事务可以读到另外一个事务中**已提交**的数据，违反了数据库的一致性

发生在READ COMMITTED（读取已提交）

#### 丢失修改

一个事务的更新操作会被另一个事务的更新操作覆盖，从而导致数据的不一致

在当前数据库的任何隔离级别下，都不会导致数据库理论意义上的丢失修改，因为即使是READ UNCOMMITED的事务隔离，对于行的DML操作，需要对行或其他粗粒度级别的对象加锁。

## 其他

数据库：物理操作系统文件或其他形式文件类型的集合

数据库实例：MySQL数据库由后台线程以及一个共享内存区组成

```mysql
mysql> show engines\G
*************************** 1. row ***************************
      Engine: InnoDB
     Support: DEFAULT
     Comment: Supports transactions, row-level locking, and foreign keys
Transactions: YES
          XA: YES
  Savepoints: YES
*************************** 2. row ***************************
      Engine: MRG_MYISAM
     Support: YES
     Comment: Collection of identical MyISAM tables
Transactions: NO
          XA: NO
  Savepoints: NO
```

连接MySQL操作是一个连接进程和MySQL数据库实例进行通信，本质是进程通信，有管道，命名管道，命名字，TCP/IP套接字、UNIX域套接字



InnoDB为MySQL的默认引擎，支持事务，行级锁，外键，有保存点。基于磁盘的数据库系统，通过使用缓冲池技术来协调CPU速度与磁盘速度之间的鸿沟。

在InnoDB存储引擎中，表是根据主键顺序组织存放的，称为索引组织表（index organized table）。每个表都有主键，在创建表时没有显示定义主键，则先判断表中是否有非空的唯一索引（Unique Not Null）,如果有，则该列即为主键。如果没有，自动创建一个6个字节大小的指针



## MySQL Again

bin目录下的可执行文件
mysqld：直接启动一个服务器程序
mysqld_safe：间接调用mysqld，监控服务器运行状态，服务器进程出错时会自启动
mysql.server：间接调用 mysqld_safe

将mysql注册为windows服务
"可执行文件的的全路径" --install [-manual] [服务名]
net start 服务名
net stop 服务名

短形式参数（单短划线） -h
长形式参数（双短划线） --host

客户端和服务器之间的通信本质是进程间通信
1 TCP/IP
2 命名管道和共享内存
3 UNIX 域套接字

C/S交互过程
1. 连接管理
2. 查询缓存（8.0后被删除）解析与优化
3. 存储引擎

查询优化后会生成执行计划，交给存储引擎(表处理器)获取数据，存储引擎接口以记录为单位



启动选项（startup option）：程序在启动时指定的设置，也可以在配置文件(选项文件)中配置
多个配置文件my.ini 中设置了相同的启动选项 ，后执行的会覆盖前面的配置
系统变量：程序在运行时影响程序行为的变量
show [GLOBAL|SESSION] variables [like xxx ]
系统变量作用范围
- GLOBAL：全局变量
- SESSION：会话变量
  每个新连接到服务器的用户都会从GLOBAL拷贝一份系统变量（SESSION范围），

状态变量：程序运行时的状态
show [GLOBAL|SESSION] status [like xxx]

utf8mb3，阉割版的UTF-8, 只用1~3个字节
utf8mb4 标准的UTF-8

字符串在计算机上的体现为一个字节序列



### innodb 行格式

1. COMPACT

2. REDUNDANT， before 5.0, 

3. DYNAMIC，5.7版本默认，溢出列记录溢出页的地址

4. COMPRESSED：对页进行压缩

  

COMPACT 格式
变长字段长度 列表（字节） | NULL值列表 |记录头信息|隐藏列|列1的值|...|列n的值

变长字段：字段数据类型为varchar(m)，VARBINARY(M)，各种TEXT类型，BLOB类型的字段

varchar(m) 最多可存储m个**字符**，一个字符由w个字节表示



变长字段长度列表（字节）：值为非null的列的长度（字节数）

NULL值列表：一个二进制位序列，与列顺序相反，记录哪些列为null，为null的二进制位为1
记录头信息：长40位

记录头信息：

| 名称         | 大小（位） | 描述                                                         |
| ------------ | ---------- | ------------------------------------------------------------ |
| delete_flag  | 1          | 0：未删除，1：删除。如果直接将记录从页中删除，那么页中的其他记录还需重新排序，从而浪费性能。可以通过将这些标记为删除的记录组成一个垃圾列表，后续新增记录时覆盖这些标记为删除的记录 |
| min_rec_flag | 1          | B+树中每层非叶子节点中最小的目录项记录其值为1                |
| n_owned      |            | 将记录分组，每组中的最后一条记录中的n_owned字段记录该组有多少条记录（包括记录本身） |
| heap_no      | 13         | 记录在页面堆中的相对位置。所有的记录组成一个堆。创建页的时候同时MySql默认会增加两条记录，Infimum记录和Supremum记录，他们的heap_no 分别为0和1。Infimum表示页中的最小记录，Supremum表示页中的最大记录。这里的大小指的是主键的大小 |
| record_type  | 3          | 0：普通记录，1：B+数非叶子节点的**目录项记录**，2：Infimum记录，3：Supremum记录。目录项记录只有主键值和页号两列 |
| next_record  |            | 表示从当前记录的**真实数据**到下一条记录的真实数据的距离（偏移量）。Infimum记录的下一条记录是主键值最小的记录，Supremum记录的上一条记录时主键值最大的记录。记录间通过next_record字段组成了一个按照主键升序的单向链表。 |

删除一个行记录时，会将delete_flag 置为1，同时将next_record值修改为到下下一条记录真实数据的距离

隐藏列：

- DB_ROW_ID：表中无主键时才添加该隐藏列
- DB_TRX_ID
- DB_ROLL_PTR

主键生成规则：

1. 优先使用用户定义的主键
2. 如果用户未定义, 选取不为NULL值的UNIQUE键作为主键
3. 为表默认添加一个row_id 隐藏列作为主键



如果一个列的数据长度非常大（溢出列， off-page 列），记录只存储该列的一部分数据，把剩下的数据存储大其他页中（溢出页）

### 页

数据存储在磁盘中，页是磁盘和内存交互的基本单位，默认16kb

索引页（数据页）：存放行记录的页



页内空间分布：主要分成7部分

| 名称             |          | 描述                                                         |
| ---------------- | -------- | ------------------------------------------------------------ |
| File Header      | 页维度   | 页本身的信息，包含FILE_PAGE_PREV, FILE_PAGE_NEXT             |
| Page Header      | 记录维度 | 数据页的状态信息，统计信息                                   |
| Infimum+Supremum |          |                                                              |
| User Records     |          | 保存用户插入的行记录                                         |
| Free Space       |          | 页中未使用的部分                                             |
| Page Directory   |          | 将记录分组，每个分组（组间组内都有序）中最后一条记录的地址偏移量作为一个Slot，按照顺序存储到Page Directory中。Infimum所在的分组只有其本身一条记录，supremum所在的分组的记录数为1-8，其他的记录数为4-8 |
| File Trailer     |          | 校验页的完整性，通过比较File Header 中的校验和与File Trailer中校验和是否相同来校验页的完整性 |

PS:

1.   页在磁盘上的位置不是相互挨着的，所以页与页之间通过File Header 部分中的FILE_PAGE_PREV, FILE_PAGE_NEX 组成一个双向链表

如何在**一个页**中根据**主键**查找数据？

1. 通过二分法确定该记录所在的slot，并找到该槽所在分组中主键值最小的记录。slot之间在物理空间上相连
2. 通过记录中的next_record 属性遍历该槽所在的组中的各个记录。记录之间通过next_record形成一个按照主键值升序的单向链表

### 索引

通过主键查找指定一条记录时，如果用户数据量小，用户数据都在一个数据页中，用户可以通过上述方法快速定位到指定记录。而当用户数据量非常大时，数据会占用非常多的数据页。虽然数据页之间是一个按照主键值大小排序的双向链表，但是定位记录时需要先定位到页，那么需要遍历页链表来定位十分耗时。所以参考Page Dictory，用一个数据页来保存目录项记录（主键值和页编号），查找记录时先查找目录项记录来定位目的记录所在的数据页。

索引就是一颗B+树，页可以看成B+树的节点，

- 非叶子节点（内节点）：存放目录项记录的节点
- 叶子节点：存放用户数据的节点

InnoDB 索引分类：

- 聚簇索引：以**主键值的大小作为页和记录的排序规则**，叶子节点存放记录的所有列，所以 "索引即数据,数据即索引”。非叶子节点中的目录项记录保存（页中最小主键值和页编号）
- 二级索引（辅助索引）：**以索引列的大小作为页和记录的排序规则**，叶子节点存放只记录的索引列和主键值，非叶子节点中的目录项记录保存（页中最小主键值+索引值+页编号）。**如果查找时查找非索引列的值，需要根据主键信息到聚簇索引中查找完整的用户信息**。该操作称为回表查询。
- 联合索引：多个列的大小作为页和记录的排序规则

InnoDB 在创建表示就创建了一棵聚簇索引，此时只有一个根节点，插入记录时会直接在根节点中插入记录，当根节点可用空间用完时，创建一个新的页A，并将根节点中的所有记录复制到页A中，并对页A进行页分裂操作，得到新的页B。根节点晋升为存储目录项的页。所以根节点创建时就不再移动。

MyISAM的数据和索引是分开的。



索引缺点：

1. 空间上：创建索引需要占用磁盘空间
2. 时间上：对数据进行增删时，都需要修改索引
3. 



 ```sql
select * from table where id>= 2 and id <= 100
扫描区间：[2,100]
边界条件：id>= 2 and id <= 100

select * from table where key_part1 <= 'b' and key_part2 = 'a';
扫描区间：((负无穷，负无穷), ('b','a')]
边界条件：key_part1 <= 'b' and key_part2 = 'a'
从二级索引的最左边一直扫描到 key_part1 = 'b' and key_part2 = 'a'
 ```

文件排序：在内存或磁盘中排序



索引可以减少扫描的记录数量，可以用于排序（不能混用ASC, DESC）和分组

Advice

1. 只为用于搜索，排序，分组的列创建索引
2. 索引列的值应尽量唯一，减少回表操作
3. 索引列的类型尽量小，为了让一个目录项页存储更多的目录，从而减少磁盘IO
4. 只为索引列前缀创建索引（索引列前缀有序），减少索引占用的存储空间 add index idx_key1(key1(10))
5. 查询列表中尽量使用索引列进行查询，而不是使用slect *。减少回表操作
6. 让索引列以单独的列名出现在搜索条件中，id*2 < 4 会使索引失效
7. 为了减少聚簇索引（页中的记录按照主键值大小排序）发生页面分裂，建议使用让主键拥有AUTO_INCREMENT
8. 避免创建表的冗余和重复索引，idx_union_key(key1, key2) 覆盖了idx_key1(key1)，没必要创建idx_key1

### 数据目录

存储引擎将数据存储在文件系统上（磁盘）

运行过程中的数据存储在数据目录上

```
SHOW VARIABLES LIKE 'datadir'

一个database 对应一个目录
db.opt 数据库描述文件
t_book.frm 表t_book的结构信息
t_book.ibd 独立表空间，存储表t_book的数据

 D:\phpstudy_pro\Extensions\MySQL5.7.26\data\bookshop 的目录
2023/06/24  11:26                61 db.opt     
2023/06/24  11:26             8,956 t_book.frm：
2023/06/24  11:26            98,304 t_book.ibd
2023/06/24  11:26             8,770 t_order.frm
2023/06/24  11:26           114,688 t_order.ibd

SHOW DATABASES;
information_schema： 用户创建的数据库信息，有哪些表，哪些列，视图，索引，只保存描述性信息，不报错数据
bookshop            
learnjdbc           
mysql               ：存储用户信息，存储过程，事件，日志信息
performance_schema  ：运行时的状态信息，性能监控
spring_again        
sys    : 通过视图将 information_schema 和performance_schema关联
```

为了更好的管理页，引入了表空间概念。一个表空间对应文件系统中一个或多个文件

-  系统表空间（system tablespace）：数据目录下的ibdata1 文件，一个MySQL服务器中只有一份，在版本5.5.7-5.6.5 之间，表中的数据默认存储到这个文件中
- 独立表空间(file-per-table tablespace)：在版本5.6.6以及之后的版本，MySQL 会为每一张表创建一个独立表空间。文件名为  表名.ibd
- 通用表空间，undo表空间，临时表空间

MyISAM 

- test.frm
- test.MYD 数据文件
- test.MYI 索引文件



### 事务

事务：Transaction,  一次交易

Atomicity：要么全做，要么全不做

Isolation: 两个事务之间互不影响

Consistency: 数据符合现实世界的约束

Durability: 修改的数据都在磁盘中保留



show variables like 'autocommit';

自动提交：自动提交事务开启时，每条语句都是一个独立的事务。

非自动提交事务：关闭自动提交事务或者使用begin开启一个新的事务，则多条语句属于同一个事务，需要手动输入commit 来提交事务或者输入roallback 回滚事务。

隐式提交：当当前事务为非自动提交时，输入DDL语句，BEGIN 新开事务时会自动提交上一个事务



```
开启事务
BEGIN; -- 等价 START TRACTION [READ ONLY|READWRITE]; READWRITE DEFAULT 
....
COMMIT;

回滚事务
BEGIN;
...
SAVEPOINT s1;
....
READWRITE s2;
ROLLBACK to  s1;
```

