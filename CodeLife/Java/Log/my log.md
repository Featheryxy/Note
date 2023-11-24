## Log4j2

### 概括

Application --> Logger -->Appenders(Handler) --> Layouts(Formatter)

Logger：控制日志的输出级别与日志是否输出，
Appenders：指定日志的输出方式
Layout：控制日志信息的输出格式

### 规约

```
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
```

### Level

OFF     为最高等级 关闭了日志信息 最大整数
FATAL      为可能导致应用中止的严重事件错误
ERROR    为严重错误 主要是程序的错误
WARN     为一般警告，比如session丢失
INFO     为一般要显示的信息，比如登录登出
DEBUG     为程序的调试信息
TRACE     为比DEBUG更细粒度的事件信息
ALL     为最低等级，将打开所有级别的日志

### Logger

控制日志的输出级别与日志是否输出

1. logger对象的实例名为类的全限定名，大小写敏感，且有继承机制

2. root是所有logger的根

### Appender

指定日志的输出方式

1. ConsoleAppender：将日志输出到**控制台**
2. FileAppender：将日志输出到**文件**中
3. DailyRollingFileAppender：将日志输出到一个日志文件，并且每天输出到一个新的文件
4. RollingFileAppender：将日志信息输出到一个日志文件，并且指定文件的尺寸，当文件大小达到指定尺寸时，会自动把文件改名，同时产生一个新的文件
5. JDBCAppender：把日志信息保存到**数据库**中

### Layout

布局器 Layouts用于控制日志输出内容的格式

- PatternLayout：最强大的格式化期，可以根据自定义格式输出日志，如果没有指定转换格式，就是用**默认的转换格式**

- SimpleLayout：简单的日志输出格式化，打印的日志格式为（info - message）

- HTMLLayout：格式化日志输出为HTML表格形式

```c
    %m message 输出代码中指定的日志信息
    %p priority 输出优先级，及 DEBUG、INFO 等
    %n 换行符（Windows平台的换行符为 "\n"，Unix 平台为 "\n"）
    %c class 输出打印语句所属的类的全名
    %t 输出产生该日志的线程全名
    %d 输出服务器当前时间，默认为 ISO8601，也可以指定格式，如：%d{yyyy年MM月dd日HH:mm:ss}
    %l 输出日志时间发生的位置，包括类名、线程、及在代码中的行数。如：Test.main(Test.java:10)

    %F 输出日志消息产生时所在的文件名称
    %L 输出代码中的行号
     %r 输出自应用启动到输出该 log 信息耗费的毫秒数
    %% 输出一个 "%" 字符
* 可以在 % 与字符之间加上修饰符来控制最小宽度、最大宽度和文本的对其方式。如：
    %5c 输出类的全名，最小宽度是5，若名称不足长度< 5，左补空格，category<5，默认的情况下右对齐
    %-5c 输出category名称，最小宽度是5，category<5，"-"号指定左对齐,会有空格
    %.5c 输出category名称，最大宽度是5，category>5，就会将左边多出的字符截掉，<5不会有空格
    %20.30c category名称<20补空格，并且右对齐，>30字符，就从左边交远销出的字符截掉
```

### Maven

```xml
<!-- Log4j2 门面API-->
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-api</artifactId>
    <version>2.11.1</version>
</dependency>
<!-- Log4j2 日志实现 -->
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-core</artifactId>
    <version>2.11.1</version>
</dependency>
<!--使用slf4j作为日志的门面,使用log4j2来记录日志 -->
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-api</artifactId>
    <version>1.7.25</version>
</dependency>
<!--为slf4j绑定日志实现 log4j2的适配器 -->
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-slf4j-impl</artifactId>
    <version>2.10.0</version>
</dependency>
```

### log4j2配置文件

log4j2默认加载classpath下的 log4j2.xml 文件中的配置

为了让IDE中输出的日志有颜色，可以在输出日志格式中加“%highlight{[%p]}”修饰，IDEA下需要在VM options中添加“-Dlog4j.skipJansi=false”；Eclipse下安装“AnsiConsole”插件即可。

```xml
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

    <appenders>
        <console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="${patternLayout}"/>
        </console>

        <!--File :同步输出日志到本地文件，开发时使用，生产环境下不需要使用 -->
        <!--append="false" :每次清空文件重新输入日志,可用于测试-->
        <File name="log" fileName="${logFilePath}/${logFileName}" append="false">
            <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss.SSS} %-5level %class %L %M - %msg%xEx%n"/>
        </File>

<!--设置级别为INFO日志输出到info.log中-->
        <RollingFile name="INFO" filename="${logPath}/wms_info.log"
                     filepattern="${logPath}/wms_info-%d{yyyy-MM-dd}-%i.log">
            <Filters>
                <!--设置只输出级别为INFO的日志-->
                <ThresholdFilter level="INFO"/>
                <ThresholdFilter level="WARN" onMatch="DENY" onMismatch="NEUTRAL"/>
            </Filters>
            <PatternLayout charset="UTF-8"  pattern="[%-5p]%d{yyyy-MM-dd HH:mm:ss:SSS} [%t] [%c.%M] [%L]- %m%n" />
            <Policies>
                <!--设置每天打包日志一次-->
                <!--  <TimeBasedTriggeringPolicy interval="10" modulate="true"/>-->
                <!--设置日志文件满50MB后打包-->
                <SizeBasedTriggeringPolicy size="50 MB" />
            </Policies>
            <!-- DefaultRolloverStrategy属性如不设置，max为单位时间日志文件分片数上限 -->
            <DefaultRolloverStrategy max="1000">
                <Delete basePath="${logPath}" maxDepth="2">
                    <IfFileName glob="${componentId}_info-*.log">
                        <IfAny>
                            <!--debug日志最多1000个，30天，或关系-->
                            <IfAccumulatedFileCount exceeds="1000"/>
                            <IfLastModified age="30d"/>
                        </IfAny>
                    </IfFileName>
                </Delete>
            </DefaultRolloverStrategy>
        </RollingFile>

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
        <!--过滤掉spring和mybatis的一些无用的DEBUG信息，所以level 设置为INFO-->
        <!--Logger节点用来单独指定日志的形式，name为包路径,比如要为org.springframework包下所有日志指定为INFO级别等。 -->
        <logger name="org.springframework" level="INFO"></logger>
        
        <logger name="org.mybatis" level="INFO"></logger>
        <logger name="org.apache" level="INFO"></logger>
        <logger name="org.hibernate" level="INFO"></logger>
        <!-- 自定义logger
                避免重复打印日志，浪费磁盘空间，请务必设置additivity为false
         -->
        <!-- 将xxx.TestController包下的日志（日志级别在warn（包含） 以上）使用appender输出-->
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

### 代码

```java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;


public class Test {

    @org.junit.jupiter.api.Test
    public void test(){
        Logger logger = LogManager.getLogger();
        logger.error("error");
        logger.warn("warn");
        logger.info("info");
        logger.debug("debug");
    }
}
```

### 