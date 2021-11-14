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

列表：有序，可重复

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

集合：无序，不重复

```
set-key:{
	item, item1, item2
}
```



```shell
127.0.0.1:6379> sadd set-key item
(integer) 1
127.0.0.1:6379> sadd set-key item2
(integer) 1
127.0.0.1:6379> sadd set-key item3
(integer) 1
127.0.0.1:6379> sadd set-key item
(integer) 0
127.0.0.1:6379> smembers set-key
1) "item"
2) "item3"
3) "item2"
127.0.0.1:6379> sismember set-key item4
(integer) 0
127.0.0.1:6379> sismember set-key item
(integer) 1
127.0.0.1:6379> srem set-key item2
(integer) 1
127.0.0.1:6379> srem set-key item2
(integer) 0
127.0.0.1:6379> smembers set-key
1) "item"
2) "item3"
```

总结

```
SADD: 将给定元素添加到集合
SMEMBERS: 返回集合包含的所有元素
SISMEMBER: 检查给定元素是否存在于集合中
SREM: 如果给定的元素存在于集合中，那么移除这个元素
```

## HASH

散列

```
hash-key {
 sub-key1: value1
 sub-key2: value2
}
```



```shell
127.0.0.1:6379> hset hash-key sub-key1 value1
(integer) 1
127.0.0.1:6379> hset hash-key sub-key2 value2
(integer) 1
127.0.0.1:6379> hset hash-key sub-key2 value2
(integer) 0
127.0.0.1:6379> hgetall hash-key
1) "sub-key1"
2) "value1"
3) "sub-key2"
4) "value2"
127.0.0.1:6379> hdel hash-key sub-key2
(integer) 1
127.0.0.1:6379> hdel hash-key sub-key2
(integer) 0
127.0.0.1:6379> hget hash-key sub-key1
"value1"
127.0.0.1:6379> hgetall hash-key
1) "sub-key1"
2) "value1"
```

总结

```
HSET: 在散列⾥⾯关联起给定的键值对
HGET: 获取指定散列键的值
HGETALL: 获取散列包含的所有键值对
HDEL: 如果给定键存在于散列⾥⾯，那么移除这个键

```

## ZSET

有序集合: 有序集合的值被称为成员member,键被称为分值score,必须为浮点数

```
zset-key: {
 score: member
}
```



```shell
127.0.0.1:6379> zadd zset-key 728 member1
(integer) 1
127.0.0.1:6379> zadd zset-key 982 member0
(integer) 1
127.0.0.1:6379> zadd zset-key 982 member0
(integer) 0
127.0.0.1:6379> zrange zset-key 0 -1 withscores
1) "member1"
2) "728"
3) "member0"
4) "982"
127.0.0.1:6379> zrangebyscore zset-key 0 800 withscores
1) "member1"
2) "728"
127.0.0.1:6379> zrem zset-key member1
(integer) 1
127.0.0.1:6379> zrange zset-key 0 -1 withscores
1) "member0"
2) "982"
```

总结

```
ZADD: 将⼀个带有给定分值的成员添加到有序集合⾥⾯
ZRANGE: 根据元素在有序排列中所处的位置，从有序集合⾥⾯获取多个元素
ZRANGEBYSCORE: 获取有序集合在给定分值范围内的所有元素
ZREM: 如果给定成员存在于有序集合，那么移除这个成员
```

# Web

cookie

- signed
- token

