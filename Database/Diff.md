1- MySql

2- Oracle

### 修改列


```mysql
1. ALTER TABLE table_name MODIFY [COLUMN]  column_name data_type constraints ; -- mysql 替换所有的
2. ALTER TABLE table_name MODIFY column_name data_type constraints; -- oracle 只修改改变的部分
```

### 大小写

1. mysql：以原生字符保留
2. 将输入的字符都自动转换成大写





### 单引号

1.引用一个字符串常量，也就是界定一个字符串的开始和结束

```sql
    select * from t_sys_user where id='15';  --查询id为15的字符
    
    select * from t_sys_score where id=15;  --查询id为15的整形数字
```

2.转义符，对紧随其后出现的字符(单引号)进行转义 

```sql
    select ' '' ' result from dual; --第二个单引号被作为转义符,第三个单引号被转义.结果为 '
    
    select 'name''''' result from dual; --结果为name''
    
    select 'name'||'''' result from dual;  --结果为name','||' 被转义为字符拼接
```

二、双引号

**关键字、对象名、字段名、别名、表名**加双引号，则示意 Oracle将**严格区分大小写**，否则Oracl都默认大写。 

```sql
    --关键字
    select "sysdate" from dual;  -- 等同于select sysdate from dual; 
    
    --字段名 
    select * from emp where "ENAME" = scott; --双引号提示oracle严格区分大小写,ename将报错
    
    --别名
    select ename "姓 名",sal "$工资" from emp; --别名中若有特殊字符或关键字,需要双引号包住
```

https://blog.csdn.net/mmake1994/article/details/85982743