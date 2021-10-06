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

