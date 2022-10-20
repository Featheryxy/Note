## Log4J

### 简介

```xml
<dependency>
    <groupId>log4j</groupId>
    <artifactId>log4j</artifactId>
    <version>1.2.17</version>
</dependency>
```

### 日志级别

**OFF** 	为最高等级 关闭了日志信息
FATAL  	为可能导致应用中止的严重事件错误
**ERROR** 	为**严重错误** 主要是程序的错误
**WARN** 	为**一般警告**，比如session丢失
**INFO** 	  为**一般要显示的信息**，比如登录登出
**DEBUG** 	为程序的**调试信息**
TRACE 	为比DEBUG更细粒度的事件信息
**ALL** 	为**最低等级，将打开所有级别的日志**

### 组件

Log4J 主要由 Loggers (日志记录器)、Appenders（输出端）和 Layout（日志格式化器）组成

1. Loggers 控制日志的输出级别与日志是否输出；
2. Appenders 指定日志的输出方式（输出到控制台、文件等）；
3. Layout 控制日志信息的输出格式。

#### Loggers 

日志记录器，负责收集处理日志记录，**实例的命名就是类“XX”的full quailied name（类的全限定名）**，Logger的名字大小写敏感，其命名**有继承机制**：例如：name为org.apache.commons的logger会继承name为org.apache的logger。
Log4J中有一个特殊的logger叫做**“root”，他是所有logger的根**，也就意味着其他所有的logger都会直接或者间接地继承自root。root logger可以用Logger.getRootLogger()方法获取。

#### Appender

用来指定日志输出到哪个地方，可以同时指定日志的输出目的地。Log4j 常用的输出目的地有以下几种：

ConsoleAppender：将日志输出到控制台
FileAppender：将日志输出到文件中
DailyRollingFileAppender：将日志输出到一个日志文件，并且每天输出到一个新的文件
RollingFileAppender：将日志信息输出到一个日志文件，并且指定文件的尺寸，当文件大小达到指定尺寸时，会自动把文件改名，同时产生一个新的文件
JDBCAppender：把日志信息保存到数据库中

#### Layouts

布局器 Layouts用于控制日志输出内容的格式，让我们可以使用各种需要的格式输出日志。Log4j常用的Layouts:

HTMLLayout：格式化日志输出为HTML表格形式
SimpleLayout：简单的日志输出格式化，打印的日志格式为（info - message）
PatternLayout：最强大的格式化期，可以根据自定义格式输出日志，如果没有指定转换格式，就是用**默认的转换格式**



#### Layout的格式

```
 log4j 采用类似 C 语言的 printf 函数的打印格式格式化日志信息，具体的占位符及其含义如下：
    %m 输出代码中指定的日志信息
    %p 输出优先级，及 DEBUG、INFO 等
    %n 换行符（Windows平台的换行符为 "\n"，Unix 平台为 "\n"）
    %r 输出自应用启动到输出该 log 信息耗费的毫秒数
    %c 输出打印语句所属的类的全名
    %t 输出产生该日志的线程全名
    %d 输出服务器当前时间，默认为 ISO8601，也可以指定格式，如：%d{yyyy年MM月dd日HH:mm:ss}
    %l 输出日志时间发生的位置，包括类名、线程、及在代码中的行数。如：Test.main(Test.java:10)
    %F 输出日志消息产生时所在的文件名称
    %L 输出代码中的行号
    %% 输出一个 "%" 字符
* 可以在 % 与字符之间加上修饰符来控制最小宽度、最大宽度和文本的对其方式。如：
    %5c 输出category名称，最小宽度是5，category<5，默认的情况下右对齐
    %-5c 输出category名称，最小宽度是5，category<5，"-"号指定左对齐,会有空格
    %.5c 输出category名称，最大宽度是5，category>5，就会将左边多出的字符截掉，<5不会有空格
    %20.30c category名称<20补空格，并且右对齐，>30字符，就从左边交远销出的字符截掉
```

### 自定义Logger

```properties
# RootLogger配置
log4j.rootLogger = trace,console

# 自定义Logger
log4j.logger.com.itheima = info,file
log4j.logger.org.apache = error
```

```java
@Test
public void testCustomLogger() throws Exception {
// 自定义 com.itheima
Logger logger1 = Logger.getLogger(Log4jTest.class);
logger1.fatal("fatal"); // 严重错误，一般会造成系统崩溃和终止运行
logger1.error("error"); // 错误信息，但不会影响系统运行
logger1.warn("warn"); // 警告信息，可能会发生问题
logger1.info("info"); // 程序运行信息，数据库的连接、网络、IO操作等
logger1.debug("debug"); // 调试信息，一般在开发阶段使用，记录程序的变量、参数等
logger1.trace("trace"); // 追踪信息，记录程序的所有流程信息
// 自定义 org.apache
Logger logger2 = Logger.getLogger(Logger.class);
logger2.fatal("fatal logger2"); // 严重错误，一般会造成系统崩溃和终止运行
logger2.error("error logger2"); // 错误信息，但不会影响系统运行
logger2.warn("warn logger2"); // 警告信息，可能会发生问题
logger2.info("info logger2"); // 程序运行信息，数据库的连接、网络、IO操作等
logger2.debug("debug logger2"); // 调试信息，一般在开发阶段使用，记录程序的变量、参
数等
logger2.trace("trace logger2"); // 追踪信息，记录程序的所有流程信息
}
```



### demo

```properties
# 指定 RootLogger 顶级父元素默认配置信息
# 指定日志级别=trace，使用的 apeender 为=console
log4j.rootLogger = trace,console

# 自定义 logger 对象设置

log4j.logger.com.itheima = info,console
log4j.logger.org.apache = error,console

# 指定控制台日志输出的 appender
log4j.appender.console = org.apache.log4j.ConsoleAppender
# 指定消息格式 layout
log4j.appender.console.layout = org.apache.log4j.PatternLayout
# 指定消息格式的内容
log4j.appender.console.layout.conversionPattern = [%-10p]%r  %l %d{yyyy-MM-dd HH:mm:ss.SSS} %m%n

# 日志文件输出的 appender 对象
log4j.appender.file = org.apache.log4j.FileAppender
# 指定消息格式 layout
log4j.appender.file.layout = org.apache.log4j.PatternLayout
# 指定消息格式的内容
log4j.appender.file.layout.conversionPattern = [%-10p]%r  %l %d{yyyy-MM-dd HH:mm:ss.SSS} %m%n
# 指定日志文件保存路径
log4j.appender.file.file = /logs/log4j.log
# 指定日志文件的字符集
log4j.appender.file.encoding = UTF-8


# 按照文件大小拆分的 appender 对象
# 日志文件输出的 appender 对象
log4j.appender.rollingFile = org.apache.log4j.RollingFileAppender
# 指定消息格式 layout
log4j.appender.rollingFile.layout = org.apache.log4j.PatternLayout
# 指定消息格式的内容
log4j.appender.rollingFile.layout.conversionPattern = [%-10p]%r  %l %d{yyyy-MM-dd HH:mm:ss.SSS} %m%n
# 指定日志文件保存路径
log4j.appender.rollingFile.file = /logs/log4j.log
# 指定日志文件的字符集
log4j.appender.rollingFile.encoding = UTF-8
# 指定日志文件内容的大小
log4j.appender.rollingFile.maxFileSize = 1MB 
# 指定日志文件的数量
log4j.appender.rollingFile.maxBackupIndex = 10


# 按照时间规则拆分的 appender 对象
log4j.appender.dailyFile = org.apache.log4j.DailyRollingFileAppender
# 指定消息格式 layout
log4j.appender.dailyFile.layout = org.apache.log4j.PatternLayout
# 指定消息格式的内容
log4j.appender.dailyFile.layout.conversionPattern = [%-10p]%r  %l %d{yyyy-MM-dd HH:mm:ss.SSS} %m%n
# 指定日志文件保存路径
log4j.appender.dailyFile.file = /logs/log4j.log
# 指定日志文件的字符集
log4j.appender.dailyFile.encoding = UTF-8
# 指定日期拆分规则
log4j.appender.dailyFile.datePattern = '.'yyyy-MM-dd-HH-mm-ss


#mysql
log4j.appender.logDB=org.apache.log4j.jdbc.JDBCAppender
log4j.appender.logDB.layout=org.apache.log4j.PatternLayout
log4j.appender.logDB.Driver=com.mysql.jdbc.Driver
log4j.appender.logDB.URL=jdbc:mysql://localhost:3306/test
log4j.appender.logDB.User=root
log4j.appender.logDB.Password=root
log4j.appender.logDB.Sql=INSERT INTO log(project_name,create_date,level,category,file_name,thread_name,line,all_category,message) values('itcast','%d{yyyy-MM-dd HH:mm:ss}','%p','%c','%F','%t','%L','%l','%m')
```

```java
package com.itheima;

import org.apache.log4j.Logger;
import org.apache.log4j.helpers.LogLog;
import org.junit.Test;

public class Log4jTest {

    // 快速入门
    @Test
    public void testQuick()throws Exception{
        // 开启 log4j 内置日志记录
        LogLog.setInternalDebugging(true);

        // 初始化配置信息，在入门案例中暂不使用配置文件
        // BasicConfigurator.configure();

        // 获取日志记录器对象
        Logger logger = Logger.getLogger(Log4jTest.class);

        //for (int i = 0; i < 10000; i++) {

            // 日志级别
            logger.fatal("fatal"); // 严重错误，一般会造成系统崩溃并终止运行

            logger.error("error"); // 错误信息，不会影响系统运行
            logger.warn("warn");   // 警告信息，可能会发生问题
            logger.info("info");   // 运行信息，数据连接、网络连接、IO 操作等等
            logger.debug("debug"); // 调试信息，一般在开发中使用，记录程序变量参数传递信息等等

            logger.trace("trace"); // 追踪信息，记录程序所有的流程信息
        //}


        // 再创建一个日志记录器对象
        Logger logger1 = Logger.getLogger(Logger.class);
        logger1.fatal("fatal logger1"); // 严重错误，一般会造成系统崩溃并终止运行
        logger1.error("error logger1"); // 错误信息，不会影响系统运行
        logger1.warn("warn logger1");   // 警告信息，可能会发生问题
        logger1.info("info logger1");   // 运行信息，数据连接、网络连接、IO 操作等等
        logger1.debug("debug logger1"); // 调试信息，一般在开发中使用，记录程序变量参数传递信息等等
        logger1.trace("trace logger1"); // 追踪信息，记录程序所有的流程信息

    }
}


D:\Java\jdk-11.0.6\bin\java.exe -ea -Didea.test.cyclic.buffer.size=1048576 "-javaagent:D:\IntelliJ IDEA 2021.1.3\lib\idea_rt.jar=59440:D:\IntelliJ IDEA 2021.1.3\bin" -Dfile.encoding=UTF-8 -classpath "D:\IntelliJ IDEA 2021.1.3\lib\idea_rt.jar;D:\IntelliJ IDEA 2021.1.3\plugins\junit\lib\junit5-rt.jar;D:\IntelliJ IDEA 2021.1.3\plugins\junit\lib\junit-rt.jar;F:\BaiduNetdiskDownload\资料-Java日志\day01资料\代码\log4j_demo\target\classes;C:\Users\yexy34716\.m2\repository\log4j\log4j\1.2.17\log4j-1.2.17.jar;C:\Users\yexy34716\.m2\repository\junit\junit\4.12\junit-4.12.jar;C:\Users\yexy34716\.m2\repository\org\hamcrest\hamcrest-core\1.3\hamcrest-core-1.3.jar;C:\Users\yexy34716\.m2\repository\mysql\mysql-connector-java\5.1.47\mysql-connector-java-5.1.47.jar" com.intellij.rt.junit.JUnitStarter -ideVersion5 -junit4 com.itheima.Log4jTest,testQuick
log4j: Trying to find [log4j.xml] using context classloader jdk.internal.loader.ClassLoaders$AppClassLoader@1f89ab83.
log4j: Trying to find [log4j.xml] using jdk.internal.loader.ClassLoaders$AppClassLoader@1f89ab83 class loader.
log4j: Trying to find [log4j.xml] using ClassLoader.getSystemResource().
log4j: Trying to find [log4j.properties] using context classloader jdk.internal.loader.ClassLoaders$AppClassLoader@1f89ab83.
log4j: Using URL [file:/F:/BaiduNetdiskDownload/%e8%b5%84%e6%96%99-Java%e6%97%a5%e5%bf%97/day01%e8%b5%84%e6%96%99/%e4%bb%a3%e7%a0%81/log4j_demo/target/classes/log4j.properties] for automatic log4j configuration.
log4j: Reading configuration from URL file:/F:/BaiduNetdiskDownload/%e8%b5%84%e6%96%99-Java%e6%97%a5%e5%bf%97/day01%e8%b5%84%e6%96%99/%e4%bb%a3%e7%a0%81/log4j_demo/target/classes/log4j.properties
log4j: Parsing for [root] with value=[].
log4j: Parsing for [com.itheima] with value=[info,console].
log4j: Level token is [info].
log4j: Category com.itheima set to INFO
log4j: Parsing appender named "console".
log4j: Parsing layout options for "console".
log4j: Setting property [conversionPattern] to [[%-10p]%r  %l %d{yyyy-MM-dd HH:mm:ss.SSS} %m%n].
log4j: End of parsing for "console".
log4j: Parsed "console" options.
log4j: Handling log4j.additivity.com.itheima=[null]
log4j: Parsing for [org.apache] with value=[error,console].
log4j: Level token is [error].
log4j: Category org.apache set to ERROR
log4j: Parsing appender named "console".
log4j: Appender "console" was already parsed.
log4j: Handling log4j.additivity.org.apache=[null]
log4j: Finished configuring.
[FATAL     ]0  com.itheima.Log4jTest.testQuick(Log4jTest.java:24) 2022-03-05 20:02:58.799 fatal
[ERROR     ]2  com.itheima.Log4jTest.testQuick(Log4jTest.java:26) 2022-03-05 20:02:58.801 error
[WARN      ]2  com.itheima.Log4jTest.testQuick(Log4jTest.java:27) 2022-03-05 20:02:58.801 warn
[INFO      ]3  com.itheima.Log4jTest.testQuick(Log4jTest.java:28) 2022-03-05 20:02:58.802 info
[FATAL     ]3  com.itheima.Log4jTest.testQuick(Log4jTest.java:37) 2022-03-05 20:02:58.802 fatal logger1
[ERROR     ]3  com.itheima.Log4jTest.testQuick(Log4jTest.java:38) 2022-03-05 20:02:58.802 error logger1

Process finished with exit code 0

```





































