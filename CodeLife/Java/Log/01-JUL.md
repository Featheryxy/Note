## JUL

### 简介

JUL: Java Util Logging是Java原生的日志框架，不用引入第三方jar包

```
Application --> Logger --> Handler --> Formatter

Loggers：被称为记录器，应用程序通过获取Logger对象，调用其API来来发布日志信息。Logger通常时应用程序访问日志系统的入口程序。
Appenders：也被称为Handlers，每个Logger都会关联一组Handlers，Logger会将日志交给关联
Handlers处理，由Handlers负责将日志做记录。Handlers在此是一个抽象，其具体的实现决定了
日志记录的位置可以是控制台、文件、网络上的其他日志服务或操作系统日志等。
Layouts：也被称为Formatters，它负责对日志事件中的数据进行转换和格式化。Layouts决定了数据在一条日志记录中的最终形式。
Level：每条日志消息都有一个关联的日志级别。该级别粗略指导了日志消息的重要性和紧迫，我可以将Level和Loggers，Appenders做关联以便于我们过滤消息。
Filters：过滤器，根据需要定制哪些信息会被记录，哪些信息会被放过。
```

### 日志级别

```java
import java.util.logging.*;
/*
日志级别，一个日志级别由一个整形数字来定义
OFF, SEVERE, WARNING, INFO, CONFIG, FINE, FINER, FINEST, ALL


OFF Integer.MAX_VALUE
INFO 800    
ALL Integer.MIN_VALUE
*/

@Test
public void testLogLevel()throws Exception{
    // 1.获取日志记录器对象
    Logger logger = Logger.getLogger("com.itheima.JULTest");
    // 2.日志记录输出
    logger.severe("severe");
    logger.warning("warning");
    logger.info("info"); // 默认日志输出级别
    logger.config("config");
    logger.fine("fine");
    logger.finer("finer");
    logger.finest("finest");

}    
```

### 父子关系

```java
        Logger logger1 = Logger.getLogger("com");
        Logger logger2 = Logger.getLogger("com.milo");

        System.out.println("logger1's: "+logger1.getName());
        System.out.println("logger2's: "+logger2.getName());
        System.out.println(logger2.getParent() == logger1);

        // 所有日志记录器的顶级父元素 LogManager$RootLogger，name ""
        System.out.println("logger1 Parent: "+logger1.getParent() + ",name:" + logger1.getParent().getName());
        //logger1's: com
        //logger2's: com.milo
        //true
        //logger1 Parent: java.util.logging.LogManager$RootLogger@7a36aefa,name:
```

### 文件配置

```java
     @Test
    public void testLogProperties()throws Exception{

        // 读取配置文件，通过类加载器
        InputStream ins = JULTest.class.getClassLoader().getResourceAsStream("logging.properties");
        // 创建LogManager
        LogManager logManager = LogManager.getLogManager();
        // 通过LogManager加载配置文件
        logManager.readConfiguration(ins);

        // 创建日志记录器
        Logger logger = Logger.getLogger("test");

        logger.severe("severe");
        logger.warning("warning");
        logger.info("info");
        logger.config("config");
        logger.fine("fine");
        logger.finer("finer");
        logger.finest("finest");

    }
```

```pr
# RootLogger 顶级父元素指定的默认处理器为：ConsoleHandler
#handlers= java.util.logging.ConsoleHandler

# RootLogger 顶级父元素默认的日志级别为：ALL
#.level= ALL

# 自定义 Logger 使用 名为com.itheima的logger
test.handlers = java.util.logging.ConsoleHandler
test.level = CONFIG

# 关闭默认配置
#test.useParentHanlders = false


# 向日志文件输出的 handler 对象
# 指定日志文件路径 /logs/java0.log
java.util.logging.FileHandler.pattern = E:/log/java%u.log
# 指定日志文件内容大小
java.util.logging.FileHandler.limit = 50000
# 指定日志文件数量
java.util.logging.FileHandler.count = 1
# 指定 handler 对象日志消息格式对象
java.util.logging.FileHandler.formatter = java.util.logging.SimpleFormatter
# 指定以追加方式添加日志内容
java.util.logging.FileHandler.append = true


# 向控制台输出的 handler 对象
# 指定 handler 对象的日志级别
java.util.logging.ConsoleHandler.level = ALL
# 指定 handler 对象的日志消息格式对象
java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter
# 指定 handler 对象的字符集
java.util.logging.ConsoleHandler.encoding = UTF-8

# 指定日志消息格式
java.util.logging.SimpleFormatter.format = %4$s: %5$s [%1$tc]%n
```

### 原理

1. 初始化LogManager
2. LogManager加载logging.properties配置
3. 添加Logger到LogManager
4. 从单例LogManager获取Logger
5. 设置级别Level，并指定日志记录LogRecord
6. Filter提供了日志级别之外更细粒度的控制
7. Handler是用来处理日志输出位置
8. Formatter是用来格式化LogRecord的

![image-20220305135037338](E:\GitHubNote\Note\Java\Log\JUL.assets\image-20220305135037338.png)