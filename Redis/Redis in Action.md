# 概述

Redis是⼀个内存数据库（或者说内存数据结构）服务器，开源软件。

Redis是⼀个速度⾮常快的⾮关系数据库（non-relational database），它可以存储键（key）与5种不同类型的值（value）之间的映射（mapping），可以将存储在内存的键值对数据持久化到硬盘，可以使⽤复制特性来扩展读性能，还可以使⽤客⼾端分⽚ ① 来扩展写性能

# 数据结构

## STRING

字符串

```shell
127.0.0.1:6379> set hello world
OK
127.0.0.1:6379> get hello
"world"
127.0.0.1:6379> del hello
(integer) 1
127.0.0.1:6379> get hello
(nil)
```



总结

```
set key value 设置存储在给定键中的值
get key 获取存储在给定键中的值
del key 删除存储在给定键中的值（这个命令可以⽤于所有类型）
```

## LIST

列表

```shell
127.0.0.1:6379> rpush list-key item
(integer) 1
127.0.0.1:6379> rpush list-key item2
(integer) 2
127.0.0.1:6379> rpush list-key item
(integer) 3
127.0.0.1:6379> lrange list-key 0 -1
1) "item"
2) "item2"
3) "item"
127.0.0.1:6379> lindex list-key 1
"item2"
127.0.0.1:6379> lpop list-key
"item"
127.0.0.1:6379> lrange list-key 0 -1
1) "item2"
2) "item"
```

总结

```shell
RPUSH 将给定值推⼊列表的右端
LRANGE 获取列表在给定范围上的所有值
LINDEX 获取列表在给定位置上的单个元素
LPOP 从列表的左端弹出⼀个值，并返回被弹出的值
```



## SET

集合

## HASH

散列

## ZSET

有序集合