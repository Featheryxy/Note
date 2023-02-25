## 实践

在连表操作的时候，其实是先进行了2表的全连接（笛卡尔积，也就是所有能组合的情况a.rowCount*b.rowCount），然后根据on后面的条件进行筛选，最后如果是左连接或者右连接，再补全左表或者右表的数据

join on 

### 数据库

```sql
create table `class` (
	`cls_id` int (11),
	`cls_name` varchar (60)
); 
insert into `class` (`cls_id`, `cls_name`) values('1','1班');
insert into `class` (`cls_id`, `cls_name`) values('2','2班');
insert into `class` (`cls_id`, `cls_name`) values('3','3班');

create table `student` (
	`stu_id` int (11),
	`stu_name` varchar (60),
	`cls_id` int (11),
	`gender` varchar (3)
); 
insert into `student` (`stu_id`, `stu_name`, `cls_id`, `gender`) values('1','小明','1','1');
insert into `student` (`stu_id`, `stu_name`, `cls_id`, `gender`) values('2','小红','1','0');
insert into `student` (`stu_id`, `stu_name`, `cls_id`, `gender`) values('3','小兰','4','0');

```

### join

```sql
SELECT * FROM class;

cls_id  cls_name  
------  ----------
     1  1班      
     2  2班      
     3  3班    
          
select * from student;     

stu_id  stu_name  cls_id  gender  
------  --------  ------  --------
     1  小明             1  1       
     2  小红             1  0       
     3  小兰             4  0    
     
-- 笛卡尔积
SELECT * FROM class a, student b;

cls_id  cls_name  stu_id  stu_name  cls_id  gender  
------  --------  ------  --------  ------  --------
     1  1班             1  小明             1  1       
     2  2班             1  小明             1  1       
     3  3班             1  小明             1  1       
     1  1班             2  小红             1  0       
     2  2班             2  小红             1  0       
     3  3班             2  小红             1  0       
     1  1班             3  小兰             4  0       
     2  2班             3  小兰             4  0       
     3  3班             3  小兰             4  0       
     
-- 全外连接, oracle中使用full [outer] join
SELECT * FROM class a 
LEFT OUTER JOIN STUDENT b ON a.cls_id=b.cls_id
UNION
SELECT * FROM class a 
RIGHT OUTER JOIN STUDENT b ON a.cls_id=b.cls_id;

cls_id  cls_name  stu_id  stu_name  cls_id  gender  
------  --------  ------  --------  ------  --------
     1  1班             1  小明             1  1       
     1  1班             2  小红             1  0       
     2  2班        (NULL)  (NULL)    (NULL)  (NULL)  
     3  3班        (NULL)  (NULL)    (NULL)  (NULL)  
(NULL)  (NULL)         3  小兰             4  0       


-- 左外连接 left [outer] join
SELECT * FROM class a 
LEFT OUTER JOIN STUDENT b ON a.cls_id=b.cls_id;

cls_id  cls_name  stu_id  stu_name  cls_id  gender  
------  --------  ------  --------  ------  --------
     1  1班             1  小明             1  1       
     1  1班             2  小红             1  0       
     2  2班        (NULL)  (NULL)    (NULL)  (NULL)  
     3  3班        (NULL)  (NULL)    (NULL)  (NULL)  
     
-- 右外连接 left [outer] join
SELECT * FROM class a 
RIGHT OUTER JOIN STUDENT b ON a.cls_id=b.cls_id;     

cls_id  cls_name  stu_id  stu_name  cls_id  gender  
------  --------  ------  --------  ------  --------
     1  1班             1  小明             1  1       
     1  1班             2  小红             1  0       
(NULL)  (NULL)         3  小兰             4  0       



-- 内连接 [inner] join
SELECT * FROM class a
INNER JOIN STUDENT b ON a.cls_id=b.cls_id;

cls_id  cls_name  stu_id  stu_name  cls_id  gender  
------  --------  ------  --------  ------  --------
     1  1班             1  小明             1  1       
     1  1班             2  小红             1  0      
     

```

### join and

- where  在join生成临时表后帅选元组
- join and 在join生成临时表前帅选元组

> 当使用left join, and后 关于主表的帅选无效
>
> SELECT * FROM class a
> LEFT JOIN STUDENT b ON a.cls_id=b.cls_id
> AND a.cls_id = 1;
>
> 1. class join student 进行笛卡尔积，生成临时表temp1
> 2.  ON a.cls_id=b.cls_id AND a.cls_id = 1 对表temp1进行帅选，帅选a.cls_id=b.cls_id AND a.cls_id=1
> 3. left join 添加class 表中



```sql
SELECT * FROM class a
LEFT JOIN STUDENT b ON a.cls_id=b.cls_id
WHERE a.cls_id = 1;

cls_id  cls_name  stu_id  stu_name  cls_id  gender  
------  --------  ------  --------  ------  --------
     1  1班             1  小明             1  1       
     1  1班             2  小红             1  0       
     
     
-- 由于使用left join, and后 关于主表的帅选无效
SELECT * FROM class a
LEFT JOIN STUDENT b ON a.cls_id=b.cls_id
AND a.cls_id = 1;

cls_id  cls_name  stu_id  stu_name  cls_id  gender  
------  --------  ------  --------  ------  --------
     1  1班             1  小明             1  1       
     1  1班             2  小红             1  0       
     2  2班        (NULL)  (NULL)    (NULL)  (NULL)  
     3  3班        (NULL)  (NULL)    (NULL)  (NULL)  
     
-- 等价于
SELECT * FROM class a
LEFT JOIN STUDENT b ON a.cls_id=b.cls_id;

cls_id  cls_name  stu_id  stu_name  cls_id  gender  
------  --------  ------  --------  ------  --------
     1  1班             1  小明             1  1       
     1  1班             2  小红             1  0       
     2  2班        (NULL)  (NULL)    (NULL)  (NULL)  
     3  3班        (NULL)  (NULL)    (NULL)  (NULL)  


SELECT * FROM student a
LEFT JOIN class b ON a.cls_id=b.cls_id 
WHERE b.cls_id = 4;     

stu_id  stu_name  cls_id  gender  cls_id  cls_name  
------  --------  ------  ------  ------  ----------    



SELECT * FROM class a
LEFT JOIN STUDENT b ON a.cls_id=b.cls_id 
AND b.`cls_id`=4

cls_id  cls_name  stu_id  stu_name  cls_id  gender  
------  --------  ------  --------  ------  --------
     1  1班        (NULL)  (NULL)    (NULL)  (NULL)  
     2  2班        (NULL)  (NULL)    (NULL)  (NULL)  
     3  3班        (NULL)  (NULL)    (NULL)  (NULL)  
              
SELECT * FROM student a
LEFT JOIN class b ON a.cls_id=b.cls_id 
WHERE b.cls_id = 3;

stu_id  stu_name  cls_id  gender  cls_id  cls_name  
------  --------  ------  ------  ------  ----------
     4  小军             3  0            3  3班       
     
SELECT * FROM class a
LEFT JOIN STUDENT b ON a.cls_id=b.cls_id 
AND b.`cls_id`=3

cls_id  cls_name  stu_id  stu_name  cls_id  gender  
------  --------  ------  --------  ------  --------
     3  3班             4  小军             3  0       
     1  1班        (NULL)  (NULL)    (NULL)  (NULL)  
     2  2班        (NULL)  (NULL)    (NULL)  (NULL)  
```



### 自然连接

`natural join` 不需要指定连接条件, 消除重复属性列，是一种特殊的等值连接

```sql
-- 内连接 [inner] join
SELECT * FROM class a
INNER JOIN STUDENT b ON a.cls_id=b.cls_id;

cls_id  cls_name  stu_id  stu_name  cls_id  gender  
------  --------  ------  --------  ------  --------
     1  1班             1  小明             1  1       
     1  1班             2  小红             1  0      
     
     
-- 自然连接 natural join 不需要指定连接条件
SELECT * FROM class a
NATURAL  JOIN STUDENT b 

cls_id  cls_name  stu_id  stu_name  gender  
------  --------  ------  --------  --------
     1  1班             1  小明        1       
     1  1班             2  小红        0       


-- 左外连接 left [outer] join
SELECT * FROM class a 
LEFT OUTER JOIN STUDENT b ON a.cls_id=b.cls_id;

cls_id  cls_name  stu_id  stu_name  cls_id  gender  
------  --------  ------  --------  ------  --------
     1  1班             1  小明             1  1       
     1  1班             2  小红             1  0       
     2  2班        (NULL)  (NULL)    (NULL)  (NULL)  
     3  3班        (NULL)  (NULL)    (NULL)  (NULL)  

     
-- 左外自然连接 left [outer] join
SELECT * FROM class a 
NATURAL LEFT OUTER JOIN STUDENT b ;

cls_id  cls_name  stu_id  stu_name  gender  
------  --------  ------  --------  --------
     1  1班             1  小明        1       
     1  1班             2  小红        0       
     2  2班        (NULL)  (NULL)    (NULL)  
     3  3班        (NULL)  (NULL)    (NULL)  
```

https://blog.csdn.net/weixin_36979214/article/details/105993194

执行顺序：https://blog.csdn.net/weixin_44457814/article/details/106715422