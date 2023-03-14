https://www.cnblogs.com/tjudzj/p/8758391.html


```java
// 使用org.springframework.beans.BeanUtils.copyProperties方法进行对象之间属性的赋值，
// 避免通过get、set方法一个一个属性的赋值
public static void copyProperties(Object source, Object target) throws BeansException {
        copyProperties(source, target, (Class)null, (String[])null);
}
```



Spring Boot 是一个基于 Spring 框架的开源框架，它简化了 Spring应用程序的构建和部署过程。Spring Boot减少了大量配置，提供了**自动配置**和**约定优于配置**的原则

 自动配置：
 独立运行：Spring Boot应用程序可以独立运行，不需要外部容器支持。它内嵌了Tomcat、Jetty、Undertow等Web容器，可以通过运行一个可执行的JAR文件来启动应用程序，使得部署和运行变得非常简单。
 约定优于配置：Spring Boot采用约定优于配置的方式来配置应用程序，即通过默认的配置和约定，来避免开发者手动配置所带来的繁琐和错误。例如，Spring Boot默认会扫描应用程序的类路径，自动加载并配置所依赖的各种组件。
 组件化：Spring Boot将应用程序分解成若干个组件，每个组件都可以独立开发、测试和部署，具有良好的复用性和可维护性。组件化的设计也使得Spring Boot应用程序具有良好的可扩展性和可定制性。
 面向生产环境：Spring Boot设计之初就考虑了应用程序在生产环境下的部署和运行。它提供了丰富的健康检查、监控、日志记录等功能，可以帮助开发者快速定位和解决问题。

 综上所述，Spring Boot通过自动配置、独立运行、约定优于配置、组件化和面向生产环境等特性，大大简化了Spring应用程序的开发和部署，提高了开发效率和运行效率。



**SpringBoot** 

- 基于Spring框架搭建起来的应用，
- 内嵌Tomcat等服务器，不需要传统的war包进行部署；
- 通过Maven管理依赖starter，starter可以直接获取开发所需的相关包
- 默认配置了其他常用框架
- 基于注解开发

**控制反转（IoC）**：管理各类 Java 资源，从而降低了各种资源的耦合  。在IoC模式下，控制权发生了反转，即从应用程序转移到了IoC容器，所有组件不再由**应用程序**自己创建和配置，而是由**IoC容器**负责，这样，应用程序只需要直接使用已经创建好并且配置好的组件

- 对象之间并不是孤立的，它们之间还可能存在依赖的关系 ，为此 Spring 还提供了**依赖注入**的功能  
- 在 Spring 中把每一个**需要管理的对象**称为 **Spring Bean（简称 Bean）**，而 Spring **管理这些 Bean 的容器**，被我们称为 **SpringIoC 容器（或者简称 IoC 容器）**。 IoC 容器需要具备两个基本的功能：
  - 通过描述管理 Bean，包括发布和获取 Bean；
  - 通过描述完成 Bean 之间的依赖关系。  

**面向切面的编程（AOP）**通过**动态代理**技术，允许我们按照约定进行配置编程，进而增强了 Bean 的功能

**视图解析器**的作用主要是定位视图，**当控制器只是返回一个逻辑名称的时候，是没有办法直接对应找到视图的**，这就需要视图解析器进行解析了  







```
@Configuration 代表这是一个 Java 配置文件， Spring 的容器会根据它来生成 IoC 容器去装配 Bean；（包含@Component）
- @Bean 将实例对象装配到 IoC 容器中

@Component 是标明哪个类被扫描进入 Spring IoC 容器
- Autowired
@ComponentScan 则是标明采用何种策略去扫描装配 Bean。

 @Component 注解作⽤于类，⽽ @Bean 注解作⽤于⽅法

@Autowired 自动装配Bean，首先它会根据类型找到对应的 Bean，如果对应类型的 Bean 不是唯一的，那么它会根据其属性名称和 Bean 的名称进行匹配。如果匹配得上，就会使用该 Bean；如果还无法匹配，就会抛出异常    
  - 如果不能确定其标注属性一定会存在并且允许这个被标注的属性为 null，那么你可以配置@Autowired 属性 required 为 false  
  - `@Autowired(required = false)  `

- 当使用@Autowired 时，存在多个Bean时，可以通过@Primary 和@Quelifier  消除歧视
  - @Primary  优先使用该Bean
  - @Quelifier  通过类型和名称一起找到 Bean  
```

SpringBoot 初始化Bean过程

1. 资源定位：如@ComponentScan所定义的扫描包
2. Bean定义：将Bean的定义保存到BeanDefinition实例中
3. 发布Bean定义：IoC容器装载Bean定义
4. 实例化：创建Bean的实例对象
5. 依赖注入：@Autowired
6. 

Spring 中的 bean 的作⽤域有哪些?  

- singleton : 唯⼀ bean 实例， Spring 中的 bean 默认都是单例的。
- prototype : 每次请求都会创建⼀个新的 bean 实例。
- request : 每⼀次HTTP请求都会产⽣⼀个新的bean，该bean仅在当前HTTP request内有效。
- session : 每⼀次HTTP请求都会产⽣⼀个新的 bean，该bean仅在当前 HTTP session 内有效。
- global-session： 全局session作⽤域，仅仅在基于portlet的web应⽤中才有意义， Spring5已经没有了。 Portlet是能够⽣成语义代码(例如： HTML)⽚段的⼩型Java Web插件。它们基于portlet容器，可以像servlet⼀样处理HTTP请求。但是，与 servlet 不同，每个 portlet 都有不同的会话  



@Component 和 @Bean 的区别是什么？

1. 作⽤对象不同: @Component 注解作⽤于类，⽽ @Bean 注解作⽤于⽅法。
2. @Component 通常是通过类路径扫描来⾃动侦测以及⾃动装配到Spring容器中（我们可以使⽤@ComponentScan 注解定义要扫描的路径从中找出标识了需要装配的类⾃动装配到 Spring 的bean 容器中）。 @Bean 注解通常是我们在标有该注解的⽅法中定义产⽣这个 bean, @Bean 告诉了Spring这是某个类的示例，当我需要⽤它的时候还给我。
3. @Bean 注解⽐ Component 注解的⾃定义性更强，⽽且很多地⽅我们只能通过 @Bean 注解来注册bean。⽐如当我们引⽤第三⽅库中的类需要装配到 Spring 容器时，则只能通过@Bean 来实现。  



简便部署

- 通过`mvn package`将项目打包成jar包，或war包
- `F:\DestTop>java -jar springboot-helloworld-0.0.1-SNAPSHOT.jar`