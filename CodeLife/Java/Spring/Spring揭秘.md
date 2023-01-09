#### Spring

Spring是什么?

Spring是一个轻量级的IoC和AOP容器框架。是为Java应用程序提供基础性服务的一套框架，目的是用于简化企业应用程序的开发，它使得开发者只需要关心业务需求。

常见的配置方式有三种：基于XML的配置、基于注解的配置、基于Java的配置。

主要由以下几个模块组成：

Spring Core：核心类库，提供IOC服务；

Spring Context：提供框架式的Bean访问方式，以及企业级功能（JNDI、定时任务等）；

Spring AOP：AOP服务；

Spring DAO：对JDBC的抽象，简化了数据访问异常的处理；

Spring ORM：对现有的ORM框架的支持；

Spring Web：提供了基本的面向Web的综合特性，例如多方文件上传；

Spring MVC：提供面向Web应用的Model-View-Controller实现。



![](SpringLifeTree.png)上层模块依赖下层模块，同层模块相互独立



优点：

（1）spring属于低侵入式设计，代码的污染极低；

（2）spring的DI机制将对象之间的依赖关系交由框架处理，减低组件的耦合性；

（3）Spring提供了AOP技术，支持将一些通用任务，如安全、事务、日志、权限等进行集中式管理，从而提供更好的复用。

（4）spring对于主流的应用框架提供了集成支持。





#### IoC

Spring 提供了IOC容器实现，帮助我们以依赖注入的方式管理对象之间的依赖关系。解耦各业务对象间依赖关系的对象绑定方式



依赖注入方式：

1. 构造器注入
   - 优点：对象构造完成后即可使用
   - 缺点：
     - 当依赖对象较多时，构造方法的参数列表会比较长。
     - 构造方法无法被继承，无法设置默认值
2. setter注入：最提倡，可被继承，允许设置默认值
3. 接口注入：要求被注入的对象实现不必要的接口，带有侵入性

IoC职责：

1. 对象的构建
2. 对象之间的依赖绑定



如何管理对象间的依赖关系：

1. 直接编码
2. 配置文件方式
3. 元数据方式, 如注解



容器类型：

1. BeanFactory：默认lazy-load
2. ApplicationContext：扩展了BeanFactory， 支持国际化等功能，启动即加载



常用注解：

@Component 

@Autowired



Autowired自动绑定模式：

1. no，default
2. byName，实例名称和beanName相同
3. byType
4. constructor， 根据byType
5. autodetect



自动绑定

手动绑定





#### Other

面向切面编程（Aspect Oriented Programming， AOP） 

项目对象模型 (POM： Project Object Model)，一组标准集合，一个项目生命周期(Project Lifecycle)，一个依赖管理系统(Dependency Management System)，和用来运行定义在生命周期阶段(phase)中插件(plugin)目标(goal)的逻辑。 

DAO(Data Access Object) 数据访问对象是一个面向对象的数据库接口





spring通过描述来创建对象 ,在 Spring 中把每一个需要管理的对象称为 Spring Bean（简称 Bean），而 Spring 管理这些 Bean 的容器，被我们称为 Spring
IoC 容器（或者简称 IoC 容器）， 通过注解来装配 Bean 到 Spring IoC 容器中 。IoC 容器具备两个基本的功能： 

- 通过描述管理 Bean，包括发布和获取 Bean； 
- 通过描述完成 Bean 之间的依赖关系。 



dependency injection
passing in objects into your constructor without you having to explicitly create or pass them.
注解代替xml
Spring Boot is simply a configuration framework for the Spring framework.



Bean生命周期

Bean 定义、Bean 的初始化、 Bean 的生存期和 Bean 的销毁  



1. 将 Bean 的定义发布到 IoC 容器 

只是将定义发布到 IoC 容器而不做实例化和依赖注入，当我们取出来的时候才做初始化和依赖注入等操作 

- Spring 通过我们的配置，如@ComponentScan 定义的扫描路径去找到带有@Component 的类，这个过程就是一个资源定位的过程。
-  一旦找到了资源，那么它就开始解析，并且将定义的信息保存起来。注意，此时还没有初始化 Bean，也就没有 Bean 的实例，它有的仅仅是 Bean 的定义。
-  然后就会把 Bean 定义发布到 Spring IoC 容器中。此时， IoC 容器也只有 Bean 的定义，还是没有 Bean 的实例生成。 

![1584363163737](1584363163737.png)



先在 Maven 配置文件中加载依赖 (从本地仓库中加载各种jar包，如果本地仓库没有，则从中央仓库下载)

通过@Value 注解，使用${......}这样的占位符读取配置在属性文件（src/main/resources/application.properties）的内容 



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



- @Configuration:指明当前类是一个配置类； 
  **配置类 ----- 配置文件；**配置类也是容器中的一个**组件**；@Componen 



- @ConfigurationProperties：告诉SpringBoot将本类中的所有属性和配置文件中相关的配置进行绑定；

  prefix = "person"：配置文件中哪个下面的所有属性进行一一映射

  @ConfigurationProperties(prefix = "person")默认从全局配置文件中获取值； 

- @Component 

  -- 只有这个组件是容器中的组件，才能容器提供的@ConfigurationProperties功能；



- @PropertySource(value = {"classpath:person.properties"}) ：加载指定的配置文件  同时需要

  @Component @ConfigurationProperties(prefix = "person") 

  

- @Bean //给容器中添加一个组件，这个组件的某些值需要从properties中获取 



F5刷新按钮只对当前页面进行刷新，只刷新本地缓存；

Ctrl + F5 的行为也是刷新页面，但是会把浏览器中的临时文件夹的文件删除再重新从服务器下载。

Model、View、Controller即模型、视图、控制器

**MVC要实现的目标是将软件用户界面和业务逻辑分离以使代码可扩展性、可复用性、可维护性、灵活性加强。**

View层是界面，Model层是业务逻辑，Controller层用来调度View层和Model层，将用户界面和业务逻辑合理的组织在一起，起粘合剂的效果。所以Controller中的内容能少则少，这样才能提供最大的灵活性。**用来将不同的View和不同的Model组织在一起，顺便替双方传递消息**

View层，单独实现了组合模式

Model层和View层，实现了观察者模式

View层和Controller层，实现了策咯模式

**Model是被观察的对象，View是观察者，Model层一旦发生变化，View层即被通知更新**

一个View被多个Controller引用

策略模式中的策略通常都很小很薄，不会包含太多的内容， Controller是一个策略， 自然不应该在里面放置过多的内容

模型层（Model）：指从现实世界中抽象出来的对象模型，是应用逻辑的反应；它封装了数据和对数据的操作，是实际进行数据处理的地方（模型层与数据库才有交互）

视图层（View）：是应用和用户之间的接口，它负责将应用显示给用户 和 显示模型的状态。

控制器（Controller）:控制器负责视图和模型之间的交互，控制对用户输入的响应、响应方式和流程；它主要负责两方面的动作，一是把用户的请求分发到相应的模型，二是吧模型的改变及时地反映到视图上。

WebJars是将客户端（浏览器）资源（JavaScript，Css等）打成jar包文件，以对资源进行统一依赖管理

crud是指在做计算处理时的增加(Create)、读取(Retrieve)、更新(Update)和删除(Delete)几个单词的首字母简写。crud主要被用在描述软件系统中数据库或者[持久层](https://baike.baidu.com/item/持久层/3584971)的基本操作功能。

#### 名词

POJO（Plain Old Java Object, 简单Java对象）

IoC：Inversion of Control  控制反转 

DI：依赖注入（ Dependency Injection） 

轻量级容器（ Lightweight Container) 

EJB是的Enterprise Java Beans

Bean：所有注册到容器中的业务对象称之为Bean
