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



自动配置：Auto-Configuration

自动装配：Autowire



自动配置：通过Maven将Spring Boot Starter依赖引入来实现，Starter依赖包含了应用程序所需要的各种组件和配置信息。当应用程序引入spring-boot-starter-web依赖时，Spring Boot会自动配置Web应用程序所需的组件，包括Tomcat服务器、Spring MVC框架、Jackson JSON处理库等等



SpringBoot应用启动时通过@SpringBootApplication中的@EnableAutoConfiguration中的@Import({AutoConfigurationImportSelector.class})，AutoConfigurationImportSelector中的List<String> configurations = SpringFactoriesLoader.loadFactoryNames(this.getSpringFactoriesLoaderFactoryClass(), this.getBeanClassLoader());

SpringFactorisLoader中的找到jar包下的"META-INF/spring.factories"的配置



在jar包中的spring.factories中，@EnableConfigurationProperties({HttpProperties.class}) ，将配置注入到Ioc容器中，@ConfigurationProperties将配置文件Properties中的属性绑定到类中的成员变量上，@Bean 从配置文件Properties获取变量



配置文件-----@Bean获取对应的值----->@ConfigurationProperties将值绑定到类中变量 ----> @EnableConfigurationProperties将key-value注入到Ioc容器中

组件（对应的类）



- @SpringBootApplication: 

  -- Spring Boot应用标注在某个类上说明这个类是SpringBoot的主配置类，SpringBoot就应该运行这个类的main方法来启动SpringBoot应用； 

  - @SpringBootConfiguration:

    -- 标注在某个类上，表示这是一个Spring Boot的配置类； 

  - @EnableAutoConfiguration：

    -- 开启自动配置功能；以前我们需要配置的东西，Spring Boot帮我们自动配置；@EnableAutoConfiguration告诉SpringBoot开启自动配置功能；这样自动配置才能生效； 

    - @AutoConfigurationPackage：自动配置包 

    - @Import({AutoConfigurationImportSelector.class})

      -- EnableAutoConfigurationImportSelector：导入哪些组件的选择器；将所有需要导入的组件以全类名的方式返回；这些组件就会被添加到容器中；会给容器中导入非常多的自动配置类（xxxAutoConfiguration）；就是给容器中导入这个场景需要的所有组件，并配置好这些组件； 



- @ConfigurationProperties：告诉SpringBoot将本类中的所有属性和配置文件中相关的配置进行绑定；

  prefix = "person"：配置文件中哪个下面的所有属性进行一一映射

  @ConfigurationProperties(prefix = "person")默认从全局配置文件中获取值； 

- @Component 

  -- 只有这个组件是容器中的组件，才能容器提供的@ConfigurationProperties功能；

- @PropertySource(value = {"classpath:person.properties"}) ：加载指定的配置文件  同时需要

  @Component @ConfigurationProperties(prefix = "person") 

- @Bean //给容器中添加一个组件，这个组件的某些值需要从properties中获取 

- @Value 使用${......}这样的占位符读取配置在属性文件（src/main/resources/application.properties）的内容 

- 



#### @Bean

```java
@Bean注解用于定义一个bean。通过@Bean注解，我们可以将一个方法返回的对象注册为一个Spring应用程序上下文中的bean。
    
@Configuration
public class AppConfig {

    @Bean
    public DataSource dataSource() {
        // create and configure a DataSource object
        return dataSource;
    }

}    

Spring应用程序上下文加载这个配置类时，它会调用这个方法并将其返回值注册为一个名为"dataSource"的bean。之后，我们就可以在应用程序中使用@Autowired注解将这个bean注入到其他的组件中。
    
@Bean注解默认情况下会使用方法名作为bean的名称。如果我们想要指定不同的名称，可以使用value属性或name属性
@Bean("myDataSource")
public DataSource dataSource() {
    // create and configure a DataSource object
    return dataSource;
}    
```

#### @Import

@Import注解是一个用于引入其他配置类的注解。它允许我们将其他配置类加载到当前配置类中，从而实现对其他配置类的重用和组合。除了使用@Import注解引入其他的配置类外，还可以使用它来引入其他的普通Java类、XML配置文件等等

```java
@Configuration
@Import({DataSourceConfig.class, SecurityConfig.class})
public class AppConfig {
    // ...
}
```

![image-20230330202141497](03_SpringBoot.assets/image-20230330202141497.png)
