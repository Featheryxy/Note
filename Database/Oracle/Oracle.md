# Oracle

- 数据文件是数据库的物理存储单位，数据存储在表空间（由多个数据文件组成）
- 表空间是数据文件的逻辑映射，一个数据库（特指整个数据库）在逻辑上被分成多个表空间（都包含system表空间）
- 用户是在实例下建立的。不同实例中可以建相同名字的用户
- 一个数据库schema可以存在于多个表空间，一个表空间里面可以有多个schema

>数据文件 ----表空间                       

A schema is a collection of database objects (used by a user.).

Schema objects are the logical structures that directly refer to the database’s data.

A user is a name defined in the database that can connect to and access objects.

Schemas and users help database administrators manage database security.

oracle database 由 多个 schema 组成

schema 由 database objects 组成，如 tables，views, stored procedures等

**Oracle 不能新创建一个 schema, 只能通过创建一个用户来创建 Schema, 且将用户名作为该 Schema 的 名字。各个Schema之间相互独立，一个User默认只能操作自己的Schema，除非他有相应的权限或者DBA权限，如果我们访问一个表时，没有指明该表属于哪一个schema中的，系统就会自动给我们在表上加上缺省的sheman名。**

```sql
SQL> set linesize 32767
SQL> set pagesize 1000;

-- 请输入用户名:  sys as sysdba
-- 输入口令:

-- 以其他用户登录
conn scott/213213

-- 查看当前用户名称/schema
show user;

-- 查看当前用户的schema_name
select SYS_CONTEXT('USERENV','CURRENT_SCHEMA') CURRENT_SCHEMA from dual;

-- 查询用户对应的表空间, DBA_USERS存储所有用户信息
SELECT * FROM DBA_USERS ;

-- 查询当前用户权限
SELECT * FROM user_role_privs;

-- 查询 dba 角色权限
select * from dba_sys_privs where grantee='DBA';

grant dba to scott;

-- group by
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
--  1. select查询列只能是 group by 中出现的字段或 对其他字段使用过了 聚合函数
--  2. where 作用于表，having 作用于分组

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

```