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
	
​	--IN:输入参数，向存储过程传递值，默认类型，可以不写
​	--OUT:输出参数，用于返回结果。
​	--IN OUT：作为IN参数向存储过程传递值，同时作为OUT参数返回值。
​	--REPLACE：指明若已有同名的存储过程存在，那么将被替换成当前创建的版本。
​	--RETURN只能返回单个值，不能返回多个值。
	--可以使用DEFAULT关键字为输入参数指定默认值。




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





## 散记

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





