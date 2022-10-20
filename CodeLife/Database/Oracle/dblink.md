在databaseA中创建连接databaseB的link

```sql
 select * from user_sys_privs where privilege like upper('%DATABASE LINK%') and username = 'userA'; 
 
 grant CREATE PUBLIC DATABASE LINK,DROP PUBLIC DATABASE LINK to userA; 
 
 create public database link NC65DBLINK    
 connect to nc56 identified by nc56  
 using '(DESCRIPTION =(ADDRESS_LIST =(ADDRESS =(PROTOCOL = TCP)(HOST = 192.168.17.254)(PORT = 1521)))(CONNECT_DATA =(SERVICE_NAME = orcl)))';
 查看是否创建成功

select * from dba_db_links;
select owner,object_name from dba_objects where object_type='DATABASE LINK';--查询时间久

 select * from crm_bd_building@NC65DBLINK
 
drop  public database link  NC65DBLINK
```

