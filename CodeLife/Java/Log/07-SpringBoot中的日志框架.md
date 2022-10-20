springboot默认就是使用SLF4J作为日志门面，logback作为日志实现来记录日志。

```xml
<dependency>
	<artifactId>spring-boot-starter-logging</artifactId>
	<groupId>org.springframework.boot</groupId>
</dependency>
```

1. springboot 底层默认使用logback作为日志实现。
2. 使用了SLF4J作为日志门面
3. 将JUL也转换成slf4j
4. 也可以使用log4j2作为日志门面，但是最终也是通过slf4j调用logback

### 使用

```java
@SpringBootTest
class SpringbootLogApplicationTests {
    //记录器
    public static final Logger LOGGER =
    LoggerFactory.getLogger(SpringbootLogApplicationTests.class);
    @Test
    public void contextLoads() {
    // 打印日志信息
    LOGGER.error("error");
    LOGGER.warn("warn");
    LOGGER.info("info"); // 默认日志级别
    LOGGER.debug("debug");
    LOGGER.trace("trace");

    }
}
```

    2. 修改默认日志配置
    logging.level.com.itheima=trace
    # 在控制台输出的日志的格式 同logback
    logging.pattern.console=%d{yyyy-MM-dd} [%thread] [%-5level] %logger{50} -
    %msg%n
    # 指定文件中日志输出的格式
    logging.file=D:/logs/springboot.log
    logging.pattern.file=%d{yyyy-MM-dd} [%thread] %-5level %logger{50} - %msg%n

3. 指定配置

   给类路径下放上每个日志框架自己的配置文件；SpringBoot就不使用默认配置的了

   Logback logback-spring.xml , logback.xml
   Log4j2 log4j2-spring.xml ， log4j2.xml
   JUL logging.properties

4. 使用SpringBoot解析日志配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>


    <property name="pattern" value="[%-5level] %d{yyyy-MM-dd HH:mm:ss.SSS} %c %M %L [%thread] -------- %m %n"></property>



    <!--控制台日志输出的 appender-->
    <appender name="console" class="ch.qos.logback.core.ConsoleAppender">
        <!--控制输出流对象 默认 System.out 改为 System.err-->
        <target>System.err</target>
        <!--日志消息格式配置-->
        <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
            <springProfile name="dev">
                <pattern>${pattern}</pattern>
            </springProfile>
            <springProfile name="pro">
                <pattern>[%-5level] %d{yyyy-MM-dd HH:mm:ss.SSS} %c %M %L [%thread] xxxxxxxx %m %n</pattern>
            </springProfile>
        </encoder>
    </appender>



    <!--自定义 looger 对象
        additivity="false" 自定义 logger 对象是否继承 rootLogger
     -->
    <logger name="com.itheima" level="info" additivity="false">
        <appender-ref ref="console"/>
    </logger>
</configuration>
```

application.properties

```
spring.profiles.active=dev
```

5. 将日志切换为log4j2

   ```xml
   <dependencies>
           <dependency>
               <groupId>org.springframework.boot</groupId>
               <artifactId>spring-boot-starter-web</artifactId>
               <exclusions>
                   <!--排除 logback 日志实现-->
                   <exclusion>
                       <artifactId>spring-boot-starter-logging</artifactId>
                       <groupId>org.springframework.boot</groupId>
                   </exclusion>
               </exclusions>
           </dependency>
   
           <!--使用 log4j2 的日志启动器-->
           <dependency>
               <groupId>org.springframework.boot</groupId>
               <artifactId>spring-boot-starter-log4j2</artifactId>
           </dependency>
           <dependency>
               <groupId>org.springframework.boot</groupId>
               <artifactId>spring-boot-starter-test</artifactId>
               <scope>test</scope>
               <exclusions>
                   <exclusion>
                       <groupId>org.junit.vintage</groupId>
                       <artifactId>junit-vintage-engine</artifactId>
                   </exclusion>
               </exclusions>
           </dependency>
       </dependencies>
   ```

   