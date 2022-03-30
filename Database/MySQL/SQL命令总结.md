## 常规操作

```mysql
net stop mysql

net start mysql

help select

show databases;
use 数据库名;
show 表名;

{EXPLAIN | DESCRIBE | DESC} 表名; 
等价于
show columns from 表名;

status

# 查看字符编码
show variables like '%char%';

# 参看创建表的语句
show create table 表名;

# 修改字符集为utf-8
set character_set_database = utf8;
set character_set_server = utf8;

delimiter 分隔符  -- 定义新的分隔符
```

## 查询

```mysql
select [all|distinct] 列名1 [as 别名], 列名2, ...
from [左表 [inner[left|right outer]] join 右表]
on 条件
where 子句
group by 列名
having 条件
order by 列名1, 列名2, ... [ASC|DESC] -- 默认为ASC

limit [offset], row_count, # offset default=0, 行索引从0开始
取第二高价格 order by price limit 1, 1 

/*
select distinct name, sex from tb_students; -- 如果姓名相同、性别不同是不会去重的
-- distinct 只能写在所有查询字段的前面
-- distinct 对后面所有的字段均起作用, 

group by`：可以包含任意数目的列，可以嵌套
  - 如果分组列中具有`NULL`值，则`NULL`作为一个分组返回。如果有多行`NULL`值，将其分为一组
  - 必须出现在`where`子句之后，`order by` 子句之前
- `where`过滤行，指定行对应的条件，`having`过滤分组，指定分组对应的条件
- `where`在数据分组前过滤，`having`在数据分组后过滤
*/

-- SQL执行顺序
FROM <left_table> <join_type> JOIN <right_table>
ON <join_condition>
WHERE <where_condition>
GROUP BY <group_by_list>
HAVING <having_condition>

SELECT
DISTINCT <select_list>

ORDER BY <order_by_condition>
LIMIT <limit_number>

-- -------------------------
where 子句
/*
算术操作符：=, <>, !=, <，<=, >, >=,
逻辑操作符：AND，OR, NOT，AND优先级高于OR
与字符比较时，按照*字典顺序*进行比较，即按照条目在字典中出现的顺序来进行排序，
-- 以相同字符开头的单词比不同字符开头的单词更相近。
*/

where 列名 算术操作符 值
where 列名 IS NULL
where 列名 算术操作符 值 逻辑操作符 列名 算术操作符 值
where 列名 in (值1， 值2) 等价于 where 列名=值1 OR 列名=值2


# 谓词
LIKE
- where 列 like 字符串
- %：匹配0个，1个或多个字符
- _：只能匹配一个字符

列 BETWEEN 值1 AND 值2
- 值1<= 列<=值2

NOT
- IS NULL, IS NOT NULL
- IN, NOT IN

EXISTS # 判读是否存在满足某种条件的记录

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
# 等价于 多个else if 语句
# 如果 when中的求值表达式为真，则返回THEN子句中的表示，
# 如果 when中的求值表达式为假，跳到下一个when子句中。
# 如果 when中的求值表达式都为假，执行ELSE中的子句，返回表达式的值
```

## 插入

```mysql
# 插入所有列值
insert [IGNORE] into 表名 values(值1，值2，...);
# IGNORE:忽略重复数据/唯一索引

# 插入特定列值
insert into 表名(列名1， 列名2，...) values(值1，值2，DEFAULT,...);

# 从其他表复制数据，列名数量相同
insert into 表名(列名1， 列名2，...) 
select子句

# 列名匹配, 没有value
insert into 表名
select子句
```

## 改

```mysql
# 如果没有where子句，则修改整张表
update 表名 set 列名1 = 列值1,  列名2 = 列值2, ... where子句;
```

## 删

```mysql
# 如果没有where子句，则删除表中所有行
delete from 表名 where子句;

# 速度比delete快
# 原理：删除原来的表并重新创建一个表
truncate 表名;
```

## 创建表

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

## 更改表

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

## 删除表

```mysql
drop table 表名；

rename table 旧表名 to 新表名;
```



## 系统函数

```mysql
# 常用函数
# 算术
abs()
mod(被除数，除数)
round(数，位数)
# 字符串函数
Concat('字符or列名', '字符or列名', '字符or列名', ...)
char_length(字符串)
replace(列名，old字符串, new字符串)
lower()
upper()
ltrim(), rtrim(), trim() # 只能删除左右两端的空格
as 别名
# 日期 yyyy-mm-dd
Date()# 提取列的日期部分 
year()
month() # 提取列的年份，月份部分 `yyyy, mm`
DATADIFF(expr, expr2)# 返回两个日期相减（expr1 − expr2 ）相差的天数
current_date
# 聚集函数
AVG(), COUNT(), MAX(), MIN(), SUM()
COUNT(*) # 统计表的函数，包括列值为`NULL`的行
COUNT(column) # 对特定列统计函数，不包括列值为`NULL`的行
```

