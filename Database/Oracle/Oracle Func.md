# Oracle Func

## 数值型函数

可以将输入的参数隐式地转换成数值类型

- ABS(n)
- MOD(n2, n1): n2/n1
- SIGN(n): if(n>0)  return 1; if (n=0) return 0;
- CEIL(n): 大于等于n的最小整数
- FLOOR(n): 小于等于n的最大整数
- SQRT(n): n的平方根
- POWER(n2, n1): n2的n1次幂
- EXP(n): e的n次幂
- LOG(n1, n2): 以n1为底n2的对数

```sql
SQL> select ABS(100), ABS(-100), ABS('100') from dual;

  ABS(100)  ABS(-100) ABS('100')
---------- ---------- ----------
       100        100        100

SQL> select mod(5,2),mod(8/3,5),mod('10',5),mod(-10,6),mod(-1,0) from dual;

  MOD(5,2) MOD(8/3,5) MOD('10',5) MOD(-10,6)  MOD(-1,0)
---------- ---------- ----------- ---------- ----------
         1 2.66666667           0         -4         -1

SQL> select sign('9'), sign(-9),sign(0.00),sign(-2*'9') from dual;

 SIGN('9')   SIGN(-9) SIGN(0.00) SIGN(-2*'9')
---------- ---------- ---------- ------------
         1         -1          0           -1

SQL> select ceil(10), ceil('10.5'), ceil(-10.2) from dual;

  CEIL(10) CEIL('10.5') CEIL(-10.2)
---------- ------------ -----------
        10           11         -10

SQL> select floor(10), floor('10.5'),floor(-10.2) from dual;

 FLOOR(10) FLOOR('10.5') FLOOR(-10.2)
---------- ------------- ------------
        10            10          -11
```

## 字符型函数

- chr(n): 将给定的ASCII码转换为字符
- ASCII(char): 返回参数首字母的ASCII码，char可以是任意字符集
- LENGTH(char)
- SUBSTR(char, position[,substring_length])
    - substr: 以字符为单位
    - substrb: 以字节为单位
    - substrc: 以unicode字符为单位
    - position: 要截取的字符串的开始位置。默认1，如果该值为负数，则表示从char的右边算起。
- CONCAT(char1, char2), 等价于 || ，'a'||'b'  || 左边不能有空格
- INSTR(string, substring[,position[, occurrence]]): 在指定的字符串中搜索是否存在另一个字符串
    - INSTR: 以字符为单位进行搜索
    - INSTRB: 以字节为单位进行搜索
    - INSTRC: 以unicode字符为单位进行搜索
    - INSTR2: 以UCS2代码点为单位进行搜索
    - INSTR4: 以UCS4代码点为单位进行搜索
    - string: 待搜索的字符串
    - substring: 要搜索的字符串
    - position: 搜索开始的位置。默认1，如果该值为负数，则表示从char的右边算起。
    - occurrence: 表示substring第几次出现，默认是1
- UPPER(char), LOWER(char)
- INITCAP(char): 所有单词的首字符大写
- REPLACE(char, search_string[,replacement_string]): 在char中搜索search_string，并用replacement_string替代
- TRIM([LEADING|TRAILING|BOTH][trim_character FROM]trim_source)
    - LEADING: 删除trim_source的前缀字符
    - TRAILING: 删除trim_source的后缀字符
    - BOTH: 删除trim_source的前缀和后缀字符
    - trim_character: 删除指定的字符，默认为空格
    - trim_source: 被操作的字符串
- RTRIM(char[, set])
- LTRIM(char[, set])

```sql
SQL> select chr(65)||chr(66)||chr(67) ABC, chr(54678) from dual;

ABC    CHR(
------ ----
ABC    ？

SQL> select ascii('明'), ascii('Adb'),ascii('ABC') from dual;

ASCII('明') ASCII('ADB') ASCII('ABC')
----------- ------------ ------------
   15112334           65           65

SQL> select length('ABCDE我FGHI') from dual;

LENGTH('ABCDE我FGHI')
---------------------
                   10

SQL> select substr('ABCDE我FGHI',5,2), substr('ABCDE我FGHI',-5,2) from dual;

SUBSTR(' SUBSTR('
-------- --------
E我      我F

SQL> select concat('我的', '测试! '), '我的'||'测试!' from dual;

CONCAT('我的','测试!')       '我的'||'测试!'
---------------------------- --------------------------
我的测试!                    我的测试!

SQL> select instr('this is a 测试！','测'), instr('this is a 测试！','s',-1) from dual;

INSTR('THISISA测试！','测') INSTR('THISISA测试！','S',-1)
--------------------------- -----------------------------
                         11                             7

SQL> select replace('this is a test', 'tes', 'resul') from dual;

REPLACE('THISISATEST','TES','RES
--------------------------------
this is a result

SQL> select trim(trailing 't' from 'test'), trim(' test ') from dual;

TRIM(T TRIM('TE
------ --------
tes    test
```

## 日期函数

## 转换函数

- ASCIISTR(char): 将任意字符集的字符串转换为数据库字符集对应的ASCII字符串
- BIN_TO_NUM(data[, data...])：将二进制数据转换成对应的十进制数据

```sql
SQL> select asciistr('这是测试!') from dual;

ASCIISTR('这是测试!')
------------------------------------------
\8FD9\662F\6D4B\8BD5!

SQL> select bin_to_num(1),bin_to_num(1,0,0), bin_to_num(1,1,1) from dual;

BIN_TO_NUM(1) BIN_TO_NUM(1,0,0) BIN_TO_NUM(1,1,1)
------------- ----------------- -----------------
            1                 4                 7
```

## NULL函数

- COALESCE(expr):  返回列表中第一个部位null的表达式，如果参数都为null，则返回一个null
- NVL(expr1, expr2): if expr1 is null, return expr2, else return expr1
- NVL2(expr1, expr2, expr3): if expr1 is null, return expr3; if expr1 is not null, return expr2

```sql
SQL> select coalesce(null, 9-9,null) from dual;

COALESCE(NULL,9-9,NULL)
-----------------------
                      0
```

## 集合函数

- AVG([distinct|all] expr)
- COUNT(*|[distinct][all] exper)

## 其他函数

- USER
- DECODE(expr, search, result[,search1,result1][,default]): 当expr符合条件search时就返回result的值

```sql
SQL> select user from dual;

USER
------------------------------------------------------------
SCOTT

select productname,quantity,decode(sign(quantity-100),1,'充足'，-1，'不足'，0，'不足') from productinfo;

```