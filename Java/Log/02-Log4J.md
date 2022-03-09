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





































```xml
日志使用规范手册
（一）日志规约
1. 【强制】应用中不可直接使用日志系统（Log4j、Logback）中的API，而应依赖使用日志框架SLF4J中的API，使用门面模式的日志框架，有利于维护和各个类的日志处理方式统一。
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
 
private static final Logger logger = LoggerFactory.getLogger(Abc.class);
 
2. 【强制】日志文件至少保存15天，因为有些异常具备以“周”为频次发生的特点。
 
3. 【强制】应用中的扩展日志（如打点、临时监控、访问日志等）命名方式：
appName_logType_logName.log。
logType:日志类型，如 stats/monitor/access 等；logName:日志描述。这种命名的好处：
通过文件名就可知道日志文件属于什么应用，什么类型，什么目的，也有利于归类查找。
正例：mppserver 应用中单独监控时区转换异常，如：
mppserver_monitor_timeZoneConvert.log
说明：推荐对日志进行分类，如将错误日志和业务日志分开存放，便于开发人员查看，也便于
通过日志对系统进行及时监控。
 
4. 【强制】对 trace/debug/info 级别的日志输出，必须使用条件输出形式或者使用占位符的方式。
说明：logger.debug("Processing trade with id: " + id + " and symbol: " + symbol);
如果日志级别是 warn，上述日志不会打印，但是会执行字符串拼接操作，如果 symbol 是对象，会执行 toString()方法，浪费了系统资源，执行了上述操作，最终日志却没有打印。
正例：（条件）建设采用如下方式
if (logger.isDebugEnabled()) {
logger.debug("Processing trade with id: " + id + " and symbol: " + symbol);
}
正例：（占位符）
logger.debug("Processing trade with id: {} and symbol : {} ", id, symbol);
 
5. 【强制】避免重复打印日志，浪费磁盘空间，务必在 log4j.xml 中设置 additivity=false。
正例：<logger name="com.taobao.dubbo.config" additivity="false">
 
6. 【强制】异常信息应该包括两类信息：案发现场信息和异常堆栈信息。如果不处理，那么通过关键字 throws 往上抛出。
正例：logger.error(各类参数或者对象 toString() + "_" + e.getMessage(), e);
 
7. 【推荐】谨慎地记录日志。生产环境禁止输出 debug 日志；有选择地输出 info 日志；如果使用warn来记录刚上线时的业务行为信息，一定要注意日志输出量的问题，避免把服务器磁盘撑爆，并记得及时删除这些观察日志。
说明：大量地输出无效日志，不利于系统性能提升，也不利于快速定位错误点。记录日志时请
思考：这些日志真的有人看吗？看到这条日志你能做什么？能不能给问题排查带来好处？
 
8. 【推荐】可以使用warn日志级别来记录用户输入参数错误的情况，避免用户投诉时，无所适从。如非必要，请不要在此场景打出error级别，避免频繁报警。
说明：注意日志输出的级别，error级别只记录系统逻辑出错、异常或者重要的错误信息。
 
9. 【推荐】尽量用英文来描述日志错误信息，如果日志中的错误信息用英文描述不清楚的话使用中文描述即可，否则容易产生歧义。国际化团队或海外部署的服务器由于字符集问题，【强制】使用全英文来注释和描述日志错误信息。
（二）日志输出文件和日志行文规范
TIPS
以下规范均是在log4j.xml文件中配置，不需要手动创建文件夹，配置文件模板会在后面给出。
1. 运行时日志输出文件路径
日志文件统一存放在用户目录下的logs文件夹中，根据应用名称生成文件夹进行区分，如图2-1所示。单项目多应用情况下，可根据实际情况修改log4j.xml中的路径（依然存放在logs目录下）。
                       
图2-1  运行时日志输出文件路径
2. 存档日志输出文件路径
日志文件统一存放在用户目录下的logs文件夹中，根据应用名称生成文件夹进行区分，然后以年月“yyyy-MM”生成文件夹，以日志级别（如info / warn / error等）或日志类型（如stats / monitor / access等）生成文件夹，如图2-2和图2-3所示。
                       
图2-2  存档日志输出文件路径1
              
图2-3  存档日志输出文件路径2
 
3. 各日志级别文件命名规范
普通类型日志，以应用名称开头 + 日志级别 + 日期 + 序号，以“.log”结尾，如图2-3所示。
其它类型日志，以应用名称开头 + 日志类型 + 描述 + 日期 + 序号，以“.log”结尾，如图2-4所示。
               
图2-4  其它类型日志文件命名示例
 
4. 日志清理策略
我们可以利用log4j自带的日志清理功能，当同一文件夹下的文件数量大于设置的阈值时，log4j会清理最旧的一个或多个文件，来满足新文件的生成。
在文件路径规范章节中，我们以日志级别或日志类型为文件夹，这样我们就可以通过设置一个阈值，来根据不同日志级别或类型来定制清理策略。
对应的log4j配置为<DefaultRolloverStrategy max="20"/>，其中max属性值就是上述提到的阈值。详细说明会在后面章节的配置模板中阐述。
5. 日志行文输出规范
一条日志输出中会包含日期时间、日志级别、输出日志事件发生位置（类相关信息、发生线程、代码中所在行数）以及日志内容，如图2-5所示。
       
图2-5  日志行文输出规范示例
 
（三）项目中使用日志系统
1. SpringBoot框架下使用Log4j2
（1）Maven依赖
<dependency>
   <groupId>org.springframework.boot</groupId>
   <artifactId>spring-boot-starter-log4j2</artifactId>
</dependency>
因为SpringBoot默认使用的日志框架是Logback，为了避免冲突，需要将它从SpringBoot中移除。
<dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
        <exclusions>
            <exclusion>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-logging</artifactId>
            </exclusion>
         </exclusions>
</dependency>   
（2）编写配置
配置文件命名和存放位置有多种方式，以“log4j2.xml”和“log4j2-spring.xml”命名时，可以直接将配置文件放到项目resources目录下，就不需要在application.yml配置对应的位置；如果想自定义文件名称和路径时，可以在application.yml中配置对应的位置，如图3-1所示。
图3-1  指定配置文件所在位置
为了统一，请以图3-1的方式为准。
在章节将给出log4j2的配置模板，里面有详细的注释，可以根据实际情况进行更改。
（3）代码中使用
我们使用Slf4j的api打印日志，如图3-2所示。
图3-2  使用Slf4j-api打印日志
 
有lombok使用经验的同学可以在项目中引入lombok依赖，然后以图3-3的方式打印日志。
图3-3  使用lombok打印日志
 
2. 其它Maven项目下使用Log4j2
除了maven依赖不同外，配置和使用方式与SpringBoot一样。
Maven依赖
<dependency>
        <groupId>org.apache.logging.log4j</groupId>
        <artifactId>log4j-slf4j-impl</artifactId>
        <version>2.12.1</version>
    </dependency>
附录
1. log4j2配置模板
为了让IDE中输出的日志有颜色，可以在输出日志格式中加“%highlight{[%p]}”修饰，IDEA下需要在VM options中添加“-Dlog4j.skipJansi=false”；Eclipse下安装“AnsiConsole”插件即可。
<?xml version="1.0" encoding="UTF-8"?>
<!--日志级别以及优先级排序: OFF > FATAL > ERROR > WARN > INFO > DEBUG > TRACE > ALL -->
<!--status="WARN" :用于设置log4j2自身内部日志的信息输出级别，默认是OFF-->
<!--monitorInterval="30"  :间隔秒数,自动检测配置文件的变更和重新配置本身-->
<configuration status="WARN" monitorInterval="30">
    <Properties>
        <!--自定义常量，之后使用${变量名}引用-->
        <Property name="logFilePath">log</Property>
        <Property name="logFileName">test.log</Property>
        <!-- 应用名称 -->
        <Property name="appName">demo</Property>
        <!-- 运行时日志保存路径前缀 -->
        <Property name="fileNamePrefix">${sys:user.home}/logs/${appName}</Property>
        <!-- 存档日志保存路径前缀 -->
        <Property name="filePatternPrefix">${sys:user.home}/logs/${appName}/$${date:yyyy-MM}</Property>
        <!-- 日志输出格式 -->
        <Property name="patternLayout">%d{yyyy-MM-dd HH:mm:ss.SSS} [%p] - %t - %l- :%m%n</Property>
    </Properties>
    <!--appenders:定义输出内容,输出格式,输出方式,日志保存策略等,常用其下三种标签[console,File,RollingFile]-->
    <appenders>
        <!--console :控制台输出的配置-->
        <console name="Console" target="SYSTEM_OUT">
            <!--PatternLayout :输出日志行文的格式 -->
            <PatternLayout pattern="${patternLayout}"/>
        </console>
        <!--File :同步输出日志到本地文件，开发时使用，生产环境下不需要使用 -->
        <!--append="false" :每次清空文件重新输入日志,可用于测试-->
        <File name="log" fileName="${logFilePath}/${logFileName}" append="false">
            <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level %class %L %M - %msg%xEx%n"/>
        </File>
        <!-- ${sys:user.home} :项目路径 -->
        <RollingFile name="RollingFileInfo" fileName="${fileNamePrefix}/${appName}_info.log"
                     filePattern="${filePatternPrefix}/info/${appName}_info-%d{yyyy-MM-dd}-%i.log.gz">
            <!--ThresholdFilter :日志输出过滤-->
            <!--level="info" :日志级别,onMatch="ACCEPT" :级别在info之上则接受,onMismatch="DENY" :级别在info之下则拒绝-->
            <ThresholdFilter level="info" onMatch="ACCEPT" onMismatch="DENY"/>
            <PatternLayout pattern="${patternLayout}"/>
            <!-- Policies :日志滚动策略-->
            <Policies>
                <!-- TimeBasedTriggeringPolicy :时间滚动策略，自定义文件滚动时间间隔，每隔一段时间就产生新文件。
                interval="2"：这个参数的含义由filePattern决定，当filePattern中的时间格式为{yyyy-MM-dd}时，代表以2天为间隔；
                              当filePattern中的时间格式为{yyyy-MM-dd HH:mm}时，代表以2分钟为间隔
                modulate="true": boolean型，说明是否对封存时间进行调制。
                               -->
                <TimeBasedTriggeringPolicy interval="2" modulate="true"/>
                <!-- SizeBasedTriggeringPolicy :文件大小滚动策略，大于这个阈值时，会将当前日志文件备份存档 -->
                <SizeBasedTriggeringPolicy size="300 MB"/>
            </Policies>
            <!-- DefaultRolloverStrategy属性如不设置，则默认为最多同一文件夹下7个文件，超过这个阈值就会清理最旧的日志文件。
                    这里设置了20，理由：假设日志文件大小都小于阈值时，interval=2day，有1个RollingFile都在一个文件夹下，
                    文件夹名称为月份，即一个月理想状态下会产生1 x (30天 / 2) = 15个文件
             -->
            <DefaultRolloverStrategy max="20"/>
        </RollingFile>
        <RollingFile name="RollingFileWarn" fileName="${fileNamePrefix}/${appName}_warn.log"
                     filePattern="${filePatternPrefix}/warn/${appName}_warn-%d{yyyy-MM-dd}-%i.log.gz">
            <ThresholdFilter level="warn" onMatch="ACCEPT" onMismatch="DENY"/>
            <PatternLayout pattern="${patternLayout}"/>
            <Policies>
                <TimeBasedTriggeringPolicy interval="2" modulate="true"/>
                <SizeBasedTriggeringPolicy size="200 MB"/>
            </Policies>
            <DefaultRolloverStrategy max="20"/>
        </RollingFile>
        <RollingFile name="RollingFileError" fileName="${fileNamePrefix}/${appName}_error.log"
                     filePattern="${filePatternPrefix}/error/${appName}_error-%d{yyyy-MM-dd}-%i.log.gz">
            <ThresholdFilter level="error" onMatch="ACCEPT" onMismatch="DENY"/>
            <PatternLayout pattern="${patternLayout}"/>
            <Policies>
                <TimeBasedTriggeringPolicy interval="2" modulate="true"/>
                <SizeBasedTriggeringPolicy size="100 MB"/>
            </Policies>
            <DefaultRolloverStrategy max="20"/>
        </RollingFile>
        <!-- 自定义appender -->
        <RollingFile name="MonitorTestController" fileName="${fileNamePrefix}/${appName}_monitor_testController.log"
                     filePattern="${filePatternPrefix}/monitor/${appName}_monitor_testController-%d{yyyy-MM-dd}-%i.log.gz">
            <ThresholdFilter level="warn" onMatch="ACCEPT" onMismatch="DENY" />
            <PatternLayout pattern="${patternLayout}" />
            <Policies>
                <TimeBasedTriggeringPolicy interval="2" modulate="true"/>
                <SizeBasedTriggeringPolicy size="100 MB" />
            </Policies>
            <DefaultRolloverStrategy max="20"/>
        </RollingFile>
    </appenders>
    <!--然后定义logger，只有定义了logger并引入的appender，appender才会生效-->
    <loggers>
        <!--过滤掉spring和mybatis的一些无用的DEBUG信息-->
        <!--Logger节点用来单独指定日志的形式，name为包路径,比如要为org.springframework包下所有日志指定为INFO级别等。 -->
        <logger name="org.springframework" level="INFO"></logger>
        <logger name="org.mybatis" level="INFO"></logger>
        <logger name="org.apache" level="INFO"></logger>
        <logger name="org.hibernate" level="INFO"></logger>
        <!-- 自定义logger
                避免重复打印日志，浪费磁盘空间，请务必设置additivity为false
         -->
        <logger name="com.fline.demo.log.controller.TestController" level="WARN" additivity="false">
            <appender-ref ref="MonitorTestController" />
        </logger>
        <!-- Root节点用来指定项目的根日志，如果没有单独指定Logger，那么就会默认使用该Root日志输出 -->
        <root level="all">
            <appender-ref ref="log"/>
            <appender-ref ref="Console"/>
            <appender-ref ref="RollingFileInfo"/>
            <appender-ref ref="RollingFileWarn"/>
            <appender-ref ref="RollingFileError"/>
        </root>
    </loggers>
</configuration>
```