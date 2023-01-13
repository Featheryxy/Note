#### Spring

Spring是什么?

Spring是一个轻量级的IoC和AOP容器框架，目的是用于简化企业应用程序的开发，它使得开发者只需要关心业务需求。

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

IOC就是控制反转，是指创建对象的控制权的转移，以前创建对象的主动权和时机是由自己把控的，而现在这种权力转移到Spring容器中，并由容器根据配置文件去创建实例和管理各个实例之间的依赖关系，对象与对象之间松散耦合，也利于功能的复用。







依赖注入方式：

1. 构造器注入
   - 优点：对象构造完成后即可使用
   - 缺点：
     - 当依赖对象较多时，构造方法的参数列表会比较长。
     - 构造方法无法被继承，无法设置默认值
2. setter注入：最提倡，可被继承，允许设置默认值
3. 接口注入：要求被注入的对象实现不必要的接口，带有侵入性
3. 注解注入

IoC职责：

1. 对象的构建
2. 对象之间的依赖绑定



如何管理对象间的依赖关系：

1. 直接编码
2. 配置文件方式
3. 元数据方式, 如注解





BeanFactory 和 ApplicationContext的区别？

Spring的两大核心接口，都可以当做Spring的容器。其中ApplicationContext是BeanFactory的子接口

容器类型：

1. BeanFactory：默认lazy-load，是Spring里面最底层的接口，包含了各种Bean的定义，读取bean配置文档，管理bean的加载、实例化，控制bean的生命周期，维护bean之间的依赖关系
2. ApplicationContext：ApplicationContext接口作为BeanFactory的派生，除了提供BeanFactory所具有的功能外，还提供了更完整的框架功能。启动后会实例化所有的bean定义
   - 统一资源加载策略
   - 国际化信息支持
   - 容器内事件发布
   - 多配置模块加载简化
   - 提供在监听器中注册bean的事件

① BeanFactroy采用的是延迟加载形式来注入Bean的，即只有在使用到某个Bean时(调用getBean())，才对该Bean进行加载实例化。
	这样，我们就不能发现一些存在的Spring的配置问题。如果Bean的某一个属性没有注入，BeanFacotry加载后，直至第一次使用调用getBean方法才会抛出异常。

 ② ApplicationContext，它是在容器启动时，一次性创建了所有的Bean。这样，在容器启动时，我们就可以发现Spring中存在的配置错误，这样有利于检查所依赖属性是否注入。
 ApplicationContext启动后预载入所有的单实例Bean，通过预载入单实例bean ,确保当你需要的时候，你就不用等待，因为它们已经创建好了。

 ③ 相对于基本的BeanFactory，ApplicationContext 唯一的不足是占用内存空间。当应用程序配置Bean较多时，程序启动较慢。

（3）BeanFactory通常以编程的方式被创建，ApplicationContext还能以声明的方式创建，如使用ContextLoader。

（4）BeanFactory和ApplicationContext都支持BeanPostProcessor、BeanFactoryPostProcessor的使用，
但两者之间的区别是：BeanFactory需要手动注册，而ApplicationContext则是自动注册。





常用注解：

@Component 

@Repository

@Service

@Controller

> @Repository，@Service，@Controller和@Component 主要在语义上不同，都会被component-scan扫描到并注入到容器中，其默认名称为将类名首字母小写



@Autowired, byType

@Qualifier, byName, IoC容器无法自己从多个同一类型的实例中选取我们真正想要的那个, 可以使用@Qualifier直接点名





JSR250 标注依赖注入关系

@Resource，byName

@PostConstruct和@PreDestroy不是服务于依赖注入的，它们主要用于标注对象生命周期管理相关方法。

与Spring的InitializingBean和DisposableBean接口，以及配置项中的init-method和destroy-method起到类似的作用



Autowired自动绑定模式：

1. no，default
2. byName，实例名称和beanName相同
3. byType
4. constructor， 根据byType
5. autodetect



自动绑定

手动绑定



FactoryBean：还是个Bean，同样会注册到容器中，只不过该类型的Bean本身就是生产对象的工厂

BeanFactory：容器本身，



IOC原理：

1. 容器启动阶段

   - 加载配置
   - 分析配置信息
   - 装备到BeanDefinition，注册到相应的BeanDefinitionRegistry
   - 其他处理
   - BeanFactoryPostProcessor会修改BeanDefinition中的信息

2. Bean实例化阶段

   第一次调用getBean()后会进入实例化阶段



BeanPostProcessor：对象实例化阶段

BeanFactoryPostProcessor：容器启动阶段

6、请解释Spring Bean的生命周期？

 首先说一下Servlet的生命周期：实例化，初始init，接收请求service，销毁destroy；

 Spring上下文中的Bean生命周期也类似，如下：

（1）实例化Bean：

对于BeanFactory容器，当客户向容器请求一个尚未初始化的bean时，或初始化bean的时候需要注入另一个尚未初始化的依赖时，容器就会调用createBean进行实例化。
对于ApplicationContext容器，当容器启动结束后，通过获取BeanDefinition对象中的信息，实例化所有的bean。

（2）设置对象属性（依赖注入）：

实例化后的对象被封装在BeanWrapper对象中，紧接着，Spring根据BeanDefinition中的信息 以及 通过BeanWrapper提供的设置属性的接口完成依赖注入。

（3）处理Aware接口：

接着，Spring会检测该对象是否实现了xxxAware接口，并将相关的xxxAware实例注入给Bean：

①如果这个Bean已经实现了BeanNameAware接口，会调用它实现的setBeanName(String beanId)方法，此处传递的就是Spring配置文件中Bean的id值；

②如果这个Bean已经实现了BeanFactoryAware接口，会调用它实现的setBeanFactory()方法，传递的是Spring工厂自身。

③如果这个Bean已经实现了ApplicationContextAware接口，会调用setApplicationContext(ApplicationContext)方法，传入Spring上下文；

（4）BeanPostProcessor：

如果想对Bean进行一些自定义的处理，那么可以让Bean实现了BeanPostProcessor接口，那将会调用postProcessBeforeInitialization(Object obj, String s)方法。

（5）InitializingBean 与 init-method：

如果Bean在Spring配置文件中配置了 init-method 属性，则会自动调用其配置的初始化方法。

（6）如果这个Bean实现了BeanPostProcessor接口，将会调用postProcessAfterInitialization(Object obj, String s)方法；由于这个方法是在Bean初始化结束时调用的，所以可以被应用于内存或缓存技术；

以上几个步骤完成后，Bean就已经被正确创建了，之后就可以使用这个Bean了。

（7）DisposableBean：

当Bean不再需要时，会经过清理阶段，如果Bean实现了DisposableBean这个接口，会调用其实现的destroy()方法；

（8）destroy-method：

最后，如果这个Bean的Spring配置中配置了destroy-method属性，会自动调用其配置的销毁方法。



7、 解释Spring支持的几种bean的作用域scope。

Spring容器中的bean可以分为5个范围：

（1）singleton：默认，每个容器中只有一个bean的实例，单例的模式由BeanFactory自身来维护, 与容器具有相同的生命周期。

（2）prototype：为每一个bean请求提供一个实例，当改对象实例返回给请求方后，其生命周期由请求方管理。

（3）request：为每一个Http请求创建一个实例，在请求完成以后，bean会失效并被垃圾回收器回收。

（4）session：与request范围类似，活的比request长，确保每个session中有一个bean的实例，在session过期后，bean会随之失效。

（5）global-session：全局作用域，global-session和Portlet应用相关。当你的应用部署在Portlet容器中工作时，它包含很多portlet。
如果你想要声明让所有的portlet共用全局的存储变量的话，那么这全局变量需要存储在global-session中。全局作用域与Servlet中的session作用域效果相同。

8、Spring框架中的单例Beans是线程安全的么？

Spring框架并没有对单例bean进行任何多线程的封装处理。关于单例bean的线程安全和并发问题需要开发者自行去搞定。但实际上，大部分的Spring bean 并没有可变的状态(比如Serview类和DAO类)，所以在某种程度上说Spring的单例bean是线程安全的。如果你的bean有多种状态的话（比如 View Model 对象），就需要自行保证线程安全。最浅显的解决办法就是将多态bean的作用域由“singleton”变更为“prototype”。

9、Spring如何处理线程并发问题？

在一般情况下，只有无状态的Bean才可以在多线程环境下共享，在Spring中，绝大部分Bean都可以声明为singleton作用域，
因为Spring对一些Bean中非线程安全状态采用ThreadLocal进行处理，解决线程安全问题。
ThreadLocal和线程同步机制都是为了解决多线程中相同变量的访问冲突问题。
同步机制采用了“时间换空间”的方式，仅提供一份变量，不同的线程在访问前需要获取锁，没获得锁的线程则需要排队。
而ThreadLocal采用了“空间换时间”的方式。ThreadLocal会为每一个线程提供一个独立的变量副本，从而隔离了多个线程对数据的访问冲突。
因为每一个线程都拥有自己的变量副本，从而也就没有必要对该变量进行同步了。
ThreadLocal提供了线程安全的共享对象，在编写多线程代码时，可以把不安全的变量封装进 ThreadLocal。





#### AOP

面向切面编程（Aspect Oriented Programming， AOP） 

AOL（Aspect-Oriented Language）

类比：

- Aspect -- AOP

- Class -- OOP



AOP主要是对OOP的补充，OOP负责业务相关代码的抽象，定义纵向的关系，不适用于定义横向的关系，导致了大量代码的重复

AOP，一般称为面向切面，作为面向对象的一种补充，用于将那些与业务无关，但却对多个对象产生影响的公共行为和逻辑，抽取并封装为一个可重用的模块，这个模块被命名为“切面”（Aspect），减少系统中的重复代码，降低了模块间的耦合度，同时提高了系统的可维护性。可用于权限认证、日志、事务处理。

AOP实现的关键在于 代理模式，AOP代理主要分为**静态代理**和**动态代理**。

- 静态代理的代表为AspectJ；AspectJ是静态代理的增强，所谓静态代理，就是AOP框架会在**编译阶段生成AOP代理类**，因此也称为编译时增强，他会在编译阶段将AspectJ(切面)织入到Java字节码中，运行的时候就是增强之后的AOP对象。
- 动态代理则以Spring AOP为代表：Spring AOP使用的动态代理，所谓的动态代理就是说AOP框架不会去修改字节码，而是每次**运行时在内存中临时为方法生成一个AOP对象**，这个AOP对象包含了目标对象的全部方法，并且在特定的切点做了增强处理，并回调原对象的方法。

Spring AOP 中的动态代理主要有两种方式，

- JDK动态代理：

  JDK动态代理只提供接口的代理，不支持类的代理。核心InvocationHandler接口和Proxy类，InvocationHandler 通过invoke()方法反射来调用目标类中的代码，动态地将横切逻辑和业务编织在一起；接着，Proxy利用 InvocationHandler动态创建一个符合某一接口的的实例,  生成目标类的代理对象。

- CGLIB动态代理：

  如果代理类没有实现 InvocationHandler 接口，那么Spring AOP会选择使用CGLIB来动态代理目标类。CGLIB（Code Generation Library），是一个代码生成的类库，可以在运行时动态的生成指定类的一个子类对象，并覆盖其中特定方法并添加增强代码，从而实现AOP。CGLIB是通过继承的方式做的动态代理，因此如果某个类被标记为final，那么它是无法使用CGLIB做动态代理的。



静态代理与动态代理区别在于生成AOP代理对象的时机不同，相对来说AspectJ的静态代理方式具有更好的性能，但是AspectJ需要特定的编译器进行处理，而Spring AOP则无需特定的编译器处理。

InvocationHandler 的 invoke(Object  proxy,Method  method,Object[] args)：

- proxy是**最终生成的代理实例;**  
- method 是被代理目标实例的某个具体方法;  
- args 是被代理目标实例某个方法的具体入参, 在方法反射调用时使用。

 

Joinpoint：将AOP的功能织入到OOP系统的执行点

Joinpoint类型：

1. 方法调用（Method Call）：方法被调用时，在调用对象的执行点
2. 方法调用执行（Method Call execution）：被调用到的方法逻辑执行时
3. 构造方法调用（Constructor Call）：
4. 构造方法执行（Constructor  Call Execution）
5. 字段设置（Field Set）
6. 字段获取（Field Get）
7. 异常处理执行（Exception Handler Execution）
8. 类初始化（Class initialization）：静态初始块

Pointcut：Joinpoint的表述方式，Pointcut之间可以进行逻辑运算

Advice：相当于Class中的Method

- Before Advice
- After Advice
  - After returning Advice
  - After throwing Advice
  - After (Finally) Advice

Around Advice：可以在Joinpoint之前和之后执行相应的逻辑

Introduction：

Aspect：AOP概念实体，可以包含多个



织入（Weaving）

织入器（Weaver），编译器ajc就是AspectJ的织入器

Spring AOP 属于第二代AOP， 采用动态代理机制和字节码生成技术实现，与最初的AspectJ采用编译器将横切逻辑织入目标对象不同，动态代理机制和字节码生成都是在运行期间为目标对象生成一个代理对象，而将横切逻辑织入到这个代理对象中，系统最终使用的是织入了横切逻辑的代理对象，而不是真正的目标对象。





#### Other

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

URL：Uniform Resource Locator（统一资源定位器）

OOP：Object-Oriented Software Development

#### Reference

https://spring.io/guides





