EXPLAIN SQL

1. id：标识SQL，值越大，先执行，相同id，从上往下，顺序执行，小表先执行（小表驱动大表）
2. select_type
    - primary 包含子查询 SQL 中的主查询（最外层）
    - SUBQUERY 包含子查询 SQL 中的子查询（非最外层）
    - simple 简单查询，不包含子查询和 union
    - derived 衍生查询，使用到了临时表
        - from 子查询中只有一张表
            `explain select cr.cname from (select * from course where tid in (1, 2)) cr;`
        - from 子查询中，如果有 table1 union table2，table1 就是 derived
            `explain select cr.cname from (select * from course where tid=1 union select * from course where tid =2) cr;`
       - union result   告知关联关系的表是哪两张     
3. type：system>const>eq_ref>ref>range>index>all 
     - system 只有一条数据的系统表，或衍生表只有一条数据的主查询
     - const 只能查到一条数据的 SQL, 只能用于 primary key 或 unique 索引
     - eq_ref：
         - 对于每个索引键的查询，返回匹配有且只有一行数据
         - 常见于唯一索引和主键索引
    - ref：
        - 非唯一索引，对于每个索引键的查询，返回匹配的所有行
    - range
         - 检索指定范围的行，where 后面是一个范围查询
         - between, in, <, >, >=, <=
         - in 查询，有时会失效，从 range 级别转为 all 无索引级别
    - index，查询全部索引数据
    - all 查询全部数据
      4. possible_keys：可能用到的索引，是一种预测
      5. key：实际使用到的索引 null表示无索引
   6. key_len：索引的长度
     用于判断复合索引是否被完全使用
    utf8 中，1 个字符占 3 个字节
    char(20)，key_len = 60
    gbk 中，1 个字符 2 个字节
    latin 中，1 个字符 1 个字节
    如果索引字段可以为 null，mysql 底层会用 1 个字节用于标识
    索引字段为 varchar，用 2 个字节代表可变长度
 7. ref：指明当前表所参照的字段
    select ... where a.c=b.x
    其中 b.x 可以是常量，const
 8. rows：实际通过索引查询到的数据个数
9. Extra 
       Using filesort
       Using temporary
       Using index
       Using where
       impossible where


   ​         
Oracle 
基数(Rows)：Oracle估计的当前步骤的返回结果集行数
字节(Bytes)：执行SQL对应步骤返回的字节数
耗费(COST)、CPU耗费：Oracle估计的该步骤的执行耗费和CPU耗费
时间(Time)：Oracle估计的执行sql对于步骤需要的时间

Oracle直接访问表中数据的方法又分为两种：
- 一种是全表扫描(TABLE ACCESS FULL)
- 另一种是ROWID扫描(TABLE ACCESS BY ROWID)：ROWID也就是表数据行所在的物理存储地址

访问索引（TABLE ACCESS BY INDEX SCAN）的情况就比较多了，可以分为：
- 索引唯一扫描（INDEX UNIQUE SCAN）
- 索引全扫描（INDEX FULL SCAN）
- 索引范围扫描（INDEX RANGE SCAN）
- 索引快速全扫描（INDEX FAST FULL SCAN）
- 索引跳跃式扫描（INDEX SKIP SCAN）

表连接方法：NESTED LOOPS
排序合并连接（merge sort join）
merge sort join是先将关联表的关联列各自做排序，然后从各自的排序表中抽取数据，到另一个排序表中做匹配

嵌套循环连接（Nested loop join）
Nested loops 工作方式是循环从一张表中读取数据(驱动表outer table)，然后访问另一张表（被查找表 inner table,通常有索引）。驱动表中的每一行与inner表中的相应记录JOIN。类似一个嵌套的循环。对于被连接的数据子集较小的情况，nested loop连接是个较好的选择

哈希连接（Hash join）
散列连接是CBO 做大数据集连接时的常用方式，优化器使用两个表中较小的表（或数据源）利用连接键在内存中建立散列表，然后扫描较大的表并探测散列表，找出与散列表匹配的行。

笛卡尔连接（Cross join）
如果两个表做表连接而没有连接条件，而会产生笛卡尔积，在实际工作中应该尽可能避免笛卡尔积


外层循坏数量应少于内层循环数量
因为从外层循坏切换到内层循环每次都有开栈和关栈的开销

多个独立的索引是否等于一个复合索引？
Using index condition？