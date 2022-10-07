## 概述

当单表的数据量达到1000W或100G以后，由于查询维度较多，即使添加从库、优化索引，做很多操作时性能仍下降严重。  

1. 通过**提升服务器硬件能力**来提高数据处理能力，比如增加存储容量 、CPU等，这种方案成本很高，并且如果瓶颈在
   MySQL本身那么提高硬件也是有很的。  
2. **分库分表**，把数据分散在不同的数据库中，使得单一数据库的数据量变小来缓解单一数据库的性能问题，从而达到提升数据库性能的目的  

## 分库分表的方式

### 垂直分表

垂直分表：将一个表按照字段分成多表，每个表存储其中一部分字段。  

优点：

1. 为了避免IO争抢并减少锁表的几率
2. 充分发挥热门数据的操作效率

拆分原则：

1. 把不常用的字段单独放在一张表;
2. 把text，blob等大字段拆分出来放在附表中;
3. 经常组合查询的列放在一张表中;  

为什么大字段IO效率低：

1. 由于数据量本身大，需要长时间读取
2. 跨页，页是数据库存储单位，很多查找及定位操作都是以页为单位，单页内的数据行越多数据库整体性能越好，而大字段占用空间大，单页内存储行数少，因此IO效率较低
3. 数据库以行为单位将数据加载到内存中，这样表中字段长度较短且访问频率较高，内存能加载更多的数据，命中率更高，减少了磁盘IO，从而提升了数据库性能

### 垂直分库  

垂直分库：**按照业务将表进行分类**，分布到不同的数据库上面，每个库可以放在不同的服务器上，它的核心理念是**专库专用** （trans, pub） 

优点：

- 解决业务层面的耦合，业务清晰
- 能对不同业务的数据进行分级管理、维护、监控、扩展等
- 高并发场景下，垂直分库一定程度的提升IO、数据库连接数、降低单机硬件资源的瓶颈  

### 水平分库  

水平分库：把同一个表的数据按一定规则拆到不同的数据库中(如根据id的奇偶)，每个库可以放在不同的服务器上。  

优点：

- 解决了单库大数据，高并发的性能瓶颈。

- 提高了系统的稳定性及可用性。  

  > 稳定性体现在IO冲突减少，锁定减少，可用性指某个库出问题，部分可用

当一个应用难以再细粒度的垂直切分，或切分后数据量行数巨大，存在单库读写、存储性能瓶颈，这时候就需要进
行水平分库了，经过水平切分的优化，往往能解决单库存储量及性能瓶颈。但由于同一个表被分配在不同的数据
库，需要额外进行数据操作的路由工作，因此大大提升了系统复杂度。  

### 水平分表

解决**单表数据量大**  

水平分表：在同一个数据库内，把同一个表的数据按一定规则拆到多个表中  

优点：

- 优化单一表数据量过大而产生的性能问题
- 避免IO争抢并减少锁表的几率  

库内的水平分表，解决了单一表数据量过大的问题，分出来的小表中只包含一部分数据，从而使得单个表的数据量
变小，提高检索性能。  

### 小结

垂直分表：可以把一个**宽表**的**字段按访问频次、是否是大字段的原则拆分为多个表**，这样既能使业务清晰，还能提
升部分性能。拆分后，尽量从业务角度避免联查，否则性能方面将得不偿失。

垂直分库：可以**把多个表按业务耦合松紧归类，分别存放在不同的库**，这些库可以分布在不同服务器，从而使访问
压力被多服务器负载，大大提升性能，同时能提高整体架构的业务清晰度，不同的业务库可根据自身情况定制优化
方案。但是它需要解决跨库带来的所有复杂问题。

水平分库：由于**单库数据量大**，可以**把一个表的数据(按数据行)分到多个不同的库**，每个库只有这个表的部分数据，这些库可以分布在
不同服务器，从而使访问压力被多服务器负载，大大提升性能。它不仅需要解决跨库带来的所有复杂问题，还要解
决数据路由的问题(数据路由问题后边介绍)。

水平分表：由于**单表数据量大**，可以**把一个表的数据(按数据行)分到多个同一个数据库的多张表中**，每个表只有这个表的部分数据，这
样做能小幅提升性能，它仅仅作为水平分库的一个补充优化。

一般来说，在系统设计阶段就应该根据业务耦合松紧来确定**垂直分库，垂直分表**方案，在数据量及访问压力不是特
别大的情况，首先考虑**缓存**、**读写分离**、**索引技术**等方案。若**数据量极大，且持续增长，再考虑水平分库水平分表**
方案  

## 分库分表带来的问题

### 事务一致性问题  

由于分库分表把数据分布在不同库甚至不同服务器，不可避免会带来**分布式事务**问题。

### 跨节点关联查询  

垂直分库后[商品信息]和[店铺信息]不在一个数据库，甚至不在一台服务器，无法进行关联查询。  

**可将原关联查询分为两次查询，第一次查询的结果集中找出关联数据id，然后根据id发起第二次请求得到关联数**
**据，最后将获得到的数据进行拼装**。  

### 跨节点分页、排序函数  

跨节点多库进行查询时，limit分页、order by排序等问题，就变得比较复杂了。需要**先在不同的分片节点中将数据进行排序并返回，然后将不同分片返回的结果集进行汇总和再次排序**。  

### 主键避重  

在分库分表环境中，由于表中数据同时存在不同数据库中，主键值平时使用的自增长将无用武之地，某个分区数据库生成的ID无法保证全局唯一。因此需要**单独设计全局主键**，以避免跨库主键重复问题。  

### 公共表  

实际的应用场景中，参数表、数据字典表等都是数据量较小，变动少，而且属于高频联合查询的依赖表。  

可以将这类表在每个数据库都保存一份，所有对公共表的更新操作都同时发送到所有分库执行  

## Sharding-JDBC介绍

Sharding-JDBC是当当网研发的开源分布式数据库中间件，从 3.0 开始Sharding-JDBC被包含在 Sharding-Sphere中，之后该项目进入进入Apache孵化器，4.0版本之后的版本为Apache版本。
ShardingSphere是一套开源的分布式数据库中间件解决方案组成的生态圈，它由Sharding-JDBC、ShardingProxy和Sharding-Sidecar（计划中）这3款相互独立的产品组成。 他们均提供标准化的数据分片、分布式事务和
数据库治理功能，可适用于如Java同构、异构语言、容器、云原生等各种多样化的应用场景。
官方地址：https://shardingsphere.apache.org/document/current/cn/overview/  

咱们目前只需关注Sharding-JDBC，它定位为轻量级Java框架，在Java的JDBC层提供的额外服务。 它使用客户端直连数据库，以jar包形式提供服务，无需额外部署和依赖，可理解为增强版的JDBC驱动，完全兼容JDBC和各种ORM框架。  

Sharding-JDBC的核心功能为**数据分片**和**读写分离**，通过Sharding-JDBC，应用可以透明的使用jdbc访问已经分库分表、读写分离的多个数据源，而**不用关心数据源的数量以及数据如何分布**。  

- 适用于任何基于Java的ORM框架，如： Hibernate, Mybatis, Spring JDBC Template或直接使用JDBC。  
- 基于任何第三方的数据库连接池，如：DBCP, C3P0, BoneCP, Druid, HikariCP等。  
- 基于任何第三方的数据库连接池，如：DBCP, C3P0, BoneCP, Druid, HikariCP等。  

### 与JDBC的比较

1. 性能损耗测试：服务器资源充足、并发数相同，比较JDBC和Sharding-JDBC性能损耗，Sharding-JDBC相对JDBC损耗不超过7%  (单库单表)
2. 性能对比测试：服务器资源使用到极限，相同的场景JDBC与Sharding-JDBC的吞吐量相当。  
3. 性能对比测试：服务器资源使用到极限，Sharding-JDBC采用分库分表后，Sharding-JDBC吞吐量较JDBC不分表有接近2倍的提升。  

## Sharding-JDBC原理

### 配置文件

#### properties

```properties
# 定义数据源 m1
spring.shardingsphere.datasource.names = m1
spring.shardingsphere.datasource.m1.type = com.alibaba.druid.pool.DruidDataSource
spring.shardingsphere.datasource.m1.driver‐class‐name = com.mysql.jdbc.Driver
spring.shardingsphere.datasource.m1.url = jdbc:mysql://localhost:3306/order_db?useUnicode=true
spring.shardingsphere.datasource.m1.username = root
spring.shardingsphere.datasource.m1.password = root

# 指定t_order表的数据分布情况，配置数据节点 m1.t_order_1 和 m1.t_order_2
spring.shardingsphere.sharding.tables.t_order.actual‐data‐nodes = m1.t_order_$‐>{1..2}

# 指定t_order表的主键生成策略为SNOWFLAKE
spring.shardingsphere.sharding.tables.t_order.key‐generator.column=order_id
spring.shardingsphere.sharding.tables.t_order.key‐generator.type=SNOWFLAKE

# 指定t_order表的分片策略，分片策略包括分片键 order_id 和分片算法，
# order_id为偶数的数据落在t_order_1，为奇数的落在t_order_2
spring.shardingsphere.sharding.tables.t_order.table‐strategy.inline.sharding‐column = order_id
spring.shardingsphere.sharding.tables.t_order.table‐strategy.inline.algorithm‐expression =
t_order_$‐>{order_id % 2 + 1}
```

#### Configuration

```java
@Configuration
public class ShardingJdbcConfig {
	// 定义数据源
    Map<String, DataSource> createDataSourceMap() {
        DruidDataSource dataSource1 = new DruidDataSource();
        dataSource1.setDriverClassName("com.mysql.jdbc.Driver");
        dataSource1.setUrl("jdbc:mysql://localhost:3306/order_db?useUnicode=true");
        dataSource1.setUsername("root");
        dataSource1.setPassword("root");
        Map<String, DataSource> result = new HashMap<>();
        result.put("m1", dataSource1);
        return result;
	}
	// 定义主键生成策略
    private static KeyGeneratorConfiguration getKeyGeneratorConfiguration() {
        KeyGeneratorConfiguration result = new
        KeyGeneratorConfiguration("SNOWFLAKE","order_id");
        return result;
    }
    
	// 定义t_order表的分片策略
    TableRuleConfiguration getOrderTableRuleConfiguration() {
        TableRuleConfiguration result = new TableRuleConfiguration("t_order","m1.t_order_$‐>
        {1..2}");
        result.setTableShardingStrategyConfig(new
        InlineShardingStrategyConfiguration("order_id", "t_order_$‐>{order_id % 2 + 1}"));
        result.setKeyGeneratorConfig(getKeyGeneratorConfiguration());
        return result;
    }
    // 定义sharding‐Jdbc数据源
    @Bean
    DataSource getShardingDataSource() throws SQLException {
        ShardingRuleConfiguration shardingRuleConfig = new ShardingRuleConfiguration();
        shardingRuleConfig.getTableRuleConfigs().add(getOrderTableRuleConfiguration());
        //spring.shardingsphere.props.sql.show = true
        Properties properties = new Properties();
        properties.put("sql.show","true");
        return ShardingDataSourceFactory.createDataSource(createDataSourceMap(),shardingRuleConfig,properties);
	}
}
```

由于采用了配置类所以需要屏蔽原来application.properties文件中spring.shardingsphere开头的配置信息。还需要在SpringBoot启动类中屏蔽使用spring.shardingsphere配置项的类：

```java
@SpringBootApplication(exclude = {SpringBootConfiguration.class})
public class ShardingJdbcSimpleDemoBootstrap {....}
```



### 基本概念

**逻辑表**：**水平拆分的数据表的总称**。例：订单数据表根据主键尾数拆分为10张表，分别是 t_order_0 、 t_order_1 到
t_order_9 ，他们的逻辑表名为 **t_order** 。  

**真实表**：在分片的数据库中真实存在的物理表, **分表**。即上个示例中的 **t_order_0 到 t_order_9** 。

**数据节点**：数据**分片的最小物理单元**。由数据源名称和数据表组成，例： **ds_0.t_order_0** 。

绑定表：指分片规则一致的主表和子表。例如： t_order 表和 t_order_item 表，均按照 order_id 分片,绑定表之间的分区
键完全相同，则此两张表互为绑定表关系。绑定表之间的多表关联查询不会出现笛卡尔积关联，关联查询效率将大
大提升  

**广播表**：指**所有的分片数据源中都存在的表**，表结构和表中的数据在每个数据库中均完全一致。适用于数据量不大且需要与海量数据的表进行关联查询的场景，例如：字典表  

**分片键**：用于分片的数据库字段，是将**数据库(表)水平拆分的关键字段**。例：将订单表中的订单主键的尾数取模分片，则订单主键为分片字段。 SQL中如果无分片字段，将执行全路由，性能较差。 除了对单分片字段的支持，ShardingJdbc也支持根据多个字段进行分片。  

**分片算法**：通过分片算法将数据分片，支持通过 = 、 BETWEEN 和 IN 分片。分片算法需要应用方开发者自行实现，可实现的灵
活度非常高。包括：精确分片算法 、范围分片算法 ，复合分片算法 等。例如：where order_id = ? 将采用精确分
片算法，where order_id in (?,?,?)将采用精确分片算法，where order_id BETWEEN ? and ? 将采用范围分片算
法，复合分片算法用于分片键有多个复杂情况。  

**分片策略**：**包含分片键和分片算法**，由于分片算法的独立性，将其独立抽离。真正可用于分片操作的是分片键 + 分片算法，也
就是分片策略。内置的分片策略大致可分为尾数取模、哈希、范围、标签、时间等。由用户方配置的分片策略则更
加灵活，常用的使用行表达式配置分片策略，它采用Groovy表达式表示，如: **t_user_$->{u_id % 8}** 表示t_user
表根据u_id模8，而分成8张表，表名称为 t_user_0 到 t_user_7 。  

**自增主键生成策略**：通过在客户端生成自增主键替换以数据库原生自增主键的方式，做到分布式主键无重复。

**$**： **占位符**

### SQL解析

当Sharding-JDBC接受到一条SQL语句时，会陆续执行 **SQL解析（逻辑SQL） => 查询优化 => SQL路由 => SQL改写(真实SQL) => SQL执行 =>结果归并** ，最终返回执行结果。  

**SQL解析**过程**分为词法解析和语法解析**。 

- **词法解析器**用于将**SQL拆解为**不可再分的原子符号**Token**，并根据不同数据库方言所提供的字典，将其归类为关键字，表达式，字面量和操作符。 
- 再使用**语法解析器将SQL转换为抽象语法树**  

### SQL路由  

SQL路由就是把针对**逻辑表**的数据操作映射到对**数据结点**操作的过程。

根据解析上下文匹配数据库和表的分片策略，并生成路由路径。 对于携带分片键的SQL，根据分片键操作符不同可
以划分为单片路由(分片键的操作符是等号)、多片路由(分片键的操作符是IN)和范围路由(分片键的操作符是
BETWEEN)，不携带分片键的SQL则采用广播路由。根据分片键进行路由的场景可分为直接路由、标准路由、笛卡
尔路由等。  

**标准路由**

标准路由是Sharding-Jdbc最为推荐使用的分片方式，它的适用范围是不包含关联查询或仅包含绑定表之间关联查
询的SQL。 当分片运算符是等于号时，路由结果将落入单库（表），当分片运算符是BETWEEN或IN时，则路由结
果不一定落入唯一的库（表），因此一条逻辑SQL最终可能被拆分为多条用于执行的真实SQL。 举例说明，如果按
照 order_id 的奇数和偶数进行数据分片，一个单表查询的SQL如下：

SELECT * FROM t_order WHERE order_id IN (1, 2);

那么路由的结果应为：

SELECT * FROM t_order_0 WHERE order_id IN (1, 2);
SELECT * FROM t_order_1 WHERE order_id IN (1, 2);  

**笛卡尔路由**

笛卡尔路由是最复杂的情况，它无法根据绑定表的关系定位分片规则，因此非绑定表之间的关联查询需要拆解为笛
卡尔积组合执行。   

**全库表路由**

对于不携带分片键的SQL，则采取广播路由的方式。根据SQL类型又可以划分为全库表路由、全库路由、全实例路
由、单播路由和阻断路由这5种类型。其中全库表路由用于处理对数据库中与其逻辑表相关的所有真实表的操作，
主要包括不带分片键的DQL(数据查询)和DML（数据操纵），以及DDL（数据定义）等  

### **SQL改写**  

工程师面向逻辑表书写的SQL，并不能够直接在真实的数据库中执行，SQL改写用于将逻辑SQL改写为在真实数据
库中可以正确执行的SQL。  

### SQL执行  

Sharding-JDBC采用一套自动化的执行引擎，负责将路由和改写完成之后的真实SQL安全且高效发送到底层数据源
执行。 它不是简单地将SQL通过JDBC直接发送至数据源执行；也并非直接将执行请求放入线程池去并发执行。它
更关注平衡数据源连接创建以及内存占用所产生的消耗，以及最大限度地合理利用并发等问题。 执行引擎的目标是
自动化的平衡资源控制与执行效率，他能在以下两种模式自适应切换：  

**内存限制模式**

使用此模式的前提是，Sharding-JDBC对一次操作所耗费的数据库连接数量不做限制。 如果实际执行的SQL需要对
某数据库实例中的200张表做操作，则对每张表创建一个新的数据库连接，并通过多线程的方式并发处理，以达成
执行效率最大化。  

**连接限制模式**

使用此模式的前提是，Sharding-JDBC严格控制对一次操作所耗费的数据库连接数量。 如果实际执行的SQL需要对
某数据库实例中的200张表做操作，那么只会创建唯一的数据库连接，并对其200张表串行处理。 如果一次操作中
的分片散落在不同的数据库，仍然采用多线程处理对不同库的操作，但每个库的每次操作仍然只创建一个唯一的数
据库连接。
内存限制模式适用于OLAP操作，可以通过放宽对数据库连接的限制提升系统吞吐量； 连接限制模式适用于OLTP操
作，OLTP通常带有分片键，会路由到单一的分片，因此严格控制数据库连接，以保证在线系统数据库资源能够被
更多的应用所使用，是明智的选择。  

### 结果归并  

将从各个数据节点获取的多数据结果集，组合成为一个结果集并正确的返回至请求客户端，称为结果归并。
Sharding-JDBC支持的结果归并从功能上可分为遍历、排序、分组、分页和聚合5种类型，它们是组合而非互斥的
关系  

结果归并从结构划分可分为流式归并、内存归并和装饰者归并。流式归并和内存归并是互斥的，装饰者归并可以在
流式归并和内存归并之上做进一步的处理。
**内存归并**很容易理解，他是将所有分片结果集的数据都遍历并存储在内存中，再通过统一的分组、排序以及聚合等
计算之后，再将其封装成为逐条访问的数据结果集返回。  

**流式归并**是指每一次从数据库结果集中获取到的数据，都能够通过游标逐条获取的方式返回正确的单条数据，它与
数据库原生的返回结果集的方式最为契合。  

**装饰者归并**是对所有的结果集归并进行统一的功能增强，比如归并时需要聚合SUM前，在进行聚合计算前，都会通
过内存归并或流式归并查询出结果集。因此，聚合归并是在之前介绍的归并类型之上追加的归并能力，即装饰者模
式。  



## 分库

### 分片策略

```properties
# 分库策略，以user_id为分片键，分片策略为user_id % 2 + 1，user_id为偶数操作m1数据源，否则操作m2。
spring.shardingsphere.sharding.tables.t_order.database‐strategy.inline.sharding‐column = user_id
spring.shardingsphere.sharding.tables.t_order.database‐strategy.inline.algorithm‐expression =
m$‐>{user_id % 2 + 1}

#分库策略，如何将一个逻辑表映射到多个数据源
spring.shardingsphere.sharding.tables.<逻辑表名称>.database‐strategy.<分片策略>.<分片策略属性名>= #
分片策略属性值
#分表策略，如何将一个逻辑表映射为多个实际表
spring.shardingsphere.sharding.tables.<逻辑表名称>.table‐strategy.<分片策略>.<分片策略属性名>= #分
片策略属性值
```



不管理分库还是分表，分片策略基本一样。

- **standard**：标准分片策略，对应StandardShardingStrategy。提供对SQL语句中的=, IN和BETWEEN AND的分片操作支持。StandardShardingStrategy只支持单分片键，提供PreciseShardingAlgorithm和RangeShardingAlgorithm两个分片算法。PreciseShardingAlgorithm是必选的，用于处理=和IN的分片。RangeShardingAlgorithm是可选的，用于处理BETWEEN AND分片，如果不配置RangeShardingAlgorithm，SQL中的BETWEEN AND将按照全库路由处理。
- **complex**：符合分片策略，对应ComplexShardingStrategy。复合分片策略。提供对SQL语句中的=, IN和BETWEEN AND的分片操作支持。ComplexShardingStrategy支持多分片键，由于多分片键之间的关系复杂，因此并未进行过多的封装，而是直接将分片键值组合以及分片操作符透传至分片算法，完全由应用开发者实现，提供最大的灵活度。
- **inline**：行表达式分片策略，对应InlineShardingStrategy。使用Groovy的表达式，提供对SQL语句中的=和IN的分片操作支持，**只支持单分片键**。对于简单的分片算法，可以通过简单的配置使用，从而避免繁琐的Java代码开发，如: t_user_$->{u_id % 8} 表示t_user表根据u_id模8，而分成8张表，表名称为 t_user_0 到t_user_7 。
- **hint**：Hint分片策略，对应HintShardingStrategy。通过Hint而非SQL解析的方式分片的策略。对于分片字段非SQL决定，而由其他外置条件决定的场景，可使用SQL Hint灵活的注入分片字段。例：内部系统，按照员工登录主键分库，而数据库中并无此字段。SQL Hint支持通过Java API和SQL注释(待实现)两种方式使用。
- **none**：不分片策略，对应NoneShardingStrategy。不分片的策略。目前例子中都使用inline分片策略，若对其他分片策略细节若感兴趣，请查阅官方文档：https://shardingsphere.apache.org  







数据源

分库

数据节点

主键生成策略

分片策略



## 读写分离

将数据库拆分为主库和从库

- **主库**负责处理**事务性的增删改操作**，
- **从库**负责处理**查询操作**，能够有效的避免由数据更新导致的行锁，使得整个系统的查询性能得到极大的改善  



Sharding-JDBC读写分离则是根据SQL语义的分析，将读操作和写操作分别路由至主库与从库。Sharding-JDBC提供一主多从的读写分离配置，可独立使用，也可配合分库分表使用，同一线程且同一数据库连接
内，如有写入操作，以后的读操作均从主库读取，用于保证数据一致性。Sharding-JDBC不提供主从数据库的数据
同步功能，需要采用其他机制支持。    