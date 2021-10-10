Geek
数据类型
1. 字符型，以ASCII码的格式存储，
	单位（字节）
	varchar2，0-4000，可变长度的字符串
	nvarchar2，0-1000，用来存储Unicode字符集的变长字符型数据
	char,0-2000,定长
	nchar,0-1000,
	long, 0-2GB
2. 数字型
	number(p, s), p最大精度是38位（十进制），p精度，s小数位数，用来存储定长的整数和小数
	float, 126位数据（二进制），1-126
3. 日期类型
	date, 精确到秒
	timestamp, 精确到小数秒
4. 其他数据类型
	blob, 0-4GB, 存储二进制数据
	clob, 0-4GB，存储字符串数据
	bfile, 大小与操作系统有关，用来吧非结构化的二进制数据存储在数据库以外的操作系统文件中

/ 或run  使用斜杠命令运行缓冲区中保存的SQL语句
list/edit  查看/编辑缓冲区中保存的SQL语句

DDL(数据定义语言)
DML（数据操纵语言）
DQL(数据查询语言)
DCL（数据控制语言）

```
CREATE [SCHEMA.]TABLE table_name
（
	column_name datatype [null|not null],
	column_name datatype [null|not null],
	...
	[constraint]
 )
 

ALTER TABLE table_name 
ADD column_name | MODIFY column_name | DROP COLUMN column_name
ADD CONSTRAINTS constraint_name PRIMARY KEY(column_name)
DROP CONSTRAINT constraint_name

DROP TABLE table_name;
 

 ```

DML
```
INSERT INTO  table_name(column_name1, column_name2, ...) VALUES (data1, data2...);
INSERT INTO table_name1(column_name1, column_name2,...)
Select column_name1, column_name2... FROM table_name2;

UPDATE table_name SET column_name1=data1, column_name1=data2, ...[WHERE condition];

DELETE FROM table_name [Where condition];
DELETE FROM table_name;
TRUNCATE TABLE table_name;
```

DQL
```
SELECT
	[DISTINCT|ALL]
		select_list
	FROM tbale_list
	[ where_clause ]
	[ group_by_clause ]
	[ HAVING condition ]
	[ order_by_clause]

select_list
	{ * | {[schema.]{table|view}.* | expr [[AS] c_alias]} }
order_by_clause
	ORDER BY 
		{expr | position | c_alias}
		[ASC|DESC]
		[NULLS FIRST | NULLS LAST]
			[,{expr | position | c_alias}
			  [ASC|DESC]
		 	  [NULLS FIRST | NULLS LAST]
			]...
where_clause
	1. 关系操作符
		<,<=,>,>=,=,!=,<>
	2.	比较操作符
		IS NULL, LIKE, BETWEEN...AND, IN
	3. 逻辑操作符
		AND, OR, NOT
group_by_clause
	GROUP BY
	{ expr
	| { ROLLUP | CUBE } ({expr[, expr]...})
	}
子查询
	ANY,SOME,ALL

|| 连接符
```
