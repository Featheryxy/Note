# Redis

## 1 简介

Redis (Remote DIctionary Server) 是用 C 语言开发的一个开源的高性能键值对（ key-value）数据库。  

**Redis优点**

- **性能极高** – Redis能读的速度是110000次/s,写的速度是81000次/s 。
- **丰富的数据类型** – Redis支持的类型 String, Hash,List, Set 及 Ordered Set 数据类型操作。
- **原子性** – Redis的所有操作都是原子性的，意思就是要么成功执行要么失败完全不执行。单个操作是原子性的。多个操作也支持事务，即原子性，通过MULTI和EXEC指令包起来。
- **丰富的特性** – Redis还支持 publish/subscribe, 通知, key 过期等等特性。
- **高速读写**，redis使用自己实现的分离器，代码量很短，没有使用 lock（MySQL），因此效率非常高  

```
Redis是一个简单的，高效的，分布式的，基于内存的缓存工具。
架设好服务器后，通过网络连接（类似数据库），提供Key－Value式缓存服务。
简单，是Redis突出的特色。
简单可以保证核心功能的稳定和优异
```

**Redis 缺点**  

- **持久化**。Redis直接将数据存储到内存中，要将数据保存到磁盘上，Redis可以使用两种方式实现持久化过程。
  - 定时快照（snapshot）：每隔一段时间将整个数据库写到磁盘上，每次均是写全部数据，代价非常高。
  - 基于语句追加（aof）：只追踪变化的数据，但是追加的log可能过大，同时所有的操作均重新执行一遍，
    回复速度慢。
- **耗内存**，占用内存过高。  

### 1.1 NoSQL  

NoSQL，泛指非关系型的数据库，NoSQL即Not-Only SQL 。解决大规模数据集合多重数据种类带来的挑战  

### 1.2 NoSQL的类别  

### 1.3 Redis历史  

## 2 安装

Redis是C语言开发，安装Redis需要先将官网下载的源码进行编译，编译依赖gcc环境，如果没有gcc环境，需要安装gcc 。

安装gcc

```linux
yum -y install gcc automake autoconf libtool make
```

下载redis二进制安装包  

```
wget http://download.redis.io/releases/redis-5.0.0.tar.gz
```

解压到/opt目录下

```
tar zxvf redis-5.0.0.tar.gz -C /opt
```

编译

```
cd /opt/redis-5.0.0 && make MALLOC=libc //或 make MALLOC=libc

# 成功
Hint: It's a good idea to run 'make test' ;)
```

指定安装位置

```
[root@localhost redis-5.0.0]# pwd
/opt/redis-5.0.0
[root@localhost redis-5.0.0]# make PREFIX=/usr/local/redis install
cd src && make install
make[1]: Entering directory `/opt/redis-5.0.0/src'
    CC Makefile.dep
make[1]: Leaving directory `/opt/redis-5.0.0/src'
make[1]: Entering directory `/opt/redis-5.0.0/src'

Hint: It's a good idea to run 'make test' ;)

    INSTALL install
    INSTALL install
    INSTALL install
    INSTALL install
    INSTALL install
make[1]: Leaving directory `/opt/redis-5.0.0/src'
```

启动服务端

```
[root@localhost bin]# pwd
/usr/local/redis/bin
[root@localhost bin]# ./redis-server 
24900:C 12 Jun 2020 21:07:56.290 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
24900:C 12 Jun 2020 21:07:56.290 # Redis version=5.0.0, bits=64, commit=00000000, modified=0, pid=24900, just started
24900:C 12 Jun 2020 21:07:56.290 # Warning: no config file specified, using the default config. In order to specify a config file use ./redis-server /path/to/redis.conf
24900:M 12 Jun 2020 21:07:56.292 * Increased maximum number of open files to 10032 (it was originally set to 1024).
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 5.0.0 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 24900
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

24900:M 12 Jun 2020 21:07:56.307 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
24900:M 12 Jun 2020 21:07:56.307 # Server initialized
24900:M 12 Jun 2020 21:07:56.308 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
24900:M 12 Jun 2020 21:07:56.308 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
24900:M 12 Jun 2020 21:07:56.309 * Ready to accept connections
```

启动客户端

```
[root@localhost bin]# pwd
/usr/local/redis/bin
[root@localhost bin]# ./redis-cli
127.0.0.1:6379> 
127.0.0.1:6379> set year 2020
OK
127.0.0.1:6379> get year
"2020"
```

退出

```
ctrl+C
```

检测是否服务端启动

```
127.0.0.1:6379> PING
PONG
```

## 3 配置

### 3.1 redis.conf

```
[root@localhost bin]# cp /opt/redis-5.0.0/redis.conf .
[root@localhost bin]# ll
total 32696
-rw-r--r--. 1 root root      92 Jun 12 21:10 dump.rdb
-rwxr-xr-x. 1 root root 4366552 Jun 12 20:54 redis-benchmark
-rwxr-xr-x. 1 root root 8082696 Jun 12 20:54 redis-check-aof
-rwxr-xr-x. 1 root root 8082696 Jun 12 20:54 redis-check-rdb
-rwxr-xr-x. 1 root root 4783456 Jun 12 20:54 redis-cli
-rw-r--r--. 1 root root   62155 Jun 12 21:22 redis.conf
lrwxrwxrwx. 1 root root      12 Jun 12 20:54 redis-sentinel -> redis-server
-rwxr-xr-x. 1 root root 8082696 Jun 12 20:54 redis-server
```

**redis.conf**

```
**1. Redis默认不是以守护进程的方式运行，可以通过该配置项修改，使用yes启用守护进程
daemonize no

2. 当Redis以守护进程方式运行时，Redis默认会把pid写入/var/run/redis.pid文件，可以通过pidfile指定pidfile /var/run/redis.pid

**3. 指定Redis监听端口，默认端口为6379，作者在自己的一篇博文中解释了为什么选用6379作为默认端口，因为6379在手机按键上MERZ对应的号码，而MERZ取自意大利歌女Alessia Merz的名字
port 6379

**4. 绑定的主机地址
bind 127.0.0.1

5.当 客户端闲置多长时间后关闭连接，如果指定为0，表示关闭该功能
timeout 300

6. 指定日志记录级别，Redis总共支持四个级别：debug、verbose、notice、warning，默认为verbose
loglevel verbose

7. 日志记录方式，默认为标准输出，如果配置Redis为守护进程方式运行，而这里又配置为日志记录方式为标准输出，则日志将会发送给/dev/null 
logfile stdout

**8. 设置数据库的数量，默认数据库为0，可以使用SELECT <dbid>命令在连接上指定数据库id
databases 16

**9. 指定在多长时间内，有多少次更新操作，就将数据同步到数据文件，可以多个条件配合
save <seconds> <changes>
Redis默认配置文件中提供了三个条件：
save 900 1
save 300 10
save 60 10000
分别表示900秒（15分钟）内有1个更改，300秒（5分钟）内有10个更改以及60秒内有10000个更改。

**10. 指定存储至本地数据库时是否压缩数据，默认为yes，Redis采用LZF(压缩算法）压缩，如果为了节省CPU时间，可以关闭该选项，但会导致数据库文件变的巨大
rdbcompression yes

**11. 指定本地数据库文件名，默认值为dump.rdb
dbfilename dump.rdb

**12. 指定本地数据库存放目录结尾10个
dir ./

13. 设置当本机为slav服务时，设置master服务的IP地址及端口，在Redis启动时，它会自动从master进行数据同步
slaveof <masterip> <masterport>

14. 当master服务设置了密码保护时，slav服务连接master的密码
masterauth <master-password>

**15. 设置Redis连接密码，如果配置了连接密码，客户端在连接Redis时需要通过AUTH <password>命令提供密码，默认关闭
requirepass foobared

16. 设置同一时间最大客户端连接数，默认无限制，Redis可以同时打开的客户端连接数为Redis进程可以打开的最大文件描述符数，如果设置 maxclients 0，表示不作限制。当客户端连接数到达限制时，Redis会关闭新的连接并向客户端返回max number of clients reached错误信息
maxclients 128

17. 指定Redis最大内存限制，Redis在启动时会把数据加载到内存中，达到最大内存后，Redis会先尝试清除已到期或即将到期的Key，当此方法处理 后，仍然到达最大内存设置，将无法再进行写入操作，但仍然可以进行读取操作。Redis新的vm机制，会把Key存放内存，Value会存放在swap区
maxmemory <bytes>

18. 指定是否在每次更新操作后进行日志记录，Redis在默认情况下是异步的把数据写入磁盘，如果不开启，可能会在断电时导致一段时间内的数据丢失。因为 redis本身同步数据文件是按上面save条件来同步的，所以有的数据会在一段时间内只存在于内存中。默认为no
appendonly no

19. 指定更新日志文件名，默认为appendonly.aof
appendfilename appendonly.aof

20. 指定更新日志条件，共有3个可选值：
no：表示等操作系统进行数据缓存同步到磁盘（快）
always：表示每次更新操作后手动调用fsync()将数据写到磁盘（慢，安全）
everysec：表示每秒同步一次（折衷，默认值）
appendfsync everysec

21. 指定是否启用虚拟内存机制，默认值为no，简单的介绍一下，VM机制将数据分页存放，由Redis将访问量较少的页即冷
数据swap到磁盘上，访问多的页面由磁盘自动换出到内存中（在后面的文章我会仔细分析Redis的VM机制）
vm-enabled no

22. 虚拟内存文件路径，默认值为/tmp/redis.swap，不可多个Redis实例共享
vm-swap-file /tmp/redis.swap

23. 将所有大于vm-max-memory的数据存入虚拟内存,无论vm-max-memory设置多小,所有索引数据都是内存存储的(Redis的索引数据 就是keys),也就是说,当vm-max-memory设置为0的时候,其实是所有value都存在于磁盘。默认值为0
vm-max-memory 0

24. Redis swap文件分成了很多的page，一个对象可以保存在多个page上面，但一个page上不能被多个对象共享，vmpage-size是要根据存储的 数据大小来设定的，作者建议如果存储很多小对象，page大小最好设置为32或者64bytes；如果存储很大大对象，则可以使用更大的page，如果不 确定，就使用默认值
vm-page-size 32

25. 设置swap文件中的page数量，由于页表（一种表示页面空闲或使用的bitmap）是在放在内存中的，，在磁盘上每8个
pages将消耗1byte的内存。
vm-pages 134217728

26. 设置访问swap文件的线程数,最好不要超过机器的核数,如果设置为0,那么所有对swap文件的操作都是串行的，可能会
造成比较长时间的延迟。默认值为4
vm-max-threads 4

27. 设置在向客户端应答时，是否把较小的包合并为一个包发送，默认为开启
glueoutputbuf yes

28. 指定在超过一定的数量或者最大的元素超过某一临界值时，采用一种特殊的哈希算法
hash-max-zipmap-entries 64
hash-max-zipmap-value 512

29. 指定是否激活重置哈希，默认为开启（后面在介绍Redis的哈希算法时具体介绍）
activerehashing yes

30. 指定包含其它的配置文件，可以在同一主机上多个Redis实例之间使用同一份配置文件，而同时各个实例又拥有自己的特定配置文件
include /path/to/local.conf
```

### 3.2 Redis中的内存维护策略

redis作为优秀的中间缓存件，时常会存储大量的数据，即使采取了集群部署来动态扩容，也应该即时的整理内存，维持系统性能。  

**在redis中有两种解决方案**

1. 为数据设置超时时间

   > 设置过期时间
   >
   > ```
   > expire key time(以秒为单位)--这是最常用的方式
   > setex(String key, int seconds, String value)--字符串独有的方式
   > ```
   >
   > - 除了字符串自己独有设置过期时间的方法外，其他方法都需要依靠expire方法来设置时间
   > - 如果没有设置时间，那缓存就是永不过期
   > - 如果设置了过期时间，之后又想让缓存永不过期，使用persist key

   ```
   127.0.0.1:6379> ttl year
   (integer) -1
   127.0.0.1:6379> set short 10
   OK
   127.0.0.1:6379> expire short 5
   (integer) 1
   127.0.0.1:6379> ttl short
   (integer) -2
   127.0.0.1:6379> key *
   (error) ERR unknown command `key`, with args beginning with: `*`, 
   127.0.0.1:6379> keys *
   1) "year"
   ```

2. 采用LRU算法动态将不用的数据删除
   > 内存管理的一种页面置换算法，对于在内存中但又不用的数据块（内存块）叫做LRU，
   > 操作系统会根据哪些数据属于LRU而将其移出内存而腾出空间来加载另外的数据。  
   
   1.**volatile-lru**：设定超时时间的数据中,删除最不常使用的数据.
   2.**allkeys-lru**：查询所有的key中最近最不常使用的数据进行删除，这是应用最广泛的策略.
   3.volatile-random：在已经设定了超时的数据中随机删除.
   4.allkeys-random：查询所有的key,之后随机删除.
   5.volatile-ttl：查询全部设定超时时间的数据,之后排序,将马上将要过期的数据进行删除操作.
   6.noeviction：如果设置为该属性,则不会进行删除操作,如果内存溢出则报错返回.
   7.volatile-lfu：从所有配置了过期时间的键中驱逐使用频率最少的键
   8.allkeys-lfu：从所有键中驱逐使用频率最少的键  

### 3.3 自定义配置

```
daemonize no 修改为 daemonize yes 守护进程启动
bind 127.0.01 注释掉 允许除本机外的机器访问Redis服务
requirepass 设置密码 设定数据库密码 (保证服务安全/有些情况下不设定密码是无法进行远程连接访问的)
```

> Redis采用的是单进程多线程的模式。当redis.conf中选项daemonize设置成yes时，代表开启守护进程模式。
> 在该模式下，redis会在后台运行，并将进程pid号写入至redis.conf选项pidfile设置的文件中，此时redis将一直运行，除非手动kill该进程。但当daemonize选项设置成no时，当前界面将进入redis的命令行界面，exit强制退出或者关闭连接工具(putty,xshell等)都会导致redis进程退出。 服务端开发的大部分应用都是采用后台运行的模式 

> requirepass设置密码。因为redis速度相当快，所以一台比较好的服务器下，一个外部用户在一秒内可以进行
> 15W次密码尝试，这意味着你需要设定非常强大的密码来防止暴力破解。
> 可以通过 redis 的配置文件设置密码参数，这样客户端连接到 redis 服务就需要密码验证，这样可以让你的
> redis 服务更安全  

### 3.4 启动

**服务端启动：**  

```
[root@localhost bin]# ./redis-server ./redis.conf 
24997:C 12 Jun 2020 22:15:14.825 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
24997:C 12 Jun 2020 22:15:14.825 # Redis version=5.0.0, bits=64, commit=00000000, modified=0, pid=24997, just started
24997:C 12 Jun 2020 22:15:14.825 # Configuration loaded

[root@localhost bin]# ./redis-cli
127.0.0.1:6379> keys *
(error) NOAUTH Authentication required.
127.0.0.1:6379> auth 213213
OK
```

**客户端登录**： 用redis-cli 密码登陆（redis-cli -a password）  

```
redis-cli -h host -p port -a password //redis-cli –h IP地址 –p 端口 –a 密码

[root@localhost bin]# ./redis-cli -a 213213
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
127.0.0.1:6379> 

```

### 3.5 关闭

第一种关闭方式：

- （断电、非正常关闭。容易数据丢失） 查询redis进程id

- kill对 查询的id进行强制关闭

  ```
  [root@localhost bin]# ps -ef | grep -i redis
  root      24998      1  0 22:15 ?        00:00:01 ./redis-server *:6379
  root      25004  20560  0 22:20 pts/1    00:00:00 ./redis-cli
  root      25010  24936  0 22:26 pts/3    00:00:00 grep --color=auto -i redis
  [root@localhost bin]# kill -9 24998
  [root@localhost bin]# ps -ef | grep -i redis
  root      25004  20560  0 22:20 pts/1    00:00:00 ./redis-cli
  root      25012  24936  0 22:27 pts/3    00:00:00 grep --color=auto -i redis
  ```


第二种关闭方式

- （正常关闭、数据保存）

- 关闭redis服务，通过客户端进行shutdown

- 如果redis设置了密码，需要先在客户端通过密码登录，再进行shutdown即可关闭服务端  

  ```
  [root@localhost bin]# ./redis-server ./redis.conf 
  25045:C 12 Jun 2020 22:42:50.331 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
  25045:C 12 Jun 2020 22:42:50.331 # Redis version=5.0.0, bits=64, commit=00000000, modified=0, pid=25045, just started
  25045:C 12 Jun 2020 22:42:50.331 # Configuration loaded
  [root@localhost bin]# ./redis-cli
  127.0.0.1:6379> shutdown
  (error) NOAUTH Authentication required.
  127.0.0.1:6379> auth 213213
  OK
  127.0.0.1:6379> shutdown
  not connected> 
  
  ```

## 4 基本操作

### 4.1 操作

```
127.0.0.1:6379> set name milo
OK
127.0.0.1:6379> get name
"milo"
127.0.0.1:6379> get age
(nil) // key 不存在

127.0.0.1:6379> clear // 清屏

127.0.0.1:6379> help set

  SET key value [expiration EX seconds|PX milliseconds] [NX|XX] // 格式
  summary: Set the string value of a key
  since: 1.0.0  
  group: string  // 命令所属群组
  
127.0.0.1:6379> help
redis-cli 5.0.0
To get help about Redis commands type:
      "help @<group>" to get a list of commands in <group>
      "help <command>" for help on <command>
      "help <tab>" to get a list of possible help topics
      "quit" to exit

To set redis-cli preferences:
      ":set hints" enable online hints
      ":set nohints" disable online hints
Set your preferences in ~/.redisclirc
```

### 4.2 总结

```
// 启动服务
redis-server
// 启动客户端
redis-cli

添加信息
set key value
get key

// 清屏
clear 

// 帮助
help @<group>
help <command>

//退出
quit
exit
ctrl+c
```

## 5 数据类型

### 5.1 简介

redis 数据存储格式  

- **redis 自身是一个 Map，其中所有的数据都是采用 key : value 的形式存储**
- **数据类型指**的是存储的数据的类型，也就是 **value 部分的类型**， **key 部分永远都是字符串**  

#### 5.1.1 数据的生命周期

- 设置数据具有指定的生命周期  

  ```
  setex key seconds value
  psetex key milliseconds value
  
  127.0.0.1:6379> setex tel 10 1
  OK
  127.0.0.1:6379> get tel
  "1"
  127.0.0.1:6379> get tel
  "1"
  127.0.0.1:6379> get tel
  "1"
  127.0.0.1:6379> get tel
  (nil)
  127.0.0.1:6379> setex tel 10 1
  OK
  127.0.0.1:6379> set tel 2
  OK
  ```

- redis 控制数据的生命周期，通过数据是否失效控制业务行为，适用于所有具有时效性限定控制的操作  

#### 5.1.2 注意事项

- 数据操作不成功的反馈与数据正常操作之间的差异
  - 表示运行结果是否成功  
    - (integer) 0 → false 失败  
    - (integer) 1 → true 成功  
  - 表示运行结果值  
    - (integer) 3 → 3  3个  
    - (integer) 1 → 1  1个  
- 数据未获取到  
  - （ nil）等同于null  
- 数据最大存储量  
  - 512MB  
- 数值计算最大范围（ java中的long的最大值）  
  - 9223372036854775807 = 2 ^63(第一位符号位) - 1(零值)

### 5.2 string

```shell
set key value 
```



#### 5.2.1 基本操作

- 存储的数据：单个数据，最简单的数据存储类型，也是最常用的数据存储类型
- 存储数据的格式：一个存储空间保存一个数据
- 存储内容：通常使用字符串，如果**字符串以整数的形式**展示，可以作为数字操作使用  

```
127.0.0.1:6379> get age
(nil)
127.0.0.1:6379> set age 100
OK
127.0.0.1:6379> del age
(integer) 1 // 操作成功
127.0.0.1:6379> del age
(integer) 0 // 操作失败

```

- 添加/修改多个数据

  ```
  mset key1 value1 key2 value2 // m: Multiple
  ```

- 获取多个数据

  ```
  mget key1 key2
  ```

- 获取数据字符个数（字符串长度）

  ```
  strlen key
  ```

- 字符追加

  ```
  append key value
  ```

```
127.0.0.1:6379> mset a 1 b 2 c 3
OK
127.0.0.1:6379> mget a b c
1) "1"
2) "2"
3) "3"
127.0.0.1:6379> mget a b d
1) "1"
2) "2"
3) (nil)
127.0.0.1:6379> strlen name
(integer) 4
127.0.0.1:6379> get name
"milo"
127.0.0.1:6379> append name Ye
(integer) 6
127.0.0.1:6379> get name
"miloYe"
127.0.0.1:6379> append year 2021
(integer) 4
127.0.0.1:6379> get year
"2021"
```

#### 5.2.2 数据的扩展操作  

- 设置数值数据增加指定范围的值  

  ```
  incr key
  incrby key increment
  incrbyfloat key increment
  ```

- 设置数值数据减少指定范围的值  

  ```
  decr key
  decrby key increment
  ```

```
"20202021"
127.0.0.1:6379> del year
(integer) 1
127.0.0.1:6379> append year 2021
(integer) 4
127.0.0.1:6379> get year
"2021"
127.0.0.1:6379> clear
127.0.0.1:6379> set num 1
OK
127.0.0.1:6379> incr num
(integer) 2
127.0.0.1:6379> get num
"2"
127.0.0.1:6379> incr num
(integer) 3
127.0.0.1:6379> get num
"3"
127.0.0.1:6379> decr num
(integer) 2
127.0.0.1:6379> get num
"2"
127.0.0.1:6379> help incrby

  INCRBY key increment
  summary: Increment the integer value of a key by the given amount
  since: 1.0.0
  group: string

127.0.0.1:6379> incrby num 10
(integer) 12
127.0.0.1:6379> incrbyfloat num 1.5
"13.5"

```

#### 5.2.3 原理

- string在redis内部存储**默认就是一个字符串**，当**遇到增减类操作incr， decr时会转成数值型**进行计算。
-  redis所有的操作都是原子性的，采用**单线程**处理所有业务，命令是一个一个执行的，因此无需考虑并发
    带来的数据影响。
- 注意： 按数值进行操作的数据，如果原始数据不能转成数值，或超越了redis 数值上限范围，将报错。
  9223372036854775807（ java中long型数据最大值， Long.MAX_VALUE）  
- redis用于控制数据库表主键id，为数据库表主键提供生成策略，保障数据库表的主键唯一性
- 此方案适用于所有数据库，且支持数据库集群  

#### 5.2.4 应用

大V的粉丝数量

```
% 以用户主键和属性值作为key
127.0.0.1:6379> set user:id:1:fans 111
OK
127.0.0.1:6379> set user:id:1:blogs 23
OK

% 以用户主键和属性值作为key
127.0.0.1:6379> set user:id:1 {id:1,blogs:23}
OK
127.0.0.1:6379> incr user:id:1:fans
(integer) 112

127.0.0.1:6379> set usr:id:1:fans 111
OK
127.0.0.1:6379> get usr
(nil)
127.0.0.1:6379> get id
(nil)
127.0.0.1:6379> get usr:id
(nil)
127.0.0.1:6379> get usr:id:1:fans
"111"

```

#### 5.2.5 key的设置约定

表名：主键名：主键值：字段名

user:   id:            3         :   name

### 5.3 hash

#### 5.3.1 简介

- 新的存储需求：对一系列存储的数据进行编组，方便管理，典型应用存储对象信息
- 需要的存储结构：一个存储空间保存多个键值对数据
- hash类型：底层使用哈希表结构实现数据存储  

```
user:id:1 {id:1,blogs:23}

key  user:id:1
field   id, blogs
value   1, 23
```

hash存储结构优化

- 如果field数量较少，存储结构优化为类数组结构
- 如果field数量较多，存储结构使用HashMap结构  

#### 5.3.2 基本操作

```
添加/修改数据
hset key field value

获取数据
hget key field
hgetall key

删除数据
hdel key field1 [field2]

添加/修改多个数据
hmset key field1 value1 field2 value2

获取多个数据
hmget key field1 field2 …

获取哈希表中字段的数量
hlen key

获取哈希表中是否存在指定的字段
hexists key field

获取所有的字段名或字段值
hkeys key
hvals key

设置指定字段的数值数据增加指定范围的值
hincrby key field increment
hincrbyfloat key field increment
```

```
127.0.0.1:6379> hset user name zhangsan
(integer) 1
127.0.0.1:6379> hset user age 33
(integer) 1
127.0.0.1:6379> hgetall user
1) "name"
2) "zhangsan"
3) "age"
4) "33"
127.0.0.1:6379> hget user name
"zhangsan"
127.0.0.1:6379> hdel user age
(integer) 1
127.0.0.1:6379> hgetall user
1) "name"
2) "zhangsan"
127.0.0.1:6379> hset user age 33
(integer) 1
127.0.0.1:6379> hmget user name age
1) "zhangsan"
2) "33"
127.0.0.1:6379> hmset user name zhangsanfeng weight 66
OK
127.0.0.1:6379> hgetall user
1) "name"
2) "zhangsanfeng"
3) "age"
4) "33"
5) "weight"
6) "66"
127.0.0.1:6379> hlen user
(integer) 3
127.0.0.1:6379> hexists user age
(integer) 1
127.0.0.1:6379> hexists user hight
(integer) 0
127.0.0.1:6379> hincrby user age 1
(integer) 34
```

#### 5.3.2 注意事项

- hash类型下的value只能存储字符串，不允许存储其他数据类型，不存在嵌套现象。如果数据未获取到，对应的值为（ nil）
- 每个 hash 可以存储 2^32 - 1 个键值对
- **hash类型十分贴近对象的数据存储形式**，并且可以灵活添加删除对象属性。但hash设计初衷不是为了存
  储大量对象而设计的，切记不可滥用，更**不可以将hash作为对象列表使用**
- hgetall 操作可以获取全部属性，如果内部field过多，遍历整体数据效率就很会低，有可能成为数据访问
  瓶颈  

#### 5.3.3 应用1-购物车

电商网站购物车设计与实现

- 以客户id作为key，每位客户创建一个hash存储结构存储对应的购物车信息
- 将商品编号作为field，购买数量作为value进行存储
- 添加商品：追加全新的field与value
- 浏览：遍历hash
- 更改数量：自增/自减，设置value值
- 删除商品：删除field
- 清空：删除key  

```
127.0.0.1:6379> hmset 001 g01 100 g02 200
OK
127.0.0.1:6379> hmset 002 g02 1 g04 7 g05 100
OK
127.0.0.1:6379> hset 001 g03 5
(integer) 1
127.0.0.1:6379> hgetall 001
1) "g01"
2) "100"
3) "g02"
4) "200"
5) "g03"
6) "5"
127.0.0.1:6379> hdel 001 g01
(integer) 1
127.0.0.1:6379> hgetall 001
1) "g02"
2) "200"
3) "g03"
4) "5"
127.0.0.1:6379> hincrby 001 g03 1
(integer) 6
127.0.0.1:6379> hgetall 001
1) "g02"
2) "200"
3) "g03"
4) "6"
```

当前仅仅是将数据存储到了redis中，并没有起到加速的作用，商品信息还需要二次查询数据库  

```
127.0.0.1:6379> hmset 003 g01:nums 100 g01:info {...}
OK
127.0.0.1:6379> hgetall 003
1) "g01:nums"
2) "100"
3) "g01:info"
4) "{...}"
127.0.0.1:6379> hmset 004 g01:nums 5 g01:info {...}
OK
// 购物车info信息冗余， 使用hsetnx
127.0.0.1:6379> hgetall 004
1) "g01:nums"
2) "5"
3) "g01:info"
4) "{...}"
```

#### 5.3.4 hsetnx

```
hsetnx key field value  如果 field 存在则不修改，不存在才添加

127.0.0.1:6379> hgetall 003
1) "g01:nums"
2) "200"
3) "g01:info"
4) "{...}"
127.0.0.1:6379> hsetnx 003 g01:nums 400
(integer) 0 // 003中存在 field g01:nums
127.0.0.1:6379> hsetnx 003 g05:nums 5
(integer) 1
127.0.0.1:6379> hgetall 003
1) "g01:nums"
2) "200"
3) "g01:info"
4) "{...}"
5) "g05:nums"
6) "5"
```

#### 5.3.5 应用2-抢购

- 以商家id作为key
-  将参与抢购的商品id作为field
-  将参与抢购的商品数量作为对应的value
-  抢购时使用降值的方式控制产品数  

```
127.0.0.1:6379> hmset p01 c30 1000 c50 1000 c100 1000
OK
127.0.0.1:6379> hincrby p01 c50 -1
(integer) 999
```

### 5.4 list

#### 5.4.1 简介

- 数据存储需求：存储多个数据，并对数据进入存储空间的**顺序**进行区分
- 需要的存储结构：一个存储空间保存多个数据，且通过数据可以体现进入顺序
- list类型：保存多个数据，底层使用**双向链表存储结构**实现  

#### 5.4.2 基本操作

```
添加/修改数据  
lpush key value1 [value2] ……
rpush key value1 [value2] ……

获取数据
-1 表示最后一个数据
lrange key start stop
lindex key index
llen key

获取并移除数据
lpop key
rpop key

规定时间内获取并移除数据 block 阻塞
blpop key1 [key2] timeout
brpop key1 [key2] timeout
brpoplpush source destination timeout

移除指定数据（从左向右开始删除）
lrem key count value

127.0.0.1:6379> lpush list1 huawei
(integer) 1
127.0.0.1:6379> lpush list1 apple
(integer) 2
127.0.0.1:6379> lpush list1 microsoft
(integer) 3
127.0.0.1:6379> lrange list1 0 2
1) "microsoft"
2) "apple"
3) "huawei"

127.0.0.1:6379> rpush list2 a b c
(integer) 3
127.0.0.1:6379> lrange list2 0 2
1) "a"
2) "b"
3) "c"
127.0.0.1:6379> lrange list2 0 -1
1) "a"
2) "b"
3) "c"
127.0.0.1:6379> lindex list1 0
"microsoft"

127.0.0.1:6379> llen list1
(integer) 3

127.0.0.1:6379> lpush list3 a b c
(integer) 3
127.0.0.1:6379> lpop list3
"c"
127.0.0.1:6379> llen list3
(integer) 2
127.0.0.1:6379> lpop list3
"b"
127.0.0.1:6379> lpop list3
"a"
127.0.0.1:6379> lpop list3
(nil)

% 在5s内需要在list0中push内容
127.0.0.1:6379> blpop list0 5
(nil)
(5.04s)

127.0.0.1:6379> rpush l001  a b c d e
(integer) 5
127.0.0.1:6379> lrange l001 0 -1
1) "a"
2) "b"
3) "c"
4) "d"
5) "e"
127.0.0.1:6379> lrem l001 1 d
(integer) 1
127.0.0.1:6379> lrange l001 0 -1
1) "a"
2) "b"
3) "c"
4) "e"
127.0.0.1:6379> rpush l001 d d c d e d a
(integer) 11
127.0.0.1:6379> lrange l001 0 -1
 1) "a"
 2) "b"
 3) "c"
 4) "e"
 5) "d"
 6) "d"
 7) "c"
 8) "d"
 9) "e"
10) "d"
11) "a"
127.0.0.1:6379> lrem l001 3 d
(integer) 3
127.0.0.1:6379> lrange l001 0 -1
1) "a"
2) "b"
3) "c"
4) "e"
5) "c"
6) "e"
7) "d"
8) "a"

```

#### 5.4.3 注意事项

- list中**保存的数据都是string类型**的，数据总容量是有限的，最多2^32 - 1 个元素 (4294967295)。
-  list具有**索引**的概念，但是操作数据时通常以队列的形式进行入队出队操作，或以栈的形式进行入栈出栈操作
- 获取全部数据操作**结束索引**设置为**-1**
- list可以对数据进行分页操作，通常第一页的信息来自于list，第2页及更多的信息通过数据库的形式加载  

#### 5.4.4 应用-关注列表

最新消息展示：最近添加的信息存储在列表的最顶端

先rpush,再 lrange

```
127.0.0.1:6379> rpush logs a1..
(integer) 1
127.0.0.1:6379> rpush logs a1...
(integer) 2
127.0.0.1:6379> lrange logs 0 -1
1) "a1.."
2) "a1..."
3) "b1.."
4) "c1.."
5) "b1..."
6) "c1..."
```

### 5.5 set

#### 5.5.1 简介

- 新的存储需求：存储大量的数据，在查询方面提供更高的效率
- 需要的存储结构：能够保存大量的数据，高效的内部存储机制，便于查询
- set类型：与**hash存储结构完全相同**，**仅存储键，不存储值（ nil）**，并且值是**不允许重复**的  

#### 5.5.2 基本操作

```
添加数据
sadd key member1 [member2]

获取全部数据
smembers key

删除数据
srem key member1 [member2]

获取集合数据总量
scard key

判断集合中是否包含指定数据
sismember key member

127.0.0.1:6379> sadd users zs
(integer) 1
127.0.0.1:6379> sadd users ls
(integer) 1
127.0.0.1:6379> sadd users ww
(integer) 1
127.0.0.1:6379> smembers users
1) "ls"
2) "ww"
3) "zs"
127.0.0.1:6379> srem users ww
(integer) 1
127.0.0.1:6379> smembers users
1) "ls"
2) "zs"
127.0.0.1:6379> scard users
(integer) 2
127.0.0.1:6379> sismember users zs
(integer) 1
127.0.0.1:6379> sismember users ww
(integer) 0
```

#### 5.5.3 应用

每位用户首次使用今日头条时会设置3项爱好的内容，但是后期为了增加用户的活跃度、兴趣点，必须让用户对其他信息类别逐渐产生兴趣，增加客户留存度，如何实现？  

业务分析

- 系统分析出各个分类的最新或最热点信息条目并组织成set集合
- 随机挑选其中部分信息
- 配合用户关注信息分类中的热点信息组织成展示的全信息集合  

```
随机获取集合中指定数量的数据
srandmember key [count]

随机获取集合中的某个数据并将该数据移出集合
spop key [count]

求两个集合的交、并、差集
sinter key1 [key2]
sunion key1 [key2]
sdiff key1 [key2]

求两个集合的交、并、差集并存储到指定集合中
sinterstore destination key1 [key2]
sunionstore destination key1 [key2]
sdiffstore destination key1 [key2]

将指定数据从原始集合中移动到目标集合中


127.0.0.1:6379> sadd arr1 1 2 3 4 5
(integer) 5
127.0.0.1:6379> sadd arr2 2 3 4 5 9
(integer) 5
127.0.0.1:6379> sinter arr1 arr2
1) "2"
2) "3"
3) "4"
4) "5"
```

### 5.6 sorted_set

#### 基本操作

score 用来排序

```
添加数据
zadd key score1 member1 [score2 member2]

获取全部数据
zrange key start stop [WITHSCORES]
zrevrange key start stop [WITHSCORES]


删除数据
zrem key member [member ...]

按条件获取数据
zrangebyscore key min max [WITHSCORES] [LIMIT]
zrevrangebyscore key max min [WITHSCORES]

条件删除数据
zremrangebyrank key start stop
zremrangebyscore key min max

获取集合数据总量
zcard key
zcount key min max

集合交、并操作
zinterstore destination numkeys key [key ...]
zunionstore destination numkeys key [key ...]

获取数据对应的索引（排名）
zrank key member
zrevrank key member

score值获取与修改
zscore key member
zincrby key increment member
```

#### 注意事项

- score保存的数据存储空间是64位，如果是整数范围是-9007199254740992~9007199254740992
- score保存的数据也可以是一个双精度的double值，基于双精度浮点数的特征，可能会丢失精度，使用时候要慎重
- sorted_set 底层存储还是基于set结构的，因此数据不能重复，如果重复添加相同的数据， score值将被反复覆盖，保留最后一次修改的结果 

#### 应用

任务队列

```
127.0.0.1:6379> zadd tasks 4 order:id:005
(integer) 1
127.0.0.1:6379> zadd tasks 1 order:id:425
(integer) 1
127.0.0.1:6379> zadd tasks 9 order:id:345
(integer) 1
127.0.0.1:6379> zrevrange tasks 0 -1 withscores
1) "order:id:345"
2) "9"
3) "order:id:005"
4) "4"
5) "order:id:425"
6) "1"
127.0.0.1:6379> ZREVRANGE tasks 0 0
1) "order:id:345"
127.0.0.1:6379> ZREM tasks order:id:345
(integer) 1
127.0.0.1:6379> ZREVRANGE tasks 0 -1 withscores
1) "order:id:005"
2) "4"
3) "order:id:425"
4) "1"

```

如果权重条件过多时，需要对排序score值进行处理，保障score值能够兼容2条件或者多条件，例如外贸
订单优先于国内订单，总裁订单优先于员工订单，经理订单优先于员工订单
 因score长度受限，需要对数据进行截断处理，尤其是时间设置为小时或分钟级即可（折算后）
 先设定订单类别，后设定订单发起角色类别，整体score长度必须是统一的，不足位补0。第一排序规则首
位不得是0
 例如外贸101，国内102，经理004，员工008。
 员工下的外贸单score值为101008（优先）
 经理下的国内单score值为102004 

## 6 通用操作

### 6.1 key通用指令 

- key是一个字符串，通过key获取redis中保存的数据 
- 对于key**自身状态**的相关操作，例如：删除，判定存在，获取类型等
- 对于key**有效性**控制相关操作，例如：有效期设定，判定是否有效，有效状态的切换等
- 对于key**快速查询**操作，例如：按指定策略查询key 

#### 6.1.1 基本操作

```
删除指定key
del key 

获取key是否存在
exists key

获取key的类型
type key


127.0.0.1:6379> set str str 
OK
127.0.0.1:6379> hset hash1 hash1 hash1
(integer) 1
127.0.0.1:6379> lpush list1 list1
(integer) 9
127.0.0.1:6379> sadd set1 set1
(integer) 1
127.0.0.1:6379> zadd zset1 1 zset1
(integer) 1
127.0.0.1:6379> type zset1
zset
127.0.0.1:6379> type str
string
127.0.0.1:6379> type hash1
hash
127.0.0.1:6379> exists str
(integer) 1
127.0.0.1:6379> del zset1
(integer) 1
127.0.0.1:6379> del zset1
(integer) 0
127.0.0.1:6379> exists zset1
(integer) 0

```

#### 6.1.2 时效性控制

```
为指定key设置有效期
expire key seconds
pexpire key milliseconds
expireat key timestamp
pexpireat key milliseconds-timestamp

获取key的有效时间
ttl key // -1表示永久，-2表示时效过期
pttl key

获取key的有效时间
ttl key
pttl key

切换key从时效性转换为永久性
persist key // 1 表示执行成功， -1 表示执行失败


127.0.0.1:6379> set str str
OK
127.0.0.1:6379> expire str 10
(integer) 1
127.0.0.1:6379> ttl str
(integer) 7
127.0.0.1:6379> ttl str
(integer) 3
127.0.0.1:6379> ttl str
(integer) 2
127.0.0.1:6379> ttl str
(integer) -2
127.0.0.1:6379> get str
(nil)
127.0.0.1:6379> set str str
OK
127.0.0.1:6379> ttl str
(integer) -1 

127.0.0.1:6379> lpush list1 list1
(integer) 10
127.0.0.1:6379> persist list1
(integer) 0
127.0.0.1:6379> expire list1 60
(integer) 1
127.0.0.1:6379> ttl list1
(integer) 57
127.0.0.1:6379> persist list1
(integer) 1
127.0.0.1:6379> ttl list1
(integer) -1

```

#### 6.1.3 查询模式 

```
查询key
keys pattern

* 匹配任意数量的任意符号 ? 配合一个任意符号 [] 匹配一个指定符号
keys * 查询所有
keys it* 查询所有以it开头
keys *heima 查询所有以heima结尾
keys ??heima 查询所有前面两个字符任意，后面以heima结尾
keys user:? 查询所有以user:开头，最后一个字符任意
keys u[st]er:1 查询所有以u开头，以er:1结尾，中间包含一个字母， s或t

```

#### 6.1.4 key 其他操作 

```
为key改名
rename key newkey
renamenx key newkey // 如果db中不存在该key，这修改为newkey

对所有key排序
sort 返回原来的副本，不改变原数据顺序

其他key通用操作
help @generic


127.0.0.1:6379> flushdb 
OK
127.0.0.1:6379> keys * 

127.0.0.1:6379> set str str 
OK
127.0.0.1:6379> set str1 str1
OK
127.0.0.1:6379> set str2 str2
OK
127.0.0.1:6379> keys * 
1) "str1"
2) "str"
3) "str2"
127.0.0.1:6379> rename str str3
OK
127.0.0.1:6379> keys * 
1) "str1"
2) "str3"
3) "str2"
127.0.0.1:6379> get str3
"str"
127.0.0.1:6379> rename str3 str2  // 将key为str2的值覆盖
OK
127.0.0.1:6379> get str2
"str"

127.0.0.1:6379> keys * 
1) "str1"
2) "str2"
127.0.0.1:6379> renamenx str1 str2
(integer) 0

```



### 6.2 数据库通用指令 

key 的重复问题 .

解决方案

- redis为每个服务提供有16个数据库，编号从0到15
- 每个数据库之间的数据相互独立 

```
切换数据库
select index // 0-15, 共16个数据库

其他操作
quit
ping
echo message

数据移动
move key db

数据清除
dbsize  // 查看当前库中 key 的数量
flushdb // 清空当前库里的所有数据
flushall  // 清空所有数据库的所有数据


127.0.0.1:6379[1]> select 15
OK
127.0.0.1:6379[15]> select 0
OK
127.0.0.1:6379> echo "hello"
"hello"
127.0.0.1:6379> echo hello
"hello"
127.0.0.1:6379> ping 
PONG

127.0.0.1:6379> set name milo
OK
127.0.0.1:6379> select 1
OK
127.0.0.1:6379[1]> get name
(nil)
127.0.0.1:6379[1]> select 0
OK
127.0.0.1:6379> move name 1
(integer) 1
127.0.0.1:6379> get name
(nil)
127.0.0.1:6379> select 1
OK
127.0.0.1:6379[1]> get name
"milo"

```

## 7 Jedis

```
[root@localhost bin]# ./redis-server --port 6380
4183:C 23 Jan 2021 16:37:42.977 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
4183:C 23 Jan 2021 16:37:42.977 # Redis version=5.0.0, bits=64, commit=00000000, modified=0, pid=4183, just started
4183:C 23 Jan 2021 16:37:42.977 # Configuration loaded
4183:M 23 Jan 2021 16:37:42.979 * Increased maximum number of open files to 10032 (it was originally set to 1024).
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 5.0.0 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6380
 |    `-._   `._    /     _.-'    |     PID: 4183
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                    
              
              
[root@localhost bin]# ./redis-cli -p 6380
127.0.0.1:6380> 

# 删除以 # 开头的行和空行，并将其输出到 redis-6379.conf
[root@localhost bin]# cat redis.conf | grep -v "#" | grep -v "^$" > redis-6379.conf

[root@localhost bin]# cat redis-6379.conf 
port 6379
daemonize yes
logfile "6379.log"
dir /usr/local/redis/bin/log

[root@localhost bin]# ./redis-server redis-6379.conf 
[root@localhost bin]# ps -ef | grep redis
root       2683      1  0 03:54 ?        00:01:18 ./redis-server *:6379
root       4257   4109  0 18:09 pts/2    00:00:00 grep --color=auto redis

[root@localhost bin]# ps -ef | grep redis
root       2683      1  0 03:54 ?        00:01:18 ./redis-server *:6379
root       4257   4109  0 18:09 pts/2    00:00:00 grep --color=auto redis
[root@localhost bin]# kill -s 9 2683
[root@localhost bin]# ps -ef | grep redis
root       4260   4162  0 18:11 pts/3    00:00:00 ./redis-cli
root       4265   4109  0 18:14 pts/2    00:00:00 grep --color=auto redis


```

## 8 面试问题

### 1. redis线程安全吗？

redis server 本身是一个单线程的，所以不会又线程安全问题？但是有多个redis cli 去修改同一个资源时就会有类似线程不安全的问题。
