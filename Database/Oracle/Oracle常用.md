### 登录

```sql
SQL> set linesize 32767
SQL> set pagesize 1000;

-- 请输入用户名:  sys as sysdba
-- 输入口令:

-- 以其他用户登录
conn scott/213213

C:\Users\Milo>sqlplus scott/213213

-- 查看当前用户名称/schema
show user;

-- 查看当前用户的schema_name
select SYS_CONTEXT('USERENV','CURRENT_SCHEMA') CURRENT_SCHEMA from dual;

-- 查询用户对应的表空间, DBA_USERS存储所有用户信息
SELECT * FROM DBA_USERS ;



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


SQL> create user ot identified by 213213;

用户已创建。

SQL> grant connect, resource, dba to ot;

授权成功。

SQL> connect ot
输入口令:
已连接。

```



### PLSQL连接Oracle

用户名为 system

```sql
-- 查询sid
SQL> select name from v$database;

NAME
------------------
ORCL
```

### 数据库迁移

```shell
exp xt60sc_P2/handsome@10.20.158.64:1521/ora11g file='E:\xt60sc.dmp';


imp XT60ACC_P2/handsome@127.0.0.1:1521/orcl file='E:\Desktop\dump\xt60acc.dmp' ignore=y full=y;


```

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

