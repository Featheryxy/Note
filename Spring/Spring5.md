# Spring5

## 概述

https://repo.spring.io/ui/native/release/org/springframework/spring



## IOC

IOC：控制反转，把创建对象过程交给 Spring 进行管理

> 把对象创建和对象之间的调用过程，交给 Spring 进行管理，降低耦合度。

contex ----> beanfactorybean ----> bean/factorybean



### 原理

原理：xml 解析、工厂模式、反射

1. IOC 思想基于 IOC 容器完成，IOC 容器底层就是对象工厂
2. Spring 提供 IOC 容器实现两种方式：（两个接口）
   - BeanFactory：IOC 容器基本实现，是 Spring 内部的使用接口，不提供开发人员进行使用。加载配置文件时候不会创建对象，在获取对象（使用）才去创建对象
   - ApplicationContext：BeanFactory 接口的子接口，提供更多更强大的功能，一般由开发人
     员进行使用。加载配置文件时候就会把在配置文件对象进行创建

3. ApplicationContext 接口有实现类

## Bean（基于XML）

什么是 Bean 管理

1. Spring 创建对象

2. Spirng 注入属性(DI)

   > 将对象或值赋给变量名
   >
   > - 通过set方法注入
   > - 通过构造器注入
   > - 外部bean对象注入

Bean 管理操作方式

1. 基于 xml 配置文件方式实现
2. 基于注解方式实现

### XML配置

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:p="http://www.springframework.org/schema/p"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    
    <!-- 创建对象,默认使用无参构造器创建对象 
        id 属性：唯一标识
        class 属性：类全路径（包类路径）
	-->
    <!--  1.使用property完成属性注入
        name: 类里面属性名称
        value: 向属性注入的值
    -->
    <bean id="book" class="com.milo.bean.Book">
        <property name="bname" >
            <value>&lt;&lt;peace and love&gt;&gt;</value>
        </property>
        <property name="bauthor" value="China"></property>

        <!--        <property name="adress">-->
        <!--            <null/>   -->
        <!--        </property>-->

        <!--   属性值包含特殊符号
            1. 转义 &lt; &gt; 分别代表<, >
            2. 将特殊符号内容写到CDATA
        -->
    </bean>
    
    <!--  3. 有参数构造注入属性 -->
    <bean id="orders" class="com.atguigu.spring5.Orders">
        <constructor-arg name="oname" value="电脑"></constructor-arg>
        <constructor-arg name="address" value="China"></constructor-arg>
	</bean>
    
    <!-- 在service中注入dao -->
    <bean id="userService" class="com.study.spring5.service.UserService">
        <property name="userDao" ref="userDao"></property>
    </bean>
    <bean id="userDao" class="com.study.spring5.dao.UserDaoImpl"></bean>
        <!--        注入userDao对象
                name属性值：类里面属性名称
                ref属性：创建userDao对象bean标签的id值
        -->

    <bean id="emp" class="com.study.spring5.bean.Emp">
        <property name="ename" value="lucy"></property>
        <property name="gender" value="female"></property>

        <property name="dept">
            <bean id="dept" class="com.study.spring5.bean.Dept">
                <property name="dname" value="保安部"></property>
            </bean>
        </property>
    </bean>

```

### Bean 作用域

```xml
<!-- 默认为singleton -->
<bean id="MyBean" class="com.milo.bean.MyBean" scope="prototype"></bean>
```

- 设置 scope 值是 singleton 时候，加载 spring 配置文件时候就会创建单实例对象
- 设置 scope 值是 prototype 时候，不是在加载 spring 配置文件时候创建对象，在调用
  getBean 方法时候创建多实例对象

### Bean与FactoryBean

1. Bean存放在singletonObjects, FactoryBean存放于factoryBeanObjectCache
2. 如果要获取源对象需要加上&，否则会获取getObject()方法返回的对象
3. 如果只是实现了FactoryBean这个最底层的接口，那么它和普通Bean的处理流程一模一样。如果说实现了SmartFactoryBean接口并重写了isEagerInint()并返回true的话，那么Spring在启动的时候会先去调用getObject()，然后将返回值存入factoryBeanObjectCache里面。

```java
public class MyBean implements FactoryBean {
    @Override
    public Object getObject() throws Exception {
        return new String("string object");
    }

    @Override
    public Class<?> getObjectType() {
        return null;
    }

    @Override
    public boolean isSingleton() {
        return FactoryBean.super.isSingleton();
    }
}

    @Test
    public void testMyBean(){
        ApplicationContext context = new ClassPathXmlApplicationContext("bean1.xml");
        Object myBean = context.getBean("MyBean");
        System.out.println(myBean);
        Object myBean1 = context.getBean("&MyBean");
        System.out.println(myBean1);
        // string object
        //com.milo.bean.MyBean@69b0fd6f
    }
```

### Bean生命周期

```java
public class Orders {

    //无参数构造
    public Orders() {
        System.out.println("第一步 执行无参数构造创建bean实例");
    }

    private String oname;
    public void setOname(String oname) {
        this.oname = oname;
        System.out.println("第二步 调用set方法设置属性值");
    }

    //创建执行的初始化的方法
    public void initMethod() {
        System.out.println("第三步 执行初始化的方法");
    }

    //创建执行的销毁的方法
    public void destroyMethod() {
        System.out.println("第五步 执行销毁的方法");
    }
}

public class MyBeanPost implements BeanPostProcessor {
    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("在初始化之前执行的方法");
        return bean;
    }
    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("在初始化之后执行的方法");
        return bean;
    }
}

    @Test
    public void testBean3() {
//        ApplicationContext context =
//                new ClassPathXmlApplicationContext("bean4.xml");
        ClassPathXmlApplicationContext context =
                new ClassPathXmlApplicationContext("bean4.xml");
        Orders orders = context.getBean("orders", Orders.class);
        System.out.println("第四步 获取创建 bean实例对象");
        System.out.println(orders);
        //手动让bean实例销毁
        context.close();
        
        //第一步 执行无参数构造创建bean实例
        //第二步 调用set方法设置属性值
        //在初始化之前执行的方法
        //第三步 执行初始化的方法
        //在初始化之后执行的方法
        //第四步 获取创建 bean实例对象
        //com.atguigu.spring5.bean.Orders@8646db9
        //第五步 执行销毁的方法
    }

    <bean id="orders" class="com.atguigu.spring5.bean.Orders" init-method="initMethod" destroy-method="destroyMethod">
        <property name="oname" value="手机"></property>
    </bean>

    <!--配置后置处理器-->
    <bean id="myBeanPost" class="com.atguigu.spring5.bean.MyBeanPost"></bean>
```

### xml 自动装配

根据指定装配规则（属性名称或者属性类型），Spring 自动将匹配的属性值进行注入

```xml
    <!-- 根据对象类型自动将Dept装入Emp类dept变量中装入-->
	<bean id="emp" class="com.atguigu.spring5.autowire.Emp" autowire="byType">
        <!--<property name="dept" ref="dept"></property>-->
    </bean>
    <bean id="asd" class="com.atguigu.spring5.autowire.Dept"></bean>

<!-- 实现自动装配
    bean 标签属性 autowire，配置自动装配
    autowire 属性常用两个值：
    byName 根据属性名称注入 ，注入值 bean 的 id 值和类属性名称一样
    byType 根据属性类型注入
-->
```

## Bean(基于注解)

注解是代码特殊标记，格式：@注解名称(属性名称=属性值, 属性名称=属性值..)

Spring 针对 Bean 管理中创建对象提供注解
（1）@Component
（2）@Service
（3）@Controller
（4）@Repository

* 上面四个注解功能是一样的，都可以用来创建 bean 实例, 交给Spring Contex来管理
* byType ---> byName

### 注解--对象创建

1. 注解需要 spring-aop-x.x.x.RELEASE.jar包

2. 开启组件扫描

   ```xml
   <context:component-scan base-package="com.milo"></context:component-scan>
   ```

3. 创建类，在类上面添加创建对象注解

   ```java
   //在注解里面 value 属性值可以省略不写，
   //默认值是 类名称，首字母小写
   //UserService -- userService
   @Component(value = "userService") //<bean id="userService" class=".."/>
   public class UserService {
       public void add() {
       	System.out.println("service add.......");
   	}
   }
   ```

4. 开启组件扫描细节配置

   ```xml
   <!--示例 1
       use-default-filters="false": 表示现在不使用默认 filter，自己配置 filter
       context:include-filter: 设置扫描哪些内容
   -->
   <context:component-scan base-package="com.milo" use-default-filters="false">
   	<context:include-filter type="annotation" expression="org.springframework.stereotype.Controller"/>
   </context:component-scan>
   
   <!--示例 2
   下面配置扫描包所有内容
   context:exclude-filter： 设置哪些内容不进行扫描
   -->
   <context:component-scan base-package="com.atguigu">
   	<context:exclude-filter type="annotation" expression="org.springframework.stereotype.Controller"/>
   </context:component-scan>
   ```
   
5. 基于注解方式实现属性注入
   
   ```java
   /*
   （1）@Autowired：根据属性类型进行自动装配
   	第一步 把 service 和 dao 对象创建，在 service 和 dao 类添加创建对象注解
   	第二步 在 service 注入 dao 对象，在 service 类添加 dao 类型属性，在属性上面使用注解
   */
   
   @Service
   public class UserService {
       //不需要添加 set 方法
       @Autowired
       private UserDao userDao;
       
       public void add() {
           System.out.println("service add.......");
           userDao.add();
       }
   }
   /*
   （2）@Qualifier：根据名称进行注入
   	这个@Qualifier 注解的使用，和上面@Autowired 一起使用
   */
   
   @Autowired //根据类型进行注入
   @Qualifier(value = "userDaoImpl1") //根据名称进行注入
   private UserDao userDao;
   
   // （3）@Resource：可以根据类型注入，可以根据名称注入
   
   //@Resource //根据类型进行注入
   @Resource(name = "userDaoImpl1") //根据名称进行注入
   private UserDao userDao;
   
   // （4）@Value：注入普通类型属性
   @Value(value = "abc")
   private String name;
   ```
   
6. 完全注解开发

      ```java
      @Configuration //作为配置类，替代 xml 配置文件
      @ComponentScan(basePackages = {"com.atguigu"})
      public class SpringConfig {
          
      }
      ```

## Aop

（1）面向切面编程（方面），利用 AOP 可以对业务逻辑的各个部分进行隔离，从而使得
业务逻辑各部分之间的耦合度降低，提高程序的可重用性，同时提高了开发的效率。
（2）通俗描述：不通过修改源代码方式，在主干功能里面添加新功能

## JdbcTemplate
