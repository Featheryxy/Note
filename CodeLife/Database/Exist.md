## Exists

只关注子查询的结果集中是否有记录，不关注具体什么值。若有记录则为TRUE

### 使用场景

1. 表的交运算

   > select * from T1 where exist(select 1 from T2 where T1.F1=T2.F2); 

   取外表的一条记录，查看其值在子查询中是否有，若有，则加入结果集。然后取外表的第二条记录，重复

2. 表的补运算

   > select * from T1 where not exist(select 1 from T2 where T1.F1=T2.F2); 

3. 在数据的插入，当数据库中存在时，不要插入数据，以防止数据重复插入