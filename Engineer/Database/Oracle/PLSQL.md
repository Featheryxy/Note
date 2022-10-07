# PL/SQL

## 简介

PL/SQL是Oracle数据库对SQL语句的扩展，PL/SQL的基本单位叫做块，由三个部分组成：

1. 声明部分
2. 执行部分
3. 异常处理部分

特点：

- 支持**事务控制**和SQL数据操作命令
- 它支持SQL的所有数据类型，并扩展了新的数据类型
- PL/SQL可以**存储在Oracle服务器**中
- 服务器上的PL/SQL 程序可以通过权限进行控制
- Oracle 有自己DBMS包，可以处理数据的控制和定义命令。

```sql
SQL> set  serveroutput on;
SQL> BEGIN
  2  DBMS_OUTPUT.PUT_LINE('这是执行部分...');
  3  END;
  4  /
这是执行部分...

SQL> DECLARE
  2  v_result number(8,2);
  3  BEGIN
  4  v_result := 100/6;
  5  DBMS_OUTPUT.PUT_LINE('最后结果是：'||v_result);
  6  END;
  7  /
最后结果是：16.67

DECLARE v_result NUMBER ( 8, 2 );
BEGIN
	v_result := 100 / 6;
	DBMS_OUTPUT.PUT_LINE ( '最后结果是：' || v_result );
	EXCEPTION 
		WHEN NO_DATA_FOUND THEN
		DBMS_OUTPUT.PUT_LINE ( '没有对应的编码' );
END;
/
```

## 书写规范

1. 变量命名应该使用**下划线**连接

2. **变量应该加前缀**，用以区分数据类型和作用；

3. **字符和日期**应该使用**单引号**括起

4. 单行注释：“--”

5. 多行注释：“/\*...\*/”

## 变量的使用

**临时变量**：只在使用它的SQL语句中有效，值不能保留

**已定义变量**：一直保留到被显示地删除、重定义或退出SQL*Plus为止。

```sql
-- 声明变量的语法结构
variable_name datatype
	[
		[NOT NULL]
		{:= | DEFAULT}expression
	];

-- 常量声明
constant_name CONSTANT datatype
	[NOT NULL]
	{:=|DEFAULT} expression;

v_productid productinfo.productid%TYPE;
-- v_productid 和productinfo.productid类型一致

select var into variable_name from table_name;  
```

当使用NOT NULL属性时，大括号里的内容必填

```sql
--  DEF[INE] [variable] | [variable = text]

SQL> define v_deptno=10

SQL> define v_deptno
DEFINE V_DEPTNO        = "10" (CHAR)

SQL> define -- 查看当前会话所有变量
DEFINE _DATE           = "27-1月 -21" (CHAR)
DEFINE _CONNECT_IDENTIFIER = "orcl" (CHAR)
DEFINE _USER           = "SCOTT" (CHAR)
DEFINE _PRIVILEGE      = "" (CHAR)
DEFINE _SQLPLUS_RELEASE = "1102000100" (CHAR)
DEFINE _EDITOR         = "Notepad" (CHAR)
DEFINE _O_VERSION      = "Oracle Database 11g Enterprise Edition Release 11.2.0.1.0 - 64bit Production
With the Partitioning, OLAP, Data Mining and Real Application Testing options" (CHAR)
DEFINE _O_RELEASE      = "1102000100" (CHAR)
DEFINE _RC             = "0" (CHAR)
DEFINE V_DEPTNO        = "10" (CHAR)

SQL> undefine v_deptno;

SQL> select deptno, dname, loc from dept
  2  where deptno=&v_deptno;
输入 v_deptno 的值:  10
原值    2: where deptno=&v_deptno
新值    2: where deptno=10

    DEPTNO DNAME                        LOC
---------- ---------------------------- --------------------------
        10 ACCOUNTING                   NEW YORK

SQL> set verify off
SQL> /
输入 v_deptno 的值:  10

    DEPTNO DNAME                        LOC
---------- ---------------------------- --------------------------
        10 ACCOUNTING                   NEW YORK
```

/ 或run  使用斜杠命令运行缓冲区中保存的SQL语句

list/edit  查看/编辑缓冲区中保存的SQL语句

## 流程控制

### IF

```sql
IF condition THEN
	statements;
END IF;

IF condition THEN
	statements;
ELSE
	statements;
END IF;

IF condition1 THEN
	statements;
ELSEIF condition2 THEN
	statements;
[ELSE statements;]
END IF;

-- 简单CASE语句
[<<label_name>>]
CASE case_operand
WHEN whern_operand THEN statement;
[WHEN when_operand THEN statement;]...
[ELSE statement [statement]]...;
END CASE [label_name];

-- 搜索CASE语句
[<<label_name>>]
CASE 
WHEN boolean_expression THEN statement;
[WHEN boolean_expression THEN statement;]...
[ELSE statement [statement]]...;
END CASE [label_name];
```

### LOOP

```sql
[<<label_name>>]
LOOP
	statement...
IF v_num > 5 THEN
	DBMS...
	EXIT;
END IF;
END LOOP [label_name]

DECLARE
	v_num NUMBER(8):=1;
	BEGIN
		<<basic_loop>>
		LOOP
			DBMS_OUTPUT.PUT_LINE('当前v_num变量的值是：' || v_num);
			v_num := v_num+1;
			IF v_num > 5 THEN
				DBMS_OUTPUT.PUT_LINE('退出！当前v_num变量的值是：' || v_num);
				EXIT basic_loop;
			END IF;
		END LOOP;
		DBMS_OUTPUT.PUT_LINE('循环LOOP已经结束！');
	END;

DECLARE
	v_num NUMBER(8):=1;
	BEGIN
		<<basic_loop>>
		LOOP
			DBMS_OUTPUT.PUT_LINE('当前v_num变量的值是：' || v_num);
			v_num := v_num+1;
			EXIT basic_loop WHEN v_num > 5;
		END LOOP;
		
		DBMS_OUTPUT.PUT_LINE('退出！当前v_num变量的值是：' || v_num);
		DBMS_OUTPUT.PUT_LINE('循环LOOP已经结束！');
	END;
```