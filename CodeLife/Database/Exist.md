## Exist

### 使用场景

1. 表的交运算

   > select * from T1 where exist(select 1 from T2 where T1.F1=T2.F2); 

2. 表的补运算

   > select * from T1 where not exist(select 1 from T2 where T1.F1=T2.F2); 

3. 在数据的插入，当数据库中存在时，不要插入数据，以防止数据重复插入