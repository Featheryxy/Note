### 登录

```sql
SQL> set linesize 32767;
SQL> set pagesize 1000;

-- 请输入用户名:  sys as sysdba
-- 输入口令:

sqlplus 用户名/密码@ip地址[:端口]/service_name [as sysdba]

-- 以其他用户登录
conn scott/213213

C:\Users\Milo>sqlplus scott/213213

-- 查看当前用户名称/schema
show user;

-- 查看当前用户的schema_name
select SYS_CONTEXT('USERENV','CURRENT_SCHEMA') CURRENT_SCHEMA from dual;

-- 查询用户对应的表空间, DBA_USERS存储所有用户信息
SELECT * FROM DBA_USERS ;

-- 查询sid
SQL> select name from v$database;

SQL> @path_to_sql_file

```

### Group By

```sql
SELECT SNAME,SAGE, MAX(SCORE)
FROM STUDENT 
where SSEX='男' 
GROUP BY SNAME,SAGE 
HAVING SAGE>'21'
ORDER By SAGE;
-- 1. 从表STUDENT中选取 SSEX='男' 的元组
-- 2. 在 1 的基础上先按 SNAME 分组，再按 SAGE 分组
-- 3. 在 2 的基础上，在每个分组中，筛选出  SAGE>'21' 的元组
-- 4. 在 3 的基础上，SELECT SNAME,SAGE, MAX(SCORE)
-- 5. 在 4 的基础上，按照 SAGE 排序
-- ps:
--  1. select 查询列只能是 group by 中出现的字段或 对其他字段使用过了 聚合函数
--  2. where 作用于表，having 作用于分组
```

### 用户创建与角色赋予

```sql
create user 用户名 identified by 口令[即密码];
drop user 用户名 cascade;

-- 查询当前用户权限
SELECT * FROM user_role_privs;

-- 查询 dba 角色权限
select * from dba_sys_privs where grantee='DBA';


SQL> create user ot identified by 213213 default tablespace BTADATA temporary tablespace test_temp;

用户已创建。

SQL> grant connect, resource, dba to ot;

授权成功。

SQL> connect ot
输入口令:
已连接。
```

### 数据库迁移

```shell
exp root/password@remote_address:1521/ora11g file='E:\db.dmp';

imp root/password@127.0.0.1:1521/orcl file='E:\Desktop\dump\db.dmp' ignore=y full=y;
```

### 引号

#### 一、单引号

##### 1.引用一个字符串常量，也就是界定一个字符串的开始和结束

```sql
    select * from t_sys_user where id='15';  --查询id为15的字符
    
    select * from t_sys_score where id=15;  --查询id为15的整形数字
```

##### 2.转义符，对紧随其后出现的字符(单引号)进行转义

```sql
    select ' '' ' result from dual; --第二个单引号被作为转义符,第三个单引号被转义.结果为 '
    
    select 'name''''' result from dual; --结果为name''
    
    select 'name'||'''' result from dual;  --结果为name','||' 被转义为字符拼接
    
    select 'hello' from dual;
```

#### 二、双引号

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

### 常见BUG

ORA-00907: 缺失右括号

```sql
create table a (ca int,cb integer,cc long); -- ok
create table a (ca int(11),cb integer,cc long); -- ORA-00907: 缺失右括号
```

ORA-01950: 对表空间 'USERS' 无权限

```sql
-- ORA-01950: 对表空间 'USERS' 无权限
ALTER USER XT60PUB quota unlimited on users;
```

ORA-01031: 权限不足

```
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

