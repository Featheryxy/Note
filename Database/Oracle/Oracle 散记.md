- 数据文件是数据库的物理存储单位，数据存储在表空间（由多个数据文件组成）
- 表空间是数据文件的逻辑映射，一个数据库在逻辑上被分成多个表空间（都包含system表空间）
- 用户是在实例下建立的。不同实例中可以建相同名字的用户

创建过程： 表空间--->用户--->表;
所属关系： 表空间 包含 用户 和 表



- **用户**是用来连接数据库访问数据库

- **模式**是数据库对象的集合。模式对象是数据库数据的逻辑结构。

查看所有tablespace

	-- 打印错误信息
	dbms_output.put_line('**Error line: '||dbms_utility.format_error_backtrace());
	dbms_output.put_line('**Error code: '||SQLCODE);
	dbms_output.put_line('**Error info: '||SQLERRM);


​	CREATE [OR REPLACE] FUNCTION function_name [(argment [ { IN| IN OUT }] type,...)]
​	RETURN return_type  
​	{ IS | AS }
​	<变量名 变量类型(长度)> 
​	BEGIN
​	FUNCTION_body
​	EXCEPTION
​	异常处理语句
​	END;
​	
​	--IN:输入参数，向存储过程传递值，默认类型，可以不写
​	--OUT:输出参数，用于返回结果。
​	--IN OUT：作为IN参数向存储过程传递值，同时作为OUT参数返回值。
​	--REPLACE：指明若已有同名的存储过程存在，那么将被替换成当前创建的版本。
​	--RETURN只能返回单个值，不能返回多个值。
​	--可以使用DEFAULT关键字为输入参数指定默认值。




```
一个汉字在Oracle数据库里占多少字节跟数据库的字符集有关，UTF８时，长度为三。
```



## 一、单引号

### 1.引用一个字符串常量，也就是界定一个字符串的开始和结束

```sql
    select * from t_sys_user where id='15';  --查询id为15的字符
    
    select * from t_sys_score where id=15;  --查询id为15的整形数字
```

### 2.转义符，对紧随其后出现的字符(单引号)进行转义 

```sql
    select ' '' ' result from dual; --第二个单引号被作为转义符,第三个单引号被转义.结果为 '
    
    select 'name''''' result from dual; --结果为name''
    
    select 'name'||'''' result from dual;  --结果为name','||' 被转义为字符拼接
    
    select 'hello' from dual;
```

## 二、双引号

**关键字、对象名、字段名、别名、表名**加双引号，则示意 Oracle将**严格区分大小写**，否则Oracl都默认大写。 

```sql
    --关键字
    select "sysdate" from dual;  -- 等同于select sysdate from dual; 
    
    --字段名 
    select * from emp where "ENAME" = scott; --双引号提示oracle严格区分大小写,ename将报错
    
    --别名
    select ename "姓 名",sal "$工资" from emp; --别名中若有特殊字符或关键字,需要双引号包住
    
    SELECT "hello" FROM dual; -- error，hello 标识符无效
```

https://blog.csdn.net/mmake1994/article/details/85982743



## Bug

```plsql
create table a (ca int,cb integer,cc long); -- ok
create table a (ca int(11),cb integer,cc long); -- ORA-00907: 缺失右括号


-- ORA-01950: 对表空间 'USERS' 无权限
ALTER USER XT60PUB quota unlimited on users;
```



```sql
   create  or  replace  procedure  p_create_table  
   is
   begin
   Execute  Immediate  'create table create_table(id int)' ;
   end  p_create_table;
   
   SQL>  exec  p_create_table;
 
   begin  p_create_table;  end ;
 
   ORA-01031: 权限不足
   ORA-06512: 在 "SUK.P_CREATE_TABLE" , line 3
   ORA-06512: 在line 1
   
   
   create  or  replace  procedure  p_create_table  
   Authid Current_User  is
   begin
   Execute  Immediate  'create table create_table(id int)' ;
   end  p_create_table;
 
   --再尝试执行：
   SQL>  exec  p_create_table;
 
   PL/SQL  procedure  successfully completed
```

## 散记

```sql

请输入用户名:  sys as sysdba
输入口令:

Oracle是不支持创建自定义模式的，想要创建模式的话只能新建一个用户，每个用户会有一个默认的和用户名相同的模式

create user 用户名 identified by 口令[即密码];

drop user 用户名 cascade;

SQL> create user ot identified by 213213;

用户已创建。

SQL> grant connect, resource, dba to ot;

授权成功。

SQL> connect ot
输入口令:
已连接。

SQL> @path_to_sql_file

SQL> connect scott;
输入口令:
已连接。
SQL> select table_name from user_tables order by table_name;

TABLE_NAME
------------------------------------------------------------
BONUS
DEPT
EMP
SALGRADE
```





```plsql
SQL> set linesize 32767
SQL> set pagesize 1000;
SQL> select username, account_status from dba_users;

USERNAME                                                     ACCOUNT_STATUS
------------------------------------------------------------ ----------------------------------------------------------------
MGMT_VIEW                                                    OPEN
SYS                                                          OPEN
SYSTEM                                                       OPEN
DBSNMP                                                       OPEN
SYSMAN                                                       OPEN
XT60PUB1                                                     OPEN
SCOTT                                                        OPEN
OT                                                           OPEN
XT60PUB2                                                     OPEN
XT60PUB

SQL> alter user scott account unlock;

用户已更改。

SQL> alter user scott identified by 213213;

用户已更改。


SQL> show user;
USER 为 "SYSTEM"


C:\Users\Milo>sqlplus scott/213213

SQL*Plus: Release 11.2.0.1.0 Production on 星期三 1月 27 17:14:26 2021

Copyright (c) 1982, 2010, Oracle.  All rights reserved.


连接到:
Oracle Database 11g Enterprise Edition Release 11.2.0.1.0 - 64bit Production
With the Partitioning, OLAP, Data Mining and Real Application Testing options

SQL>

SQL> disconnect
从 Oracle Database 11g Enterprise Edition Release 11.2.0.1.0 - 64bit Production
With the Partitioning, OLAP, Data Mining and Real Application Testing options 断开
SQL> show user;
USER 为 ""

SQL> describe dept;
 名称                                      是否为空? 类型
 ----------------------------------------- -------- ----------------------------
 DEPTNO                                    NOT NULL NUMBER(2)
 DNAME                                              VARCHAR2(14)
 LOC                                                VARCHAR2(13)
 TEST                                               VARCHAR2(64)
 TEST3                                              VARCHAR2(64)
 TEST7                                              VARCHAR2(64)
 TEST8                                              VARCHAR2(64)
 TEST9                                              VARCHAR2(64)
```

临时变量：只在使用它的SQL语句中有效，值不能保留

已定义变量：一直保留到被显示地删除、重定义或退出SQL*Plus为止。

```sql
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



/ 或润run  使用斜杠命令运行缓冲区中保存的SQL语句

list/edit  查看/编辑缓冲区中保存的SQL语句

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
```

@ path\file.sql   有空格时使用双引号

p132





