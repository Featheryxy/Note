## JCL

### 简介

JCL: Jakarta Commons Logging 是Apache提供的一个通用日志API

它是为 "所有的Java日志实现"提供一个统一的接口，它自身也提供一个日志的实现，但是功能非常常弱（SimpleLog）。所以一般不会单独使用它。他允许开发人员使用不同的具体日志实现工具: Log4j, Jdk自带的日志（JUL)

JCL 有两个基本的抽象类：Log(基本记录器)和LogFactory(负责创建Log实例)

![image-20220305200735548](E:\GitHubNote\Note\Java\Log\JCL.assets\image-20220305200735548.png)

```xml
<dependency>
    <groupId>commons-logging</groupId>
    <artifactId>commons-logging</artifactId>
    <version>1.2</version>
</dependency>
```

**why**

1. 面向接口开发，不再依赖具体的实现类。减少代码的耦合
2. 项目通过导入不同的日志实现类，可以灵活的切换日志框架
3. 统一API，方便开发者学习和使用
4. 统一配置便于项目日志的管理

### 原理

1. 通过LogFactory动态加载Log实现类

   ![image-20220305201337289](E:\GitHubNote\Note\Java\Log\JCL.assets\image-20220305201337289.png)

2. 日志门面支持的日志实现数组

```java
private static final String[] classesToDiscover =
	new String[]{"org.apache.commons.logging.impl.Log4JLogger",
        "org.apache.commons.logging.impl.Jdk14Logger",
        "org.apache.commons.logging.impl.Jdk13LumberjackLogger",
        "org.apache.commons.logging.impl.SimpleLog"};
```

3. 获取具体的日志实现

   ```java
   for(int i = 0; i < classesToDiscover.length && result == null; ++i) {
   	result = this.createLogFromClass(classesToDiscover[i], logCategory, true);
   }
   ```

   